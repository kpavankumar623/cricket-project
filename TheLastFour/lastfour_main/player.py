import random


class Player:
    run_can_score = [0,1,2,3,4,5,6,"OUT"]

    def __init__(self, name, prob, runs=0, balls=0):
        self.name = name
        self.runs = runs
        self.balls = balls
        self.prob = prob

    def __str__(self):
        return "{} - {}({}balls)".format(self.name, self.runs, self.balls )

    def rand_score(self):
        """ This Function is to get runs can score and probability of scoring runs
         return some random number or string(out) as result to the calling obj"""
        rand_list = random.choices(self.run_can_score, self.prob, k=1)  # k is noted how many random numbers u need
        return random.choice(rand_list)  # choices return list , choice return single element

    def increase_ball(self):
        """function is for increase striker ball count by one"""
        self.balls += 1

    def increase_runs(self, runs):
        """function increase the batesmen runs by runs_scored"""
        self.runs += runs

