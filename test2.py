import pandas as pd

file_path = 'Grocery_Inventory_and_Sales_Dataset.csv'

try:
    df = pd.read_csv(file_path)

    print(f"總共讀取到 {len(df)} 筆商品數據。\n")
except FileNotFoundError:
    print(f"【錯誤】找不到檔案：'{file_path}'")
    print("請確保 CSV 檔案與此 Python 程式放在同一個資料夾下，且名稱完全相同。")
    exit()

df['Unit_Price'] = df['Unit_Price'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False)
df['Unit_Price'] = pd.to_numeric(df['Unit_Price'], errors='coerce')
df['Stock_Quantity'] = pd.to_numeric(df['Stock_Quantity'], errors='coerce')
df['Sales_Volume'] = pd.to_numeric(df['Sales_Volume'], errors='coerce')

df['Total_Inventory_Value'] = df['Stock_Quantity'] * df['Unit_Price']
df['Original_Revenue'] = df['Sales_Volume'] * df['Unit_Price']
df['Discounted_Revenue'] = df['Original_Revenue'] * 0.9
total_discounted_revenue = df['Discounted_Revenue'].sum()

best_seller_idx = df['Sales_Volume'].idxmax()
best_seller = df.loc[best_seller_idx]




print(df[['Product_ID', 'Product_Name', 'Stock_Quantity', 'Unit_Price', 'Total_Inventory_Value']].head())


print(f"    商品名稱 (Product_Name) : {best_seller['Product_Name']}")
print(f"    商品編號 (Product_ID)   : {best_seller['Product_ID']}")
print(f"    總銷售量 (Sales_Volume) : {best_seller['Sales_Volume']} 件")
print(f"    該品項原始總銷售額      : ${best_seller['Original_Revenue']:.2f}")


print(f"    總收入 (Total Discounted Revenue): ${total_discounted_revenue:,.2f}")
print("="*40)

output_path = 'grocery_analysis_results.csv'
df.to_csv(output_path, index=False)
