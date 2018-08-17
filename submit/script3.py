import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')

species.fillna('No Intervention', inplace = True)

species['is_protected'] = species.conservation_status != 'No Intervention'

category_counts = species.groupby(['category', 'is_protected']).scientific_name.nunique().reset_index()
print category_counts.head()

category_pivot = category_counts.pivot(columns='is_protected', index='category', values='scientific_name').reset_index()
category_pivot.columns = ['category', 'not_protected', 'protected']


category_pivot['percent_protected'] = 100.0 * category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)

print category_pivot