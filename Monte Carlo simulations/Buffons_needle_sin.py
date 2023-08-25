import numpy as np
import matplotlib.pyplot as plt
import time as t

#n_needle=int(100)


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
# counter = 0
# n_needle = 100000
# for _ in range(n_needle):
#     i = createneedle(length)
#     for n in np.arange(0,1,0.1):
#         if checkmultintersection(i,n):
#             counter+=1
#             break

# print(n_needle/counter)

#######################AVERAGE CASE###################################
# fv=[]
# for _ in range(10):
#     counter = 0

#     for _ in range(n_needle):
#         i = createneedle(length)
#         for n in np.arange(0,1,0.1):
#             if checkmultintersection(i,n):
#                 counter+=1
#     fv.append((n_needle/counter))

# np.array(fv)
# print(fv)
# print(np.mean(fv))

#################### Testing the convergence of the monte carlo simulation #########################


# n_needle = 10
# needles = []
# value = []
# while n_needle < 100001:
#     counter = 0
#     for _ in range(n_needle):
#         i = createneedle(length)
#         for n in np.arange(0,1,0.1):
#             if checkmultintersection(i,n):
#                 counter+=1
#     needles.append(n_needle)
#     value.append((n_needle/counter))
#     n_needle = n_needle*2


# print(needles)
# print(value)
# # plt.plot(needles, value)
# # plt.xlabel('Needles')
# # plt.ylabel('Value of Pi')
# # plt.xticks(needles)
# # plt.title('Convergence of monte carlo')
# # plt.show()

# f = open("Sin_Values.txt", "w" )
# for i in range (0,len(needles)-1,1):
#     f.write("X Y")
#     f.write("%s  %s \n"%(needles[i],value[i]))

########################## Print out in Text##############################################

n_needle = 10
f = open("sin_Values.txt", "w" )
f.write("X Y \n")
while n_needle < 1000001:
    counter = 0
    for _ in range(n_needle):
        i = createneedle(length)
        for n in np.arange(0,1,0.1):
            if checkmultintersection(i,n):
                counter+=1 
                break      
        

    f.write("%s %s \n"%(n_needle,n_needle/counter))
    n_needle= n_needle*2

