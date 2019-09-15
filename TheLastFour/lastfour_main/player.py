import random
class Player:

    run_can_score = [0,1,2,3,4,5,6,"OUT"]

    def __init__(self, name, prob,team="Lengaburu", runs=0, balls=0):
        self.name = name
        self.runs = runs
        self.team = team
        self.balls = balls
        self.prob = prob

    def __str__(self):
        return "{} - {}({}balls)".format(self.name, self.runs, self.balls )

    def rand_score(self):
        """ This Function is to get runs can score and probability of scoring runs
         return some random number or string(out) as result to the calling obj"""
        rand_list = random.choices(self.run_can_score, self.prob, k=1)  # k is noted how many random numbers u need
        return random.choice(rand_list)  # choices return list , choice return single element

    def increase_score(self,runs):
        """function is for increase player ball count and increse score 
        when player scores run"""
        self.balls += 1
        self.runs += runs
        
    def player_out(self):
        self.balls +=1 