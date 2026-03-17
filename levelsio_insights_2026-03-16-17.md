# Levelsio (@levelsio) Insights — March 16-17, 2026

Curated from Pieter Levels' posts on X, focused on AI, building products, and developer workflows.

---

## 1. Building Features with Claude Code: Hoodmaps x Airbnb

> "This was asked for for YEARS and I could never find time to build it myself. Hoodmaps for Airbnb. I asked Claude Code to [build it]."

Hoodmaps classifies neighborhoods by: Tourists, Cool, Rich, Suits, Normies. He finally shipped the long-requested Airbnb integration by delegating the build to Claude Code.

**Takeaway:** AI coding agents unlock features that have been on the backlog for years. The bottleneck shifts from "can I build it" to "what should I build next."

🔗 [Tweet](https://x.com/levelsio/status/2033725611835859380) — 737 likes

---

## 2. Phone-First Coding Workflow with Claude Code

> "Are you guys aware I am coding mostly on my phone now all day via Termius to Claude Code on my server while I go with gf to the dentist, clothing store, cafe, etc."

His stack: **iPhone → Termius (SSH) → Claude Code on Hetzner VPS**. He codes while doing errands.

**Takeaway:** AI coding agents decouple development from sitting at a desk. The "IDE" becomes a chat interface you can use anywhere. This fundamentally changes what it means to be a developer.

🔗 [Tweet](https://x.com/levelsio/status/2033640947469209911) — 1,276 likes

---

## 3. AI as Your Sysadmin / Server Companion

> "This basic stuff does sound complicated but it takes 5 minutes to set up. After this part, running a VPS is cheap, safe and easy. Especially with Claude Code running it, which you can ask to check if the server is safe and stuff like enable auto upgrades and auto reboot after [updates]."

> "Like having a best mate that helps you out with your server."

**Takeaway:** AI agents are becoming the go-to ops assistant for indie hackers. Instead of learning sysadmin from scratch, you pair with an AI that handles security hardening, updates, and monitoring. Lowers the barrier for solo developers to run their own infra.

🔗 [Tweet](https://x.com/levelsio/status/2033547042396557421) — 468 likes
🔗 [Tweet](https://x.com/levelsio/status/2033551152977990046) — 110 likes

---

## 4. AI-Powered Photorealistic Game Rendering at 60 FPS

> "Crazy so I think they essentially built consistent img2img of game frames into AI image models to make it photorealistic at 60 FPS. You could have a very basic rudimentary 3d scene in games and just let AI finish it off with a prompt and some media assets of the characters."

**Takeaway:** Real-time AI image models applied to game frames = photorealistic rendering from low-poly scenes. This could democratize AAA-quality visuals for indie game devs.

🔗 [Tweet](https://x.com/levelsio/status/2033656989214281785) — 414 likes

---

## 5. The AI Spam Crisis on Social Media

> "FCC should make undisclosed AI bot posts, replies and DMs a federal crime with high fines, same EU. It's fine if you post on social media with AI but it has to be disclosed, so we can easily filter it out. Right now replies on X have become unusable for me and many others."

> "I think I've blocked 100+ AI accounts today."

> "If I didn't have AI in my bio I'd say you can block 99% of accounts with AI in their bio for being AI reply spammers."

**Takeaway:** AI-generated spam is degrading social platforms. There's a market opportunity for AI-powered filtering/verification tools. Disclosure requirements may become law.

🔗 [Tweet](https://x.com/levelsio/status/2033740684901884278) — 87 likes

---

## 6. Retro Projects Revived with AI

> "So many retro projects getting revived now with AI, which ones should I check out? I saw people reverse engineering Gameboy games etc."

He also set up a browser-based Quake III server — reviving a 7-year-old project.

**Takeaway:** AI lowers the cost of reviving abandoned/legacy projects. Reverse engineering, porting old games, and breathing life into dormant codebases is becoming a trend.

🔗 [Tweet](https://x.com/levelsio/status/2033330111764746333) — 447 likes
🔗 [Tweet](https://x.com/levelsio/status/2033674799382405354) — 219 likes

---

## 7. Modern Dev Tooling: Tmux is Dead, Zellij is the Future

> "I hate tmux. It's so incredibly user unfriendly. The shortcuts make no sense."

> "Tmux is a terrible experience on a phone. And a phone will be where we're coding at least half the time now."

He discovered **Zellij** as a modern replacement and also uses `/resume` in Claude Code when SSH disconnects.

**Takeaway:** Phone-based AI coding is creating demand for better terminal multiplexers. The tooling around AI agents (not just the agents themselves) is a growing space.

🔗 [Tweet](https://x.com/levelsio/status/2033657882160386084) — 700 likes
🔗 [Tweet](https://x.com/levelsio/status/2033715645422936206) — 389 likes

---

## 8. VPS Security Blueprint for Indie Hackers

> "When I set up a new Hetzner VPS first thing I do install Tailscale and once I'm in via Tailscale lock down the firewall to only accept web traffic on HTTPS 443 for Cloudflare IPs and SSH 22 for Tailscale IP. That way nobody can get in."

His security layers: Tailscale VPN → SSH key auth → locked-down firewall (Cloudflare IPs + Tailscale only).

**Takeaway:** Simple, repeatable security setup. An AI agent could automate this entire hardening process for new VPS instances.

🔗 [Tweet](https://x.com/levelsio/status/2033546675063554213) — 3,602 likes

---

## 9. Playing Games While Claude Code Thinks

> "My friend said it's perfect to play [Quake] while Claude Code is thinking. So match time is now 10 minutes, a bit faster!"

**Takeaway:** The async nature of AI coding creates "idle time" that didn't exist before. Developers are finding new rhythms — review prompts, fire off tasks, do something else, come back. This is a UX design consideration for AI agent tools.

🔗 [Tweet](https://x.com/levelsio/status/2033681140075147349) — 30 likes

---

## Summary: Key Themes for AI Agent Builders

| Theme | Signal |
|---|---|
| **AI as coding partner** | Claude Code is his primary dev tool — building features, managing servers, coding from phone |
| **Mobile-first development** | Phone + SSH + AI agent = full dev environment. Tooling needs to catch up (Zellij > tmux) |
| **AI for ops/infra** | AI agents as sysadmins — security hardening, monitoring, auto-updates |
| **Real-time AI rendering** | img2img on game frames at 60 FPS — new frontier for AI in gaming |
| **AI spam problem** | Undisclosed AI bots are destroying social platforms — opportunity for detection/filtering |
| **Legacy revival** | AI makes it cheap to revive abandoned projects and reverse-engineer old software |
| **Async workflows** | AI "thinking time" creates new developer workflows and UX patterns |
