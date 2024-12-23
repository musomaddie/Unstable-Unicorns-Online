from abc import ABC, abstractmethod

""" All the methods each runner will need to implement. 

Runners are different from 'deciders' in that a decider makes a decision for a particular occasion, while the runner 
controls the entire game. They use the same type enum if needed though."""


class Runner(ABC):

    @abstractmethod
    def setup(self):
        pass

    def run(self):
        self.setup()
        # TODO -> actually get the game variable!
