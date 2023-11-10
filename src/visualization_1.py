# Data exploration
# dawn

# Data exploration
# dawn
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'NBS_merged.xlsx'  # Google Colab file path
data = pd.read_excel(file_path)

# Transposing the dataset for easier plotting
data_transposed = data.set_index('Indicators').T
data_transposed.index = pd.to_datetime(data_transposed.index)

# Selecting an indicator for visualization
# Example: 'Total Retail Sales of Consumer Goods, Current Period(100 million yuan)'
indicator = 'Total Retail Sales of Consumer Goods, Current Period(100 million yuan)'

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(data_transposed[indicator], marker='o')  # Added markers for clarity
plt.title(f'Time Series of {indicator}')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()
