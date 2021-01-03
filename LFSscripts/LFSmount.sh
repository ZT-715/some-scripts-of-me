#!bin/bash
# Script to mount LFS partiton.

echo 'LFS device partiton path:'
read partition
if [[ -e $partition ]] 
	then echo '...'
else echo "Please insert an usable unmounted partition"
fi

export LFS=/mnt/lfs;

if [[ !(-e $LFS) ]] 
	then mkdir -pv $LFS
fi
mount -v -t ext4 $partition $LFS
