import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("manufacturing_data.csv")

data["Defect_Rate"] = data["Defective_Units"] / data["Units_Produced"] * 100

print(data)

product_defects = data.groupby("Product")["Defect_Rate"].mean()

product_defects.plot(kind="bar")
plt.title("Average Defect Rate by Product")
plt.ylabel("Defect Rate (%)")
plt.show()
