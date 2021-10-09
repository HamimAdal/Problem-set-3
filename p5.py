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

def boot_median(B,sample,year):
    
    sample = np.array(sample)
    median_length, sims = [], B
    for i in range(sims):
        med_sample = np.random.choice(sample, replace=True, size=len(sample))
        sample_median = np.median(med_sample)
        median_length.append(sample_median)
    med_boot = np.median(median_length)
    con_inter_boot = np.percentile(median_length, [2.5, 97.5])
    print("For the year {}, Bootstrap Median = {}, 95% C Interval = {}".format(year, med_boot, con_inter_boot))

def boot_variance(B,sample_data,year):
   
    sample_data = np.array(sample_data)
    variance_length, sims = [], B
    for j in range(sims):
        var_sample = np.random.choice(sample_data, replace=True, size=len(sample_data))
        sample_variance = np.var(var_sample)
        variance_length.append(sample_variance)
    var_boot = np.mean(variance_length)
    con_inter_boot = np.percentile(variance_length, [2.5, 97.5])
    print("For the year {}, Bootstrap Variance = {}, 95% C Interval = {}".format(year, var_boot, con_inter_boot))
    
 
boot_median(1000,samples1,2015)
boot_median(1000,samples2,2019)
print("\n")
boot_variance(1000,samples1,2015)
boot_variance(1000,samples2,2019)

























