import matplotlib.pyplot as plt


plt.scatter([2,1,3,4],[45,22,80,98], color='green',marker='o', label='Class A')
plt.scatter([2,1,3,4],[35,12,78,88], color='orange',marker='o', label='Class B')
plt.legend()
plt.xlabel('Time')
plt.ylabel('scores')
plt.title('Comparion of different classes')
plt.grid()
plt.show()
