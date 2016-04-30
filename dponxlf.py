from ctypes import *
import numpy as np
import tensorflow as tf
import os

import glob

mydll = cdll.LoadLibrary("/home/xuan/PycharmProjects/LearnTensorFlow/libexportXLF.so")

exportXLFData = mydll.exportXLFData

length = 2048*2048*6

allData = (c_double*length)()

total_data = np.ndarray(shape=(100, 2048, 2048, 6), dtype=np.float64)


path = "./data"

files = os.listdir(path)

for file in files:
    if file.endswith("xlf"):
        exportXLFData("./a.xlf", allData)
        pydata = np.ctypeslib.as_array(allData)
        readabledata = pydata.reshape((2048, 2048, 6))