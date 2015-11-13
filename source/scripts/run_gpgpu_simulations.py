#!/usr/bin/python

import os
import sys
import re
import subprocess
import argparse


HOME = "/home/nandita/GPUSims/"
CONFIG_DIR = "/home/nandita/GPU_PROJECT/gpgpusim_configs/"
BASH_SCRIPTS = "./run_scripts/"

batch1 = ["CUDA","BFS", "JPEG", "LPS"]
batch2 = ["CUDA","MUM", "NN"]
batch3 = ["CUDA","STO", "CONS", "SCP"]

batch4 = ["parboil","sad", "spmv"]

batch5 = ["rodinia","backprop", "hotspot", "streamcluster"]

batch6 = ["Mars","PageViewCount", "PageViewRank", "SimilarityScore", "InvertedIndex"]

batch7 = ["lonestar","bfs", "bh", "dmr"]
batch8 = ["lonestar","mst", "sp", "sssp"]

batch_list = [batch1,batch2,batch3,batch4,batch5,batch6,batch7,batch8]

parser = argparse.ArgumentParser('Launch gpgpusim jobs')
parser.add_argument('-configs',required=True,type=str,dest='configs')
parser.add_argument('-label',required=True,type=str,dest='label')
parser.add_argument('-batch',required=True,type=str,dest='batch')
parser.add_argument('-result_dir',required=True,type=str,dest='result_dir')
args = parser.parse_args()

bin_path = {}
bin_path["JPEG"] = "/gpu-compression/gpgpu-sim/benchmarks/CUDA/JPEG/gpgpu_ptx_sim__JPEG" 
bin_path["BFS"] = "/gpu-compression/gpgpu-sim/benchmarks/CUDA/BFS/gpgpu_ptx_sim__BFS" 
bin_path["LPS"] = "/gpu-compression/gpgpu-sim/benchmarks/CUDA/LPS/gpgpu_ptx_sim__LPS" 
bin_path["MUM"] = "/gpu-compression/gpgpu-sim/benchmarks/CUDA/MUM/gpgpu_ptx_sim__MUM" 
bin_path["SCP"] = "/gpu-compression/gpgpu-sim/benchmarks/CUDA/SCP/gpgpu_ptx_sim__SCP" 	
bin_path["NN"] = "/gpu-compression/gpgpu-sim/benchmarks/CUDA/NN/gpgpu_ptx_sim__NN" 	
bin_path["STO"] = "/gpu-compression/gpgpu-sim/benchmarks/CUDA/STO/gpgpu_ptx_sim__STO" 	
bin_path["CONS"] = "/gpu-compression/gpgpu-sim/benchmarks/CUDA/CONS/gpgpu_ptx_sim__CONS" 	
bin_path["backprop"] = "/gpu-compression/gpgpu-sim/benchmarks/rodinia/cuda/backprop/gpgpu_ptx_sim__backprop" 	
bin_path["hotspot"] = "/gpu-compression/gpgpu-sim/benchmarks/rodinia/cuda/hotspot/gpgpu_ptx_sim__hotspot" 	
bin_path["streamcluster"] = "/gpu-compression/gpgpu-sim/benchmarks/rodinia/cuda/streamcluster/gpgpu_ptx_sim__streamcluster" 	
bin_path["PageViewCount"] = "/gpu-compression/gpgpu-sim/benchmarks/Mars/sample_apps/PageViewCount/gpgpu_ptx_sim__PageViewCount" 	
bin_path["PageViewRank"] = "/gpu-compression/gpgpu-sim/benchmarks/Mars/sample_apps/PageViewRank/gpgpu_ptx_sim__PageViewRank" 	
bin_path["InvertedIndex"] = "/gpu-compression/gpgpu-sim/benchmarks/Mars/sample_apps/InvertedIndex/gpgpu_ptx_sim__InvertedIndex" 	
bin_path["SimilarityScore"] = "/gpu-compression/gpgpu-sim/benchmarks/Mars/sample_apps/SimilarityScore/gpgpu_ptx_sim__SimilarityScore" 	
bin_path["bfs"] = "/gpu-compression/gpgpu-sim/benchmarks/lonestar/bin/bfs" 	
bin_path["bh"] = "/gpu-compression/gpgpu-sim/benchmarks/lonestar/bin/bh" 	
bin_path["dmr"] = "/gpu-compression/gpgpu-sim/benchmarks/lonestar/bin/dmr" 	
bin_path["mst"] = "/gpu-compression/gpgpu-sim/benchmarks/lonestar/bin/mst" 	
bin_path["sp"] = "/gpu-compression/gpgpu-sim/benchmarks/lonestar/bin/sp" 	
bin_path["sssp"] = "/gpu-compression/gpgpu-sim/benchmarks/lonestar/bin/sssp" 	

