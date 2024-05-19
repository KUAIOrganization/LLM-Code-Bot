# RAPIDSai base image, only compatible with 12.0 and 3.10
FROM nvcr.io/nvidia/rapidsai/base:24.02-cuda12.0-py3.10

# Print Ubuntu version
RUN lsb_release -a || cat /etc/os-release

USER root

# Set non-interactive installation
ARG DEBIAN_FRONTEND=noninteractive

# Install tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    wget \
    gnupg \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Add CUDA repository and its GPG key
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin && \
    mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600 && \
    wget https://developer.download.nvidia.com/compute/cuda/12.3.0/local_installers/cuda-repo-ubuntu2204-12-3-local_12.3.0-545.23.06-1_amd64.deb && \
    dpkg -i cuda-repo-ubuntu2204-12-3-local_12.3.0-545.23.06-1_amd64.deb && \
    cp /var/cuda-repo-ubuntu2204-12-3-local/cuda-*-keyring.gpg /usr/share/keyrings/ && \
    apt-get update

# Install CUDA Toolkit 12-3
RUN apt-get install -y cuda-toolkit-12-3

# Install cuDNN from local file
# https://developer.nvidia.com/downloads/compute/cudnn/secure/8.9.7/local_installers/12.x/cudnn-local-repo-ubuntu2204-8.9.7.29_1.0-1_amd64.deb/
COPY cudnn-local-repo-ubuntu2204-8.9.7.29_1.0-1_amd64.deb /tmp/
RUN dpkg -i /tmp/cudnn-local-repo-ubuntu2204-8.9.7.29_1.0-1_amd64.deb && \
    cp /var/cudnn-local-repo-ubuntu2204-8.9.7.29/cudnn-local-08A7D361-keyring.gpg /usr/share/keyrings/ && \
    apt-key add /usr/share/keyrings/cudnn-local-08A7D361-keyring.gpg && \
    apt-get update && \
    apt-get install -y libcudnn8 libcudnn8-dev libcudnn8-samples

# Install Python packages
RUN pip install --no-cache-dir tensorflow[and-cuda]==2.16.1 keras==3.0 matplotlib numpy pandas tensorboard==2.16.2

# Cleanup
RUN apt-get clean && \
    rm -f /tmp/cudnn-local-repo-ubuntu2204-8.9.7.29_1.0-1_amd64.deb && \
    rm -rf /var/lib/apt/lists/* /var/cuda-repo-ubuntu2204-12-3-local

# Set PATH for CUDA 12.3
ENV PATH=/usr/local/cuda-12.3/bin:${PATH}
ENV LD_LIBRARY_PATH=/usr/local/cuda-12.3/lib64:${LD_LIBRARY_PATH}