def main():
    while True:
        try:
            length = input(float"Enter the length") 
            width = input(float"Enter the width") 
            height = input(float"Enter the height") 
            volume = (1/3) * length * width * height
        except:
            print:("input the vaild maber")


if __name__ == "__main__":
    # execute only if run as a script
    main()
