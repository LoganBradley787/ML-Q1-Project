import pandas as pd
df = pd.read_csv('cleaned_dropped_missingvals_replaced.csv')
descriptions = df["Description"].unique()

def categorize_speeding(description):
    if "speed" not in description.lower():
        return "No"
    if "mph in a posted" in description.lower():
        return "Measured" 
    return "Yes"

def categorize_alcohol(description):
    if "alcohol" in description.lower():
        return "Yes"
    return "No"
# Applying the function to the DataFrame
df["Speeding"] = df["Description"].apply(categorize_speeding)
df["Alcohol"] = df["Description"].apply(categorize_alcohol)

# Move Violation Type to last column so Weka sees it as class
df['Violation Type'] = df.pop('Violation Type')
df.to_csv("description_split.csv", index=False)