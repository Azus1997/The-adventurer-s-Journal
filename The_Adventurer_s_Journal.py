from tkinter.constants import END, EXTENDED, NONE
import pandas as pd
import numpy as np
import matplotlib as plt
import tkinter as tk
from tkinter import messagebox
import selenium.webdriver as sl
import openpyxl as xl
import PyPDF2 as pdf
import shutil
import os
from pathlib import Path

#CONSTANTS:

pyPath = os.path.realpath(__file__)
pyPathLen = len(pyPath)
pyNameLen = len(Path(__file__).name)
basePathPf = pyPath[:pyPathLen - pyNameLen] + "PCs\\PF\\"



#Para hacer:
#    -Crear funcion de creacion de Pjs
#    -crear almacenamiento de pjs
#    -crear algoritmo de razas/clases
#    -crear botones/gui para todo lo anterior
#    -crear barras de desplazamiento
#    -DOCUMENTAR

class pc5e():

    def __init__(self, *args,**kwargs):
        #arranco TODAS las variables
        name = ""
        PCclass = ""
        race = ""
        player = ""
        deity = ""
        backg = ""
        xp = 0
        statStr = 0
        statDex = 0
        statCon = 0
        statWis = 0
        statInt = 0
        statCha = 0
        inspiration = 0
        hp = 0
        ac = 0
        iniciativeB = 0
        speed = 0
        passPerc = 0
        languages = []



