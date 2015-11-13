export GPGPUSIM_ROOT=/home/rausavar/GPGPU/gpgpu-sim
export CUDAHOME=/usr/old_local/cuda/cuda
export CUDA_INSTALL_PATH=/usr/old_local/cuda/cuda
export NVIDIA_CUDA_SDK_LOCATION=/home/nandita/NVIDIA_GPU_Computing_SDK
export BOOST_ROOT=/home/rachata/boost_1_54_0

######################

export LD_LIBRARY_PATH=$CUDAHOME/lib/:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$CUDAHOME/lib64/:$LD_LIBRARY_PATH:/usr/local/cuda/lib/:
export LD_LIBRARY_PATH=$GPGPUSIM_ROOT/lib/4000/release:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$GPGPUSIM_ROOT/lib/4000/release:$GPGPUSIM_ROOT/lib/4000/release:/usr/old_local/cuda/cuda/lib64/:/usr/old_local/cuda/cuda/lib/:$GPGPUSIM_ROOT/lib/4000/release:/usr/old_local/cuda/cuda/lib64/:/usr/old_local/cuda/cuda/lib/:/usr/local/cuda/lib:/usr/local/cuda/lib:
export GPGPUSIM_POWER_MODEL=$GPGPUSIM_ROOT/src/gpuwattch
export PATH=$CUDAHOME/bin/:$PATH
export PARBOIL_ROOT=$GPGPUSIM_ROOT/benchmarks/parboil
