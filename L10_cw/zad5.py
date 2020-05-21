import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns = iris.feature_names)
s = abs(df['sepal length (cm)']-df['sepal width (cm)']) 
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=iris.target , s=s)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()