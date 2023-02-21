# Import the functions and packages that are used
from dwave.system import EmbeddingComposite, DWaveSampler

# Define the problem as two Python dictionaries:
#   h for linear terms, J for quadratic terms
h = {'A':-1.0, 'B':-1.0, 'C':-1.0, 'D':-1.0}
J = {('A','B'): 0.5,
    ('B','D'): 0.5, 
    ('A','C'): 0.5,
    ('B','D'): 0.5,
    ('B','C'): 0.25,
    ('A','D'): 0.25}

# Define the sampler that will be used to run the problem
sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
sampleset = sampler.sample_ising(h, J,
                                 num_reads = 10,
                                 label='Example - Simple Ocean Programs: Ising')
print(sampleset)