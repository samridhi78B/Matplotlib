import matplotlib.pyplot as plt
months = [1,2,3,4,5,6,7,8,9,10,11,12]
sales = [2500,1250,3000,2000,1500,2700,1000,7000,700,1500,1300,3400]

plt.plot(months,sales, color='green', linestyle='--', linewidth=3,marker='s', label='Sales 2025')
plt.legend(loc='upper left')
plt.show()
