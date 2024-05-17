if __name__ == "__main__":
    windowSize = int(input("Enter number of frames\n"))
    ack = 0

    for frame in range(windowSize):
        print(f"Frame {frame} transmitted")

    while(True):
 
        ack = int(input("Enter negative acknowledgement for not received frame\n"))
        
        if(ack == -1):
            break

        
        print(f"Frame {ack} transmitted")




    