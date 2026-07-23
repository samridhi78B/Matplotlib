import matplotlib.pyplot as plt
x=['Monday','Tuesday','Wednesday', 'Thursday','Friday','Saturday']
y=[700,120,2500,1300,550,350]

plt.plot(x,y) #to make plot

plt.title('Sales') #to set title

plt.xlabel("Days of the week") #represent x -axis name
plt.ylabel("Sales per Day")#represent x -axis name 

plt.show() #to display plot
