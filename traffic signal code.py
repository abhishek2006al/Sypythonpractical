print("==================Traffic signal stimulator================")
signal=input("Enter the colour of signal:").upper()
emer=input("Enter if you have emergency(yes/no):").lower()


if signal=="RED":
    if emer=="yes":
        print("you can go...")
    else:    
        print("Stop")
    
elif signal=="YELLOW":
    if emer=="yes":
        print("you can go")
    else:    
        print("Please wait...")
elif signal=="GREEN":
    print("You Can go..")
else:
    print("Invalid colour....")    

        
    
                