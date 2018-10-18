import pandas as pd

# Read the AIQ summary and calculate the total spend, which is $29,162,044
summary = pd.read_csv('AIQ-user-summary.csv', index_col= 0)
summary.sort_index(inplace=True)
total = summary['total_spend'].sum()
print('AIQ', total)

# Read the Johnny Jeans summary and calculate the total spend, which is $33,904,525
Jsummary = pd.read_csv('Johnny-user-summary.csv', index_col=0)
Jsummary.sort_index(inplace=True)
Jtotal = Jsummary['total_spend'].sum()
print('Johnny Jeans', Jtotal)

# Initialize a list and use a loop to read all csv files
df = []
i = 0
while i < 5:
  data = 'delta%s.csv' % str(i)
  df.append(pd.read_csv(data))
  i += 1

# Initialize final as initial set of data, delta0
final = df.pop(0).set_index('user_id')

# Loop through the list of dataframes and update the columns by matching user ids
for idx, data in enumerate(df):
  final.update(data.set_index('user_id'))

# Printing the first five rows, we can see that the data for users 1 & 3 do not match up
print(summary.head())
print(final.head())

# Printing the final from Johnny Jeans and our calculated final, they are identical
print('Johnny Jeans', Jtotal)
print('Calculated total from Final', final['total_spend'].sum())
