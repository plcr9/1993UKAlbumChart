import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

album = pd.read_csv("1993AlbumChart.csv")

max1 = album['WeeksInTop100'].max()
min1 = album['WeeksInTop100'].min()
sum1 = album['WeeksInTop100'].sum()
count1 = album['WeeksInTop100'].count()
median1 = album['WeeksInTop100'].median()
std1 = album['WeeksInTop100'].std()
var1 = album['WeeksInTop100'].var()

groupby_sum1 = album.groupby(['ReleaseYear']).sum()
groupby_count1 = album.groupby(['ReleaseYear']).count()

print(sum1)
print(groupby_sum1)
print(count1)
print(groupby_count1)

limit = 1
column_name = 'WeeksInTop10'
count2 = np.count_nonzero(album[column_name] > limit)
print(count2)