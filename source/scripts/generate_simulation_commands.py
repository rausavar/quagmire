#!/usr/bin/python

import os
import sys
import re
import subprocess
import argparse

HOME = "/home/rachata/gpgpu-sim"
CONFIG_DIR = "/home/rachata/gpgpu-sim/v3.x/configs/"
BASH_SCRIPTS = "/home/rachata/gpgpu-sim/scripts/run_scripts"

base_command = "./run_gpgpu_simulations_rachata.py "

config_list = [
"GTX480_baseline",
#"GTX480_baseline_rop60",

"GTX480_10lower_90upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf",
"GTX480_20lower_80upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf",
"GTX480_30lower_70upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf",

"GTX480_10lower_90upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf",
"GTX480_20lower_80upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf",
"GTX480_30lower_70upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf",




#"GTX480_10lower_90upper_rop60_bypassROP_insertion_10l2warmup_10kclearCycles_priomf",
#"GTX480_20lower_80upper_rop60_bypassROP_insertion_10l2warmup_10kclearCycles_priomf",
#"GTX480_30lower_70upper_rop60_bypassROP_insertion_10l2warmup_10kclearCycles_priomf",
#
#"GTX480_10lower_90upper_rop60_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf",
#"GTX480_20lower_80upper_rop60_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf",
#"GTX480_30lower_70upper_rop60_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf",


#
#
#"GTX480_25lower_80upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf",
#"GTX480_35lower_80upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf",
#"GTX480_25lower_80upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf",
#"GTX480_35lower_80upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf",
#
#"GTX480_10lower_90upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf",
#"GTX480_20lower_80upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf",
#"GTX480_30lower_80upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf",
#"GTX480_30lower_70upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf",
#
#"GTX480_10lower_90upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf",
#"GTX480_10lower_80upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf",
#"GTX480_20lower_80upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf",
#"GTX480_30lower_80upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf",


#"GTX480_25lower_90upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_25lower_80upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_35lower_80upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_35lower_70upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_25lower_90upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_25lower_80upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_35lower_80upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_35lower_70upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#
#"GTX480_10lower_90upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_10lower_80upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_20lower_90upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_20lower_80upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_30lower_80upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_30lower_70upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_40lower_60upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
##"GTX480_50lower_60upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
##"GTX480_60lower_60upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
##"GTX480_60lower_70upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
##"GTX480_70lower_80upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
##"GTX480_80lower_90upper_bypassROP_insertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#
#"GTX480_10lower_90upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_10lower_80upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_20lower_90upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_20lower_80upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_30lower_80upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_30lower_70upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_40lower_60upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
##"GTX480_50lower_60upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
##"GTX480_60lower_60upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
##"GTX480_60lower_70upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
##"GTX480_70lower_80upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
##"GTX480_80lower_90upper_bypassROP_invInsertion_30l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#
#
#
#"GTX480_25lower_90upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_25lower_80upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_35lower_80upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_35lower_70upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_25lower_90upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_25lower_80upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_35lower_80upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_35lower_70upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#
#"GTX480_10lower_90upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_10lower_80upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_20lower_90upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_20lower_80upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_30lower_80upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_30lower_70upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_40lower_60upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#
#
##"GTX480_50lower_60upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
##"GTX480_60lower_60upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
##"GTX480_60lower_70upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
##"GTX480_70lower_80upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
##"GTX480_80lower_90upper_bypassROP_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#
#"GTX480_10lower_90upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_10lower_80upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_20lower_90upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_20lower_80upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_30lower_80upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_30lower_70upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_40lower_60upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_50lower_60upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_60lower_60upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_60lower_70upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_70lower_80upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_80lower_90upper_bypassROP_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",

#"GTX480_25lower_90upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_25lower_80upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_35lower_80upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_35lower_70upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_25lower_90upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_25lower_80upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_35lower_80upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_35lower_70upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#
#"GTX480_10lower_90upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_10lower_80upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_20lower_90upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_20lower_80upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_30lower_80upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_30lower_70upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_40lower_60upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_50lower_60upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_60lower_60upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_60lower_70upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_70lower_80upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_80lower_90upper_insertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#
#"GTX480_10lower_90upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_10lower_80upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_20lower_90upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_20lower_80upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_30lower_80upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_30lower_70upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_40lower_60upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_50lower_60upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_60lower_60upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_60lower_70upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_70lower_80upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#"GTX480_80lower_90upper_invInsertion_10l2warmup_10kclearCycles_priomf_reuse_4096bloomSize",
#



#"GTX480_10lower_90upper_10l2warmup_1mclearCycles_priomf_reuse_1024bloomSize",
#"GTX480_20lower_80upper_10l2warmup_1mclearCycles_priomf_reuse_1024bloomSize",
#"GTX480_30lower_70upper_10l2warmup_1mclearCycles_priomf_reuse_1024bloomSize",
#"GTX480_10lower_90upper_10l2warmup_1mclearCycles_priomf_reuse_2048bloomSize",
#"GTX480_20lower_80upper_10l2warmup_1mclearCycles_priomf_reuse_2048bloomSize",
#"GTX480_30lower_70upper_10l2warmup_1mclearCycles_priomf_reuse_2048bloomSize",
#"GTX480_10lower_90upper_10l2warmup_10kclearCycles_priomf_reuse_1024bloomSize",
#"GTX480_20lower_80upper_10l2warmup_10kclearCycles_priomf_reuse_1024bloomSize",
#"GTX480_30lower_70upper_10l2warmup_10kclearCycles_priomf_reuse_1024bloomSize",
#"GTX480_10lower_90upper_10l2warmup_10kclearCycles_priomf_reuse_2048bloomSize",
#"GTX480_20lower_80upper_10l2warmup_10kclearCycles_priomf_reuse_2048bloomSize",
#"GTX480_30lower_70upper_10l2warmup_10kclearCycles_priomf_reuse_2048bloomSize",
#
#
#
#"GTX480_10lower_90upper_30l2warmup_1mclearCycles_priomf_reuse_1024bloomSize",
#"GTX480_20lower_80upper_30l2warmup_1mclearCycles_priomf_reuse_1024bloomSize",
#"GTX480_30lower_70upper_30l2warmup_1mclearCycles_priomf_reuse_1024bloomSize",
#"GTX480_10lower_90upper_30l2warmup_1mclearCycles_priomf_reuse_2048bloomSize",
#"GTX480_20lower_80upper_30l2warmup_1mclearCycles_priomf_reuse_2048bloomSize",
#"GTX480_30lower_70upper_30l2warmup_1mclearCycles_priomf_reuse_2048bloomSize",
#"GTX480_10lower_90upper_30l2warmup_10kclearCycles_priomf_reuse_1024bloomSize",
#"GTX480_20lower_80upper_30l2warmup_10kclearCycles_priomf_reuse_1024bloomSize",
#"GTX480_30lower_70upper_30l2warmup_10kclearCycles_priomf_reuse_1024bloomSize",
#"GTX480_10lower_90upper_30l2warmup_10kclearCycles_priomf_reuse_2048bloomSize",
#"GTX480_20lower_80upper_30l2warmup_10kclearCycles_priomf_reuse_2048bloomSize",
#"GTX480_30lower_70upper_30l2warmup_10kclearCycles_priomf_reuse_2048bloomSize",

]

