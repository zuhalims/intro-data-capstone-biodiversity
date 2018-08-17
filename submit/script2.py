import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')

species.fillna('No Intervention', inplace = True)
protection_counts = species.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by='scientific_name')
plt.figure(figsize=(10,4))
ax = plt.subplot()
plt.xticks(range(0, len(protection_counts.conservation_status.values)), protection_counts.conservation_status.values)
plt.ylabel('Number of Species')
plt.title('Conservation Status by Species')
plt.bar(range(0, len(protection_counts.conservation_status.values)), protection_counts.scientific_name.values)
plt.show()