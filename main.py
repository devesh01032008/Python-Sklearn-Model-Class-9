# Importing os module LinearRegression matplotlib numpy for this project


# os module help to automatically install sklearn and matplotlib library using CMD line


import os


try:
	os.system("pip install sklearn matplotlib")
except Exception as e:
	os.system("pip3 install sklearn matplotlib")
	
# Importing LinearRegression present in sklearn.linear_model help to make linear model


from sklearn.linear_model import LinearRegression

# Sklearn Works with numpy so importing numpy arrays as np


import numpy as np

# Importing Matplotlib for making a line graph using pyplot library as ply


from matplotlib import pyplot as plt

# Giving freezing and boiling point of water as reference for both Celsius and Fahrenheit


Celsius = np.array([[0],[100]])
Fahrenheit = np.array([[32],[212]])

# Making Linear Model

model = LinearRegression()

# Fitting Values of Celsius and Fahrenheit in model


model.fit(Celsius, Fahrenheit)

# Predicting Values using model 
# Change temperature to convert in into Fahrenheit 


user_temp = 37

celsius_test = np.array([[user_temp]])

fahrenheit_predict = model.predict(celsius_test)

# Typecasting it to float value (Optional)

fahrenheit_predict = float(fahrenheit_predict)
print(fahrenheit_predict)

# Plotting it on graph using matplotlib


plt.xlabel("Celsius")
plt.ylabel("Fahrenheit")
plt.plot(Celsius, Fahrenheit)
plt.show()
