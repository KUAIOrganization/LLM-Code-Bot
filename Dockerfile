# Use RAPIDS base image
FROM nvcr.io/nvidia/rapidsai/notebooks:23.10-cuda12.0-py3.10

# Set paths so Jupyter recognizes CUDA drivers
#ENV PATH=/usr/local/cuda-11.8/bin:${PATH}
#ENV LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64:${LD_LIBRARY_PATH}

# Copy the TensorFlow wheel file into the container
#COPY tensorflow-2.15.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl /tmp/

# Install dependencies
RUN pip install tensorflow[and-cuda]
RUN pip install numpy matplotlib
RUN pip install tensorboard