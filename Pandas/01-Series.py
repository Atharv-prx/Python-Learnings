# Series = A pandas 1-Dimensional labelled array that can hold any data type
#          Think of it like a single column in a spreadsheet (1-dimensional)
import pandas as pd

data = [10, 20, 30]
series = pd.Series(data, index = ["a", "b", "c"])
print(series)
print(series.loc["a"]) # loc = location by label 