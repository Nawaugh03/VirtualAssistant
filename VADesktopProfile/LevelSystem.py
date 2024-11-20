class LevelSystem:
    def __init__(self):
        self.baseXP=100
        self.CurrentLevel=1
        self.GrowthFactor=1.2
        self.currentxp=0
        self.QuizScore:float=[1.0]*5 #(1-10)
        self.difficulty=0
        self.NextXPRequirement=self.NextLevelFormula()

    def Levelup(self):
        self.CurrentLevel+=1

    def reset(self):
        self.CurrentLevel=1
        self.currentxp=0
        self.QuizScore=[1.0]*5
        self.NextXPRequirement=self.NextLevelFormula()
        
    def NextLevelFormula(self):
        #self.QuizScore[0:4]=[1,1,1,1,1]
        self.difficulty=self.diffChanges()
        return round(self.baseXP * (self.GrowthFactor**(self.CurrentLevel-1))* self.difficulty)
    
    def XPGained(self, taskScore):
        XPGained = self.baseXP * taskScore
        self.currentxp+=XPGained
        #print(XPGained)
        while (self.currentxp>=self.NextXPRequirement):
            self.Levelup()
            self.currentxp -= self.NextXPRequirement
            self.NextXPRequirement=self.NextLevelFormula()
        
    def diffChanges(self):
        return (self.QuizScore[0]*0.25 + self.QuizScore[1]*0.3 + self.QuizScore[2]*0.28 + self.QuizScore[3]*0.1 + self.QuizScore[4]*0.17)

if __name__ == '__main__':
    a=LevelSystem()
    print(a.CurrentLevel)

    