import matplotlib.pyplot as plt

marks=[89,56,34,12,78,36,80,98,32,16,78,56,34,72,99,55]

plt.hist(marks, bins=4,color='purple',edgecolor='black')
plt.xlabel('Marks')
plt.ylabel('No. of Students')
plt.title('Marks of students')
plt.show()
