import codecademylib
import pandas as pd
import matplotlib as plt

species = pd.read_csv('species_info.csv')
print species.head()

species_count = len(species.scientific_name.unique())
species_type = species.category.unique()
print species_type
conservation_statuses = species.conservation_status.unique()

conservation_counts = species.groupby('conservation_status').scientific_name.nunique().reset_index()
print conservation_counts

species.fillna('No Intervention', inplace = True)
conservation_counts_fixed = species.groupby('conservation_status').scientific_name.nunique().reset_index()
print conservation_counts_fixed
print conservation_counts_fixed.conservation_status.tolist()
