def interface():
    print("My Program")
    while True:
        print("Options for you:")
        print("1-HDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            return
        elif choice == '1':
            HDL_driver()

def HDL_driver()
    # Get input
    HDL=HDL_input()
    # Check if HDL is normal
    HDL_check(HDL)
    # Output

def HDL_input()
    HDL=int(input("Enter the HDL test result: "))
    return HDL

def HDL_check(HDL)
    if HDL>=60:
        print("HDL is normal")
    elif HDL<60 & HDL>=40:
        print("HDL is borderline low")
    elif HDL < 40:
        print("HDL is low")
    else:
        print("Error: input a number")

interface()