#batches = [1,2,3]
batches = [4,5,6]
#batches = [1,2,3,4,5,6]
#batches = [1,2,3,4,5,6,7,8]

for configs in config_list:
    base_file = CONFIG_DIR + "GTX480/gpgpusim.config"
    target_file = CONFIG_DIR + configs + "/gpgpusim.config"
    if("GTX480" in configs):
        base_file = CONFIG_DIR + "GTX480/gpgpusim.config"
        os.system("mkdir " + CONFIG_DIR + configs)
        os.system("cp " + CONFIG_DIR + "GTX480/*.icnt " + CONFIG_DIR + configs + "/")
        os.system("cp " + CONFIG_DIR + "GTX480/*.xml " + CONFIG_DIR + configs + "/")
    elif("QuadroFX5800" in configs):
        base_file = CONFIG_DIR + "QuadroFX5800/gpgpusim.config"
        os.system("mkdir " + CONFIG_DIR + configs)
        os.system("cp " + CONFIG_DIR + "QuadroFX5800/*.icnt " + CONFIG_DIR + configs + "/")
        os.system("cp " + CONFIG_DIR + "QuadroFX5800/*.xml " + CONFIG_DIR + configs + "/")
    elif("TeslaC2050" in configs):
        base_file = CONFIG_DIR + "TeslaC2050/gpgpusim.config"
        os.system("mkdir " + CONFIG_DIR + configs)
        os.system("cp " + CONFIG_DIR + "TeslaC2050/*.icnt " + CONFIG_DIR + configs + "/")
        os.system("cp " + CONFIG_DIR + "TeslaC2050/*.xml " + CONFIG_DIR + configs + "/")


