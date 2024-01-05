import matplotlib.pyplot as plt
from utility import *

def Pie_chart():
    x = ["A", "B", "C", "D"]
    y = [3, 8, 1, 10]
    plt.pie(y, labels=x)
    plt.show()
    
def Bar_chart():
    x = ["A", "B", "C", "D"]
    y = [3, 8, 1, 10]
    plt.bar(x, y)
    plt.show()
