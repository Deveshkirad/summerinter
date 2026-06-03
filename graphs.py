import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import Values
x=np.linspace(0,10,100)
y=np.sin(x)
plt.plot(x,y,label='sin(x)',color='blue',linestyle='--')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sine Wave')
plt.legend()
plt.grid(True)
plt.show()


Categories = ['A', 'B', 'C']
values = [10, 15, 7]
plt.bar(Categories, values, color=['red', 'green', 'blue'])
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()


data = np.random.rand(100)
plt.hist(data, bins=30, color='purple', alpha=0.7, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

labels=['python','java','c++','javascript']
sizes=[40,30,20,10]
plt.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=140)
plt.axis('equal')
plt.show()


