class Seq:

    def __init__(self, strbases = 'NULL'):
        # Initialize the sequence with the value
        # passed as argument when creating the object

        if strbases == 'NULL':
            self.strbases = 'NULL'
            print('NULL Seq created')
            return

        # Check if the input is valid
        if not self.valid_str(strbases):
            self.strbases = "ERROR"
            print("INVALID Seq!")
            return

        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):

        # -- We just return the string with the sequence
        return self.strbases

    @staticmethod
    def valid_str(strbases):
        # -- Valid bases
        valid_bases = ['A', 'C', 'T', 'G']
        for b in strbases:
            if b not in valid_bases:
                return False
        return True

    def len(self):
        if self.strbases in ['NULL', 'ERROR']:
            return 0
        return len(self.strbases)

    def count_base(self, base):
        return self.strbases.count(base)


class Gene(Seq):

    def __init__(self, strbases, name=""):
        # -- Call the Seq initializer Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        # Gene name along with the sequence
        return self.name + "-" + self.strbases