# Copy the case config and add additional configs
    f = open(base_file)
    out_config = open(target_file,"w")
    for lines in f:
        out_config.write(lines)
    if(not ("baseline") in configs):
        out_config.write("\n#GPUDivergence study configs\n\n")
        out_config.write("-gpgpu_cache:cache_aware 1\n")
    if("baseline" in configs):
        out_config.write("-gpgpu_cache:cache_aware 0\n")
        out_config.write("-gpgpu_cache:bypass_rop 0\n")
    if("bypassROP" in configs):
        out_config.write("-gpgpu_cache:bypass_rop 1\n")
    if("rop120" in configs):
        out_config.write("-rop_latency 120\n")
    elif("rop110" in configs):
        out_config.write("-rop_latency 110\n")
    elif("rop100" in configs):
        out_config.write("-rop_latency 100\n")
    elif("rop90" in configs):
        out_config.write("-rop_latency 90\n")
    elif("rop80" in configs):
        out_config.write("-rop_latency 80\n")
    elif("rop70" in configs):
        out_config.write("-rop_latency 70\n")
    elif("rop60" in configs):
        out_config.write("-rop_latency 60\n")
    elif("rop50" in configs):
        out_config.write("-rop_latency 50\n")
    elif("rop40" in configs):
        out_config.write("-rop_latency 40\n")
    elif("rop30" in configs):
        out_config.write("-rop_latency 30\n")
    if("invInsertion" in configs):
        out_config.write("-gpgpu_cache:cache_aware_insertion 2\n")
    elif("insertion" in configs):
        out_config.write("-gpgpu_cache:cache_aware_insertion 1\n")
    else:
        out_config.write("-gpgpu_cache:cache_aware_insertion 0\n")
    if("upper" in configs):
        if("90upper" in configs):
            out_config.write("-gpgpu_cache:l2_warp_hit_ratio_high 0.9\n")
        elif("80upper" in configs):
            out_config.write("-gpgpu_cache:l2_warp_hit_ratio_high 0.8\n")
        elif("70upper" in configs):
            out_config.write("-gpgpu_cache:l2_warp_hit_ratio_high 0.7\n")
        elif("60upper" in configs):
            out_config.write("-gpgpu_cache:l2_warp_hit_ratio_high 0.6\n")
    if("lower" in configs):
        if("10lower" in configs):
            out_config.write("-gpgpu_cache:l2_warp_hit_ratio 0.1\n")
        if("20lower" in configs):
            out_config.write("-gpgpu_cache:l2_warp_hit_ratio 0.2\n")
        if("25lower" in configs):
            out_config.write("-gpgpu_cache:l2_warp_hit_ratio 0.25\n")
        if("30lower" in configs):
            out_config.write("-gpgpu_cache:l2_warp_hit_ratio 0.3\n")
        if("35lower" in configs):
            out_config.write("-gpgpu_cache:l2_warp_hit_ratio 0.35\n")
        if("40lower" in configs):
            out_config.write("-gpgpu_cache:l2_warp_hit_ratio 0.4\n")
        if("50lower" in configs):
            out_config.write("-gpgpu_cache:l2_warp_hit_ratio 0.5\n")
        if("60lower" in configs):
            out_config.write("-gpgpu_cache:l2_warp_hit_ratio 0.6\n")
        if("70lower" in configs):
            out_config.write("-gpgpu_cache:l2_warp_hit_ratio 0.7\n")
        if("80lower" in configs):
            out_config.write("-gpgpu_cache:l2_warp_hit_ratio 0.8\n")
    if("clearCycles" in configs):
        if("10kclearCycles" in configs):
            out_config.write("-gpgpu_cache:l2_warp_info_clear 10000\n")
        if("100kclearCycles" in configs):
            out_config.write("-gpgpu_cache:l2_warp_info_clear 100000\n")
        if("1mclearCycles" in configs):
            out_config.write("-gpgpu_cache:l2_warp_info_clear 1000000\n")
        if("50kclearCycles" in configs):
            out_config.write("-gpgpu_cache:l2_warp_info_clear 50000\n")
        if("500kclearCycles" in configs):
            out_config.write("-gpgpu_cache:l2_warp_info_clear 500000\n")
    if("l2warmup" in configs):
        if("100l2warmup" in configs):
            out_config.write("-gpgpu_cache:l2_warmup 100\n")
        if("50l2warmup" in configs):
            out_config.write("-gpgpu_cache:l2_warmup 50\n")
        if("30l2warmup" in configs):
            out_config.write("-gpgpu_cache:l2_warmup 30\n")
        if("10l2warmup" in configs):
            out_config.write("-gpgpu_cache:l2_warmup 10\n")
    if("priomf" in configs):
        out_config.write("-gpgpu_cache:prioritize_mf 1\n")
    if("reuse" in configs):
        out_config.write("-gpgpu_cache:reuse_aware 1\n")
        if("bloomSize" in configs):
            if("512bloomSize" in configs):
                out_config.write("-gpgpu_cache:l2_bloom_filter_size 512\n")
            if("1024bloomSize" in configs):
                out_config.write("-gpgpu_cache:l2_bloom_filter_size 1024\n")
            if("2048bloomSize" in configs):
                out_config.write("-gpgpu_cache:l2_bloom_filter_size 2048\n")
            if("4096bloomSize" in configs):
                out_config.write("-gpgpu_cache:l2_bloom_filter_size 4096\n")
    else:
        out_config.write("-gpgpu_cache:reuse_aware 0\n")

    for i in batches:
        print "./run_gpgpu_simulations_rachata.py -configs " + configs + " -label " + configs + " -batch " + str(i) +" -result_dir results"

    f.close()
    out_config.close()

