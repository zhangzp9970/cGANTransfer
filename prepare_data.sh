#!/bin/bash
python make_hdf5.py --dataset I128 --batch_size 256 --data_root /mnt/efs/fs1/MG/data/
python calculate_inception_moments.py --dataset I128_hdf5 --data_root /mnt/efs/fs1/MG/data/

