import os
from src.data.generate_data_optimal_pairs import SlurmOptimalPairs

print(os.path.realpath(__file__))
# sbatch = SlurmOptimalPairs(sigma_1=1.0, sigma_2=0.16)
# sbatch.generate_sbatch()