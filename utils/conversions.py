
import numpy as np

def to_kp_format(flat_arr):
    img_kp = np.asarray(flat_arr)
    img_kp = np.reshape(img_kp, (17, 3))
    return img_kp