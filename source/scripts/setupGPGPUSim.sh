#!/bin/bash

source ./set_env_rachata.sh
cd ../
source setup_environment
cd ./v3.x
make
cd ../scripts
