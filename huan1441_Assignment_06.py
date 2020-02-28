# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Author: Tao Huang (huan1441)
#
# Created: Feb 21, 2020
#
# Script: ABE65100 huan1441_Assignment_06.py
#
# Purpose: Script to read in a data file and generate summary figures for that file.
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import numpy as np
import matplotlib.pyplot as plt

# list of input filenames (txt)

inputfiles=["Tippecanoe_River_at_Ora.Annual_Metrics.txt",
            "Wildcat_Creek_at_Lafayette.Annual_Metrics.txt"]

# list of output filenames (pdf)

outputfiles=["Tippecanoe_River_at_Ora.Annual_Metrics.pdf",
             "Wildcat_Creek_at_Lafayette.Annual_Metrics.pdf"]

# # # open and store the data file in the same driectory as the script

for i in range(len(inputfiles)):

    # read and store the original data as data

    data=np.genfromtxt(inputfiles[i],
                       dtype=["int","float","float","float","float","float","float"],
                       delimiter='\t',
                       names=True)

# # # select the corresponding data to generate a single pdf file with three plots

    # set the size of the figure
    
    plt.figure(figsize=(10,10))

    # set the space between subplots
    
    plt.subplots_adjust(hspace=0.3)
    
    # generate the first subplot

    plt.subplot(311)
    plt.plot(data['Year'],data['Mean'], 'k',
             data['Year'],data['Max'], 'r',
             data['Year'],data['Min'], 'b')
    plt.legend(["Mean","Max","Min"], loc='best',edgecolor='k')
    plt.xlabel("Year")
    plt.ylabel("Streamflow (cfs)")

    # generate the second subplot

    plt.subplot(312)
    plt.plot(data['Year'],data['Tqmean']*100, 'g^')
    plt.xlabel("Year")
    plt.ylabel("Tqmean (%)")

    # generate the third subplot

    plt.subplot(313)
    plt.bar(data['Year'],data['RBindex'])
    plt.xlabel("Year")
    plt.ylabel("R-B Index (ratio)")

    # save the figure as pdf

    plt.savefig(outputfiles[i])
    
    plt.close()
