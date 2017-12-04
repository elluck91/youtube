file = open("channel_data.txt", 'r')
import pickle

dictionary = dict()

for line in file:
    l = line.replace("\n", '')
    l = l.split(',')
    key = l[0]
    values = l[1:]
    value = ','.join([str(x) for x in values])
    dictionary[key] = value

with open("channel_dictionary.pickle", 'wb') as handle:
    pickle.dump(dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)
