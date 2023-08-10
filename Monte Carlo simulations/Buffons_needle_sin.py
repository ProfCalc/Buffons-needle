import numpy as np
import matplotlib.pyplot as plt
import time as t

n_needle=int(100000)

ping = t.time()

length = 0.5

y_lines= [-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12]

def createneedle(l = 1):
    startpoint = (np.random.uniform(0,10),np.random.uniform(0,10))

    theta = np.random.uniform(0,np.pi)

    endpoint =(startpoint[0] + (l*np.cos(theta)) , startpoint[1] + (l*np.sin(theta)))
    return np.array([startpoint, endpoint])

# def checkintersection(s):
#     for i in y_lines:
#         if s[0][1] < (np.sin(s[0][0])+i) and s[1][1] > (np.sin(s[1][0])+i):
#             return True
#         elif s[0][1] > (np.sin(s[0][0])+i) and s[1][1] < (np.sin(s[1][0])+i):   ##### ~REDUNDUNT~ ##########
#             return True
    
#     return False

def checkmultintersection(s,n):
    ycord = ((s[0][1]*n) + (s[1][1]*(1-n)))
    xcord = ((s[0][0]*n) + (s[1][0]*(1-n)))
    for i in y_lines:
        if (s[0][1]-(np.sin(s[0][0])+i))*(ycord - (np.sin(xcord)+i)) < 0:
            return True
    return False



#######################SIMPLE CASE##########################################
counter = 0

for _ in range(n_needle):
    i = createneedle(length)
    for n in np.arange(0,1,0.1):
        if checkmultintersection(i,n):
            counter+=1

print(counter/n_needle)

#######################AVERAGE CASE###################################
fv=[]
for _ in range(100):
    counter = 0

    for _ in range(n_needle):
        i = createneedle(length)
        for n in np.arange(0,1,0.1):
            if checkmultintersection(i,n):
                counter+=1
    fv.append((counter/n_needle))

np.array(fv)
print(np.mean(fv))


