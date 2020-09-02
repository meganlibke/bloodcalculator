def interface():
    print("My Program")
    while True:
        print("Options for you: ")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()

def HDL_driver():
    # Get input
    HDL=HDL_input()
    # Check if HDL is normal
    check=HDL_check(HDL)
    # Output
    HDL_output(check)

def HDL_input():
    HDL=int(input("Enter the HDL test result: "))
    return HDL

def HDL_check(HDL):
    if HDL>=60:
        return "Normal"
    elif 40 <= HDL < 60:
        return "Borderline Low"
    elif HDL < 40:
        return "Low"
    else:
        return "Error: input a number"

def HDL_output(check):
    print(check)
    return
if __name__ == "__main__" :
    interface()
