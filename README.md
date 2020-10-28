# Block averages

In the previous two tasks, you computed the average volume of the bubbles in the following two ways:

![](https://render.githubusercontent.com/render/math?math=V=\frac{1}{n}\sum_{i=1}^n\frac{4}{3}\pi\R^3\qquad\textrm{and}\qquad\V'=\frac{4}{3}\pi\left(\frac{1}{n}\sum_{i=1}^{n}R_i\right)^3)

The V and V' values that you obtained should be different because the ![](https://render.githubusercontent.com/render/math?math=R_i) values are random variables so V and V' are thus also random variables.  To understand if these two statistics are measures of the same quantity we thus need to look at the distributions for the random variables V and V'.  

In these next few tasks, we are going to investigate the distributions of V and V' to see if they are the same or different.  The first step in doing will be to break up our data so that we can get multiple estimates for the average radius/volume.  We are going to do this using a method called block averaging.   This method is relatively simple.  When you block average you do not use all the data to calculate a single average.  You instead calculate an average from the first n points in the data set, a second average from the second n points in the data set, a third average from the third n points in the data set and so on.

To complete the task you need to complete the function called `blockAverages`. This function takes two arguments in input:

1. `nblocks` - is the number of averages that you want to calculate from the data set.  In other words, this is the number of blocks that you want to divide your data set into.
2. `data` - is a NumPy array that contains the data set from which the block averages are calculated.

When this function is complete it should return a NumPy array with nblocks elements.  The first of these elements should be set equal to the sample mean computed from the first `len(data)/nblocks` points in data.  The second element should be set equal to the sample mean computed from the second `len(data)/nblocks` points in data and so on.  
