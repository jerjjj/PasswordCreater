#coding = utf-8
import random
def WriteResult(Path,mode,result=False,File=" "):
    if mode == 0:
        vf = int(random.randint(0,1000))
        FileName = "PasswordResult-"
        PathResult = f"{Path}{FileName}{vf}"
        open(PathResult,"w")
        return PathResult
    elif mode == 1:
        PathResult = f"{Path}{File}"
        with open(PathResult,"a") as outFile:
            if result == False:
                return 0
            else:
                outFile.write(result)
                return 1
        
        