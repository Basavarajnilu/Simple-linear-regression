import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([2,4,5,4,5])

print("maean of x" ,np.mean(x))
print("mean of y",np.mean(y))

plt.plot(x,y,color="g")    
plt.xlabel("X")
plt.ylabel("Y")
plt.title("linear regression")
plt.show() 
n=np.size(x)
ssxy=np.sum(y*x)-n*np.mean(x)*np.mean(y)
ssxx=-2*(np.sum(x*x)-n*np.mean(x)*np.mean(y))
print(ssxy)
print(ssxx)
b1=ssxy/ssxx
print("b1:",b1)
print("b0:",np.mean(y)-b1*np.mean(x))
