import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

df = pd.read_csv('dataset.csv')
# combine SERO and ESERO into Repair Order
df["Violation Type"] = df["Violation Type"].replace({"SERO": "Repair Order", "ESERO": "Repair Order"})
# stratified split, keep 0.5% of data
split = StratifiedShuffleSplit(n_splits=1, test_size=0.005, random_state=42)
# split for each violation
for train_index, sample_index in split.split(df, df['Violation Type']):
    stratified_sample = df.iloc[sample_index]
# save to csv
stratified_sample.to_csv('stratified_sample.csv', index=False)

print(stratified_sample['Violation Type'].value_counts())  # new unique value counts
