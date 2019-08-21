# Programmer : Jonas Smith
# Purpose    : A simple project to show the histogram for a set of 
#               Data, and Also show the mean, Variance, and Sta.Dev.
#               Not the sample use the Population versions.

import numpy
import matplotlib
from scipy import stats
import matplotlib.pyplot as plt

values = [  25.8, 14.3, 16.9, 18.1, 40.2, 21.3, 19.7, 15.6, 
            14.8, 30.5, 39.7, 20.0, 16.2, 15.2, 14.5, 20.8, 
            76.0, 20.0, 18.3, 45.5, 14.9, 17.7, 15.5, 19.4, 
            17.2, 19.5, 15.8, 44.3, 18.5, 14.7, 20.0, 18.7, 
            19.8, 19.2, 50.6, 15.1, 23.6, 17.4, 15.7, 16.4, 
            17.1, 23.4, 17.8, 16.8
        ]

# for x in values:
#     print(x)

res = stats.relfreq(values, numbins=4)
res.frequency
numpy.sum( res.frequency )

x = res.lowerlimit + numpy.linspace(
        0, 
        res.binsize*res.frequency.size,
        res.frequency.size)

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(1, 1, 1)
ax.bar(x, res.frequency, width=res.binsize)
ax.set_title('Relative frequency histogram for 1.1')
ax.set_xlim([x.min(), x.max()])

# simply shows the plt that is configured above.
plt.show()