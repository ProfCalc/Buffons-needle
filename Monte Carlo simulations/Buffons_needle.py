import numpy as np
import matplotlib.pyplot as plt
import time as t

n_needle=int(10000)

ping = t.time()

length = 0.5

y_lines= [-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12]

def createneedle(l = 1):
    startpoint = (np.random.uniform(0,10),np.random.uniform(0,10))

    theta = np.random.uniform(0,np.pi)

    endpoint =(startpoint[0] + (l*np.cos(theta)) , startpoint[1] + (l*np.sin(theta)))
    return [startpoint, endpoint]

def checkintersection(s):
    for i in y_lines:
        if s[0][1] < i and s[1][1] > i:
            return True
    
    return False


######This methode to simply/ mathematically simulate#########


# counter = 0

# for _ in range(n_needle):
#     i = createneedle(length)

#     if checkintersection(i):
#         counter+=1

# print(n_needle/counter)




#######This method required for ploting ##########

cords = []


for _ in range(n_needle):
    cords.append(createneedle(length))
#print(cords)    
cords = np.array(cords)
#print(cords)
#print(np.max(cords), np.min(cords))

for n in cords:
    plt.plot(n[:,0] , n[:,1])     ###Matplotlib
plt.hlines(y_lines, -2, 12, colors = "black")
plt.show()

counter = 0

for n in cords: 
   if checkintersection(n):
       counter+=1

pong = t.time()

print(n_needle/counter)      
print(pong-ping)       
    

