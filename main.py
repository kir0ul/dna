
class dna():
    """Instantiate a DNA object"""
    
    def __init__(self):
        self.sequence = []
    
    def GenSequence(self, N):
        """Generate a DNA sequence of length N in the subset [G-A-T-C]"""

        import random
        self.sequence = [random.choice(["G", "A", "T", "C"]) for i in range(N)]
        return self.sequence

    def QuerySubSequence(self, subseq):
        """Return True if the string argument `subseq` is contained inside the `sequence` property"""

        import re

        # Convert sequence in string
        seqStr = ""
        for i in self.sequence:
            seqStr += i

        # Search for sub-sequence
        p = re.compile(subseq)
        m = p.search(seqStr)
        if m == None:
            found = False
        else:
            found = True

        return found

    def GetMostFrequentSubSeq(self, m):
        """Returns the most frequent sub-sequence of length m contained in the `sequence` property"""

        

