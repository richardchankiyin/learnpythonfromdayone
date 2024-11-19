
# Process: Read No From Input With Message "Please input a number"
def readnofrominput():
    num=float(input("Please input a number: "))
    return num

def outputmsg(message):
    print(message)

if __name__ == "__main__":
    # Process: Store Result of Read No From Input
    numfrominput = readnofrominput()

    # Process: Store 0 as the value of variable "counter"
    counter = 0    

    # Decision: counter < no from input?
    while counter < numfrominput:
        # Process: Output Messag "The current value of variable counter is {current counter value}"
        outputmsg(f"The current value of variable counter is {counter}")
        # Process: Increase the value of variable "counter" by 1
        counter += 1

    # Process: Output Message "Goodbye!"
    outputmsg("Goodbye!")
