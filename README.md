# README

## Requirements

The app should have the following capabilities:

1) An API endpoint that given a number N, generates an DNA sequence of length N (DNA sequence consists of base pairs in the subset [G-A-T-C])
2) An API endpoint that given a potential sub-sequence tells if it is contained in the generated sequence
3) An API endpoint that given a number m returns the most frequent sub-sequence of length m contained in the generated sequence

## How-to

Open a python terminal and call the API with the ```import dna``` statement.

To instantiate a new DNA object, type ```myDna = dna.dna()```

1) Type ```myDna.genSequence(N)``` with ```N``` an integer. The generated sequence is saved in the ```myDna.sequence``` property.
2) Type ```myDna.querySubSequence("GATC")```
3) Type ```myDna.getMostFrequentSubSeq(m)``` with ```m``` an integer
