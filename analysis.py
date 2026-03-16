import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("manufacturing_data.csv")

# Calculate defect rate
data["Defect_Rate"] = (data["Defective_Units"] / data["Units_Produced"]) * 100

print("Dataset Preview")
print(data)

# Average defect rate by product
product_defects = data.groupby("Product")["Defect_Rate"].mean()

print("\nAverage Defect Rate by Product")
print(product_defects)

# Plot results
product_defects.plot(kind="bar")

plt.title("Average Defect Rate by Product")
plt.ylabel("Defect Rate (%)")
plt.xlabel("Product")

plt.show()
