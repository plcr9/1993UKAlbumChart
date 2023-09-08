import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

album = pd.read_csv("1993AlbumChart.csv")


entry_position = album["EntryPosition"]
peak_position = album["PeakPosition"]
plt.scatter(entry_position, peak_position)
plt.title("Correlation between entry and peak position of 1993 Album Chart entries")
m, c = np.polyfit(entry_position, peak_position, 1)
plt.plot(entry_position, m*entry_position + c, color='red')
plt.xlabel('EntryPosition')
plt.ylabel('PeakPosition')
plt.title("Scatter Plot with Line Of Best Fit")
plt.show()
print(f"The equation of line of best fit is y = {m:.4f}x + {c:.4f}")