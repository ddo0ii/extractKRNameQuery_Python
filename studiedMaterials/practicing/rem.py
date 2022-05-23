# -*- encoding: utf-8 -*-
import pandas as pd 
import numpy as np

# making data frame from csv file 
data = pd.read_csv("Nature.csv", encoding="utf-8-sig") 
  
# dropping ALL duplicte values 
data.drop_duplicates(subset ="Link",keep = "last", inplace = True) 
  
# displaying data 
print(data)

data.to_csv("./result.csv")