import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Load Dataset (FIXED)
df = pd.read_csv("marketing_campaign.csv", sep=";")

print("🔹 Columns in Dataset:")
print(df.columns)

# STEP 2: Data Cleaning
df = df.dropna()
df = df.drop_duplicates()

print("\n✅ Data cleaned successfully!")

# STEP 3: Total Spending
df["Total_Spending"] = (
    df["MntWines"] +
    df["MntFruits"] +
    df["MntMeatProducts"] +
    df["MntFishProducts"] +
    df["MntSweetProducts"] +
    df["MntGoldProds"]
)

# STEP 4: Campaign Performance
campaign_cols = [
    "AcceptedCmp1",
    "AcceptedCmp2",
    "AcceptedCmp3",
    "AcceptedCmp4",
    "AcceptedCmp5",
    "Response"
]

campaign_performance = {}

for col in campaign_cols:
    accepted = df[df[col] == 1]
    total_spend = accepted["Total_Spending"].sum()
    count = accepted.shape[0]

    avg_spend = total_spend / count if count > 0 else 0
    campaign_performance[col] = avg_spend

campaign_df = pd.DataFrame(
    list(campaign_performance.items()),
    columns=["Campaign", "Avg_Spending"]
)

print("\n📊 Campaign Performance:")
print(campaign_df)

# STEP 5: Plot
plt.figure()
plt.bar(campaign_df["Campaign"], campaign_df["Avg_Spending"])
plt.title("Campaign Performance (Avg Spending)")
plt.xlabel("Campaign")
plt.ylabel("Avg Spending")
plt.xticks(rotation=45)
plt.savefig("campaign_performance.png")
plt.show()

# STEP 6: Funnel
total_customers = df.shape[0]
total_response = df["Response"].sum()

plt.figure()
plt.bar(["Total Customers", "Responded"], [total_customers, total_response])
plt.title("Marketing Funnel")
plt.savefig("funnel.png")
plt.show()

# STEP 7: Best & Worst
best_campaign = campaign_df.loc[campaign_df["Avg_Spending"].idxmax()]
worst_campaign = campaign_df.loc[campaign_df["Avg_Spending"].idxmin()]

print("\n🏆 Best Campaign:")
print(best_campaign)

print("\n❌ Worst Campaign:")
print(worst_campaign)

print("\n🎯 TASK 04 COMPLETED SUCCESSFULLY!")