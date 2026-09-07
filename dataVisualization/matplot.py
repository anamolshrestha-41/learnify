import matplotlib.pyplot as plt

# Matplotlib is the foundation of almost every Python visualization library.
##Figure: is the entire window or canvas
#Think of it like whole paper
# Figure
# -------------------------
# |                       |
# |      Graph            |
# |                       |
# -------------------------

# fig= plt.figure(figsize=(8,5))
# plt.show() #Output: Empty window, You only created the paper.
fig= plt.figure(figsize=(5,5))
# plt.show() #Both provide diff size paper

#Axes: Axes are the actual graph area.
# Figure
# --------------------------
#       Axes
#    X-axis
#    Y-axis
# --------------------------
# One Figure can contain many Axes.

# ax=fig.add_subplot()
# ax.plot([1,2,3,4],[2,4,6,8])
# plt.show() #Output: A line graph with the specified data points

#Styles: Styles change appearance. Instead of changing every color manually. Use style.
# plt.style.use('ggplot')
# plt.style.use('dark_background')
# plt.style.use('Solarize_Light2')
# plt.plot([1,2,3,4],[2,4,6,8])
# plt.show() #Output: A line graph with the specified data points in ggplot style

#Multiple plots: More than one line in same graph. Useful for comparing.
# months=[1,2,3,4]
# boys=[2,4,6,8]
# girls=[1,3,5,7]

# plt.plot(months,boys,label='Boys',color='blue')
# plt.plot(months,girls,label='Girls',color='pink')
# #Legends: It tells which linne belongs to whom.
# plt.legend()
# plt.show() #Output: A line graph with two lines,

#Twin axes: Sometimes two datasets have different scales.
# fig,ax1=plt.subplots()
# ax2= ax1.twinx() #Creates a second axes that shares the same x-axis
# months=[1,2,3,4]
# temp=[20, 22, 25, 30]
# rain=[200, 100, 300, 190]
# ax1.plot(months, temp, color='red', label='Temperature')
# ax2.plot(months, rain, color='blue', label='Rainfall')
# plt.show()

#Subplots: Instead of many windows. Show many graphs together.
# -------------
# |     |     |
# | G1  | G2  |
# -------------
# | G3  | G4  |
# -------------

# fig, axs= plt.subplots(2,2, figsize=(10,8))
# axs[0,0].plot([1,2,3,4],[2,4,6,8])
# axs[0,1].bar([1,2,3,4],[1,3,5,7])
# axs[1,0].scatter([1,2,3,4],[2,3,5,7])
# axs[1,1].hist([1,2,3,4],[1,4,6,8])
# plt.show()

#Saving plots: Save the graph as an image file.
plt.plot([1,2,3],[5,7,6])
plt.savefig("sales.png")
plt.show()