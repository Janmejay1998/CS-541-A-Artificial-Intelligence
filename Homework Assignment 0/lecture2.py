from xml.sax.handler import feature_external_ges
import numpy as np
from pandas import array

X = np.array( [[2,3],[3,4],[4,5]])
Y = np.array( [1,2,3])

feature_count = X.shape[1]

W = np.array( [0,0] )

loss = 0

for i in range(X.shape[0]):
    val = 0
    for j in range(feature_count):
        val += X[i,j]*W[i]
    y_hat = val
    loss += (Y[i]-y_hat)**2

final_loss = loss/X.shape[0]        

print( final_loss)