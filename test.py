import blood_level
import numpy as np

bld=blood_level.alcohol_level(70)
bld.add_drink(24,60)
bld.add_drink(12,120)
bld.plot_level()

