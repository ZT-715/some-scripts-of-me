#!bin/bash
# Script to set enviroment to the LFS.

echo 'LFS device partiton path':
read partition
if [[ -e $partition ]] 
	then echo '...'
else echo "Please insert an usable umounted partition"
fi

export LFS=/mnt/lfs;

if [[ !(-e $LFS) ]] 
	then mkdir -pv $LFS
fi
mount -v -t ext4 $partition $LFS

if [[ !(-e $LFS/usr) ]] 
	then mkdir -v ${LFS}/usr
fi
mount -v -t ext4 $partition ${LFS}/usr

