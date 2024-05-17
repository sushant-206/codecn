if __name__ == "__main__":
    windowSize = int(input("Enter number of frames\n"))
    currentFrame = 0
    ack = 0
    while(True):
        for idx in range(windowSize):
            print(f"Frame {currentFrame} transmitted")
            currentFrame+=1
            if(currentFrame ==  windowSize):
                break
        
        ack = int(input("Enter acknowledgement of received frame\n"))

        if(ack == windowSize):
            break
        else:
            currentFrame = ack




    