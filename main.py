
definitionFile = "C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis IV/mod/province_program/map/definition.csv";
defaultFile = "C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis IV/mod/province_program/map/default.map"

newProvName = "";
newProvAdjName  = "";
newProvR = 0;
newProvG = 0;
newProvB = 0;

class province(object):
    def __init__(self, name, adjName, r, g, b, num):
        self.name = name;
        self.adjName = adjName;
        self.r = r;
        self.g = g;
        self.b = b;
        self.num = num;

def findProvinceDetails():
    newProvName = input("Name: ");
    newProvAdjName = input("Name adjective: ");
    newProvR = int(input("Red: "));
    newProvG = int(input("Green: "));
    newProvB = int(input("Blue: "));

def getProvinceNum():
    with open(definitionFile) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def initializeProvince():
    newProv = province(newProvName, newProvAdjName, newProvR, newProvG, newProvB, getProvinceNum());
    with open('definitionFile','a+') as f:
        f.write(str(newProv.num) + ";" + str(newProv.r) + ";" + str(newProv.g) + ";" + str(newProv.b) + ";" + newProv.name + ";x");
    f.close();


findProvinceDetails();
getProvinceNum();
initializeProvince();
