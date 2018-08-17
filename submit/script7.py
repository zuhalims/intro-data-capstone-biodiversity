baseline=15
minimum_detectable_effect=5.0/15*100.0
print minimum_detectable_effect
sample_size_per_variant=870
import math
yellowstone_weeks_observing=math.ceil(sample_size_per_variant / 507.0)
bryce_weeks_observing=math.ceil(sample_size_per_variant / 250.0)
print yellowstone_weeks_observing
print bryce_weeks_observing