class pcpf():

    def __init__(self, details, *args,**kwargs):
        #arranco TODAS las variables

        #datos personales
        self.name = details["name"]
        self.PCclass = details["class"]
        self.PClvl = int(details["level"])
        self.alignment = details["alignment"]
        self.race = details["race"]
        self.xp = int(details["xp"])
        self.deity = details["deity"]
        self.player = details["player"]

        #descripcion
        self.gender = details["gender"]
        self.age = int(details["age"])
        self.height = details["height"]
        self.weight = details["weight"]
        self.hair = details["hair"]
        self.eyes = details["eyes"]
        self.size = details["size"]

        #Stats
        self.statStr = int(details["str"])
        self.statDex = int(details["dex"])
        self.statCon = int(details["con"])
        self.statWis = int(details["wis"])
        self.statInt = int(details["int"])
        self.statCha = int(details["cha"])
        self.hp = int(details["hp"])
        self.speed = int(details["speed"])
        self.bab = int(details["bab"])

        #con precalculados
        self.ac = {"dexB": self.statDex, "armourB": 0, "sizeB": pcpf.sizeBCalc(self.size), "natArmour": 0, "defB":0, "miscB": 0, "tempB":0}
        self.iniciativeB = {"dexB": self.statDex, "miscB": 0}
        self.passPerc = 0
        self.languages = ["Common"] #Display: lista en cajita que se vean de a tres a la vez con barra de desplazamiemto

        #Skills
        self.skillAcrob = {"AM": self.statDex, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillAppraise = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillBluff = {"AM": self.statCha, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillClimb = {"AM": self.statStr, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillCraft = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillDiplo = {"AM": self.statCha, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillDDiv = {"AM": self.statDex, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": False, "APC": False}
        self.skillDisguise = {"AM": self.statCha, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillEscArt = {"AM": self.statDex, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillFly = {"AM": self.statDex, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillHandleAnimal = {"AM": self.statCha, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": False, "APC": False}
        self.skillHeal = {"AM": self.statWis, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillIntimidate = {"AM": self.statCha, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillKArcana = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": False, "APC": False}
        self.skillKDungeoneering = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": False, "APC": False}
        self.skillKEng = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": False, "APC": False}
        self.skillKGeo = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": False, "APC": False}
        self.skillKHist = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": False, "APC": False}
        self.skillKLocal = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": False, "APC": False}
        self.skillKNat = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": False, "APC": False}
        self.skillKNob = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": False, "APC": False}
        self.skillKPlanes = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": False, "APC": False}
        self.skillKRegion = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": False, "APC": False}
        self.skillLinguistics = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": False, "APC": False}
        self.skillPerc = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillPerform = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillProfession = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillRide = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillSenseMot = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillSoA = {"AM": self.statDex, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": False, "APC": False}
        self.skillSpellcraft = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": False, "APC": False}
        self.skillStealth = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillSurvival = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillSwim = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}
        self.skillUseMagDev = {"AM": self.statInt, "lvl": 0, "bonus": 0, "classSkill": False, "Untrained": True, "APC": False}

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




###              ##############################
###              ##################################
###CREACION DE PJ#######################################
###              ##################################
###              ##############################

#muestra la ventana de creacion de PJ y lanza la creacion del file
def createPFPC():
    root = tk.Tk()
    root.geometry("400x800")
    root.title("Pathfinder Character Creation")
    #datos personales
    tk.Label(root, text="Name:").grid(row=0)
    tk.Label(root, text="Class:").grid(row=1)
    tk.Label(root, text="Level:").grid(row=2)
    tk.Label(root, text="Alignment:").grid(row=3)
    tk.Label(root, text="Race:").grid(row=4)
    tk.Label(root, text="Experience:").grid(row=5)
    tk.Label(root, text="Deity:").grid(row=6)
    tk.Label(root, text="Player:").grid(row=7)
    #Descripcion
    tk.Label(root, text="Gender:").grid(row=8)
    tk.Label(root, text="Age:").grid(row=9)
    tk.Label(root, text="Height:").grid(row=10)
    tk.Label(root, text="Weight:").grid(row=11)
    tk.Label(root, text="Hair:").grid(row=12)
    tk.Label(root, text="Eyes:").grid(row=13)
    tk.Label(root, text="Size:").grid(row=14)
    #Stats
    tk.Label(root, text="Strength:").grid(row=15)
    tk.Label(root, text="Dexterity:").grid(row=16)
    tk.Label(root, text="Constitution:").grid(row=17)
    tk.Label(root, text="Wisdom:").grid(row=18)
    tk.Label(root, text="Intelligence:").grid(row=19)
    tk.Label(root, text="Charisma:").grid(row=20)
    tk.Label(root, text="Hit Points:").grid(row=21)
    tk.Label(root, text="Speed:").grid(row=22)
    tk.Label(root, text="BAB:").grid(row=23)

    #usamos atributos de funcion pq necesitamos llamar estas en otra funcion
    #datos personales entry
    createPFPC.name_entry= tk.Entry(root)
    createPFPC.pcclass_entry = tk.Entry(root)
    createPFPC.lvl_entry = tk.Entry(root)
    createPFPC.alignment_entry = tk.Entry(root)
    createPFPC.race_entry = tk.Entry(root)
    createPFPC.xp_entry = tk.Entry(root)
    createPFPC.deity_entry = tk.Entry(root)
    createPFPC.player_entry = tk.Entry(root)
    #Descripcion entry
    createPFPC.gender_entry = tk.Entry(root)
    createPFPC.age_entry = tk.Entry(root)
    createPFPC.height_entry = tk.Entry(root)
    createPFPC.weight_entry = tk.Entry(root)
    createPFPC.hair_entry = tk.Entry(root)
    createPFPC.eyes_entry = tk.Entry(root)
    createPFPC.size_entry = tk.Entry(root)
    #Stats entry
    createPFPC.statstr_entry = tk.Entry(root)
    createPFPC.statdex_entry = tk.Entry(root)
    createPFPC.statcon_entry = tk.Entry(root)
    createPFPC.statwis_entry = tk.Entry(root)
    createPFPC.statint_entry = tk.Entry(root)
    createPFPC.statcha_entry = tk.Entry(root)
    createPFPC.hp_entry = tk.Entry(root)
    createPFPC.speed_entry = tk.Entry(root)
    createPFPC.bab_entry = tk.Entry(root)


    #datos personales entry grid
    createPFPC.name_entry.grid(row=0, column=1)
    createPFPC.pcclass_entry.grid(row=1, column=1)
    createPFPC.lvl_entry.grid(row=2, column=1)
    createPFPC.alignment_entry.grid(row=3, column=1)
    createPFPC.race_entry.grid(row=4, column=1)
    createPFPC.xp_entry.grid(row=5, column=1)
    createPFPC.deity_entry.grid(row=6, column=1)
    createPFPC.player_entry.grid(row=7, column=1)
    #Descripcion entry grid
    createPFPC.gender_entry.grid(row=8, column=1)
    createPFPC.age_entry.grid(row=9, column=1)
    createPFPC.height_entry.grid(row=10, column=1)
    createPFPC.weight_entry.grid(row=11, column=1)
    createPFPC.hair_entry.grid(row=12, column=1)
    createPFPC.eyes_entry.grid(row=13, column=1)
    createPFPC.size_entry.grid(row=14, column=1)
    #Stats entry grid
    createPFPC.statstr_entry.grid(row=15, column=1)
    createPFPC.statdex_entry.grid(row=16, column=1)
    createPFPC.statcon_entry.grid(row=17, column=1)
    createPFPC.statwis_entry.grid(row=18, column=1)
    createPFPC.statint_entry.grid(row=19, column=1)
    createPFPC.statcha_entry.grid(row=20, column=1)
    createPFPC.hp_entry.grid(row=21, column=1)
    createPFPC.speed_entry.grid(row=22, column=1)
    createPFPC.bab_entry.grid(row=23, column=1)

    
    cancelB = tk.Button(root, command = root.destroy, text = "Cancel").grid(row=30, column =1)
    createB = tk.Button(root, command = lambda: saveNewPCPF(), text = "Create").grid(row=30, column =0)

    root.mainloop()

#crea un file y guarda los datos del pj 
def saveNewPCPF():

    # #guardamos todo en un diccio que dsps pasamos como argu en pfpc
    details = {"name": createPFPC.name_entry.get(),"class":createPFPC.pcclass_entry.get(),"level":createPFPC.lvl_entry.get(),"alignment":createPFPC.alignment_entry.get(),"race":createPFPC.race_entry.get(),"xp": createPFPC.xp_entry.get(),"deity":createPFPC.deity_entry.get(),"player":createPFPC.player_entry.get(),"gender":createPFPC.gender_entry.get(),\
         "age":createPFPC.age_entry.get(), "height": createPFPC.height_entry.get(), "weight":createPFPC.weight_entry.get(),"hair": createPFPC.hair_entry.get(),"eyes": createPFPC.eyes_entry.get(),"size":createPFPC.size_entry.get(), "str":createPFPC.statstr_entry.get(), "dex":createPFPC.statdex_entry.get(), "con": createPFPC.statcon_entry.get(),\
         "wis":createPFPC.statwis_entry.get(), "int": createPFPC.statint_entry.get(), "cha":createPFPC.statcha_entry.get(),"hp":createPFPC.hp_entry.get(),"speed":createPFPC.speed_entry.get(),"bab":createPFPC.bab_entry.get()}
    
    #Chequeamos de tener todos los valores introducidos
    keys = []
    for key in details:
        keys.append(details[key])


    #Si no tiene espacios en blanco
    if  keys.count("") == 0 and keys.count(None) == 0:

        #Lanzo la clase
        nc = pcpf(details)

        #creo el path del .txt
        fullPath = basePathPf + str(nc.name) + ".txt"

        #chequeo que no haya nombres repetidos asi no se sobreescribe ningun PJ
        nameChunk = fullPath[len(basePathPf): len(fullPath)]
        n = 0

        #----------------------------------------------------------------------------------------------------------

        for root, dir, files in os.walk(basePathPf):


            while nameChunk in files:
                n = n + 1
                fullPath = str(basePathPf) + str(nc.name) + " (" + str(n) + ")" + ".txt"
                nameChunk = fullPath[len(basePathPf): len(fullPath)]
            

        savefile = open(fullPath,"w+")
        savefile.seek(0)

        for var in vars(nc):
            savefile.write(str(var) + ": " + str(vars(nc)[var]) + " \n")
        
        messagebox.showinfo("Character Creation", "The GLORIOUS " + nc.name + " has been saved!")



    else:
        #Muestra un msj de error y vacia las variables

        messagebox.showerror("Error","You must complete all the camps before continuing")


    # vaciamos el diccio asi se puede repetir el proceso si asi se desea

    details = {"name": None,"class":None,"level":None,"alignment":None,"race":None,"xp": None,"deity":None,"player":None,"gender":None,\
         "age":None, "height": None, "weight":None,"hair": None,"eyes": None,"size":None, "str":None, "dex":None, "con": None,\
         "wis":None, "int": None, "cha":None,"hp":None,"speed":None,"bab":None}
         
    #datos personales entry.delete
    createPFPC.name_entry.delete(0, "end")
    createPFPC.pcclass_entry.delete(0, "end")
    createPFPC.lvl_entry.delete(0, "end")
    createPFPC.alignment_entry.delete(0, "end")
    createPFPC.race_entry.delete(0, "end")
    createPFPC.xp_entry.delete(0, "end")
    createPFPC.deity_entry.delete(0, "end")
    createPFPC.player_entry.delete(0, "end")
    #Descripcion entry.delete
    createPFPC.gender_entry.delete(0, "end")
    createPFPC.age_entry.delete(0, "end")
    createPFPC.height_entry.delete(0, "end")
    createPFPC.weight_entry.delete(0, "end")
    createPFPC.hair_entry.delete(0, "end")
    createPFPC.eyes_entry.delete(0, "end")
    createPFPC.size_entry.delete(0, "end")
    #Stats entry.delete
    createPFPC.statstr_entry.delete(0, "end")
    createPFPC.statdex_entry.delete(0, "end")
    createPFPC.statcon_entry.delete(0, "end")
    createPFPC.statwis_entry.delete(0, "end")
    createPFPC.statint_entry.delete(0, "end")
    createPFPC.statcha_entry.delete(0, "end")
    createPFPC.hp_entry.delete(0, "end")
    createPFPC.speed_entry.delete(0, "end")
    createPFPC.bab_entry.delete(0, "end")

    
def loadPFPC():
    root = tk.Tk()
    root.geometry("400x800")
    root.title("Pathfinder Characters")

    loadPFPC.chaList = tk.Listbox(root, highlightcolor= "BLUE", selectmode= EXTENDED, xscrollcommand= True, yscrollcommand= True)
    
    for file in os.listdir(basePathPf):
        loadPFPC.chaList.insert(END, file[:len(file)-4])

    loadPFPC.chaList.grid(row=0, column =0)
    loadB = tk.Button(root, command = lambda: pfChaSheet(loadPFPC.chaList.curselection()), text = "Load").grid(row=1, column =1)




def pfChaSheet(sel):

    # allFileNames = []    # for name in sel:
    #     allFileNames.append(name)

    for fobj in sel:
        fname = loadPFPC.chaList.get(fobj)
        chaFile = open(basePathPf + str(fname) + ".txt","r+")
        dets = {}
        for line in chaFile:
            key, value = line.split(sep=":", maxsplit=1)
            dets[key] = value
        print(dets)
        # root = tk.Tk()
        # root.geometry("400x800")
        # root.title(n)






        

    #aca va a venir un for loop que por cada f, abre una ventanita de tk mostrando los datos que ya tiene

#creamos una clase de inicializacion de tk y preparacion de las frames
class TAJ(tk.Tk):
    def __init__(self,*args,**kwargs):
        #inicializamos tk
        tk.Tk.__init__(self,*args,**kwargs)


        #armamos el marco de uso gral
        #tengo que tratar de no esperar lo inevitable mas
        #te vas, te vaas
        marco = tk.Frame(self)
        marco.pack()

        marco.grid_rowconfigure(0, weight=1)
        marco.grid_columnconfigure(0, weight=1)
        
        
        #creamos un diccionario donde se van a guardar las frames para dsps poder iterar a travez de ellas y traer una al frente
        self.frames = {}

        for Fr in (mainMenu, fifthEMainMenu,pfMainMenu):

            frame = Fr(marco, self)

            self.frames[Fr] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(mainMenu)

        #creamos la funcion que va a traer al frente la frame que le pasemos como "controller"
    def show_frame(self, controller):

        frame = self.frames[controller]
        frame.tkraise()

#Frame de menu principal
class mainMenu(tk.Frame):
    #Creamos funciones que llevan a las paginas de cada juego
    #CHEQUEAR LO DEL PATH
     def webpf():
         sl.Firefox().get("https://www.d20pfsrd.com/")
     def webFiveE():
         sl.Firefox().get("https://www.5esrd.com/")

     def __init__(self, parent, controller):
         tk.Frame.__init__(self,parent)
         
         title = tk.Label(self, text = "TAJ")
         game5e = tk.Button(self, command=lambda: controller.show_frame(fifthEMainMenu), text = "DnD 5e")
         gamepf = tk.Button(self, command=lambda: controller.show_frame(pfMainMenu), text = "Pathfinder")
         web5e = tk.Button(self, command = mainMenu.webFiveE, text = "5eSRD", fg = "Blue")
         webpf = tk.Button(self, command = mainMenu.webpf, text = "PFSRD", fg = "Blue")
         quitButton = tk.Button(self, text = "Quit", command = controller.destroy, fg = "Red")
         #sueño con soñarte nunca mas
         #no repetirte mas
         #jamas, jamaaaas
         title.pack()
         game5e.pack()
         gamepf.pack()
         web5e.pack()
         webpf.pack()
         quitButton.pack()

#Frame de menu de Pathfinder
class pfMainMenu(tk.Frame):

     def __init__(self, parent, controller):
         tk.Frame.__init__(self, parent)
         
         title = tk.Label(self, text = "Pathfinder")
         webpf = tk.Button(self, command = mainMenu.webpf, text = "PFSRD", fg = "Blue")
         home = tk.Button(self, command=lambda: controller.show_frame(mainMenu), text = "Back")
         createPC = tk.Button(self, command=lambda: createPFPC(), text = "Create new PC")
         loadPC =  tk.Button(self, command=lambda: loadPFPC(), text = "Load PC")

         title.pack()
         createPC.pack()
         loadPC.pack()
         webpf.pack()
         home.pack()
         
#Frame de menu de 5e
class fifthEMainMenu(tk.Frame):

     def __init__(self, parent, controller):
         tk.Frame.__init__(self,parent)
         
         title = tk.Label(self, text = "DnD 5e")
         web5e = tk.Button(self, command = mainMenu.webFiveE, text = "5eSRD", fg = "Blue")
         home = tk.Button(self, command=lambda: controller.show_frame(mainMenu), text = "Go Back")


         title.pack()
         web5e.pack()
         home.pack()



#cree y almacene pj modificables

#de acceso directo a la data de la clase y la raza del pj

#de acceso directo a srd

app = TAJ()
app.geometry("1200x800")
app.mainloop()