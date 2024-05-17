
def xor(divisor:str,dividend:str):
    tmp = ""
    for idx in range(0,len(divisor)):
        if(divisor[idx] != dividend[idx]):
            tmp += "1"
        else:
            tmp += "0"
    
    return tmp
            
def mod2div(frame: str, generator: str) -> str:

    GEN_LEN = len(generator)
    FRAME_LEN = len(frame)

    tmp = frame[0:GEN_LEN]
    nextBitIdx = GEN_LEN

    while nextBitIdx < FRAME_LEN :
      
        if len(tmp) == GEN_LEN:
            tmp = xor(generator,tmp) + frame[nextBitIdx]
        else:
            tmp += frame[nextBitIdx]
    
        tmp = tmp.lstrip('0')
        nextBitIdx+=1

    if len(tmp) == GEN_LEN:
        tmp = xor(generator,tmp)
    
    return tmp[1:]

 
def senderSide(frame: str, generator: str) -> str:

    print("\nSender Side:")

    GEN_LEN = len(generator)
    endBits = "0" * (GEN_LEN - 1)

    appendedFrame = ''+frame

    appendedFrame += endBits

    result = mod2div(appendedFrame, generator)
    transmittedFrame = frame + result

    print(
        f"Frame: {frame}\nGenerator: {generator}\nNo of 0's to be appended: {endBits}"
    )
    print(f"Message after appending 0's: {appendedFrame}\nCRC bits: {result}\nTransmitted Frame: {transmittedFrame}")

    return transmittedFrame


# CRC checker -> receiver
def receiverSide(frame: str, generator:str) -> None:
    result = mod2div(frame, generator)
    
    print(f"\nReceiver side \nReceived Frame: {frame}\nRemainder:{result}\n ")

    if "1" not in result:
        print("Data received without corruption")
    else:
        print("Data has been corrupted")


if __name__ == "__main__":
    frame = input("Enter frame\n")
    generator = input("Enter generator\n")

    data = senderSide(frame, generator)
    receiverSide(data, generator)
