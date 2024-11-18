
# Process: Read No From Input With Message "Please input a number"
def readnofrominput():
    num=float(input("Please input a number: "))
    return num

# Process: Prepare Positive Number Message "{num} is a positive number"
def preparepositivemsg(n):
    return f"{n} is a positive number"

# Process: Prepare Non-Positive Number Message "{num} is not a positive number"
def preparenonpositivemsg(n):
    return f"{n} is not a positive number"

def outputmsg(message):
    print(message)

if __name__ == "__main__":
    # Process: Store Result of Read No From Input
    numfrominput = readnofrominput()

    # Condition: Is num positive (Yes)
    if numfrominput > 0:
        # Process: Store Return Message
        msg = preparepositivemsg(numfrominput)
    # Condition: Is num positive (No)
    else:
        # Process: Store Return Message
        msg = preparenonpositivemsg(numfrominput)

    # Process: Output Message
    outputmsg(msg)
