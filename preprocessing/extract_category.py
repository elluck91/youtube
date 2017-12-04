import re
import sys
from nltk.stem.porter import *

def main(input_file, output_file='output.txt'):
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'w')
    count = 1
    for line in in_f:
        #print count
        line = line.split(", ")
        category = line[3]
        if not category.isdigit() or int(category) > 45:
            
            for i in range(len(line)):
                if line[i].isdigit() and int(line[i]) < 45:
                    print "Line: ", count
                    print line[i]
                    
                    category = line[i]
                    break
        out_f.write(category + "\n")
        count += 1
    in_f.close()
    out_f.close()
    
if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
