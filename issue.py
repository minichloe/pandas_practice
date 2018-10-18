import pandas as pd

summary = pd.read_csv('AIQ-user-summary.csv', index_col= 0)
summary.sort_index(inplace=True)
total = summary['total_spend'].sum()

df = []
i = 0
while i < 5:
  data = 'delta%s.csv' % str(i)
  df.append(pd.read_csv(data))
  i += 1

# Initialize final as initial set of data, delta0
initial = df.pop(0).set_index('user_id')

finalOmission = []

# Loop through the list of dataframes and update the columns by matching user ids
i = 1
delta2 = {}
while i < 5:
  final = initial.copy()
  # Calculate updated final dataframe but omitting one 'delta' update
  for idx, data in enumerate(df):
    if idx == i:
      continue
    final.update(data.set_index('user_id'))
  # Appending sum of total spend with the number of the delta file update that was omitted
  finalOmission.append((i, final['total_spend'].sum()))
  # Saving the dataframe that has the correct omitted file
  if i == 2:
    delta2 = final
  i+=1

# Printing the total sum of AIQ and all the calculated ones, we can see that delta2 was omitted from the calculations
print('AIQ', total)
print(finalOmission)

# Result: we can see that by omitting the delta2 file, the results are identical to the AIQ summary
('AIQ', 29162044)
[(1, 31002456.0), (2, 29162044.0), (3, 25402783.0), (4, 33904525.0)]

# Printing the first five rows for the newly computed dataframe and AIQ summary, we can see they are identical
print(delta2.head())
print(summary.head())
