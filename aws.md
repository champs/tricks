Adding new EBS volumn to EC2
1.) Use the lsblk command to view your available disk devices and their mount points (if applicable) to help you determine the correct device name to use.
```
>> lsblk 
exablox@ip-10-0-2-201:~$ lsblk
NAME                              MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
xvda                              202:0    0    20G  0 disk 
└─xvda1                           202:1    0    20G  0 part /
xvdb                              202:16   0   500G  0 disk 
loop0                               7:0    0   100G  0 loop 
└─docker-202:1-271709-pool (dm-0) 252:0    0   100G  0 dm   
loop1                               7:1    0     2G  0 loop 
└─docker-202:1-271709-pool (dm-0) 252:0    0   100G  0 dm   
```



2.) list special information, such as file system type.
```
sudo file -s /dev/xvdb
```
3.) sudo mkfs -t ext4 /dev/xvdb  Make filesystem on device
```
exablox@ip-10-0-2-201:~$ sudo mkfs -t ext4 /dev/xvdb
sudo: unable to resolve host ip-10-0-2-201
mke2fs 1.42.9 (4-Feb-2014)
Filesystem label=
OS type: Linux
Block size=4096 (log=2)
Fragment size=4096 (log=2)
Stride=0 blocks, Stripe width=0 blocks
32768000 inodes, 131072000 blocks
6553600 blocks (5.00%) reserved for the super user
First data block=0
Maximum filesystem blocks=4294967296
4000 block groups
32768 blocks per group, 32768 fragments per group
8192 inodes per group
Superblock backups stored on blocks: 
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 
	4096000, 7962624, 11239424, 20480000, 23887872, 71663616, 78675968, 
	102400000

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (32768 blocks): done
Writing superblocks and filesystem accounting information: done     
```

4.) sudo mkdir /mnt/data

5.) edit fstab make sure fs is persist after reboot
```
exablox@ip-10-0-2-201:~$ sudo cat /etc/fstab
sudo: unable to resolve host ip-10-0-2-201
LABEL=cloudimg-rootfs	/	 ext4	defaults,discard	0 0
/dev/xvdb	/mnt/data	ext4	defaults,nobootwait,nofail	0	2
```
6.) sudo mount -a
