---
title: "Troubleshooting DRBD9 in LINSTOR"
date: 2021-07-19T15:31:24+00:00
link: https://dev.to/kvaps/troubleshooting-drbd9-in-linstor-40fn
source: dev.to
---

![](https://res.cloudinary.com/practicaldev/image/fetch/s--adsGY0kU--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://habrastorage.org/webt/ft/tb/2v/fttb2vkaex5-wur6zygsbkkwj2k.png)

Over the past few years of tight work with LINSTOR and DRBD9, I have accumulated a some amount of problems and solutions for them. I decided to collect all of them into single article. Not sure that you will face exactly the same problems, but now you could at least understand the mechanics of managing and troubleshooting the DRBD9-devices.

There is not much information on this matter on the Internet. Hope you'll find it useful in case if you use or plan to use LINSTOR.

## Case 1: Unknown and DELETING resources

```
# linstor r l -r one-vm-10417-disk-0
╭────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName        ┊ Node   ┊ Port  ┊ Usage  ┊ Conns ┊    State ┊ CreatedOn           ┊
╞════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-10417-disk-0 ┊ m14c18 ┊ 56263 ┊        ┊       ┊  Unknown ┊ 2021-07-09 14:20:31 ┊
┊ one-vm-10417-disk-0 ┊ m15c38 ┊ 56263 ┊ Unused ┊ Ok    ┊ Diskless ┊ 2021-04-08 07:46:43 ┊
┊ one-vm-10417-disk-0 ┊ m8c12  ┊ 56263 ┊ Unused ┊ Ok    ┊ UpToDate ┊ 2020-10-14 13:10:42 ┊
╰────────────────────────────────────────────────────────────────────────────────────────╯
```

Usually it is nothing critical. Just the node on which it is most likely `OFFLINE`:

```
# linstor n l -n m14c18
╭─────────────────────────────────────────────────────────╮
┊ Node   ┊ NodeType  ┊ Addresses                ┊ State   ┊
╞═════════════════════════════════════════════════════════╡
┊ m14c18 ┊ SATELLITE ┊ 10.36.130.153:3367 (SSL) ┊ OFFLINE ┊
╰─────────────────────────────────────────────────────────╯
```

Check if node has linstor-satellite service running and if it's accessible for linstor-controller.

If at least one resource in `Unknown` state, then removing any other resources will stuck on `DELETING`. In last versions of LINSTOR such deleting resources can be switched back to live by executing `resource create`, example:

```
# linstor r l -r one-vm-10417-disk-0
╭────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName        ┊ Node   ┊ Port  ┊ Usage  ┊ Conns ┊    State ┊ CreatedOn           ┊
╞════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-10417-disk-0 ┊ m14c18 ┊ 56263 ┊        ┊       ┊  Unknown ┊ 2021-07-09 14:20:31 ┊
┊ one-vm-10417-disk-0 ┊ m15c38 ┊ 56263 ┊        ┊ Ok    ┊ DELETING ┊ 2021-04-08 07:46:43 ┊
┊ one-vm-10417-disk-0 ┊ m16c2  ┊ 56263 ┊        ┊ Ok    ┊ DELETING ┊ 2021-05-01 03:36:21 ┊
┊ one-vm-10417-disk-0 ┊ m8c12  ┊ 56263 ┊ Unused ┊ Ok    ┊ UpToDate ┊ 2020-10-14 13:10:42 ┊
╰────────────────────────────────────────────────────────────────────────────────────────╯

# linstor r c m15c38 one-vm-10417-disk-0 --diskless
╭────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName        ┊ Node   ┊ Port  ┊ Usage  ┊ Conns ┊    State ┊ CreatedOn           ┊
╞════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-10417-disk-0 ┊ m14c18 ┊ 56263 ┊        ┊       ┊  Unknown ┊ 2021-07-09 14:20:31 ┊
┊ one-vm-10417-disk-0 ┊ m15c38 ┊ 56263 ┊ Unused ┊ Ok    ┊ Diskless ┊ 2021-04-08 07:46:43 ┊
┊ one-vm-10417-disk-0 ┊ m16c2  ┊ 56263 ┊        ┊ Ok    ┊ DELETING ┊ 2021-05-01 03:36:21 ┊
┊ one-vm-10417-disk-0 ┊ m8c12  ┊ 56263 ┊ Unused ┊ Ok    ┊ UpToDate ┊ 2020-10-14 13:10:42 ┊
╰────────────────────────────────────────────────────────────────────────────────────────╯
```

Any case, if your node totally died, the only way to get rid of `Unknown` resource is to perform `node lost`:

```
# linstor node lost m14c18
# linstor r l -r one-vm-10417-disk-0
╭────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName        ┊ Node   ┊ Port  ┊ Usage  ┊ Conns ┊    State ┊ CreatedOn           ┊
╞════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-10417-disk-0 ┊ m15c38 ┊ 56263 ┊ Unused ┊ Ok    ┊ Diskless ┊ 2021-04-08 07:46:43 ┊
┊ one-vm-10417-disk-0 ┊ m8c12  ┊ 56263 ┊ Unused ┊ Ok    ┊ UpToDate ┊ 2020-10-14 13:10:42 ┊
╰────────────────────────────────────────────────────────────────────────────────────────╯
```

As we can see, the rest of the `DELETING` resources have also disappeared. This behavior is related to the DRBD logic. If there is a chance that the resource is still existing somewhere, there is a chance that it will return to the cluster and make conflict with the other members. To avoid this, you can delete Unknown resources from a faulty node only by removing the entire faulty node.

## Case 2: Outdated replica

We have found replica which is Outdated for some reason:

```
# linstor r l -r one-vm-5899-disk-0
╭──────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port ┊ Usage  ┊ Conns ┊    State ┊ CreatedOn           ┊
╞══════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-5899-disk-0 ┊ m11c30 ┊ 8306 ┊ Unused ┊ Ok    ┊ UpToDate ┊ 2021-02-03 09:43:02 ┊
┊ one-vm-5899-disk-0 ┊ m13c25 ┊ 8306 ┊ Unused ┊ Ok    ┊ Outdated ┊ 2021-02-02 17:51:26 ┊
┊ one-vm-5899-disk-0 ┊ m15c25 ┊ 8306 ┊ InUse  ┊ Ok    ┊ Diskless ┊ 2021-01-18 15:51:40 ┊
╰──────────────────────────────────────────────────────────────────────────────────────╯
```

It can be fixed quite simply:

```
root@m13c25:~# drbdadm disconnect one-vm-5899-disk-0
root@m13c25:~# drbdadm connect --discard-my-data one-vm-5899-disk-0
root@m13c25:~# drbdadm status one-vm-5899-disk-0
one-vm-5899-disk-0 role:Secondary
  disk:UpToDate
  m11c30 role:Secondary
    peer-disk:UpToDate
  m15c25 role:Primary
    peer-disk:Diskless
```

**Note:** option `--discard-my-data` is valid only for split-brain situations, in all other cases the specifying of it has no effect.

## Case 3: Inconsistent replica

Here we have resource where one of the replicas become `Inconsistent` for some reason:

```
linstor r l -r one-vm-6372-disk-0
╭──────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port ┊ Usage  ┊ Conns ┊        State ┊ CreatedOn           ┊
╞══════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-6372-disk-0 ┊ m10c17 ┊ 8262 ┊ Unused ┊ Ok    ┊     UpToDate ┊ 2021-02-03 09:43:31 ┊
┊ one-vm-6372-disk-0 ┊ m13c35 ┊ 8262 ┊ Unused ┊ Ok    ┊ Inconsistent ┊                     ┊
┊ one-vm-6372-disk-0 ┊ m8c10  ┊ 8262 ┊ InUse  ┊ Ok    ┊     Diskless ┊ 2021-01-05 20:22:14 ┊
╰──────────────────────────────────────────────────────────────────────────────────────────╯

linstor v l -r one-vm-6372-disk-0
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ Node   ┊ Resource           ┊ StoragePool          ┊ VolNr ┊ MinorNr ┊ DeviceName    ┊ Allocated ┊ InUse  ┊        State ┊
╞══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ m10c17 ┊ one-vm-6372-disk-0 ┊ thindata             ┊     0 ┊    2261 ┊ /dev/drbd2261 ┊ 19.38 GiB ┊ Unused ┊     UpToDate ┊
┊ m13c35 ┊ one-vm-6372-disk-0 ┊ thindata             ┊     0 ┊    2261 ┊ /dev/drbd2261 ┊ 20.01 GiB ┊ Unused ┊ Inconsistent ┊
┊ m8c10  ┊ one-vm-6372-disk-0 ┊ DfltDisklessStorPool ┊     0 ┊    2261 ┊ /dev/drbd2261 ┊           ┊ InUse  ┊     Diskless ┊
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

When logging in into the node, we can found that it is stuck in a sync state:

```
root@m13c35:~# drbdadm status one-vm-6372-disk-0
one-vm-6372-disk-0 role:Secondary
  disk:Inconsistent
  m10c17 role:Secondary
    replication:SyncTarget peer-disk:UpToDate done:51.52
  m8c10 role:Primary
    peer-disk:Diskless
```

Let's try to reconnect it to the second diskful replica:

```
root@m13c35:~# drbdadm disconnect one-vm-6372-disk-0:m10c17
root@m13c35:~# drbdadm connect one-vm-6372-disk-0:m10c17
root@m13c35:~# drbdadm status one-vm-6372-disk-0
one-vm-6372-disk-0 role:Secondary
  disk:Inconsistent
  m10c17 role:Secondary
    replication:SyncTarget peer-disk:UpToDate done:0.00
  m8c10 role:Primary
    peer-disk:Diskless
```

Hmm, now replication is stuck at zero percent. Damn, let's recreate the resource:

```
linstor r d m13c35 one-vm-6372-disk-0
linstor rd ap one-vm-6618-disk-9
linstor r l -r one-vm-6372-disk-0
╭────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port ┊ Usage  ┊ Conns ┊              State ┊ CreatedOn           ┊
╞════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-6372-disk-0 ┊ m10c17 ┊ 8262 ┊ Unused ┊ Ok    ┊           UpToDate ┊ 2021-02-03 09:43:31 ┊
┊ one-vm-6372-disk-0 ┊ m13c35 ┊ 8262 ┊ Unused ┊ Ok    ┊ SyncTarget(43.43%) ┊ 2021-07-09 13:36:51 ┊
┊ one-vm-6372-disk-0 ┊ m8c10  ┊ 8262 ┊ InUse  ┊ Ok    ┊           Diskless ┊ 2021-01-05 20:22:14 ┊
╰────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Hooray, replication has started!

**Note:** Case 7 shows that `drbdadm down / up` on`m13c35` would most likely bring the replica back to life.

## Case 4: StandAlone towards the diskless replica

```
linstor r l -r one-vm-8586-disk-0
╭───────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port ┊ Usage  ┊ Conns              ┊    State ┊ CreatedOn           ┊
╞═══════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-8586-disk-0 ┊ m11c42 ┊ 8543 ┊ Unused ┊ StandAlone(m13c34) ┊ Outdated ┊ 2020-11-28 22:07:23 ┊
┊ one-vm-8586-disk-0 ┊ m13c17 ┊ 8543 ┊ Unused ┊ Ok                 ┊ Diskless ┊                     ┊
┊ one-vm-8586-disk-0 ┊ m13c34 ┊ 8543 ┊ InUse  ┊ Connecting(m11c42) ┊ Diskless ┊ 2021-01-20 14:40:04 ┊
┊ one-vm-8586-disk-0 ┊ m15c36 ┊ 8543 ┊ Unused ┊ Ok                 ┊ UpToDate ┊                     ┊
╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Here we can see that the resource on `m11c42` is in`StandAlone` state towards the diskless replica on `m13c34`. Resources become `StandAlone` state when they found data inconsistencies among themselves. The fix is quite simple:

```
root@m11c42:~# drbdadm disconnect one-vm-8586-disk-0
root@m11c42:~# drbdadm connect one-vm-8586-disk-0 --discard-my-data
root@m11c42:~# drbdadm status one-vm-8586-disk-0
one-vm-8586-disk-0 role:Secondary
  disk:UpToDate
  m13c17 role:Secondary
    peer-disk:Diskless
  m13c34 role:Primary
    peer-disk:Diskless
  m15c36 role:Secondary
    peer-disk:UpToDate
```

## Case 5: StandAlone towards the diskful replica

Here we have a different situation, the resource on `m11c44` is in `StandAlone` towards another diskful replica on `m10c27`:

```
# linstor r l -r one-vm-8536-disk-0
╭───────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port ┊ Usage  ┊ Conns              ┊    State ┊ CreatedOn           ┊
╞═══════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-8536-disk-0 ┊ m10c27 ┊ 8656 ┊ Unused ┊ Connecting(m11c44) ┊ UpToDate ┊ 2021-02-02 17:41:36 ┊
┊ one-vm-8536-disk-0 ┊ m11c44 ┊ 8656 ┊ Unused ┊ StandAlone(m10c27) ┊ Outdated ┊ 2021-02-03 09:51:30 ┊
┊ one-vm-8536-disk-0 ┊ m13c29 ┊ 8656 ┊ Unused ┊ Ok                 ┊ Diskless ┊                     ┊
┊ one-vm-8536-disk-0 ┊ m13c9  ┊ 8656 ┊ InUse  ┊ Ok                 ┊ Diskless ┊ 2021-01-21 09:21:55 ┊
╰───────────────────────────────────────────────────────────────────────────────────────────────────╯

root@m11c44:~# drbdadm status one-vm-8536-disk-0
one-vm-8536-disk-0 role:Secondary
  disk:Outdated quorum:no
  m10c27 connection:StandAlone
  m13c29 role:Secondary
    peer-disk:Diskless
  m13c9 role:Primary
    peer-disk:Diskless
```

We can try to fix it, just like in the previous case:

```
root@m11c44:~# drbdadm disconnect one-vm-8536-disk-0
root@m11c44:~# drbdadm connect one-vm-8536-disk-0 --discard-my-data
root@m11c44:~# drbdadm status one-vm-8536-disk-0
one-vm-8536-disk-0 role:Secondary
  disk:Outdated quorum:no
  m10c27 connection:StandAlone
  m13c29 role:Secondary
    peer-disk:Diskless
  m13c9 role:Primary
    peer-disk:Diskless
```

But after connecting, the replica almost instantly returns back to `StandAlone`. In dmesg for this resource, you can see the error `Unrelated data, aborting!`:

```
[706520.163680] drbd one-vm-8536-disk-0/0 drbd2655 m10c27: drbd_sync_handshake:
[706520.163691] drbd one-vm-8536-disk-0/0 drbd2655 m10c27: self E54E31513A64A2EE:0000000000000000:35BC97142AF7A8A4:0000000000000000 bits:1266688 flags:3
[706520.163699] drbd one-vm-8536-disk-0/0 drbd2655 m10c27: peer 591D9E9CA26B4F98:66E67F43AB59AB30:4F01DD98B884F10E:0000000000000000 bits:24982941 flags:1100
[706520.163708] drbd one-vm-8536-disk-0/0 drbd2655 m10c27: uuid_compare()=unrelated-data by rule=history-both
[706520.163710] drbd one-vm-8536-disk-0/0 drbd2655: Unrelated data, aborting!
[706520.528669] drbd one-vm-8536-disk-0 m10c27: Aborting remote state change 1918960097
```

It is easier to delete and recreate such a resource:

```
linstor r d m11c44 one-vm-8536-disk-0
linstor rd ap one-vm-8536-disk-0
linstor r l -r one-vm-8536-disk-0
╭───────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port ┊ Usage  ┊ Conns ┊             State ┊ CreatedOn           ┊
╞═══════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-8536-disk-0 ┊ m10c27 ┊ 8656 ┊ Unused ┊ Ok    ┊          UpToDate ┊ 2021-02-02 17:41:36 ┊
┊ one-vm-8536-disk-0 ┊ m11c44 ┊ 8656 ┊ Unused ┊ Ok    ┊ SyncTarget(0.48%) ┊ 2021-07-09 15:40:17 ┊
┊ one-vm-8536-disk-0 ┊ m13c29 ┊ 8656 ┊ Unused ┊ Ok    ┊          Diskless ┊                     ┊
┊ one-vm-8536-disk-0 ┊ m13c9  ┊ 8656 ┊ InUse  ┊ Ok    ┊          Diskless ┊ 2021-01-21 09:21:55 ┊
╰───────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Case 6: Consistent replica

Almost the same as the previous case, but instead of `StandAlone`, the replica is marked as`Consistent`:

```
linstor r l -r one-vm-8379-disk-0
╭─────────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port ┊ Usage  ┊ Conns              ┊      State ┊ CreatedOn           ┊
╞═════════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-8379-disk-0 ┊ m13c40 ┊ 8052 ┊ Unused ┊ StandAlone(m14c6)  ┊ Consistent ┊ 2021-02-02 18:03:36 ┊
┊ one-vm-8379-disk-0 ┊ m14c15 ┊ 8052 ┊ InUse  ┊ Ok                 ┊   Diskless ┊ 2021-02-03 07:53:58 ┊
┊ one-vm-8379-disk-0 ┊ m14c6  ┊ 8052 ┊ Unused ┊ StandAlone(m13c40) ┊   UpToDate ┊                     ┊
╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯

linstor v l -r one-vm-8379-disk-0
╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ Node   ┊ Resource           ┊ StoragePool          ┊ VolNr ┊ MinorNr ┊ DeviceName    ┊ Allocated ┊ InUse  ┊      State ┊
╞════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ m13c40 ┊ one-vm-8379-disk-0 ┊ thindata             ┊     0 ┊    2051 ┊ /dev/drbd2051 ┊ 24.16 GiB ┊ Unused ┊ Consistent ┊
┊ m14c15 ┊ one-vm-8379-disk-0 ┊ DfltDisklessStorPool ┊     0 ┊    2051 ┊ /dev/drbd2051 ┊           ┊ InUse  ┊   Diskless ┊
┊ m14c6  ┊ one-vm-8379-disk-0 ┊ thindata             ┊     0 ┊    2051 ┊ /dev/drbd2051 ┊ 40.01 GiB ┊ Unused ┊   UpToDate ┊
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

In the dmesg you can see the `Unrelated data` errors:

```
root@m14c6:~# dmesg  |grep one-vm-8379-disk-0 | grep 'Unrelated data'
[2983657.291734] drbd one-vm-8379-disk-0/0 drbd2051: Unrelated data, aborting!
[2983659.335697] drbd one-vm-8379-disk-0/0 drbd2051: Unrelated data, aborting!
```

Let's recreate the device:

```
linstor r d m13c40 one-vm-8379-disk-0
linstor rd ap one-vm-8379-disk-0
linstor r l -r one-vm-8379-disk-0
╭───────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port ┊ Usage  ┊ Conns ┊             State ┊ CreatedOn           ┊
╞═══════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-8379-disk-0 ┊ m11c44 ┊ 8052 ┊ Unused ┊ Ok    ┊ SyncTarget(8.62%) ┊ 2021-07-09 15:44:51 ┊
┊ one-vm-8379-disk-0 ┊ m14c15 ┊ 8052 ┊ InUse  ┊ Ok    ┊          Diskless ┊ 2021-02-03 07:53:58 ┊
┊ one-vm-8379-disk-0 ┊ m14c6  ┊ 8052 ┊ Unused ┊ Ok    ┊          UpToDate ┊                     ┊
╰───────────────────────────────────────────────────────────────────────────────────────────────╯
```

Replication started, hurray!

## Case 7: Classic split-brain situation

Here we have two diskful replicas that cannot agree between themselves:

```
# linstor r l -r one-vm-8373-disk-2
╭───────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port ┊ Usage  ┊ Conns              ┊    State ┊ CreatedOn           ┊
╞═══════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-8373-disk-2 ┊ m11c12 ┊ 8069 ┊ InUse  ┊ Ok                 ┊ Diskless ┊ 2021-01-05 19:06:18 ┊
┊ one-vm-8373-disk-2 ┊ m13c23 ┊ 8069 ┊ Unused ┊ StandAlone(m14c6)  ┊ Outdated ┊                     ┊
┊ one-vm-8373-disk-2 ┊ m14c6  ┊ 8069 ┊ Unused ┊ StandAlone(m13c23) ┊ UpToDate ┊                     ┊
╰───────────────────────────────────────────────────────────────────────────────────────────────────╯

# linstor v l -r one-vm-8373-disk-2
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ Node   ┊ Resource           ┊ StoragePool          ┊ VolNr ┊ MinorNr ┊ DeviceName    ┊ Allocated ┊ InUse  ┊    State ┊
╞══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ m11c12 ┊ one-vm-8373-disk-2 ┊ DfltDisklessStorPool ┊     0 ┊    2068 ┊ /dev/drbd2068 ┊           ┊ InUse  ┊ Diskless ┊
┊ m13c23 ┊ one-vm-8373-disk-2 ┊ thindata             ┊     0 ┊    2068 ┊ /dev/drbd2068 ┊ 19.51 GiB ┊ Unused ┊ Outdated ┊
┊ m14c6  ┊ one-vm-8373-disk-2 ┊ thindata             ┊     0 ┊    2068 ┊ /dev/drbd2068 ┊ 19.51 GiB ┊ Unused ┊ UpToDate ┊
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Now we have to select the replica on which we want to replace the data, and perform reconnect with discard-my-data on it:

```
root@m13c23:~# drbdadm status one-vm-8373-disk-2
one-vm-8373-disk-2 role:Secondary
  disk:Outdated quorum:no
  m11c12 role:Primary
    peer-disk:Diskless
  m14c6 connection:StandAlone

root@m13c23:~# drbdadm disconnect one-vm-8373-disk-2
root@m13c23:~# drbdadm connect one-vm-8373-disk-2 --discard-my-data
root@m13c23:~# drbdadm status one-vm-8373-disk-2
one-vm-8373-disk-2 role:Secondary
  disk:Outdated quorum:no
  m11c12 role:Primary
    peer-disk:Diskless
  m14c6 connection:Connecting
```

It becomes to `Connecting`, now we need to reconnect the second replica:

```
root@m14c6:~# drbdadm disconnect  one-vm-8373-disk-2:m13c23
root@m14c6:~# drbdadm connect  one-vm-8373-disk-2:m13c23
root@m14c6:~# drbdadm status one-vm-8373-disk-2
one-vm-8373-disk-2 role:Secondary
  disk:UpToDate
  m11c12 role:Primary
    peer-disk:Diskless
  m13c23 role:Secondary congested:yes ap-in-flight:0 rs-in-flight:2264
    replication:SyncSource peer-disk:Inconsistent done:72.42

root@m14c6:~# drbdadm status one-vm-8373-disk-2
one-vm-8373-disk-2 role:Secondary
  disk:UpToDate
  m11c12 role:Primary
    peer-disk:Diskless
  m13c23 role:Secondary
    peer-disk:UpToDate
```

## Case 8: Stuck SyncTarget

Sync is stuck at 81.71% and does not move

```
# linstor r l -r one-vm-7584-disk-0
╭────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port ┊ Usage  ┊ Conns ┊              State ┊ CreatedOn           ┊
╞════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-7584-disk-0 ┊ m11c24 ┊ 8006 ┊ InUse  ┊ Ok    ┊           Diskless ┊ 2021-01-18 13:55:17 ┊
┊ one-vm-7584-disk-0 ┊ m13c3  ┊ 8006 ┊ Unused ┊ Ok    ┊ SyncTarget(81.71%) ┊                     ┊
┊ one-vm-7584-disk-0 ┊ m8c37  ┊ 8006 ┊ Unused ┊ Ok    ┊           UpToDate ┊ 2021-02-03 09:47:01 ┊
╰────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Let's try to reconnect:

```
root@m13c3:~# drbdadm status one-vm-7584-disk-0
one-vm-7584-disk-0 role:Secondary
  disk:Inconsistent
  m11c24 role:Primary
    peer-disk:Diskless
  m8c37 role:Secondary
    replication:SyncTarget peer-disk:UpToDate done:81.71

root@m13c3:~# drbdadm disconnect one-vm-7584-disk-0:m8c37
root@m13c3:~# drbdadm connect one-vm-7584-disk-0:m8c37
root@m13c3:~# drbdadm status one-vm-7584-disk-0
one-vm-7584-disk-0 role:Secondary
  disk:Inconsistent
  m11c24 role:Primary
    peer-disk:Diskless
  m8c37 role:Secondary
    replication:SyncTarget peer-disk:UpToDate done:0.00
```

Now replication is stuck at zero percent, let's try to completely extinguish the device and start again:

```
root@m13c3:~# drbdadm down one-vm-7584-disk-0
root@m13c3:~# drbdadm up one-vm-7584-disk-0
root@m13c3:~# drbdadm status one-vm-7584-disk-0
one-vm-7584-disk-0 role:Secondary
  disk:Inconsistent quorum:no
  m11c24 role:Primary
    peer-disk:Diskless
  m8c37 connection:Connecting

root@m13c3:~# drbdadm status one-vm-7584-disk-0
one-vm-7584-disk-0 role:Secondary
  disk:UpToDate
  m11c24 role:Primary
    peer-disk:Diskless
  m8c37 role:Secondary
    peer-disk:UpToDate
```

Hurray, job is done!

## Case 9: Outdated replica, which is Connecting

```
# linstor r l -r one-vm-7577-disk-2
╭────────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port  ┊ Usage  ┊ Conns              ┊    State ┊ CreatedOn           ┊
╞════════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-7577-disk-2 ┊ m10c21 ┊ 57064 ┊ Unused ┊ Ok                 ┊ Diskless ┊ 2021-02-05 20:52:31 ┊
┊ one-vm-7577-disk-2 ┊ m13c10 ┊ 57064 ┊ InUse  ┊ Ok                 ┊ UpToDate ┊ 2021-02-05 20:52:23 ┊
┊ one-vm-7577-disk-2 ┊ m14c29 ┊ 57064 ┊ Unused ┊ Connecting(m13c10) ┊ Outdated ┊ 2021-02-05 20:52:26 ┊
╰────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Similar to Case 2, and fixes the same way:

```
root@m14c29:~# drbdadm status one-vm-7577-disk-2
one-vm-7577-disk-2 role:Secondary
  disk:Outdated
  m10c21 role:Secondary
    peer-disk:Diskless
  m13c10 connection:Connecting

root@m14c29:~# drbdadm disconnect one-vm-7577-disk-2
root@m14c29:~# drbdadm connect one-vm-7577-disk-2
root@m14c29:~# drbdadm status one-vm-7577-disk-2
one-vm-7577-disk-2 role:Secondary
  disk:UpToDate
  m10c21 role:Secondary
    peer-disk:Diskless
  m13c10 role:Primary
    peer-disk:UpToDate
```

## Case 10: Unconnected / Connecting / NetworkFailure

**Note:** Caces 10 and 11 caused by [bug](https://github.com/LINBIT/linstor-server/issues/150#issuecomment-882489597), which should be fixed since LINSTOR v1.14.0 release

Resources are periodically flapping between these states:

```
# linstor r l -r one-vm-10154-disk-0
╭─────────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName        ┊ Node   ┊ Port  ┊ Usage  ┊ Conns              ┊    State ┊ CreatedOn           ┊
╞═════════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-10154-disk-0 ┊ m11c37 ┊ 56031 ┊ Unused ┊ Ok                 ┊ UpToDate ┊                     ┊
┊ one-vm-10154-disk-0 ┊ m15c6  ┊ 56031 ┊ Unused ┊ Connecting(m11c37) ┊ Diskless ┊ 2021-04-08 07:46:40 ┊
┊ one-vm-10154-disk-0 ┊ m8c11  ┊ 56031 ┊ Unused ┊ Unconnected(m8c8)  ┊ Outdated ┊                     ┊
┊ one-vm-10154-disk-0 ┊ m8c8   ┊ 56031 ┊ InUse  ┊ Unconnected(m8c11) ┊ Diskless ┊ 2021-04-08 09:04:32 ┊
╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯

# linstor r l -r one-vm-10154-disk-0
╭─────────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName        ┊ Node   ┊ Port  ┊ Usage  ┊ Conns              ┊    State ┊ CreatedOn           ┊
╞═════════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-10154-disk-0 ┊ m11c37 ┊ 56031 ┊ Unused ┊ Ok                 ┊ UpToDate ┊                     ┊
┊ one-vm-10154-disk-0 ┊ m15c6  ┊ 56031 ┊ Unused ┊ Connecting(m11c37) ┊ Diskless ┊ 2021-04-08 07:46:40 ┊
┊ one-vm-10154-disk-0 ┊ m8c11  ┊ 56031 ┊ Unused ┊ Connecting(m8c8)   ┊ Outdated ┊                     ┊
┊ one-vm-10154-disk-0 ┊ m8c8   ┊ 56031 ┊ InUse  ┊ Connecting(m8c11)  ┊ Diskless ┊ 2021-04-08 09:04:32 ┊
╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯

# linstor r l -r one-vm-10154-disk-0
╭───────────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName        ┊ Node   ┊ Port  ┊ Usage  ┊ Conns                ┊    State ┊ CreatedOn           ┊
╞═══════════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-10154-disk-0 ┊ m11c37 ┊ 56031 ┊ Unused ┊ Ok                   ┊ UpToDate ┊                     ┊
┊ one-vm-10154-disk-0 ┊ m15c6  ┊ 56031 ┊ Unused ┊ Connecting(m11c37)   ┊ Diskless ┊ 2021-04-08 07:46:40 ┊
┊ one-vm-10154-disk-0 ┊ m8c11  ┊ 56031 ┊ Unused ┊ NetworkFailure(m8c8) ┊ Outdated ┊                     ┊
┊ one-vm-10154-disk-0 ┊ m8c8   ┊ 56031 ┊ InUse  ┊ Connecting(m8c11)    ┊ Diskless ┊ 2021-04-08 09:04:32 ┊
╰───────────────────────────────────────────────────────────────────────────────────────────────────────╯

# linstor v l -r one-vm-10154-disk-0
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ Node   ┊ Resource            ┊ StoragePool          ┊ VolNr ┊ MinorNr ┊ DeviceName    ┊ Allocated ┊ InUse  ┊    State ┊
╞═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ m11c37 ┊ one-vm-10154-disk-0 ┊ thindata             ┊     0 ┊    3194 ┊ None          ┊ 70.66 GiB ┊ Unused ┊ UpToDate ┊
┊ m15c6  ┊ one-vm-10154-disk-0 ┊ DfltDisklessStorPool ┊     0 ┊    3194 ┊ /dev/drbd3194 ┊           ┊        ┊  Unknown ┊
┊ m8c11  ┊ one-vm-10154-disk-0 ┊ thindata             ┊     0 ┊    3194 ┊ /dev/drbd3194 ┊ 31.06 GiB ┊ Unused ┊ Outdated ┊
┊ m8c8   ┊ one-vm-10154-disk-0 ┊ DfltDisklessStorPool ┊     0 ┊    3194 ┊ /dev/drbd3194 ┊           ┊ InUse  ┊ Diskless ┊
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Check dmesg, if you see an `Peer presented a node_id of X instead of Y` error, then you faced a LINSTOR bug, and for some reason the IDs of the nodes were messed up:

```
[15962703.499997] drbd one-vm-10154-disk-0 m8c8: Peer presented a node_id of 2 instead of 3
[15962703.500003] drbd one-vm-10154-disk-0 m8c8: conn( Connecting -> NetworkFailure )
[15962703.551966] drbd one-vm-10154-disk-0 m8c8: Restarting sender thread
[15962703.552245] drbd one-vm-10154-disk-0 m8c8: Connection closed
[15962703.552251] drbd one-vm-10154-disk-0 m8c8: helper command: /sbin/drbdadm disconnected
[15962703.554361] drbd one-vm-10154-disk-0 m8c8: helper command: /sbin/drbdadm disconnected exit code 0
[15962703.554390] drbd one-vm-10154-disk-0 m8c8: conn( NetworkFailure -> Unconnected )
[15962704.555917] drbd one-vm-10154-disk-0 m8c8: conn( Unconnected -> Connecting )
```

Here you can see that m8c8 is represented for m8c11 as a node with `node-id:0`, but in fact it is `node-id:2`. Likewise, m8c8 sees m8c11 as a node with `node-id:0`, when it is actually `node-id: 0`:

```
root@m8c11:~# drbdsetup status one-vm-10154-disk-0 --verbose
one-vm-10154-disk-0 node-id:0 role:Secondary suspended:no
  volume:0 minor:3194 disk:Outdated quorum:yes blocked:no
  m11c37 node-id:1 connection:Connected role:Secondary congested:no ap-in-flight:0 rs-in-flight:0
    volume:0 replication:Established peer-disk:UpToDate resync-suspended:no
  m8c8 node-id:3 connection:Unconnected role:Unknown congested:no ap-in-flight:0 rs-in-flight:0
    volume:0 replication:Off peer-disk:DUnknown resync-suspended:no

root@m8c8:~# drbdsetup status one-vm-10154-disk-0 --verbose
one-vm-10154-disk-0 node-id:2 role:Primary suspended:no
  volume:0 minor:3194 disk:Diskless client:yes quorum:yes blocked:no
  m11c37 node-id:1 connection:Connected role:Secondary congested:no ap-in-flight:0 rs-in-flight:0
    volume:0 replication:Established peer-disk:UpToDate resync-suspended:no
  m8c11 node-id:0 connection:Unconnected role:Unknown congested:no ap-in-flight:0 rs-in-flight:0
    volume:0 replication:Off peer-disk:Outdated resync-suspended:no
```

This is a big problem for DRBD. In this case we have to migrate the virtual machine to a correct replica, delete all other resources and create new ones:

```
# linstor r d m15c6 m8c11 one-vm-10154-disk-0
# linstor r l -r one-vm-10154-disk-0
╭───────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName        ┊ Node   ┊ Port  ┊ Usage ┊ Conns ┊    State ┊ CreatedOn           ┊
╞═══════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-10154-disk-0 ┊ m11c37 ┊ 56031 ┊ InUse ┊ Ok    ┊ UpToDate ┊                     ┊
┊ one-vm-10154-disk-0 ┊ m15c6  ┊ 56031 ┊       ┊ Ok    ┊ DELETING ┊ 2021-04-08 07:46:40 ┊
┊ one-vm-10154-disk-0 ┊ m8c11  ┊ 56031 ┊       ┊ Ok    ┊ DELETING ┊                     ┊
╰───────────────────────────────────────────────────────────────────────────────────────╯

# linstor r l -r one-vm-10154-disk-0
╭───────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName        ┊ Node   ┊ Port  ┊ Usage ┊ Conns ┊    State ┊ CreatedOn           ┊
╞═══════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-10154-disk-0 ┊ m11c37 ┊ 56031 ┊ InUse ┊ Ok    ┊ UpToDate ┊                     ┊
╰───────────────────────────────────────────────────────────────────────────────────────╯

# linstor rd ap one-vm-10154-disk-0
╭──────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName        ┊ Node   ┊ Port  ┊ Usage  ┊ Conns ┊              State ┊ CreatedOn           ┊
╞══════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-10154-disk-0 ┊ m10c2  ┊ 56031 ┊ Unused ┊ Ok    ┊ SyncTarget(27.34%) ┊ 2021-07-09 14:55:47 ┊
┊ one-vm-10154-disk-0 ┊ m11c37 ┊ 56031 ┊ InUse  ┊ Ok    ┊           UpToDate ┊                     ┊
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Case 11: One of the diskful replicas has no connection to the diskless replica

**Note:** Caces 10 and 11 caused by [bug](https://github.com/LINBIT/linstor-server/issues/150#issuecomment-882489597), which should be fixed since LINSTOR v1.14.0 release

```
linstor r l -r one-vm-8760-disk-0
╭────────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port  ┊ Usage  ┊ Conns              ┊    State ┊ CreatedOn           ┊
╞════════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-8760-disk-0 ┊ m13c18 ┊ 55165 ┊ Unused ┊ Connecting(m8c9)   ┊ Outdated ┊                     ┊
┊ one-vm-8760-disk-0 ┊ m14c27 ┊ 55165 ┊ Unused ┊ Ok                 ┊ UpToDate ┊ 2021-02-03 12:00:35 ┊
┊ one-vm-8760-disk-0 ┊ m8c9   ┊ 55165 ┊ InUse  ┊ Connecting(m13c18) ┊ Diskless ┊ 2021-04-08 09:04:07 ┊
╰────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Let's try some magic here:

```
root@m13c18:~# drbdadm down one-vm-8760-disk-0
root@m13c18:~# drbdadm up one-vm-8760-disk-0
root@m13c18:~# drbdadm status one-vm-8760-disk-0
one-vm-8760-disk-0 role:Secondary
  disk:Outdated
  m14c27 role:Secondary
    peer-disk:UpToDate
  m8c9 connection:Connecting
root@m13c18:~# drbdadm status one-vm-8760-disk-0
one-vm-8760-disk-0 role:Secondary
  disk:Outdated
  m14c27 role:Secondary
    peer-disk:UpToDate
  m8c9 connection:Unconnected

root@m8c9:~# drbdadm disconnect one-vm-8760-disk-0:m13c18
root@m8c9:~# drbdadm connect one-vm-8760-disk-0:m13c18
root@m8c9:~# drbdadm status one-vm-8760-disk-0
one-vm-8760-disk-0 role:Primary
  disk:Diskless
  m13c18 connection:Unconnected
  m14c27 role:Secondary
    peer-disk:UpToDate
```

Damn, the same situation as in the previous case:

```
linstor r l -r one-vm-8760-disk-0
╭──────────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port  ┊ Usage  ┊ Conns                ┊    State ┊ CreatedOn           ┊
╞══════════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-8760-disk-0 ┊ m13c18 ┊ 55165 ┊ Unused ┊ NetworkFailure(m8c9) ┊ Outdated ┊                     ┊
┊ one-vm-8760-disk-0 ┊ m14c27 ┊ 55165 ┊ Unused ┊ Ok                   ┊ UpToDate ┊ 2021-02-03 12:00:35 ┊
┊ one-vm-8760-disk-0 ┊ m8c9   ┊ 55165 ┊ InUse  ┊ Unconnected(m13c18)  ┊ Diskless ┊ 2021-04-08 09:04:07 ┊
╰──────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Check dmesg:

```
[14635995.191931] drbd one-vm-8760-disk-0 m8c9: conn( Unconnected -> Connecting )
[14635995.740020] drbd one-vm-8760-disk-0 m8c9: Peer presented a node_id of 3 instead of 2
[14635995.740051] drbd one-vm-8760-disk-0 m8c9: conn( Connecting -> NetworkFailure )
[14635995.775994] drbd one-vm-8760-disk-0 m8c9: Restarting sender thread
[14635995.777153] drbd one-vm-8760-disk-0 m8c9: Connection closed
[14635995.777174] drbd one-vm-8760-disk-0 m8c9: helper command: /sbin/drbdadm disconnected
[14635995.789649] drbd one-vm-8760-disk-0 m8c9: helper command: /sbin/drbdadm disconnected exit code 0
[14635995.789707] drbd one-vm-8760-disk-0 m8c9: conn( NetworkFailure -> Unconnected )
```

Yep, exactly! The node IDs are messed up again.

```
root@m8c9:~# drbdsetup status one-vm-8760-disk-0 --verbose
one-vm-8760-disk-0 node-id:3 role:Primary suspended:no
  volume:0 minor:1016 disk:Diskless client:yes quorum:yes blocked:no
  m13c18 node-id:0 connection:Unconnected role:Unknown congested:no ap-in-flight:0 rs-in-flight:0
    volume:0 replication:Off peer-disk:Outdated resync-suspended:no
  m14c27 node-id:1 connection:Connected role:Secondary congested:no ap-in-flight:0 rs-in-flight:0
    volume:0 replication:Established peer-disk:UpToDate resync-suspended:no

root@m13c18:~# drbdsetup status one-vm-8760-disk-0 --verbose
one-vm-8760-disk-0 node-id:0 role:Secondary suspended:no
  volume:0 minor:1016 disk:Outdated quorum:yes blocked:no
  m14c27 node-id:1 connection:Connected role:Secondary congested:no ap-in-flight:0 rs-in-flight:0
    volume:0 replication:Established peer-disk:UpToDate resync-suspended:no
  m8c9 node-id:2 connection:Unconnected role:Unknown congested:no ap-in-flight:0 rs-in-flight:0
    volume:0 replication:Off peer-disk:DUnknown resync-suspended:no

root@m14c27:~# drbdsetup status one-vm-8760-disk-0 --verbose
one-vm-8760-disk-0 node-id:1 role:Secondary suspended:no
  volume:0 minor:1016 disk:UpToDate quorum:yes blocked:no
  m13c18 node-id:0 connection:Connected role:Secondary congested:no ap-in-flight:0 rs-in-flight:0
    volume:0 replication:Established peer-disk:Outdated resync-suspended:no
  m8c9 node-id:3 connection:Connected role:Primary congested:no ap-in-flight:0 rs-in-flight:0
    volume:0 replication:Established peer-disk:Diskless peer-client:yes resync-suspended:no
```

m13c18 sees m8c9 as `node-id:2`, but in fact it is `node-id:3`. We have to migrate the VM to a correct replica and recreate the rest of them:

```
# linstor r l -r one-vm-8760-disk-0
╭─────────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port  ┊ Usage  ┊ Conns               ┊    State ┊ CreatedOn           ┊
╞═════════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-8760-disk-0 ┊ m13c18 ┊ 55165 ┊ Unused ┊ Unconnected(m8c9)   ┊ Outdated ┊                     ┊
┊ one-vm-8760-disk-0 ┊ m14c27 ┊ 55165 ┊ Unused ┊ Ok                  ┊ UpToDate ┊ 2021-02-03 12:00:35 ┊
┊ one-vm-8760-disk-0 ┊ m8c9   ┊ 55165 ┊ InUse  ┊ Unconnected(m13c18) ┊ Diskless ┊ 2021-04-08 09:04:07 ┊
╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯

# linstor r l -r one-vm-8760-disk-0
╭───────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port  ┊ Usage  ┊ Conns ┊    State ┊ CreatedOn           ┊
╞═══════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-8760-disk-0 ┊ m13c18 ┊ 55165 ┊ Unused ┊ Ok    ┊ UpToDate ┊                     ┊
┊ one-vm-8760-disk-0 ┊ m14c27 ┊ 55165 ┊ InUse  ┊ Ok    ┊ UpToDate ┊ 2021-02-03 12:00:35 ┊
╰───────────────────────────────────────────────────────────────────────────────────────╯

# linstor r d m13c18 one-vm-8760-disk-0
# linstor rd ap one-vm-8760-disk-0
# linstor r l -r one-vm-8760-disk-0
╭─────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ ResourceName       ┊ Node   ┊ Port  ┊ Usage  ┊ Conns ┊              State ┊ CreatedOn           ┊
╞═════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ one-vm-8760-disk-0 ┊ m14c27 ┊ 55165 ┊ InUse  ┊ Ok    ┊           UpToDate ┊ 2021-02-03 12:00:35 ┊
┊ one-vm-8760-disk-0 ┊ m8c6   ┊ 55165 ┊ Unused ┊ Ok    ┊ SyncTarget(78.57%) ┊ 2021-07-09 15:30:55 ┊
╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Case 12: Consistent replica

We are on a diskless node and looking at the resource states:

```
root@m11c39:~# drbdadm status one-vm-6967-disk-0
one-vm-6967-disk-0 role:Primary
  disk:Diskless
  m13c15 role:Secondary
    peer-disk:Consistent
  m14c40 role:Secondary
    peer-disk:UpToDate
```

This is an very unpleasant situation. Both diskfull replicas are `UpToDate`, but the diskless replica works only with one of them, the second is marked as `Consistent`. It occurs as a result of bug with the dikless primary on 9.0.19, . However I also managed to catch it on 9.0.21, but much less often.

When you try to disconnect the resource on the `m14c40` node, you will see that this is impossible, since the diskless replica is currently using it:

```
root@m14c40:~# drbdadm disconnect one-vm-6967-disk-0
one-vm-6967-disk-0: State change failed: (-10) State change was refused by peer node
additional info from kernel:
Declined by peer m11c39 (id: 3), see the kernel log there
Command 'drbdsetup disconnect one-vm-6967-disk-0 3' terminated with exit code 11
```

This can be fixed as follows:

Do the disconnect and invalidate on Consistent node:

```
root@m13c15:~# drbdadm disconnect one-vm-6967-disk-0
root@m13c15:~# drbdadm invalidate one-vm-6967-disk-0
root@m13c15:~# drbdadm connect one-vm-6967-disk-0
root@m13c15:~# drbdadm status one-vm-6967-disk-0
one-vm-6967-disk-0 role:Secondary
  disk:Inconsistent
  m11c39 role:Primary
    peer-disk:Diskless
  m14c40 role:Secondary
    replication:SyncTarget peer-disk:UpToDate done:3.04
```

Here we see that the synchronization was completed, but the resource become into `Inconsistent` state:

```
root@m13c15:~# drbdadm status one-vm-6967-disk-0
one-vm-6967-disk-0 role:Secondary
  disk:Inconsistent
  m11c39 role:Primary
    peer-disk:Diskless
  m14c40 role:Secondary
    peer-disk:UpToDate
```

To solve this situation, you need to perform the disconnect/connect operation with the other diskful replica:

```
root@m13c15:~# drbdadm disconnect one-vm-6967-disk-0:m14c40
root@m13c15:~# drbdadm connect one-vm-6967-disk-0:m14c40
root@m13c15:~# drbdadm status one-vm-6967-disk-0
one-vm-6967-disk-0 role:Secondary
  disk:UpToDate
  m11c39 role:Primary
    peer-disk:Diskless
  m14c40 role:Secondary
    peer-disk:UpToDate
```

## Case 13: Forgotten resource

In older versions of LINSTOR it was possible to face a bug when a resource was deleted but diskless replicas remained on the node:

```
one-vm-7792-disk-0 role:Secondary
  disk:Diskless quorum:no
  m13c9 connection:Connecting
  m14c13 connection:Connecting
```

This resource is not existing in LINSTOR anymore:

```
linstor r l -r one-vm-7792-disk-0
```

So we can safely shut it down via drbdsetup:

```
root@m14c43:~# drbdsetup down one-vm-7792-disk-0
```

**Note:** drbdsetup is a lower-level utility than drbdadm. drbdsetup communicates directly with the kernel and does not require a config file for the drbd resource.

## Case 14: Corrupted bitmap

And finally, the most delicious. A DRBD bug that was found in 9.0.19 version, but was later fixed. Let's say you have just created a new replica on m10c23, it has synchronized and went into this state:

```
# linstor v l -r one-vm-5460-disk-2
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
┊ Node   ┊ Resource           ┊ StoragePool          ┊ VolNr ┊ MinorNr ┊ DeviceName    ┊ Allocated ┊ InUse  ┊    State ┊
╞══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╡
┊ m10c23 ┊ one-vm-5460-disk-2 ┊ thindata             ┊     0 ┊    2665 ┊ /dev/drbd2665 ┊ 11.71 GiB ┊ Unused ┊ UpToDate ┊
┊ m11c35 ┊ one-vm-5460-disk-2 ┊ DfltDisklessStorPool ┊     0 ┊    2665 ┊ /dev/drbd2665 ┊           ┊ InUse  ┊ Diskless ┊
┊ m14c2  ┊ one-vm-5460-disk-2 ┊ diskless             ┊     0 ┊    2665 ┊ /dev/drbd2665 ┊           ┊ InUse  ┊ Diskless ┊
┊ m15c17 ┊ one-vm-5460-disk-2 ┊ thindata             ┊     0 ┊    2665 ┊ /dev/drbd2665 ┊ 28.01 GiB ┊ Unused ┊ UpToDate ┊
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

Both replicas are `UpToDate`, but note the Allocated size. One of them uses much less space than the other one.

According the DRBD logic, the primary diskless replica works with all secondary replicas, that is, it reads and writes to both diskful replicas at once.

Thus, the virtual machine will begin to be confused as it will read some data from the normal replica, and some from the bad one, thereby damaging its own file system.

The cause of this problem is a broken bitmap, and now we need to fix it.

The fact is that DRBD has some kind of changelog inside the device, which records where and what data was changed during the time. Thus, in case of disconnect and reconnection, only the changed data is synchronized, but not the entire device. In other words, now, as a result of a DRBD bug, we have an incorrect changelog.

Here I would like to note right away that there is a difference in the logic of the classic DRBD and how LINSTOR works with it. The fact is that LINSTOR stores the zero-day value of the changelog in its metadata and sets this value each time when a new replica is created. Thus, changes to a new replica are synchronized only according to the changelog. Due to this, if the changelog is small, then the synchronization is completed very quickly, unlike the case of performing full initial synchronization.

While the standard DRBD logic does not offer such an "improvement" and performs full resync every time for all new replicas, that is, even if your changelog is damaged, synchronization will always be successful.

You can diagnose differences in two replicas by running the command `drbdadm verify` on one of them, for example:

```
drbdadm verify one-vm-5460-disk-2:m15c17
```

Will perform the check `one-vm-5460-disk-2` against the resource located on `m15c17`

After that, all unsynchronized sectors will be marked for synchronization, and it will be enough to do:

```
drbdadm disconnect one-vm-5460-disk-2
drbdadm connect one-vm-5460-disk-2
```

To start the syncing. An alternative solution would be to invalidate the entire replica at once and reconnect it:

```
drbdadm disconnect one-vm-5460-disk-2
drbdadm invalidate one-vm-5460-disk-2
drbdadm connect one-vm-5460-disk-2
```

Then it will be fully synchronized. But even though the sync is successful, it will continue to have the wrong changelog. Thus, all new replicas synchronized through the changelog will have the same problem again.

Okay, we're done with the theory, now let's get back to our situation. Usually, in this case, it makes sense to immediately delete the created replica and perform the following actions:

Shutdown our virtual machine, or if this action is not available make an external snapshot, and then run:

```
dd if=/dev/drbd2665 of=/dev/drbd2665 status=progress bs=65536 conv=notrunc,sparse iflag=direct,fullblock oflag=direct
```

Here dd will read and write it back by byte the entire device, thereby correcting our changelog. Do not forget to commit our external snapshot (if you did), and now you can safely create new replicas using LINSTOR.

That's all for now. Thank you for your attention. Hope it is useful to you.

[Read on DEV →](https://dev.to/kvaps/troubleshooting-drbd9-in-linstor-40fn)
