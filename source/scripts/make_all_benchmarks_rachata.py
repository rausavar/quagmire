#!/usr/bin/python

import os
import sys
import re
import subprocess
import argparse

home = "/home/rachata"
subprocess.call("source set_env_rachata.sh",shell=True)
# BFS 
#os.chdir(home + "/gpgpu-sim/benchmarks/CUDA/BFS/")
#subprocess.call("make clean",shell=True)
#subprocess.call("make -i",shell=True)
#print "BFS compiled\n"
os.chdir(home + "/gpgpu-sim/benchmarks/CUDA/JPEG/")
subprocess.call("pwd")
subprocess.call("make clean",shell=True)
subprocess.call("make -i",shell=True)
print "JPEG compiled\n"
os.chdir(home + "/gpgpu-sim/benchmarks/CUDA/LPS/")
subprocess.call("make clean",shell=True)
subprocess.call("make -i",shell=True)
print "LPS compiled\n"
os.chdir(home + "/gpgpu-sim/benchmarks/CUDA/MUM/")
subprocess.call("make clean",shell=True)
subprocess.call("make -i",shell=True)
print "MUM compiled\n"
os.chdir(home + "/gpgpu-sim/benchmarks/CUDA/NN/")
subprocess.call("make clean",shell=True)
subprocess.call("make -i",shell=True)
print "NN compiled\n"
os.chdir(home + "/gpgpu-sim/benchmarks/CUDA/STO/")
subprocess.call("make clean",shell=True)
subprocess.call("make -i",shell=True)
print "STO compiled\n"
os.chdir(home + "/gpgpu-sim/benchmarks/CUDA/SCP/")
subprocess.call("make clean",shell=True)
subprocess.call("make -i",shell=True)
print "SCP compiled\n"
os.chdir(home + "/gpgpu-sim/benchmarks/Mars/sample_apps/PageViewRank/")
subprocess.call("make clean",shell=True)
subprocess.call("make -i",shell=True)
print "PVR compiled\n"
os.chdir(home + "/gpgpu-sim/benchmarks/Mars/sample_apps/PageViewCount/")
subprocess.call("make clean",shell=True)
subprocess.call("make -i",shell=True)
print "PVC compiled\n"
os.chdir(home + "/gpgpu-sim/benchmarks/Mars/sample_apps/SimilarityScore/")
subprocess.call("make clean",shell=True)
subprocess.call("make -i",shell=True)
print "SimilarityScore compiled\n"
os.chdir(home + "/gpgpu-sim/benchmarks/Mars/sample_apps/InvertedIndex/")
subprocess.call("make clean",shell=True)
subprocess.call("make -i",shell=True)
print "InvertedIndex compiled\n"
os.chdir(home + "/gpgpu-sim/benchmarks/rodinia/cuda/backprop/")
subprocess.call("make clean",shell=True)
subprocess.call("make -i",shell=True)
print "backprop compiled\n"
os.chdir(home + "/gpgpu-sim/benchmarks/rodinia/cuda/hotspot/")
subprocess.call("make clean",shell=True)
subprocess.call("make -i",shell=True)
print "hotspot compiled\n"
os.chdir(home + "/gpgpu-sim/benchmarks/rodinia/cuda/streamcluster/")
subprocess.call("make clean",shell=True)
subprocess.call("make -i",shell=True)
print "streamcluster compiled\n"
os.chdir(home + "/gpgpu-sim/benchmarks/lonestar/")
subprocess.call("make -f Makefile.rachata clean",shell=True)
subprocess.call("make -f Makefile.rachata",shell=True)
print "lonestar compiled\n"
