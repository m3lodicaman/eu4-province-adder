
definitionFile = "C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis IV/mod/province_program/map/definition.csv";
defaultFile = "C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis IV/mod/province_program/map/default.map"

newProvName = "";
newProvAdjName  = "";
newProvR = 0;
newProvG = 0;
newProvB = 0;

####### Add to definition.csv

newProvName = input("Name: ");
newProvAdjName = input("Name adjective: ");
newProvR = input("Red: ");
newProvG = input("Green: ");
newProvB = input("Blue: ");


with open(definitionFile) as f:
    for i, l in enumerate(f):
        pass
provinceNum = i + 1;


#print(str(provinceNum) + ";" + str(newProvR) + ";" + str(newProvG) + ";" + str(newProvB) + ";" + newProvName + ";x");
with open(definitionFile,'a') as f:
    f.write("\n" + str(provinceNum) + ";" + str(newProvR) + ";" + str(newProvG) + ";" + str(newProvB) + ";" + newProvName + ";x");

####### Add to default.map

with open(defaultFile, 'r') as f:
    x = f.readlines();

y = len(x[3]);
x[3] = x[3][0:16] + str(provinceNum + 1) + '\n';

#print(x[1]);

with open(defaultFile, 'r+') as f:
    f.writelines(x);
