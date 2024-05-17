if __name__ == "__main__":
    windowSize = int(input("Enter number of frames\n"))
    currentFrame = 1

    while True:
        for idx in range(windowSize):
            print(f"Frame {currentFrame} transmitted")
            currentFrame += 1

        ack = int(input("Enter acknowledgement of received frame\n"))

        if ack > currentFrame:
            break
        else:
            currentFrame = ack
