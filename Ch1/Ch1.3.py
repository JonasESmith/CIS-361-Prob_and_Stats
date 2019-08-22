# Programmer : Jonas Smith
# Purpose    : A simple project to show the histogram for a set of 
#               Data, and Also show the mean, Variance, and Sta.Dev.
#               Not the sample use the Population versions.

import json
import numpy
import matplotlib
from scipy import stats
import matplotlib.pyplot as plot

# Loads information from a Json file
input_file = open('Ch1Data.json')
data = json.load(input_file)
assignmentNum = 'Ch1.3'

# Parse the Ch1.2 Data into a local array
values = data[assignmentNum]

res = stats.relfreq(values, numbins=4)
numpy.sum( res.frequency )

x = res.lowerlimit + numpy.linspace(
        0, 
        res.binsize*res.frequency.size,
        res.frequency.size)

# Configure the histogram that will be shown.
fig = plot.figure(figsize=(5, 4))
ax = fig.add_subplot(1, 1, 1)
ax.bar(x, res.frequency, width=res.binsize)
ax.set_title('Relative frequency histogram for {}'.format(assignmentNum))
ax.set_xlim([x.min(), x.max()])

numpy.mean(values)

mean     = 'mean      : {}'.format( numpy.mean(values) )
variance = "variance : {}".format(numpy.var(values,ddof=1))
stdDev   = "stdDev   : {}".format(numpy.std(values, ddof=1))

plotText = '{}\n{}\n{}'.format(mean, variance, stdDev)

plot.text(0.5, 0.5, plotText, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

# simply shows the plot that is configured above.
plot.show()