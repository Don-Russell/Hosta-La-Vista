'''Instructions
In this exercise we will use classes to simulate the spread of COVID 19 in Calgary

SIR Model - only included as a reference. You do not need to understand the math behind these model. 
The only important point is that our population has 3 states: susceptible, infectious, and recovered

We will create a number of classes for the various obects in our model and visualize some different scenarios

Please write a 250 word (approx.) statement on what (if) you would change your approach, what you learned in the assignment and what you may have struggled with. 
This statement is the only thing that will be marked, but in order to qualify you must also hand in your script.
'''
#set initial variables
#loop: is a person infected y/n

import statistics
import random

class Virus:
    def __init__(self, duration=14, infectionChance=.01, mortalityRate = .001):
        self.duration = duration
        self.infectionChance = infectionChance
        self.mortalityRate = mortalityRate

class Person:
    def __init__(self):
        self.state = 'S'
        self.virus = None
        self.daysTillRecovered = 0
        self.infectionChance = 0

    def _infect(self, virus):
        self.state = 'I'
        self.infectionChance = virus.infectionChance
        self.daysTillRecovered = virus.duration
        self.virus = virus

    def interaction(self, other):
        if not((self.state == 'I') ^ (other.state == 'I')):
            return 0

        if ((self.state == 'R') | (other.state == 'R')):
            return 0

        if (self.state == 'I') & (random.random() <= self.infectionChance):
            other._infect(self.virus)
            return 1

        if (other.state == 'I') & (random.random() <= other.infectionChance):
            self._infect(other.virus)
            return 1
        return 0
            
    def update(self):
        if (self.daysTillRecovered > 0):
            self.daysTillRecovered -= 1

            if (random.random() <self.virus.mortalityRate):
                self.state = 'D'
                self.daysTillRecovered = -1
                return

            if self.daysTillRecovered == 0:
                self.state = 'R'
                self.virus = None
        
        return (death, recovery)

class City:
    # def __init__(self, initial_pop, virus, average_interactions=10, starting_infected=25):
    #     self.day = 0
    #     self.stats = dict()
    #     self.average_interactions= average_interactions
    #     self.dailyInfected, self.dailydeath, self.dailyrecovery = 0,0,0
    #     self.totalInfected, self.totaldeath, self.totalrecovery = starting_infected,0,0
    #     self.people = [Person() for _ in range(initial_pop)]

    #     for person in self.people[:(starting_infected-1)]:
    #         person._infect(virus)
        
    #     random.shuffle(self.people)

    def __init__(self, initial_pop, virus, average_interactions=10, starting_infected=25):
        self.day = 0
        self.stats = dict()
        self.average_interactions = average_interactions//2
        self.dailyInfected, self.dailydeath, self.dailyrecovery = 0, 0, 0
        self.totalInfected, self.totaldeath, self.totalrecovery = starting_infected, 0, 0

        self.people = [
            Person()
            for _ in range(initial_pop)
        ]

        for person in self.people[:(starting_infected)]:
            person._infect(virus)

        random.shuffle(self.people)

    def _simulate_day(self):
        dailyInfected, dailydeath, dailyrecovery = 0,0,0
        for i, person in enumerate(self.people):
            j = i-self.average_interactions
            if j < 0:
                for other in self.people[j:]:
                    self.dailyInfected += person.interaction(other)
                for other in self.people[0:i]:
                    self.dailyInfected += person.interaction(other)
            else:
                for other in self.people[(i-5):i]:
                    self.dailyInfected += person.interaction(other) 
            
            self.dailydeath, self.dailyrecovery = person.update()
            self.totalInfected += self.dailyInfected
            self.totalrecovery += self.dailyrecovery
        

    def _collect_stats(self):
        day_stats = {"pop": len(self.people) - self.totaldeath}

        day_stats['dailydeath'] = self.dailydeath
        day_stats['dailyInfected'] = self.dailyInfected
        day_stats['dailyrecovery'] = self.dailyrecovery
        day_stats['totaldeath'] = self.totaldeath
        day_stats['totalInfected'] = self.totalInfected
        day_stats['totalrecovery'] = self.totalrecovery
        self.stats[self.year] = year_stats

    def compute_days(self,days):
        for _ in range(days):
            self._simulate_day()
            self._collect_stats()
            self.days += 1
        return self.stats

        print (self.day)

def main():
    A = Person()
    B = Person()

    covid = Virus(duration=1, infectionChance=.1, mortalityRate = .001)

    A._infect(covid)

    B.interaction(A)

    B

    calgary = City(100,covid,10,25)
    print(calgary)
    stats = calgary.compute_days(30)


if __name__ == "__main__":
    main()
