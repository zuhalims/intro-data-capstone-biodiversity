import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'

observations = pd.read_csv('observations.csv')

#print observations.head()
species['is_sheep'] = species.apply(lambda x: 'Sheep' in x.common_names, axis=1)
species_is_sheep = species[species.is_sheep]
#print species_is_sheep.head()
sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]
#print sheep_species.head()

sheep_observations = pd.merge(observations, sheep_species)
print sheep_observations
obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
print obs_by_park
