import numpy as np
import pandas as pd
import math
import time


column_names=['class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalnity of ash', 'Magnesium', 
              'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 
              'Color intensity', 'Hue', 'diluted wines', 'Proline']

wine = pd.read_csv('C:/Users/enee/Desktop/Study/PYthon/wine.csv', names = column_names)
del wine['class']
columns = wine.columns

wine2 = wine.copy()
mean_columns = pd.DataFrame(index = ['mean'], columns = columns)


for i in columns:
    mean_columns[i] = wine2[i].mean()
    ranges=[wine2[i].min(), wine2[i].mean(), wine2[i].max()]
    binned_feature_i , bins_i = pd.cut(wine2[i],
                                      ranges,
                                      labels = [-1,1],
                                      retbins = True,
                                      include_lowest=True)
    wine2[i] = binned_feature_i
    
end_time = time.time()   
print('time: ', end_time - start_time)