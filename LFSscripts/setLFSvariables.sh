#!bin/bash
# Script to set enviromental variables to the LFS.

echo 'LFS partiton path':;
read;
partition=${REPLY}


export LFS=/mnt/lfs;
mkdir -pv $LFS;
mount -v -t ext4 $partition $LFS;
mkdir -v ${LFS}/usr;
mount -v -t ext4 $partition ${LFS}/usr;

