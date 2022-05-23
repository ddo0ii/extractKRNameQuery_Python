# -*- encoding: utf-8 -*-
import pandas as pd 
import numpy as np
import os
os.system("python Nature.py")

# making data frame from csv file 
data = pd.read_csv("Nature.csv", encoding="utf-8-sig", engine='python') 
  
# dropping ALL duplicte values 
data.drop_duplicates(subset ="Headline",keep = "last", inplace = True) 
  
# displaying data 
print(data)

data.to_csv("Nature_result.csv")