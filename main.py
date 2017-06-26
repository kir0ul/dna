
class dna():

    def __init__(self):
        self.sequence = []
    
    def GenSequence(self, N):
        """Generate a DNA sequence of length N """

        import random
        self.sequence = [random.choice(["G", "A", "T", "C"]) for i in range(N)]
        return self.sequence

    def QuerySubSequence(self, substr):
        """Return True if `substr` is contained inside `seq`"""

        import re

        # Convert sequence in string
        seqStr = ""
        for i in self.sequence:
            seqStr += i

        # Search for substring
        p = re.compile(substr)
        m = p.search(seqStr)
        if m == None:
            found = False
        else:
            found = True

        return found

