import linecache
import matplotlib.pyplot as plt
import numpy as np
line_num=0
b=0
data1=[]
data_x=[]
for line in  open("laptop.txt"):
     line_num+=1
print(line_num)
for x in range(2,60):
    if x==2:
        lines=linecache.getlines('laptop.txt')[x]
    else:
        b=2+(x-2)*5
        lines=linecache.getlines('laptop.txt')[b]
    x=x+1
    b=x*20
    line=lines[14:19]
    l_line=float(line.replace('(','0'))
    data1.append(l_line)
    data_x.append(b)
    # print(data1)
    # print(data_x)
def drawpic(x_data,y_data):
    plt.title("laptop")
    # x_data = [2e-5, 3e-5, 4e-5, 5e-5]
    # y_data = [73.85, 71.35, 74.14, 74.32]
    # y_data2 = [61.32, 73.16, 73.88, 74.59]
    ln1, = plt.plot(x_data, y_data, color='red', linewidth=2.0, linestyle='--')
    # ln2, = plt.plot(x_data, y_data2, color='blue', linewidth=2.0, linestyle='--')

    plt.legend(handles=[ln1], labels=['APC_test_acc'])
    plt.xlabel("epoch")
    plt.ylabel("f1")
    plt.show()
drawpic(data_x,data1)