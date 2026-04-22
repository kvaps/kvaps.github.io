---
title: "How to resolve split-brain in DRBD9"
date: 2021-07-19T16:06:12+00:00
link: https://dev.to/kvaps/how-to-solve-split-brain-in-drbd9-15no
source: dev.to
---

![](https://res.cloudinary.com/practicaldev/image/fetch/s--p2uxD_PC--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kzyx2gkmcim5hgjk5dft.png)

First, let's define what split-brain is. Each replica can be either connected or disconnected towards to the other. If the replica spontaneously goes to StandAlone. It means that it refuses to accept the state and don't want to synchronize with the other. This is a classic split-brain situation.

Solving the split-brain for two replicas is done in the same way as for multiple replicas.

First, let's decide which replica we want to synchronize with. To do this, look into

```
drbdadm status
```

If the replica we need is in the `StandAlone` or `Outdated`/`Inconsistent` state, it must first be switched to `UpToDate`. To acheve this go to the node with this replica and execute:

```
drbdadm primary --force
drbdadm secondary
```

And in order to make the rest of the replicas forget about their state and synchronize the data from the `UpToDate` replicas. Go to the nodes with them and execute:

```
drbdadm disconnect
drbdadm connect  --discard-my-data
```

It is worth mentioning that in the latest versions of LINSTOR, the auto-tiebreaker function is enabled by default. This means, when you creating a resource in two replicas, automatically adds a third diskless replica, which is a kind of arbiter for ensuring the quorum. Thus, it is less and less usual to solve split-brain these days.

<!--more-->
