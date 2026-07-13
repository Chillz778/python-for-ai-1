# analyzer.py
import pandas as pd
from helpers import calculate_total, format_currency

# data remains the same
df = pd.read_csv('data/sales.csv')

# Calculate total for each row
df['total'] = df.apply(lambda row: calculate_total(row['quantity'], row['price']), axis=1)

# Display with formatted totals
print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

# Show grand total
grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")

# im done here 