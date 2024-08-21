#	Create a Python script that reads a CSV file and computes the mean, median, and mode of numerical columns.
import tensorflow as tf
import pandas as pd
import numpy as np
from scipy import stats

file_path = 'C:/Users/91932/Downloads/top_120_best-selling_mobile_phones.csv'
df = pd.read_csv(file_path)
numeric_df = df.select_dtypes(include=[np.number])
numeric_tensor = tf.convert_to_tensor(numeric_df.values, dtype= tf.float32)
mean = tf.reduce_mean(numeric_tensor, axis =0)
print("Mean of dataset is:")
print(mean.numpy())
median = np.median(numeric_tensor, axis = 0)
print("Median of dataset:")
print(median)
mode = stats.mode(numeric_df.values,axis=0)
print("Mode of dataset:")
print(mode.mode[0])