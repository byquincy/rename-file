import os
import glob
from tqdm import tqdm

class Stage:
    def __init__(self, pathExpression:str, renameRule) -> None:
        self.renameRule = renameRule
        self.path = '/'.join(
            pathExpression.split("/")[:-1]
        ) + '/'
        self.fileList = glob.glob(pathExpression)

        for i in range(len(self.fileList)):
            self.fileList[i] = self.fileList[i].split("/")[-1]
        
    
    def runInteractiveStage(self):
        self.preview()
        if "execute" == input("Do you want to excute? [execute] "):
            self.execute()
        else:
            print("Rename cancled")

    def preview(self):
        printCache = "===Rename Preview===\n"

        for name in self.fileList:
            printCache += (self.renameRule(name) + "\n")
        
        print( printCache )
        
    def execute(self):
        os.chdir(self.path)
        for name in tqdm(self.fileList):
            os.rename(name, self.renameRule(name))



# def testRule(fileName:str):
#     returnValue = fileName.replace("Test", "").strip()
#     return returnValue
# if __name__ == "__main__":
#     test = Stage("./testSet/*.txt", testRule)