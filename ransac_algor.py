from csv import reader

import numpy
import pyransac3d

def read_csv(name,nl="\n",dl=","):
    cloud=[]
    with open(name,newline=nl) as csvfile:
        csvreader=reader(csvfile,delimiter=dl)
        for xx, yy, zz in csvreader:
            cloud.append([float(xx), float(yy), float(zz)])
    return cloud

if __name__=="__main__":

    cloud=numpy.array(read_csv("LidarData.xyz"))

    plane=pyransac3d.Plane()
    best_eq, best_inliers=plane.fit(cloud, thresh=0.01, minPoints=100, maxIteration=1000)

    print(f'best euation Ax+By+Cz+D:{best_eq}')
    print(f'best inliers:{best_inliers}')

