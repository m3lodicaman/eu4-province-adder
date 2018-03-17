
import random;

defintionFile = "C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis IV/mod/province_program/map/definition.csv";
defaultFile = "C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis IV/mod/province_program/map/default.map"

newProvName;
newProvAdjName;
newProvR;
newProvG;
newProvB;

class province(object):
    def __init__(self, name, adjName, r, g, b, num):
        self.name = name;
        self.adjName = adjName;
        self.r = r;
        self.g = g;
        self.b = b;
        self.num = num;

def findProvinceDetails(name, adjName, r, g, b):
    newProvName = name;
    newProvAdjName = adjName;
    newProvR = r;
    newProvG = g;
    newProvB = b;

def getProvinceNum():
    with open(definitionFile) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


with open(outputFile, 'r') as f:
    x = f.readlines();

y = len(x[1]);
x[1] = x[1][0:(y-1)]

with open(outputFile, 'r+') as f:
    f.writelines(x);
