---
title: "What dozens of AI agents taught me: how I wrote the Blockstor storage system as an experiment"
date: 2026-08-10T09:02:46+00:00
link: https://blog.aenix.io/what-dozens-of-ai-agents-taught-me-how-i-wrote-the-blockstor-storage-system-as-an-experiment-921f7d3a1137?source=rss-d8a829bb74d8------2
source: medium
---

![](https://cdn-images-1.medium.com/max/1024/1*ep6GUdvlFLIwsXN-U0ovnQ.png)

A couple of months ago I decided to run an experiment: build a clean-room implementation of LINSTOR from scratch, working only from its references and public API types. It started as a Friday joke. I wanted to spend as little time on it as possible, leave it running in the background, and see where it went. The point was to find out how far a modern model can get on its own, with no human in the loop.

Spoiler: full autonomy didn’t happen, and I ended up wrestling with the project quite a bit. But the process pulled me in completely, and the end result beat every expectation I had.
