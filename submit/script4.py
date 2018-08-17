import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

# Loading the Data
species = pd.read_csv('species_info.csv')

# print species.head()

# Inspecting the DataFrame
species_count = len(species)

species_type = species.category.unique()

conservation_statuses = species.conservation_status.unique()

# Analyze Species Conservation Status
conservation_counts = species.groupby('conservation_status').scientific_name.count().reset_index()

# print conservation_counts

# Analyze Species Conservation Status II
species.fillna('No Intervention', inplace = True)

conservation_counts_fixed = species.groupby('conservation_status').scientific_name.count().reset_index()

# Plotting Conservation Status by Species
protection_counts = species.groupby('conservation_status')\
    .scientific_name.count().reset_index()\
    .sort_values(by='scientific_name')
    
# plt.figure(figsize=(10, 4))
# ax = plt.subplot()
# plt.bar(range(len(protection_counts)),
#        protection_counts.scientific_name.values)
# ax.set_xticks(range(len(protection_counts)))
# ax.set_xticklabels(protection_counts.conservation_status.values)
# plt.ylabel('Number of Species')
# plt.title('Conservation Status by Species')
# labels = [e.get_text() for e in ax.get_xticklabels()]
# print ax.get_title()
# plt.show()

species['is_protected'] = species.conservation_status != 'No Intervention'

category_counts = species.groupby(['category', 'is_protected'])\
                         .scientific_name.nunique().reset_index()
  
print category_counts.head()

category_pivot = category_counts.pivot(columns='is_protected', index='category', values='scientific_name').reset_index()

category_pivot.columns = ['category', 'not_protected', 'protected']

category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)

print category_pivot.head()
print 

contingency = [
  [category_pivot[category_pivot.category == 'Mammal'].iloc[0].protected, category_pivot[category_pivot.category == 'Mammal'].iloc[0].not_protected],
  [category_pivot[category_pivot.category == 'Bird'].iloc[0].protected, category_pivot[category_pivot.category == 'Bird'].iloc[0].not_protected]
]
print contingency

from scipy.stats import chi2_contingency

dummy, pval, dummy, dummy = chi2_contingency(contingency)
print pval

contingency = [
  [category_pivot[category_pivot.category == 'Mammal'].iloc[0].protected, category_pivot[category_pivot.category == 'Mammal'].iloc[0].not_protected],
  [category_pivot[category_pivot.category == 'Reptile'].iloc[0].protected, category_pivot[category_pivot.category == 'Reptile'].iloc[0].not_protected]
]
print contingency

dummy, pval_reptile_mammal, dummy, dummy = chi2_contingency(contingency)

print pval_reptile_mammal

categories = category_pivot.category.values
for x in categories:
	x_row = category_pivot[category_pivot.category == x].iloc[0]
	for y in categories:
		y_row = category_pivot[category_pivot.category == y].iloc[0]
		if x != y:
			contingency = [[x_row.protected, x_row.not_protected], [y_row.protected, y_row.not_protected]]
			dummy, pval, dummy, dummy = chi2_contingency(contingency)
			print x + " / " + y + ": " + str(pval)
