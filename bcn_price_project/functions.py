import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

## Categoricals

# Plotting Categorical variables
fig, axes = plt.subplots(3, 2, figsize=(20, 20))  # Set the figure size before the loop

for i, el in enumerate(df[categoricals]):
    counts = df[el].value_counts() / df[el].count()
    if i == 0:
        axes.flatten()[0].barh(counts.index, counts, color='green')  # Create the first subplot separately
        axes.flatten()[0].set_title(el)
    else:
        axes.flatten()[i].barh(counts.index, counts, color='green')  # Use i for subsequent subplots
        axes.flatten()[i].set_title(el)

plt.tight_layout()
plt.show()  # Display all subplots at once


####################

def category_summary(df,variables,gr_column,target):
    val = df.groupby([gr_column])[variables].mean().sort_values(by=target,ascending = False).round(3).reset_index()
    return val
