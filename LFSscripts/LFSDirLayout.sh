#! bin/bash
# set directories for LFS partition

export LFS=/mnt/lfs;

if [[ -e $LFS ]]
	then mkdir -pv $LFS/{bin,etc,lib,lib64,sbin,usr,var,tools,sources}
fi
