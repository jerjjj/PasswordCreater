# coding = utf-8
import random


class Creater:
    def __init__(self, frange, lrange):
        self.frange = frange
        self.lrange = lrange
        self.SCharLetterList = [")", "`", "!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "+", "=", "|", "}", "]",
                                ":", ";", "<>", ".", "?", "(", "{", "["]
        self.SCharLetterStr = "()`!@#$%^&*_-+=|{}[]:;'<>,.?"
        self.CaLetterList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                             "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.SmLetterList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                             "s", "t", "u", "v", "w", "x", "y", "z"]

    def IntPassword(self):
        result = str(random.randint(self.frange, self.lrange))
        return result

    def LetterPassword(self, Head=True, CaLetter=False, Count=2, UserChoice=' '):
        IntResult = str(random.randint(self.frange, self.lrange))
        if UserChoice != ' ':
            if UserChoice.isalpha() == False:
                return 0
            if not Head:
                result = f"{IntResult}{UserChoice}"
            elif Head == False:
                result = f"{UserChoice}{IntResult}"
            return result
        if CaLetter == False:
            SmLetterResultList = []
            for i in range(Count):
                SmLetterResult = random.choice(self.SmLetterList)
                SmLetterResultList.append(SmLetterResult)
            LetterResult = "".join(SmLetterResultList)
            if Head:
                result = f"{LetterResult}{IntResult}"
            elif Head == False:
                result = f"{IntResult}{LetterResult}"
            return result
        if CaLetter:
            SCLetterCount = int(Count / 2)
            SCLetterResultList = []
            for i in range(SCLetterCount):
                SmLetterResult = random.choice(self.SmLetterList)
                SCLetterResultList.append(SmLetterResult)
            for i in range(SCLetterCount):
                CaLetterResult = random.choice(self.CaLetterList)
                SCLetterResultList.append(CaLetterResult)
            LetterResult = "".join(SCLetterResultList)
            if Head:
                result = f"{LetterResult}{IntResult}"
            elif Head == False:
                result = f"{IntResult}{LetterResult}"
            return result

    def SCharLetterPassword(self, Head=True, Count=1, UserChoice=' '):
        IntResult = str(random.randint(self.frange, self.lrange))
        SCharLetterResultList = []
        if UserChoice != ' ':
            if UserChoice not in self.SCharLetterStr:
                result = 0
            else:
                if Head:
                    result = f"{UserChoice}{IntResult}"
                elif Head == False:
                    result = f"{IntResult}{UserChoice}"
            return result
        for i in range(Count):
            SCharLetter = random.choice(self.SCharLetterList)
            SCharLetterResultList.append(SCharLetter)
        LetterResult = "".join(SCharLetterResultList)
        if Head:
            result = f"{LetterResult}{IntResult}"
        elif Head == False:
            result = f"{IntResult}{LetterResult}"
        return result

    def ALetterPassword(self, LHead=True, SHead=False, LCount=2, SCount=1, LUserChoice=' ', SUserChoice=' ',CaLetter=False):
        IntResult = str(random.randint(self.frange, self.lrange))
        if LUserChoice != ' ':
            if LUserChoice.isalpha() == False:
                return 0
            elif LHead:
                TempResult = f"{LUserChoice}{IntResult}"
            elif LHead == False:
                TempResult = f"{IntResult}{LUserChoice}"
        elif LUserChoice == ' ':
            TempResult = f"{IntResult}"
        if SUserChoice != ' ':
            if SUserChoice not in self.SCharLetterStr:
                return 0
            elif SHead:
                result = f"{SUserChoice}{IntResult}"
                return result
            elif SHead == False:
                result = f"{IntResult}{SUserChoice}"
                return result
        if CaLetter == False:
            SmLetterResultList = []
            for i in range(LCount):
                SmLetterResult = random.choice(self.SmLetterList)
                SmLetterResultList.append(SmLetterResult)
            LetterResult = "".join(SmLetterResultList)
            if LHead:
                TempResult = f"{LetterResult}{IntResult}"
            elif LHead == False:
                TempResult = f"{IntResult}{LetterResult}"
        if CaLetter:
            SCLetterCount = int(LCount / 2)
            SCLetterResultList = []
            for i in range(SCLetterCount):
                SmLetterResult = random.choice(self.SmLetterList)
                SCLetterResultList.append(SmLetterResult)
            for i in range(SCLetterCount):
                CaLetterResult = random.choice(self.CaLetterList)
                SCLetterResultList.append(CaLetterResult)
            LetterResult = "".join(SCLetterResultList)
            if LHead:
                TempResult = f"{LetterResult}{IntResult}"
            elif LHead == False:
                TempResult = f"{IntResult}{LetterResult}"
        SCharLetterResultList = []
        for i in range(SCount):
            SCharLetter = random.choice(self.SCharLetterList)
            SCharLetterResultList.append(SCharLetter)
        LetterResult = "".join(SCharLetterResultList)
        if SHead:
            result = f"{LetterResult}{TempResult}"
        elif SHead == False:
            result = f"{TempResult}{LetterResult}"
        return result
