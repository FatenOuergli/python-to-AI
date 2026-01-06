import pandas as pd
import os
from helpers import calculate_total, format_currency

# Read the CSV file
df = pd.read_csv('data/sales.csv')
#calculate total for each row(loop needed)
totals=[]
for index, row in df.iterrows():
    total=calculate_total(row['quantity'], row['price'])
    totals.append(total)

    #add totals to our data
df['Total']=totals
#print with the formatted total
for index ,row in df.iterrows():
    formatted_total=format_currency(row['Total'])
    print(f"{row['product']}: {formatted_total}")

#now we'll add another column for showing the total of the totals!
grand_total=df['Total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")

# Create a DataFrame
grand_total_df = pd.DataFrame({
    'Grand Total': [formatted_grand_total]
})
grand_total_df.to_csv('output/grand_total.csv',index=False)


#this part is old one! 
# Create output directory
os.makedirs('output', exist_ok=True)

# Save as different formats
# 1. JSON format (good for web APIs)
df.to_json('output/sales_data.json', orient='records', indent=2)

# 2. Excel format (good for sharing)
df.to_excel('output/sales_data.xlsx', index=False)

# 3. Updated CSV (with our new total column)
df.to_csv('output/sales_with_totals.csv', index=False)

print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx") 
print("- output/sales_with_totals.csv")