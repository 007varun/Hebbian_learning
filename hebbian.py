import random
print("Hello World")
import math
w = [0,0,0]
g = [0,0,0]
gtg = [0,0,0]
for j in range(10):
    x = []
    k = 0
    for i in range(2):
        x.append(random.randint(1000,2000))
    for i in range(2):
        x.append(random.randint(3000,3006))
    print("this is x",x)
    z=0
    gt = g.copy()
    while z<= len(x)-1 and k<=2:
        l = w[k]
        w[k] = w[k] + 0.01*x[z]*x[z+1]
        g[k] = w[k]-l
        k = k+1
        z = z+1
    for f in range(3):
        gtg[f] = g[f]- gt[f]
    print("this is w",w)
    print("the is gt",gt)
    print("the gradient vector",g)
    print("the gradient descent",gtg)
    print("-----------------------------------")
    print()
