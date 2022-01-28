from scipy.stats import norm
from csv import writer
import random
import numpy

def generate_points(num_points, locx, scalex, locy, scaley, locz, scalez, move):
    distribution_x = norm(locx, scalex)
    distribution_y = norm(locy, scaley)
    distribution_z = norm(locz, scalez)

    x=distribution_x.rvs(size=num_points)
    y=distribution_y.rvs(size=num_points)
    z=distribution_z.rvs(size=num_points)

    points=zip(x+move,y+move,z+move)
    return points

def generate_cylinder(nr_points:int=5000, r=50, h=200, move=0):
    xx=[]
    yy=[]
    zz=[]
    while(len(xx) < nr_points):
        x = random.uniform(-1,1) * r
        y = random.uniform(-1, 1) * numpy.sqrt(r**2-x**2)
        z = random.uniform(-1, 1) * h

        xx.append(x + move)
        yy.append(y + move)
        zz.append(z + move)

    return zip(xx,yy,zz)

if __name__=='__main__':
    cylinder_points = generate_cylinder(1000)
    cloud1_points = generate_points(1000, 0, 100, 0, 100, 0, 1, 300)
    cloud2_points = generate_points(1000, 0, 1, 0, 100, 0, 100, -400)
    with open('pointsdata.xyz','w',encoding='utf-8',newline='\n') as csvfile:
        csvwriter=writer(csvfile)
        #csvwriter.writerow('x','x','z')
        for p1 in cylinder_points:
            csvwriter.writerow(p1)
        for p2 in cloud1_points:
            csvwriter.writerow(p2)
        for p3 in cloud2_points:
            csvwriter.writerow(p3)