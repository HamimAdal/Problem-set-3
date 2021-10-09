import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import pyplot
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

a=s1
b=s2


def ecdf(a):
    """Generate x and y values for plotting an ECDF."""
    return np.sort(a), np.arange(1, len(a)+1) / len(a)

x1, y1 = ecdf(a)    
x2, y2 = ecdf(b) 
plt.plot(x1,y1, label = "Hitting speed for 2015")
plt.plot(x2,y2, label = "Hitting speed for 2019")

plt.xlabel('x')
plt.ylabel('y= F[x]')
plt.title('Empirical distribution function of the hitting speed for 2015 and 2019')
plt.legend()
plt.show()


# testing with a built in function

ecdf1 = ECDF(a)
plt.plot(ecdf1.x, ecdf1.y, label = "Hitting speed for 2015" )
ecdf2 = ECDF(b)
plt.plot(ecdf2.x, ecdf2.y, label = "Hitting speed for 2019")

plt.title('Empirical distribution function of the hitting speed for 2015 and 2019 (Using built in function)')
plt.legend()
plt.show()