FROM python:3.10

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /workspace

# ---------------------------------
# System dependencies
# ---------------------------------
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    wget \
    curl \
    libgl1 \
    libglib2.0-0 \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------------
# Python tooling
# ---------------------------------
RUN pip install --upgrade pip setuptools wheel

# ---------------------------------
# FORCE NumPy WHEEL ONLY (CRITICAL)
# ---------------------------------
RUN pip install --only-binary=:all: numpy==1.26.4

# ---------------------------------
# CPU-only PyTorch
# ---------------------------------
RUN pip install \
    torch torchvision torchaudio \
    --index-url https://download.pytorch.org/whl/cpu

# ---------------------------------
# Scientific & audio stack
# ---------------------------------
RUN pip install \
    scipy \
    librosa \
    tqdm \
    opencv-python

# ---------------------------------
# NLP / ASR
# ---------------------------------
RUN pip install \
    transformers \
    sentencepiece \
    openai-whisper

# ---------------------------------
# TTS (ALLOW SOURCE BUILDS)
# ---------------------------------
RUN pip install TTS==0.22.0

# ---------------------------------
# Wav2Lip (Python 3.10 compatible)
# ---------------------------------
RUN git clone https://github.com/Rudrabha/Wav2Lip.git

WORKDIR /workspace/Wav2Lip

# Remove legacy pins that break modern Python
RUN sed -i '/numpy==/d' requirements.txt \
 && sed -i '/librosa==/d' requirements.txt

# DO NOT install requirements.txt
# Modern dependencies already installed above

WORKDIR /workspace
