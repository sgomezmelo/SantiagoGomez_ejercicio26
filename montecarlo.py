import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
n = 50000000
g = 9.8
obs_max = [66.0, 120.0, 36.0,182.0]
obs_min = [56.0,110.0,26.0,172.0]

v = np.random.uniform(35.0,45.0,n)
theta = np.random.uniform(0,pi/2,n)

plt.figure()

for i in range(len(obs_max)):
    o_max = obs_max[i]
    o_min = obs_min[i]
    d = v**2*np.sin(2*theta)/g
    datos =  (d <= o_max) & (d >= o_min)
    v = v[datos]
    v = np.random.choice(v,n)
    theta = theta[:len(v)]
    print(len(v))
    plt.hist(v,normed = True,label = str(i))

plt.savefig('Montecarlo.pdf')
    

