import re
import sys
from nltk.stem.porter import *

def main(input_file, output_file='output.txt'):
    in_f = open(input_file, 'r')
    out_f = open(output_file, 'w')
    ps = PorterStemmer()
    regex = re.compile('[^a-zA-Z]')
    count = 1
    for line in in_f:
        print count
        line = line.split(", ")
        tags = line[4].split(",")
        tags_list = []
        for word in tags:
            w = ps.stem(regex.sub("",word))
            if len(w) > 0 and w not in tags_list:
                tags_list.append(w)
        if len(tags_list) == 0:
            out_f.write('unknown')
        else:
            for word in tags_list:
                out_f.write(word + ",")
        out_f.write("\n")
        count += 1
    in_f.close()
    out_f.close()
    
if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
