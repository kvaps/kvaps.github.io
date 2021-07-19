---
title: "How to Resolve Split Brain in DRBD9"
date: 2021-07-19T18:21:26+02:00
link: https://dev.to/kvaps/how-to-solve-split-brain-in-drbd9-15no
---

![split-brain](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kzyx2gkmcim5hgjk5dft.png)

First, let's define what split-brain is. Each replica can be either connected or disconnected towards to the other. If the replica spontaneously goes to StandAlone. It means that it refuses to accept the state and don't want to synchronize with the other. This is a classic split-brain situation.

<!--more-->
