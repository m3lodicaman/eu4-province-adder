outputFile = "C:/Users/Kai/Documents/Output/writeTo.txt";

##with open(outputFile, 'r+') as f:
##   f.write('This is a test\n');

with open(outputFile, 'r') as f:
    x = f.readlines();

word = input("Enter a word: \n");

y = len(x[1]);
x[1] = x[1][0:(y-1)] + " " + word + '\n';

with open(outputFile, 'r+') as f:
    f.writelines(x);
