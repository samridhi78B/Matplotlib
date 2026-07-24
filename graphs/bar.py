import matplotlib.pyplot as plt

months = [1,2,3,4,5,6]
sales = [2500,1250,3000,2000,1500,2700]

plt.bar(months, sales, color='orange',label='Sales 2025')
#FOR HORIZONTAL BAR GRAPH USE plt.barh(...)

plt.legend()
plt.title('Sales of the year 2025')
plt.show()
