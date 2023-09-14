# Base class Player
class Player:
    def play(self):
        print("The player is playing cricket.")

# Derived class Batsman
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

# Derived class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

if __name__ == "__main__":
    # Create objects of both Batsman and Bowler classes
    batsman = Batsman()
    bowler = Bowler()
    
    # Call the play() method for each object
    batsman.play()
    bowler.play()
