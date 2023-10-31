# distribution of 2 digits in pi for 2069 pairs starting with 31 41 52
# and creating a histogram

import matplotlib.pyplot as plt
import numpy as np
import math_pi

# number of precincts in Chicago, with source
# https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Ward-Precincts-2012-2022-/uvpq-qeeq
precincts = 2069 # 2069

source_pi = math_pi.pi(b=precincts*2)
random_two_digits = [31]
for i in range(1,precincts):
    two_digits = int(source_pi[i*2+1:i*2+3])
    random_two_digits.append(two_digits)

plt.hist(random_two_digits, bins=100)
plt.grid(axis = 'y')
plt.show()

# random_two_digits = np.random.randint(100, size=precincts)
