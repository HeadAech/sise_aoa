import numpy as np
from scipy.ndimage import median_filter as mf


def moving_avg_filter(angles, window_size=3):
    return np.convolve(angles, np.ones(window_size) / window_size, mode="valid")


def median_filter(angles, size=3):
    return mf(angles, size=size)
