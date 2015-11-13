./gpgpu_ptx_sim__mergedapps -apps BLK JPEG
cp stream1.txt ./results/BLK_JPEG_stream1.txt
cp stream2.txt ./results/BLK_JPEG_stream2.txt
./gpgpu_ptx_sim__mergedapps -apps BLK 3DS
cp stream1.txt ./results/BLK_3DS_stream1.txt
cp stream2.txt ./results/BLK_3DS_stream2.txt
./gpgpu_ptx_sim__mergedapps -apps BLK NN
cp stream1.txt ./results/BLK_NN_stream1.txt
cp stream2.txt ./results/BLK_NN_stream2.txt
