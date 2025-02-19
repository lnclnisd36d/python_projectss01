# Parent classes
class Dad:
    def __init__(self, color, dadhobby):
        self.color = color
        self.dadhobby = dadhobby

class Mom:
    def __init__(self, color, mumhobby):
        self.color = color
        self.mumcolor = mumhobby

# child class,sub class
class Boy(Dad):
    def boyinherits(self):
        print(f"Boy inherits {self.color} and the hobby of {self.dadhobby}")

class Girl(Mom):
    def girlinherits(self):
        print(f"Girl inherits {self.color} and the hobby of {self.mumcolor}")

# Instances
my_boy = Boy(color="African descent", dadhobby="Watching football")
my_boy.boyinherits()

my_girl = Girl(color="American descent", mumhobby="Washing utensils")
my_girl.girlinherits()