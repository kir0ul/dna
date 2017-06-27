import re

class dna():
    """Instantiate a DNA object"""
    
    def __init__(self):
        self.sequence = ""

        
    def genSequence(self, N):
        """Generate a DNA sequence of length N in the subset [G-A-T-C]"""

        import random
        
        self.sequence = ""
        for i in range(N):
            self.sequence += random.choice(["G", "A", "T", "C"])
        return self.sequence

    
    def querySubSequence(self, subseq):
        """Return True if the string argument `subseq` is contained inside the `sequence` property"""

        # Search for sub-sequence
        p = re.compile(subseq)
        m = p.search(self.sequence)
        if m == None:
            found = False
        else:
            found = True

        return found

    
    def getMostFrequentSubSeq(self, m):
        """Returns the most frequent sub-sequence of length m contained in the `sequence` property"""

        # List of every possible subsequence
        subseqList = []
        
        

        
        # Get the occurence number of each subsequence
        # OccurenceNb = len(p.findall(seqStr))
