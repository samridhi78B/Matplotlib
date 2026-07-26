import matplotlib.pyplot as plt

time= [2,1,3,4]
scores =[45,22,80,98]

plt.scatter(time,scores, color='green',marker='o', label='Scores')
plt.legend()
plt.xlabel('Time')
plt.ylabel('scores')
plt.title('Comparion of students')
plt.grid()
plt.show()
