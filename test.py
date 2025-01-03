import pandas as pd

# Load your train_data and test_data from CSV (or another source)
train_data = pd.read_csv('artifacts/train.csv')
test_data = pd.read_csv('artifacts/test.csv')

# Now check the columns
print("Columns in train_data:", train_data.columns)
print("Columns in test_data:", test_data.columns)

# Check if 'race_ethnicity' is in both datasets
assert 'race_ethnicity' in train_data.columns, "race_ethnicity not found in train_data"
assert 'race_ethnicity' in test_data.columns, "race_ethnicity not found in test_data"
