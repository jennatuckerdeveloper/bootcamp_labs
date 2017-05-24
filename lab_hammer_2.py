timecheck=input("Select one (Military Time/Standard Time): ")
if timecheck==("Military Time"):
    x=input("Enter a time: ")
    if x>1200:
        print("Time: ",x-1200,"O'clock")
    if x<1200:
        print("Time: ",x+1200,"O'clock")
if timecheck==("Standard Time"):
    mn=raw_input("(AM or PM): ")
    if mn==("AM"):
        x=input("Enter a time: ")
        if 1200<=x<=1259:
            print("Time: ",x-1200,"Hours")

        elif x<1200:
            print("Time: ",x,"Hours")
        elif x>=1200:
            print("Time: ",x+1200,"Hours")
    if mn==("PM"):
        x=input("Enter a time: ")
        if x<=1200:
            print("Time: ", x+1200,"Hours")
