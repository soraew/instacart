import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def uniques(series): return series.unique()/len(series)

def uniques_df(df):
    for column in df.columns:
        print(uniques(df[column]))