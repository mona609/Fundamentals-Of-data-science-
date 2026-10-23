import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']
temp = [25, 28, 30, 32]
rain = [20, 40, 30, 60]

plt.plot(months, temp)
plt.show()

plt.scatter(months, rain)
plt.show()
