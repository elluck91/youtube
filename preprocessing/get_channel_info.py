import sys

if __name__ == "__main__":
    file_path = str(sys.argv[1])
    output_path = str(sys.argv[2])

    channel_ids = []
    
    write_to = open(output_path, "w")
    
    try:
        file = open(file_path, "r")
    except FileNotFoundError:
        print "The path you passed cannot be found. Terminating."
    else:
        counter = 1
        for line in file:
            print counter
            channel = line.split(", ")
#            print channel
 #           if channel[1] not in channel_ids:
#            channel_ids.append(channel[1])
            counter += 1 
#        for channel_id in channel_ids:
            write_to.write(channel[1] + "\n")
            
        write_to.close()
        file.close()
