import numpy as np
import matplotlib.pyplot as plt
import scipy.io

theta = np.arange(0, (2 * np.pi)+np.pi/180 , np.pi/180)
dbm_datas = np.genfromtxt("dipole_pattern.csv", delimiter=',')

absolute_dbm = np.absolute(dbm_datas)

max_value = np.max(dbm_datas)


index_max = np.where(dbm_datas==max_value)

temp=[]
dbm_3= max_value-3

for x in dbm_datas:
    temp.append(x-dbm_3)


temp =  [abs(ele) for ele in temp]



shoted_temp= sorted(temp)
index_3dbm = temp.index(min(temp))

print(index_3dbm)

print(dbm_datas[index_3dbm])





f_csv = open("sorted.csv", 'w')
for x in range(len(shoted_temp)):
    f_csv.write("değer:{} index:{}\n".format(shoted_temp[x],temp.index(shoted_temp[x])))



#
# f_csv = open("find3dbm.csv", 'w')
# f_csv.write("max değer:{} aranan değer :{}\n".format(max_value, dbm_3))
# for x in range(len(temp)):
#     if x==index_3dbm:
#         f_csv.write("****değer:{} fark:{}\n".format(dbm_datas[x],temp[x]))
#     else:
#         f_csv.write("değer:{} fark:{}\n".format(dbm_datas[x], temp[x]))

# index_3dbm = np.where((dbm_datas < dbm_3+0.05) & (dbm_datas > dbm_3-0.05))
# #index_3dbm = np.where(dbm_datas==-1.1077)
# print("max value: {} index: {}".format(max_value, index_max))
# print("-3dbm value: {} -3dbm index: {}".format(theta[index_3dbm], index_3dbm))
#
#
# print("------------")

#
# print(dbm_datas[index_3dbm])

# new_dbm_data = []
#
#
# f_csv = open("new_dbm_datas.csv", 'w')
# for x in dbm_datas:
#     #print(x/(-1*max_value))
#     new_dbm_data.append(x/max_value)
#     f_csv.write("{}\n".format(x/max_value))
#
# dbm_3=max_value/2
#
# print("dmb_3: {}".format(dbm_3))
#
# index = np.where((dbm_datas < dbm_3+0.05) & (dbm_datas > dbm_3-0.05))
# print(index)
#
# print(dbm_datas[index])
#
#
# for x in dbm_datas[index]:
#     print(x-dbm_3)
#
# index = np.where(dbm_datas==1.0992)
# print(index)
#
# print("Degree: {}".format(theta[index]))



fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, dbm_datas)
#ax.set_rmax(2)
#ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
#ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)
ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()



# temp=[]





# mat = scipy.io.loadmat('dataset_dipole.mat')



# for x in mat.values():
#     temp.append(x)
#
# print(temp[3].size)
#
#
# dbm_datas = np.copy(temp[3])
#
# print(dbm_datas.size)













