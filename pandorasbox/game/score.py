class Score:
    def __init__(self) -> None:
        '''The Class constructor
        
        Stereotype:
            Information Holder'''
        self.score = 0

    def get_score(self):
        return self.score

    def add_score(self):
        '''Adding 10 points to every enemy destroyed'''
        self.score += 10