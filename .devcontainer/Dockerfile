# Official tf-gpu as the parent image
FROM tensorflow/tensorflow:2.16.1-gpu

# Set environment variables for CUDA and cuDNN
ENV LD_LIBRARY_PATH /usr/local/cuda-12.3/lib64:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
ENV CUDA_HOME /usr/local/cuda
ENV TF_FORCE_GPU_ALLOW_GROWTH=true

# Install required packages
# RUN apt-get update && apt-get install -y \
#     libcudnn8=8.9.7.29-1+cuda12.3 \
#     libcudnn8-dev=8.9.7.29-1+cuda12.3

# Install Python packages
RUN pip install --no-cache-dir numpy pandas matplotlib