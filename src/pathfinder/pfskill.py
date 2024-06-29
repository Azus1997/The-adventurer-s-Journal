class pfskill():

    def __init__(self, *args,**kwargs):
        self.abilityModifier = kwargs.get(abilityModifier)
        self.rank = kwargs.get(rank)
        self.bonus = kwargs.get(bonus)
        self.isClassSkill = kwargs.get(isClassSkill)
        self.isTrainedOnly = kwargs.get(isTrainedOnly)
        self.APC = kwargs.get(APC)
    

    def totalScore():

        untrainedValidation()

        if self.isClassSkill:
             classSkillB = 3 
        else: 
            classSkillB = 0
        
        return classSkillB + self.abilityModifier + self.rank + self.bonus



    def untrainedValidation():
        if self.isTrainedOnly and self.rank == 0:
            raise ValueError('This skill is Trained Only.')