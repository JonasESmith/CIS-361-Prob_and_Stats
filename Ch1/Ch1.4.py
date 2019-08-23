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
assign_name = 'Ch1.4'

# Parse the Ch1.4 Data into a local array
values = data[assign_name]

# This simply creates a histogram variable that we assign to 
#       scipy's relfreq which is a relative frequency histogram
# We then pass the values from above, and a numbers of bins 
#       we want to associate with the data set.
histogram = stats.relfreq(values, numbins=4)
numpy.sum( histogram.frequency )

x = histogram.lowerlimit + numpy.linspace(
        0, 
        histogram.binsize*histogram.frequency.size,
        histogram.frequency.size)


# Configure the histogram that will be shown.
fig = plot.figure(figsize=(5, 4))
ax = fig.add_subplot(1, 1, 1)
# Creates the bars used in the Histogram.
ax.bar( x, 
        histogram.frequency, 
        width=histogram.binsize)
ax.set_title( 'Relative frequency histogram for {}'.format(assign_name))
ax.set_xlim([x.min(), x.max()])

mean     = "mean     : {}".format( numpy.mean(values) )
variance = "variance : {}".format(numpy.var(values, ddof=1))
stdDev   = "stdDev   : {}".format(numpy.std(values, ddof=1))

plotText = '{}\n{}\n{}'.format(mean, variance, stdDev)

# add text to the plot
plot.text(
        0.5, 
        0.5, 
        plotText, 
        horizontalalignment='center', 
        verticalalignment='center', 
        transform=ax.transAxes
        )

# simply shows the plot that is configured above.
plot.show()