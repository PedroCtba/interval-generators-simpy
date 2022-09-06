import numpy as np
import pandas as pd
from random import uniform
from math import floor, ceil

class QueueTimeSimulator:
    # Def generator with initial mean and sigma
    def __init__(self, mu, sigma, rate_of_arrival):
        # Define atributes
        self.mu = mu
        self.sigma = sigma
        self.rate_of_arrival = rate_of_arrival
        self.times = []
        self.analysis = pd.Series(dtype="object")

        # Run initial method
        self.define_high_and_low_boundaries()
    
    # Make gen time method
    def gen_times(self):
        # See if the lenght of already picked times is equal or higher than a "semi-aleatory" boundarie
        if len(self.times) >= self.pick_rate_of_arrival_boundarie():
            time = 30 - sum(self.times)
            
            # Save the information about it being equal to lower boundarie, or if the higher boundarie was picked
            if len(self.times) == self.lower:
                self.analysis = pd.concat([self.analysis, pd.Series("Down")], ignore_index=True)
            
            else:
                self.analysis = pd.concat([self.analysis, pd.Series("Up")], ignore_index=True)

            # Set times list as empty
            self.times = []

            # Return the time
            return time
        
        # If not just make a smal timestamp
        else:
            time = np.random.normal(self.mu, self.sigma)
            time = time if time > 0 else 0
            self.times.append(time)
            return time

    # Define the lower and higher boundarie
    def define_high_and_low_boundaries(self):
        self.lower = floor(self.rate_of_arrival) - 1
        self.higher = ceil(self.rate_of_arrival) - 1

        return None

    def pick_rate_of_arrival_boundarie(self):
        # Select a rand between 0 and 1
        _picked_rate = uniform(0, 1)

        # Select float part of rate
        _float_part = self.rate_of_arrival % 1

        # Return picked boundarie
        if _picked_rate < (1 - _float_part):
            return self.lower

        else:
            return self.higher