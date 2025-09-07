import json as j
import os.path as p
import os
import shutil

def CleanPath(Path : str):
    CharictersToRemove = 'enter compleat file path of TXT file:'
    CleanPath = Path.replace(CharictersToRemove, "").strip('"')
    return CleanPath

def cheakfile(path):
    if p.isfile(path) == True:
        return True
    
def Linecount(file):
    lines = 0
    for line in file:
        lines += 1
    return lines
    
def FormatData(data : list):
    newdata = {"mesurment": data[0],
               "unit": data[1],}
    data.pop(0)
    data.pop(0)
    for workingdata in data:
        key = workingdata[:16]
        info = workingdata[17:]
        newdata.update({key : info})
    return newdata

def Json(Data : dict, filename):
    with open(filename, mode="w", encoding="utf-8") as file:
        output = j.dumps(Data, indent=2)
        file.write(output)
def CleanUp(path : str, filename, ComPath):
    StartPath = os.getcwd()
    src_path = p.join(StartPath, filename)
    shutil.move(src_path, ComPath)
    os.remove(path)

def GetPathName(path : str):
    PathList = path.rsplit('\\', 1)
    firstpath = str(PathList[0])
    SecondPath = str(PathList[1])
    SecondPathTwo = SecondPath.rsplit(".", 1)
    FileType = "\\" + str(SecondPathTwo[0]) + ".json"
    CompletPath = firstpath + FileType
    return CompletPath, SecondPathTwo[0] + '.json', firstpath

if __name__ == '__main__':
    while True:
        TxtFile = input('enter compleat file path of TXT file:')
        path = CleanPath(TxtFile)
        cheak = cheakfile(path)
        if cheak == True:
            break
        else:
            print("not a path")

    with open(path, "rt") as file:
        completeData = [lines.replace('\n', '') for lines in file.readlines()]

    FinalPath, FileName, firstPath = GetPathName(path)
    FormatedData = FormatData(completeData)
    Json(FormatedData, FileName)
    CleanUp(path, FileName, firstPath)