input_path = {}
input_path["JPEG"] = "/gpu-compression/gpgpu-sim/benchmarks/CUDA/JPEG/data" 
input_path["MUM"] = "/gpu-compression/gpgpu-sim/benchmarks/CUDA/MUM/data" 
input_path["BFS"] = "/gpu-compression/gpgpu-sim/benchmarks/CUDA/BFS/data" 
input_path["SCP"] = "/gpu-compression/gpgpu-sim/benchmarks/CUDA/SCP/data" 
input_path["NN"] = "/gpu-compression/gpgpu-sim/benchmarks/CUDA/NN/data" 
input_path["STO"] = "/gpu-compression/gpgpu-sim/benchmarks/CUDA/STO/data" 
input_path["CONS"] = "/gpu-compression/gpgpu-sim/benchmarks/CUDA/CONS/data" 
input_path["hotspot"] = "/gpu-compression/gpgpu-sim/benchmarks/rodinia/data" 	
input_path["PageViewCount"] = "/gpu-compression/gpgpu-sim/benchmarks/Mars/sample_apps/PageViewCount/data" 	
input_path["PageViewRank"] = "/gpu-compression/gpgpu-sim/benchmarks/Mars/sample_apps/PageViewRank/data" 	
input_path["PageViewCount"] = "/gpu-compression/gpgpu-sim/benchmarks/Mars/sample_apps/PageViewCount/data" 	
input_path["InvertedIndex"] = "/gpu-compression/gpgpu-sim/benchmarks/Mars/sample_apps/InvertedIndex/data" 	
input_path["bfs"] = "/gpu-compression/gpgpu-sim/benchmarks/lonestar/inputs"	
input_path["bh"] = "/gpu-compression/gpgpu-sim/benchmarks/lonestar/inputs" 	
input_path["dmr"] = "/gpu-compression/gpgpu-sim/benchmarks/lonestar/inputs" 	
input_path["mst"] = "/gpu-compression/gpgpu-sim/benchmarks/lonestar/inputs" 	
input_path["sp"] = "/gpu-compression/gpgpu-sim/benchmarks/lonestar/inputs" 	
input_path["sssp"] = "/gpu-compression/gpgpu-sim/benchmarks/lonestar/inputs" 	

configs = args.configs.split(',')
i = 0
batches = []
for batch in args.batch.split(','):
	batches += [batch_list[int(batch)-1]]

print ("mkdir " + args.result_dir + "/" + args.label)
subprocess.call("mkdir " + args.result_dir + "/" + args.label,shell=True)
RESULTS = args.result_dir + "/" + args.label

for batch in batches:
	for benchmark in batch[1:] :
		for config in configs : 
			filepath = "/" + config + "/" + batch[0] + "/" + benchmark + "/"
			if(not os.path.isdir(RESULTS + filepath)):
				subprocess.call("mkdir -p " + RESULTS + filepath,shell=True)
			os.chdir(RESULTS + filepath)
			subprocess.call("ln -s " + HOME + bin_path[benchmark] + " .",shell=True)
			subprocess.call("cp " + CONFIG_DIR + "/" + config + "/* .",shell=True)
			if (benchmark in ["LPS","SimilarityScore","streamcluster","backprop"]):
				pass
			else:
				subprocess.call("ln -s " + HOME + input_path[benchmark] + " .",shell=True)	
			subprocess.call("ln -s " + BASH_SCRIPTS + "/" + batch[0] + "/mainscript_" + benchmark + " .",shell=True)
			subprocess.call("chmod 777 mainscript_" + benchmark,shell=True)	
			print ("Running " + benchmark + " - "  + config)
			os.system("sh mainscript_" + benchmark + " &")


