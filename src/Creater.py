#coding = utf-8
import FileWriter
import random
class Creater:
    def __init__(self,frange,lrange):
        self.frange = frange
        self.lrange = lrange
    def IntPassword(self):
        result = long(random.randint(self.frange,self.lrange))
        return result
    def LetterPassword(self,Head=true,CaLetter=false,Count=2,UserChoice=' '):
        CaLetterList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        SmLetterList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        IntResult = str(random.randint(self.frange,self.lrange))
        if UserChoice != ' ':
            if Head:
                result = f"{UserChoice}{IntResult}"
            else:
                result = f"{IntResult}{Userchoice}"
            return result
        if CaLetter == false:
            SmLetterResultList = []
            for i in range(Count):
                SmLetterResult = random.choice(SmLetter)
                SmLetterResultList.append(SmLetterResult)
            LetterResult = "".join(SmLetterList)
            if Head:
                result = f"{LetterResult}{IntResult}"
            else:
                result = f"{InntResult{LetterResult}"
            return result
        if CaLetter:
            SCLetterCount = int(Count/2)
            SCLetterList = []
            for i in range(SCLetterCount)
                SmLetterResult = random.choice(SmLetter)
                SCLetterResultList.append(SmLetterResult)
            for i in range(SCLetterCount)
                CaLetterResult = random.choice(CaLetter)
                SCLetterResultList.append(CaLetterResult)
            LetterResult = "".join(SCLetterLisst)
            if Head:
                result = f"{LetterResult}{IntResult}"
            else:
                result = f"{InntResult{LetterResult}"
            return result
   def SCharLetterPassword(self,Head=true,Count=1,UserChoice=' '):
       SCharLetterList = [")","`","!","@","#","$","%","^","&","*","_","-","+","=","|","}","]",":",";","<>",".","?","(","{","["]
       IntResult = str(random.randint(self.frange,self.lrange))
       SCharLetterResultList = []
       if UserChoice != ' ':
           if UserChoice not in SCharLetterList:
               result = 0
           else:
               if Head:
                   result = f"{UserChoice}{IntResult}"
               else:
                   result =f"{IntResult}{UserChoice}"
           return result
       for i in range(Count):
           SCharletter = random.choice(SCharLetterList)
           SCharLetterResultList.append(SCharLetter)
       LetterResult = "".join(SCharLetterResultList)
       if Head:
           result = f"{LetterResult}{IntResult}"
       else:
           result = f"{IntResult}{LetterResult}"
       return result