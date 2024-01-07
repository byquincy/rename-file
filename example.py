import renameFile

PATH_EXPRESSION = "./testSet/*.txt"
def fileNameRule(fileName:str):
    startCusor = None
    endCusor = None
    for cusor in range(len(fileName)):
        if fileName[cusor] == '[':
            startCusor = cusor
        elif fileName[cusor] == ']':
            endCusor = cusor+1
            break
    exceptText = fileName[startCusor:endCusor]

    returnValue = fileName.replace(exceptText, "")

    returnValue = returnValue.strip()
    return returnValue

if __name__ == "__main__":
    mainStage = renameFile.Stage(PATH_EXPRESSION, fileNameRule)
    mainStage.runInteractiveStage()