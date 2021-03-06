# -*- coding: utf-8 -*-
"""proj107.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dGNny0ZJ914x76DmsKsqvq57Jj7ju0DE
"""

from google.colab import files
data_to_load = files.upload()

import pandas as pd
import plotly.express as px

df = pd.read_csv("data2.csv")
levelMean = df.groupby("level")["attempt"].mean()

print(levelMean)


fig = px.scatter(levelMean, x = "attempt", y = ["level1", "level2", "level3", "level4"], color = "attempt", size_max = 80)
fig.show()