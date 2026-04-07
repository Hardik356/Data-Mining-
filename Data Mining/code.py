import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Melt the DataFrame to long format for easier plotting
df_melted = pd.melt(
    df,
    var_name="Factors",
    value_name="Likert Scale"
)

# Print for understanding
print(df_melted)

# Set seaborn style
sns.set(style="whitegrid")

# Create the forest plot (point plot)
plt.figure(figsize=(6, 4))

sns.pointplot(
    x="Likert Scale",
    y="Factors",
    data=df_melted,
    color="steelblue"
)

# Labels and title
plt.xlabel("Likert Scale")
plt.ylabel("Factors")
plt.title("Forest Plot")

plt.tight_layout()
plt.show()