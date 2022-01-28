from csv import reader
from skimage.measure import LineModelND, ransac
import numpy

def read_csv(name,nl="\n",dl=","):
    cloud=[]
    with open(name,newline=nl) as csvfile:
        csvreader=reader(csvfile,delimiter=dl)
        for xx, yy, zz in csvreader:
            cloud.append([float(xx), float(yy), float(zz)])
    return cloud

cloud=numpy.array(read_csv("cloud_r.xyz"))

model_robotus, inliers=ransac(cloud,LineModelND,min_samples=2,residual_threshold=1,max_trials=1000)
outliers=inliers==False

import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
ax.scatter(cloud[inliers][:,0],cloud[inliers][:,1],cloud[inliers][:,2],c='g',marker='o',label='inliers')
# ax.scatter(cloud[outliers][:,0],cloud[outliers][:,1],cloud[outliers][:,2],c='r',marker='o',label='outliers')
ax.legend(loc='lower left')
plt.show()

print(inliers)
