import numpy as np
import scipy.stats

def sample_variance( data ) : 
  # Your code to calculate the sample variance from the data in 
  # the numpy array called data goes here
  
  
def testStatistic( data1, data2 ) : 
  # Your code to compute the test statistic should be inserted here.
  # Remember to use calls to sample_variance to lower the ammount of
  # code you are writing
  
def pvalue( data1, data2 ) : 
  F = testStatistic( data1, data2 )
  # Your code to calculate the  p-value given the value of the 
  # test statistic (F) should go here.
  

data1 = np.array([0.71, -1.24, -3.72, 0.08, -3.69, -3.54, 4.32, 2.08, -2.03, -5.85])
data2 = np.array([-1.04, -0.97, -0.95, -1.01, -1.28, -0.21, -0.98, -0.22, 1.71, -1.73])
print("Null hypothesis: the distributions that were sampled to generate the data in the")
print("numpy arrays data1 and data2 have the same variance")
print("Alternative hypothesis: the distribution that was sampled to generate the data in")
print("the numpy array called data1 is greater than the variance for the distribution")
print("from which the data in data2 was generated")
print("The p-value for this hypothesis test is", pvalue( data1, data2 ) )
