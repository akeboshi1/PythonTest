import main
import matplotlib.pyplot as plt

main.func()
# 绘制一个简单的线图
x = [1,2,3]
y = [2,4,1]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Graph')
plt.show()

# 绘制多个线在同一图中 
x1 = [1,2,3]  
y1 = [2,4,6]
x2 = [1,2,3]
y2 = [4,1,3]
plt.plot(x1, y1, label='line1')
plt.plot(x2, y2, label='line2', linestyle='--')  
plt.xlabel('x')
plt.ylabel('y')  
plt.title('Multiple Lines')
plt.legend()
plt.show()

# 绘制条形图
fruit = ['Apples', 'Oranges', 'Bananas', 'Cherries']
number = [4, 6, 5, 3] 
plt.bar(fruit, number)
plt.ylabel('Quantity')
plt.title('Fruit Bars')
plt.show()