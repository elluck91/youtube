
import sys

if __name__ == "__main__":
    output_path = open("video_data.txt", 'w')

    
    try:
        file = open("my_data.txt", "r")
    except FileNotFoundError:
        print "The path you passed cannot be found. Terminating."
    else:
        counter = 1
        for line in file:
            print counter
            line_list = line.split(", ")
            video_id = line_list[0]
            counter += 1 
            output_path.write(video_id + "\n")
        output_path.close()
        file.close()
