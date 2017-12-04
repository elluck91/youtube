import sys
import pickle

if __name__ == "__main__":
    input1 = sys.argv[1]
    output = sys.argv[2]

    f1 = open(input1, 'r')
    out = open(output, 'w')
    classes = open('classes.txt', 'wb')
    channel_ids = open("channel_ids.txt", 'r')

    dictionary = pickle.load(open("channel_dictionary.pickle", 'rb'))

    for line in f1:
        temp = ""
        f1_l = line.replace("\n", ',')
        # in case of video_stats index 0 contains video id
        # we don't need the id, row is an id
        vector = f1_l.split(',')
        f1_values = vector[2:]
        data_to_save = ','.join([str(x) for x in f1_values])
        clas = vector[1]
        try:
            channel_info = dictionary[channel_ids.next().replace("\n",'')]
        except:
            channel_info = "0,0,0,0"
        data_to_save += channel_info
        out.write(data_to_save + "\n")
        classes.write(clas + '\n')
    f1.close()
    out.close()
    classes.close()
