"""Twitter Fellow — MCP server for reading tweets from followed accounts."""

import json
import os
from pathlib import Path

import httpx
from dotenv import load_dotenv
from fastmcp import FastMCP

load_dotenv()

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN", "")
BASE_URL = "https://api.x.com/2"
CACHE_FILE = Path(__file__).parent / ".cache.json"
FOLLOWS_FILE = Path(__file__).parent / "follows.txt"

mcp = FastMCP("twitter-fellow")

# --- ID cache ---

_id_cache: dict[str, str] = {}


def _load_cache() -> None:
    global _id_cache
    if CACHE_FILE.exists():
        _id_cache = json.loads(CACHE_FILE.read_text())


def _save_cache() -> None:
    CACHE_FILE.write_text(json.dumps(_id_cache))


_load_cache()

# --- HTTP helper ---


def _headers() -> dict[str, str]:
    return {"Authorization": f"Bearer {BEARER_TOKEN}"}


async def _twitter_get(path: str, params: dict | None = None) -> tuple[dict, dict]:
    """Make a GET request to the Twitter API. Returns (json_body, rate_limit_info)."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}{path}", headers=_headers(), params=params)
        rate_info = {
            "remaining": resp.headers.get("x-rate-limit-remaining", "?"),
            "limit": resp.headers.get("x-rate-limit-limit", "?"),
        }
        if resp.status_code != 200:
            error_body = resp.json() if resp.headers.get("content-type", "").startswith("application/json") else {}
            raise Exception(
                f"Twitter API error {resp.status_code}: "
                f"{error_body.get('detail', error_body.get('title', resp.text))}"
            )
        return resp.json(), rate_info


# --- Resolve username → user ID ---


async def _resolve_user_id(username: str) -> str:
    username = username.lstrip("@")
    if username in _id_cache:
        return _id_cache[username]
    data, _ = await _twitter_get(f"/users/by/username/{username}")
    user_id = data["data"]["id"]
    _id_cache[username] = user_id
    _save_cache()
    return user_id


# --- Format tweets ---


def _format_tweet(tweet: dict, username: str) -> str:
    metrics = tweet.get("public_metrics", {})
    stats = []
    if metrics.get("like_count"):
        stats.append(f"{metrics['like_count']} likes")
    if metrics.get("retweet_count"):
        stats.append(f"{metrics['retweet_count']} RTs")
    if metrics.get("reply_count"):
        stats.append(f"{metrics['reply_count']} replies")

    lines = [
        tweet["text"],
        f"  {tweet.get('created_at', '?')}  |  {', '.join(stats) if stats else 'no engagement yet'}",
        f"  https://x.com/{username}/status/{tweet['id']}",
    ]
    return "\n".join(lines)


# --- Tools ---


@mcp.tool()
async def get_user_tweets(username: str, max_results: int = 5) -> str:
    """Get the latest tweets from a specific X/Twitter user.

    Args:
        username: X/Twitter username (without @)
        max_results: Number of tweets to fetch (1-100, default 5)
    """
    username = username.lstrip("@")
    max_results = max(1, min(100, max_results))

    user_id = await _resolve_user_id(username)
    data, rate_info = await _twitter_get(
        f"/users/{user_id}/tweets",
        params={
            "max_results": max_results,
            "tweet.fields": "created_at,public_metrics",
            "exclude": "retweets,replies",
        },
    )

    tweets = data.get("data", [])
    if not tweets:
        return f"No recent tweets from @{username}."

    formatted = [f"Latest tweets from @{username}:\n"]
    for tweet in tweets:
        formatted.append(_format_tweet(tweet, username))
    formatted.append(f"\n[API calls remaining: {rate_info['remaining']}/{rate_info['limit']}]")
    return "\n\n".join(formatted)


@mcp.tool()
async def get_feed(max_per_account: int = 3) -> str:
    """Get a digest of latest tweets from all followed accounts (listed in follows.txt).

    Args:
        max_per_account: Number of tweets per account (1-10, default 3)
    """
    max_per_account = max(1, min(10, max_per_account))

    if not FOLLOWS_FILE.exists():
        return "follows.txt not found. Create it with one username per line."

    usernames = [
        line.strip().lstrip("@")
        for line in FOLLOWS_FILE.read_text().splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    if not usernames:
        return "follows.txt is empty. Add usernames (one per line)."

    sections = []
    last_rate_info = {}

    for username in usernames:
        try:
            user_id = await _resolve_user_id(username)
            data, rate_info = await _twitter_get(
                f"/users/{user_id}/tweets",
                params={
                    "max_results": max_per_account,
                    "tweet.fields": "created_at,public_metrics",
                    "exclude": "retweets,replies",
                },
            )
            last_rate_info = rate_info
            tweets = data.get("data", [])
            if tweets:
                tweet_lines = [_format_tweet(t, username) for t in tweets]
                sections.append(f"--- @{username} ---\n\n" + "\n\n".join(tweet_lines))
            else:
                sections.append(f"--- @{username} ---\n\nNo recent tweets.")
        except Exception as e:
            sections.append(f"--- @{username} ---\n\nError: {e}")

    footer = f"\n[API calls remaining: {last_rate_info.get('remaining', '?')}/{last_rate_info.get('limit', '?')}]"
    return "\n\n".join(sections) + footer
