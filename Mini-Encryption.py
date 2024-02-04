while 1 :
    print("choose your option: \n\t1)Encrypt\n\t2)Decrypt\n\t3)Exit")
    choice = input("Your choice: ")
    if choice == "1":
        Plain_Text = input("Text: ")
        Encrypted_Text =""
        for i in Plain_Text:
            x = ord(i) * 2 + 7
            Encrypted_Text += chr(x)
        print("Encrypted text:",Encrypted_Text)
        print("*"*40+"\n")
    elif choice == "2":
        Plain_Text = ""
        Encrypted_Text = input("Text: ")
        for i in Encrypted_Text:
            x =(ord(i) - 7) // 2
            Plain_Text += chr(x)
        print("Plain text:", Plain_Text)
        print("*"*40+"\n")
    elif choice == "3":
        print("Goodbye!!!!!!!!!!!")
        break
    else:
        print("Wrong choice")
        print("*"*40+"\n")

