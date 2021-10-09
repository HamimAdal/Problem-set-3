
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.distributions.empirical_distribution import ECDF



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



def eps_func(n, alpha=0.95):
   return np.sqrt(1. / (2. * n) * np.log(2. / alpha))

def plot_dist(samples, low, high, year, name, pltnum=111):
   
    ecdf = ECDF(samples)
    
    x = np.linspace(low, high, 10000)
    epsi = eps_func(n=len(samples))
    df = pd.DataFrame(ecdf(x), index=x)
    df['ecdf'] = ecdf(x)
   
    #plt.plot(ecdf.x, ecdf.y)  #line plot

    df['ecdf'].plot(label='ECDF of data of %d' % (year))  #square plot
    df['upper'] = pd.Series(ecdf(x), index=x).apply(lambda x: min(x + epsi, 1.))
    df['lower'] = pd.Series(ecdf(x), index=x).apply(lambda x: max(x - epsi, 0.))


    plt.fill_between(x, df['upper'], df['lower'], alpha=0.1, label='Confidence band of data of %d' % (year))
    plt.legend(loc='best')
    plt.title('%s when (n=%d) and (n=%d)' % (name, len(samples1), len(samples2)))
    
plt.figure(1, figsize=(12, 10))


plot_dist(samples1, 85.2, 90.3, 2015, name='95 percent confidence bound of ECDF', pltnum=221)
plot_dist(samples2, 84.9, 91.4, 2019, name='95 percent confidence bound of ECDF', pltnum=221)


plt.show()

