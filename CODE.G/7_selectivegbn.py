if __name__ == "__main__":
    windowSize = int(input("Enter number of frames\n"))
    currentFrame = 1
    ack = 0

    for idx in range(windowSize):
        print(f"Frame {currentFrame} transmitted")
        currentFrame += 1

    while True:

        ack = int(input("Enter acknowledgement for not received frame\n"))

        if ack == -1 or ack > windowSize:
            break

        print(f"Frame {ack} transmitted")
