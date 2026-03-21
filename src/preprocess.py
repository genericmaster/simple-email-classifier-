import pandas as pd
import numpy as np
import re
import logging
from src.utils.dataset_loader import uncleaned

# dealing with null values
def nullvalues(df:pd.DataFrame):
    
    null_ratio = df.isna().mean()
    if (null_ratio< 0.05).any():
            df= df.dropna().reset_index(drop=True)
    for column in df.columns:      
          if (df[column].isna().sum()/len(df[column]))>=0.8:
            df = df.dropna(columns=[column])
    return df

#dealing with duplicates
def duplicates(df:pd.DataFrame):
     dupe_count = df.duplicated().sum()
     if (dupe_count==0):
          pass
     elif dupe_count>0:
          df = df.drop_duplicates().reset_index(drop=True) 
     return df  

#making sure all strings are in lower
def lowercase(df:pd.DataFrame):
    for column in df.columns:
         df[column]=df[column].astype(str).str.lower().astype("string")
    return df
         
#removing whitespace
def whitespace(sentence):
     new  =re.sub(r'\s+', ' ', str(sentence)).strip()
     return new

def removewhitespace(df:pd.DataFrame):
     for column in df.columns:
     
      df[column]= df[column].apply( lambda x: whitespace(x))
     return df

#removing uneccesary features
#uncleaned= uncleaned[['Email Address','Email Content','Category']]

