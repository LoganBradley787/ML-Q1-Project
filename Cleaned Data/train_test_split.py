import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv('description_split.csv')
train, test = train_test_split(df, test_size=0.2, random_state=42, stratify=df['Violation Type'])
# Save CSVs
train.to_csv("train_split.csv", index=False)
test.to_csv("test_split.csv", index=False)


