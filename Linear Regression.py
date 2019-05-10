#LINEAR REGRESSION
import matplotlib.pyplot as plt
x = [3, 6, 2, 1, 4, 7]
y = [15, 30, 10, 5, 20, 35]
y_predicted = [5*i for i in x]
plt.scatter(x, y, c = "b", alpha = 0.5, marker = '^', label = "#Pastries")
plt.plot(x, y_predicted, c = "r")
plt.xlabel("Pastries")
plt.ylabel("Earnings")
plt.legend(loc = 2)
plt.show()
