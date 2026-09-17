import pygame
import sounddevice as sd
import numpy as np
import math
import threading

#settings

WIDTH = 1000
HEIGHT = 500
FPS = 60

SAMPLE_RATE = 44100
BLOCK_SIZE = 2048

# HUMAN VOICE PITCH RANGE
MIN_PITCH = 70
MAX_PITCH = 500

# AUDIO VARIABLE

audio_buffer = np.zeros(BLOCK_SIZE,dtype=np.float32)

volume = 0.0
pitch = 0.0

audio_lock = threading.Lock()

# PITCH DETECTION

def detect_pitch(signal, sample_rate):
    """Delete fundamental frequency using automatically"""
    signal = signal - np.mean(signal)

    #RMS volume
    rms = np.sqrt(np.mean(signal ** 2))

    #ignore silence
    if rms < 0.008:
        return 0.0

    #normalize
    signal = signal / (np.max(np.abs(signal))+ 1e-8)

    #pitch range
    min_lag = int(sample_rate /MAX_PITCH)
    max_lag = int(sample_rate / MAX_PITCH)

    if max_lag >= len(signal):
        max_lag = len(signal) - 1

    # autocorrelation
    