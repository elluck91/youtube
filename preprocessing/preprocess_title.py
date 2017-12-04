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
        start_idx = 2
        current_idx = 2
        title = line[current_idx]
        while not line[current_idx+1].isdigit() or int(line[current_idx+1]) > 45:
            title += ", " + line[current_idx+1]
            current_idx += 1
        
        title = title.split(", ")
        words_in_title = ""

        for word in title:
            words_in_title += " " + word
        print words_in_title 
        
        words = words_in_title.split(" ")
        print words

        words_list = []
        for word in words:
            if len(word) != 0:
                words_list.append(ps.stem(regex.sub("",word)))
        if len(words_list) == 0:
            out_f.write('unknown')
        else:
            for word in words_list:
                out_f.write(word + ",")
        out_f.write("\n")
        count += 1
    in_f.close()
    out_f.close()
    
if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
