import matplotlib.pyplot as plt
plt.title("laptop-F1-scores")
x_data = [2e-5,3e-5,4e-5,5e-5]
y_data = [73.85,71.35,74.14,74.32]
y_data2 = [61.32,73.16,73.88,74.59]

ln1, = plt.plot(x_data, y_data, color='red', linewidth=2.0, linestyle='--')
ln2, = plt.plot(x_data, y_data2, color='blue', linewidth=2.0, linestyle='--')


plt.legend(handles=[ln1,ln2],labels=['GRU','TFM'])
plt.xlabel("Steps")
plt.ylabel("f1")
plt.show()
