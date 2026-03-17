# 🐦 Twitter Fellow

> Your AI-powered X/Twitter research companion — an MCP server that fetches tweets so Claude can analyze them for you.

## ✨ What it does

Twitter Fellow is a lightweight [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) server that gives Claude direct access to X/Twitter. Use it to:

- 🔍 **Fetch tweets** from any public account
- 📰 **Build a feed** from accounts you follow
- 🧠 **Curate insights** — let Claude analyze and summarize what people are posting about

## 🚀 Quick Start

### 1. Prerequisites

- 🐍 Python 3.11+
- 📦 [uv](https://github.com/astral-sh/uv) (fast Python package manager)
- 🔑 X/Twitter API Bearer Token ([get one here](https://developer.x.com/))

### 2. Setup

```bash
# Clone the repo
git clone git@github.com:BostonMarcin/twitter_fellow.git
cd twitter_fellow

# Copy the example config and add your token
cp .mcp.json.example .mcp.json
# Edit .mcp.json and replace "your_bearer_token_here" with your actual token
```

### 3. Add accounts to follow

Edit `follows.txt` — one username per line:

```
levelsio
bcherny
systematicls
```

### 4. Run with Claude Code

The `.mcp.json` is already configured. Just open the project in Claude Code and the MCP server will be available automatically! 🎉

## 🛠️ Tools

| Tool | Description |
|------|-------------|
| 🐦 `get_user_tweets` | Fetch latest tweets from any X/Twitter user |
| 📰 `get_feed` | Get a digest from all accounts in `follows.txt` |

## 📁 Project Structure

```
twitter_fellow/
├── 🐍 server.py          # MCP server (FastMCP + httpx)
├── 📋 follows.txt         # Accounts to follow
├── ⚙️ .mcp.json.example   # Example MCP config (copy to .mcp.json)
├── 🔒 .mcp.json           # Your MCP config with token (gitignored)
└── 📝 .gitignore
```

## 💡 Example Usage

Once the MCP server is running in Claude Code, just ask:

> *"Check what @levelsio posted today and summarize the key insights"*

> *"Get my feed and find anything interesting about AI agents"*

> *"Fetch the last 50 tweets from @elonmusk and analyze the themes"*

Claude will use the tools automatically to fetch tweets and give you a curated analysis. ✨

## 📄 License

MIT — do whatever you want with it! 🤙
