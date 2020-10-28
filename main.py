import matplotlib.pyplot as plt
import numpy as np

def blockAverages( nblocks, data ) :
  # You should add code here to calcualte the block 
  # averages from the data points in data.
  averages = np.zeros( nblocks )
  # Your code goes here
  
  
# The code from here on does not need to be modified.  It 
# just uses your function to calculate some block averges and 
# then plots these values on a graph
radii = np.loadtxt("bubbles.dat")
plt.plot( np.linspace(1,10,10), blockAverages( 10, radii ), 'ko' )
plt.savefig("averages.png")
