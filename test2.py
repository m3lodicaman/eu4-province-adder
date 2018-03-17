
definitionFile = "C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis IV/mod/province_program/map/definition.csv";

#with open(definitionFile, 'r') as f:
#    x = f.readline();

def fileLen(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


numberOfProvince = 0;

#print(x);
#y = len(x);

#for a in range(y):
#    if x[a] == ';':
#        numberOfProvince = int(x[0:a]);
 #       break;

numberOfProvince = fileLen(definitionFile);

print(numberOfProvince);
