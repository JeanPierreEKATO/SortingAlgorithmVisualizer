import pandas as pd
import numpy as np

myList: list = []

for i in range(0, 101):
    myList.append(i)

np.random.shuffle(myList)


dataSet = pd.DataFrame(myList, columns=["Zahlen"])

dataSet.head(10)

dataSet