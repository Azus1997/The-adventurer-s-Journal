class pfpc():

    def __init__(self, *args,**kwargs):
        #arranco TODAS las variables

        #datos personales
        self.name
        self.PCclass
        self.PClvl
        self.alignment
        self.race
        self.xp
        self.deity
        self.player

        #descripcion
        self.gender
        self.age
        self.height
        self.weight
        self.hair
        self.eyes
        self.size

        #Stats
        self.statStr
        self.statDex
        self.statCon
        self.statWis
        self.statInt
        self.statCha
        self.hp
        self.speed
        self.bab

        #con precalculados
        self.ac = {"dexB": self.statDex, "armourB": 0, "sizeB": pcpf.sizeBCalc(self.size), "natArmour": 0, "defB":0, "miscB": 0, "tempB":0}
        self.iniciativeB = {"dexB": self.statDex, "miscB": 0}
        self.passPerc
        self.languages = ["Common"] #Display: lista en cajita que se vean de a tres a la vez con barra de desplazamiemto

        #Skills
        self.skillAcrob
        self.skillAppraise
        self.skillBluff
        self.skillClimb
        self.skillCraft
        self.skillDiplo
        self.skillDDev
        self.skillDisguise
        self.skillEscArt
        self.skillFly
        self.skillHandleAnimal
        self.skillHeal
        self.skillIntimidate
        self.skillKArcana
        self.skillKDungeoneering
        self.skillKEng
        self.skillKGeo
        self.skillKHist
        self.skillKLocal
        self.skillKNat
        self.skillKNob
        self.skillKPlanes
        self.skillKRegion
        self.skillLinguistics
        self.skillPerc
        self.skillPerform
        self.skillProfession
        self.skillRide
        self.skillSenseMot
        self.skillSoA
        self.skillSpellcraft
        self.skillStealth
        self.skillSurvival
        self.skillSwim
        self.skillUseMagDev

        #mas calculados
        self.cmb = {"bab": self.bab, "strB":self.statStr, "sizeB": pcpf.sizeBCalc(self.size)}
        self.cmd = {"bab": self.bab, "strB":self.statStr, "dexB":self.statDex, "sizeB": 0}
        #Fix these:
        self.touchAC = 10 + self.ac["dexB"] + self.ac["sizeB"] + self.ac["natArmour"]
        self.ffAC =  10 + self.ac["armourB"] + self.ac["sizeB"] + self.ac["natArmour"] + self.ac["miscB"] + self.ac["tempB"]
        self.savesFort = {"base": 0, "AM": self.statCon, "magicMod": 0, "miscMod": 0, "tempMod": 0}
        self.savesWill = {"base": 0, "AM": self.statWis, "magicMod": 0, "miscMod": 0, "tempMod": 0}
        self.savesRef = {"base": 0, "AM": self.statDex, "magicMod": 0, "miscMod": 0, "tempMod": 0}

    #funcion que calcula el bonus de AC dependiendo del size del pj
    def sizeBCalc(s):
        if s == "S":
            return 1
        elif s == "M":
            return 0
    
