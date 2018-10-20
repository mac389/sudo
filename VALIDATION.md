# Validation of MLN models

Each Markov logic network consists of two parts, a first-order logic template and a weighted ensemble of Markov networks. 

**First-order logic template** The first-order logic template contains weighted first-order logic statements. The weights represent the log odds of the statement being true, which is the same thing as the log fraction of the Markov networks in which the statement is true. We write our formulas using material implication and we do not simplify negations in formulas. _PyMLN_ converts all first-order logic statements into conjunctive normal form. We leave this conversion to _PyMLN_ so that the logic files are more interpretable to the clinician.   

**Weighted ensemble of Markov networks** The template of first-order logic statements directs the creation of an ensemble of Markov networks. Each Markov network in this ensemble represents a world in which as many statements from the template are true as the odds associated with each statement indicates. 

## Validation 
We validate our MLN models on two levels, at the level of each study and at the amalgamation level. 

**Validation at study level** We abstract from each study a weighted first-order logic template. We generate synthetic data that are manually curated to develop the weights for the ensemble of Markov networks.

**Integration of studies**

**Validation at amalgamation level** 
