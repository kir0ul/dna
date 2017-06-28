
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

        import re
        
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

        import re
        import numpy as np
        
        # Create a set of every possible unique subsequence
        subseq = set()
        i = 0
        while i <= len(self.sequence) - m:
            subseq.add(self.sequence[i:i+m])
            i += 1
        subseq = list(subseq)
        
        # Get the occurrence number of each subsequence
        OccurrenceNb = []
        for i in subseq:
            p = re.compile(i)
            OccurrenceNb.append(len(p.findall(self.sequence)))
        
        # Most frequent sub-sequences
        OccurrenceNb = np.array(OccurrenceNb)
        subseq = np.array(subseq)
        result = list(subseq[OccurrenceNb == OccurrenceNb.max()])

        return result
