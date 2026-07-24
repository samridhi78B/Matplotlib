import matplotlib.pyplot as plt
regions=['CocaCola','Pepsi','Thumsup','Sprite','Fanta']
likes = [3500,2300,4700,3200,1500]

plt.pie(likes, labels=regions, colors=['lightgreen','skyblue','coral','yellow','orange'],autopct='%1.1f%%')

plt.title('Drinks liked by students')
plt.show()
