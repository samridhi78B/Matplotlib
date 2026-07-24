import matplotlib.pyplot as plt
months = [1,2,3,4,5,6,7,8,9,10,11,12]
sales = [2500,1250,3000,2000,1500,2700,1000,7000,700,1500,1300,3400]

plt.plot(months,sales, color='green', linestyle='--', linewidth=3,marker='s', label='Sales 2025') #LINE-GRAPH
plt.xlabel('Months') #X-AXIS NAME
plt.ylabel('Sales') #Y-AXIS NAME
plt.title('Monthly Sales Data 2025') #TITLE OF PLOT
plt.legend(loc='upper left', fontsize=12) #SMALL BOX (LABEL WILL SHOW IF ONLY LEGEND IS USED) IN PLOT
plt.grid(color='grey', linestyle=':', linewidth=1)  #ADD GRID LINES
plt.xlim(1,6) #LIMIT WITH X-AXIS
plt.ylim(1000,5000) #LIMIT WITH Y-AXIS
plt.xticks([1,2,3,4,5,6], ['M1','M2','M3','M4','M5','M6']) #REPLACE WITH SOME OTHER VALUES
plt.show() #DISPLAY THE PLOT

