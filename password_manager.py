def encrypter(statement):
    dict_en = {'a': '%', 'b': '^', 'c': '|', 'd': '/', 'e': '2', 'f': '!',
               'g': '@', 'h': '_', 'i': '0', 'j': "'", 'k': '[', 'l': '1',
               'm': ':', 'n': '&', 'o': ';', 'p': '8', 'q': '>', 'r': ')',
               's': '-', 't': '.', 'u': '*', 'v': '#', 'w': '}', 'x': '~',
               'y': '9', 'z': '+', ' ': ']', '3': '(', '4': '{', '5': '?',
               '6': '`', '7': '<', ',': '"', "=": "=", 'X': 'O', 'W': 'Y',
               'E': 'T', 'Z': 'F', 'J': 'L', 'Q': 'M', 'U': 'D', 'P': 'B',
               'H': 'S', 'A': 'I', 'V': 'G', 'C': 'K', 'N': 'R'}

    dict_de = {x:y for y,x in dict_en.items()}

    list = ""

    for xx in statement:
        final_dict = dict_en | dict_de
        if final_dict.get(xx) is not None:
            list +=  final_dict.get(xx)
        else:
            list += xx
    return list

loop = True
path_dir = "D:/passo.txt"  # you can have whatever directory you want

while loop:
    option_1 = input("Do you want to input password(I)\n\t\tor\n"
                     "Obtain password(OP): ")

    if option_1 == "i" or option_1 == "I":
        website = input("Give me the website name(ONLY ALPHABETS, you can also use spaces): ")

        for x in website:
            if x.isspace() or x.isalnum():
                continue
            else:
                print("C'mon dude read the GOD DAMN INSTRUCTIONS:")
                website = input("Give me the website name(ONLY ALPHABETS, you can also use spaces): ")

        username = input("Give me the username(no space allowed): ")
        username_conf = input("Confirm username: ")
        while username_conf != username or username.count(" ") > 0:
            username = input("Give it again, but correctly: ")
            username_conf = input("Confirmation of username:")

        password = input("Give me the password: ")
        password_conf = input("Confirm password: ")
        while password_conf != password:
            password = input("Give me the password, correctly: ")
            password_conf = input("Confirm password, correctly dude: ")

        with open(path_dir, "a") as password_folder:
            print(f"{encrypter(website)}={encrypter(username)}]{encrypter(password)}", file=password_folder)  # "]" is used in the statement so after encryption it becomes readable(check the 'encoder'
        print(f"its saved in \n'{path_dir}'")  # check the encoder dictionary in encrypter function for more details.
        loop = False

    elif option_1 == "op" or option_1 == "OP":
        open_website = input("give me the website name(if present): ")
        open_website = encrypter(open_website)

        with open(fr"{path_dir}", "r") as password_folder:
            text = ""
            final_str = ""
            a = 1
            for x in password_folder.readlines():
                text = ""
                for t in x:
                    text = text + t
                    if t == "=":
                        text = text.strip("=")
                        if text == open_website:
                            a = 0
                            for i in encrypter(x[len(text) + 1::]):
                                final_str = final_str + i
                                if i.isspace():
                                    username_ask = final_str.strip(" ")
                                    final_str = ""
                                else:
                                    pass

                            password_ask = final_str
                            break
                        else:
                            text = ""
                        break
                    else:
                        continue

                if a == 0:
                    break

        if a != 0:
            print("I guess you haven't entered any username/password regarding this website!!")
            master = input("perhaps you forgot the website? (y/n): ")
            if master == "y" or master == "Y":
                masterkey_g = input("give the master password: ")
                tries = 0
                while masterkey_g != "masterkey" and tries < 3:
                    tries += 1
                    masterkey_g = input(f"you have {4-tries}tries! ")
                if masterkey_g == "masterkey":
                    with open(path_dir, "r") as password_folder:
                        full_list = ""
                        for x in password_folder.readlines():
                            for t in x:
                                full_list = full_list + encrypter(t)
                            full_list = full_list + "\n"
                    print(f'\n{full_list}')
                else:
                    print("Sorry dude i cant do anything!! ")
            else:
                print("Sorry dude i cant do anything!! ")
        else:
            print(f"username: {username_ask} \npassword: {password_ask}\n")
            print("Here you go!!!")
        loop = False
    else:
        print("\n Give a valid input dude!\n")
        continue