class Seq:

    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

        print("New sequence created!")

    def __str__(self):

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        return len(self.strbases)


class Gene(Seq):

    def __init__(self, strbases, name=""):
        # -- Call the Seq initializer Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        # Gene name along with the sequence
        return self.name + "-" + self.strbases
