#!/usr/bin/python

import os
import sys
import re
import subprocess
import argparse


HOME = "/home/rachata/gpgpu-sim"
CONFIG_DIR = "/home/rachata/gpgpu-sim/v3.x/configs/"
BASH_SCRIPTS = "/home/rachata/gpgpu-sim/scripts/run_scripts"

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
bin_path["JPEG"] = "/benchmarks/CUDA/JPEG/gpgpu_ptx_sim__JPEG" 
bin_path["BFS"] = "/benchmarks/CUDA/BFS/gpgpu_ptx_sim__BFS" 
bin_path["LPS"] = "/benchmarks/CUDA/LPS/gpgpu_ptx_sim__LPS" 
bin_path["MUM"] = "/benchmarks/CUDA/MUM/gpgpu_ptx_sim__MUM" 
bin_path["SCP"] = "/benchmarks/CUDA/SCP/gpgpu_ptx_sim__SCP" 	
bin_path["NN"] = "/benchmarks/CUDA/NN/gpgpu_ptx_sim__NN" 	
bin_path["STO"] = "/benchmarks/CUDA/STO/gpgpu_ptx_sim__STO" 	
bin_path["CONS"] = "/benchmarks/CUDA/CONS/gpgpu_ptx_sim__CONS" 	
bin_path["backprop"] = "/benchmarks/rodinia/cuda/backprop/gpgpu_ptx_sim__backprop" 	
bin_path["hotspot"] = "/benchmarks/rodinia/cuda/hotspot/gpgpu_ptx_sim__hotspot" 	
bin_path["streamcluster"] = "/benchmarks/rodinia/cuda/streamcluster/gpgpu_ptx_sim__streamcluster" 	
bin_path["PageViewCount"] = "/benchmarks/Mars/sample_apps/PageViewCount/gpgpu_ptx_sim__PageViewCount" 	
bin_path["PageViewRank"] = "/benchmarks/Mars/sample_apps/PageViewRank/gpgpu_ptx_sim__PageViewRank" 	
bin_path["InvertedIndex"] = "/benchmarks/Mars/sample_apps/InvertedIndex/gpgpu_ptx_sim__InvertedIndex" 	
bin_path["SimilarityScore"] = "/benchmarks/Mars/sample_apps/SimilarityScore/gpgpu_ptx_sim__SimilarityScore" 	
bin_path["bfs"] = "/benchmarks/lonestar/bin/bfs" 	
bin_path["bh"] = "/benchmarks/lonestar/bin/bh" 	
bin_path["dmr"] = "/benchmarks/lonestar/bin/dmr" 	
bin_path["mst"] = "/benchmarks/lonestar/bin/mst" 	
bin_path["sp"] = "/benchmarks/lonestar/bin/sp" 	
bin_path["sssp"] = "/benchmarks/lonestar/bin/sssp" 	

input_path = {}
input_path["JPEG"] = "/benchmarks/CUDA/JPEG/data" 
input_path["MUM"] = "/benchmarks/CUDA/MUM/data" 
input_path["BFS"] = "/benchmarks/CUDA/BFS/data" 
input_path["SCP"] = "/benchmarks/CUDA/SCP/data" 
input_path["NN"] = "/benchmarks/CUDA/NN/data" 
input_path["STO"] = "/benchmarks/CUDA/STO/data" 
input_path["CONS"] = "/benchmarks/CUDA/CONS/data" 
input_path["hotspot"] = "/benchmarks/rodinia/data" 	
input_path["PageViewCount"] = "/benchmarks/Mars/sample_apps/PageViewCount/data" 	
input_path["PageViewRank"] = "/benchmarks/Mars/sample_apps/PageViewRank/data" 	
input_path["PageViewCount"] = "/benchmarks/Mars/sample_apps/PageViewCount/data" 	
input_path["InvertedIndex"] = "/benchmarks/Mars/sample_apps/InvertedIndex/data" 	
input_path["bfs"] = "/benchmarks/lonestar/inputs"	
input_path["bh"] = "/benchmarks/lonestar/inputs" 	
input_path["dmr"] = "/benchmarks/lonestar/inputs" 	
input_path["mst"] = "/benchmarks/lonestar/inputs" 	
input_path["sp"] = "/benchmarks/lonestar/inputs" 	
input_path["sssp"] = "/benchmarks/lonestar/inputs" 	

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
			os.chdir(HOME + "/scripts")
			filepath = "/" + config + "/" + batch[0] + "/" + benchmark + "/"
	#		print filepath
			if(not os.path.isdir(RESULTS + filepath)):
				subprocess.call("mkdir -p " + RESULTS + filepath,shell=True)
        #                        print RESULTS + (filepath)
			os.chdir(RESULTS + filepath)
			subprocess.call("ln -s " + HOME + bin_path[benchmark] + " .",shell=True)
			subprocess.call("cp " + CONFIG_DIR + "/" + config + "/* .",shell=True)
			if (benchmark in ["LPS","SimilarityScore","streamcluster","backprop"]):
				pass
			else:
				subprocess.call("ln -s " + HOME + input_path[benchmark] + " .",shell=True)	
			subprocess.call("ln -s " + BASH_SCRIPTS + "/" + batch[0] + "/mainscript_" + benchmark + " .",shell=True)
#			subprocess.call("chmod 777 mainscript_" + benchmark,shell=True)	
			print ("Running " + benchmark + " - "  + config)
			os.system("sh mainscript_" + benchmark + " &")


