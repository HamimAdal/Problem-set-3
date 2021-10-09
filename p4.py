#matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



df1 = pd.read_csv("hit_speed_2015_csv.csv")
df2 = pd.read_csv("hit_speed_2019_csv.csv")
plt.style.use('seaborn')

s1 = []
s2 = []

for i in range(0,119):
    s1_val = df1.iloc[i,0]
    s1.append(s1_val)

for i in range(0,108):
    s2_val = df2.iloc[i,0]
    s2.append(s2_val)

samples1=s1
samples2=s2

def median_calc(sample):
    n = len(sample)
    sample.sort()
    if n % 2 == 0:
        med1 = sample[n//2]
        med2 = sample[n//2 - 1]
        med = (med1 + med2)/2
    else:
        med = sample[n//2]
    return med

def var_calc(sample):
    mean = sum(sample) / len(sample)
    variance = sum((x-mean)**2 for x in sample) / len(sample)
    return variance



print("Median value of 2015 is: " + str(median_calc(samples1)))
print("Variance value of 2015 is: " + str(var_calc(samples1)))
print("Median value of 2019 is: " + str(median_calc(samples2)))
print("Variance value of 2019 is: " + str(var_calc(samples2)))