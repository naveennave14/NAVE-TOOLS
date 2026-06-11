# Importing necessary modules
import os
import time

# colours setup
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'

# Create a banner
def banner():
 os.system("clear")
 print("\033[32m")
 print("  _           _    _      _             _            ____ ____ ____  ")
 print("| |  _  _ __(_)__| |_ __| |_  __ _ _ _| |_ ___ _ __|__  |__  |__  | ")
 print("| |_| || / _| / _` | '_ \ ' \/ _` | ' \  _/ _ \ '  \ / /  / /  / /  ")
 print("|____\_,_\__|_\__,_| .__/_||_\__,_|_||_\__\___/_|_|_/_/  /_/  /_/   ")
 print("                   |_|                                              ")

# Create and display a choices
def display_choice():
    banner()
    print("____________________________________________________")
    print("| ------------- TOOL NAME : LP-TOOLS -------------- |")
    print("| --------------- AUTHOR : LP777 ------------------ |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________________")
    print(b+"|",g+"CHOICES:",b+"                                     |")
    print(b+"|",g+"1.",r+"Social media phishing tools", y+"(10)",b+"          |")
    print(b+"|",g+"2.",r+"URL hider tools",y+"            (4)",b+"           |")
    print(b+"|",g+"3.",r+"Password generator tools",y+"   (5)",b+"           |")
    print(b+"|",g+"4.",r+"Phone number osint tools",y+"   (4)",b+"           |")
    print(b+"|",g+"5.",r+"Ip changer tools",y+"           (5)",b+"           |")
    print(b+"|",g+"6.",r+"Instagram tools",y+"            (3)",b+"           |")
    print(b+"|",g+"7.",r+"Whatsapp tools",y+"             (2)",b+"           |")
    print(b+"|",g+"8.",r+"Cloud shell",y+"                (1)",b+"           |")
    print(b+"|",g+"9.",r+"Btc brute-force",y+"            (1)",b+"           |")
    print(b+"|",g+"10.",r+"DDOS-ATTACK tools",y+"         (1)",b+"           |")
    print(b+"|",g+"lp.",r+"To exit",b+"                                  |")
    print(b+"•••••••••••••••••••••••••••••••••••••••••••••••••")

# Get users choice
def get_user_choice():
    return input("Enter choice : ")

# start the script
def main():
        display_choice()
        choice = get_user_choice()

        if choice == '1':
          page_1()

        elif choice == '2':
          page_2()

        elif choice == '3':
          page_3()

        elif choice == '4':
          page_4()

        elif choice == "5":
         page_5()

        elif choice == "6":
         page_6()

        elif choice == "7":
         page_7()

        elif choice == "8":
         page_8()

        elif choice == "9":
         page_9()

        elif choice == "10":
         page_10()

        elif choice == "lp":
          os.system("exit")

        else:
          main()

# Create a phishing tools choice page
def page_1():
    banner()
    print("____________________________________________________")
    print("| ------------- TOOL NAME : PHISHING TOOLS -------- |")
    print("| ----------------- AUTHOR : LP777 ---------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________________")
    print(b+"|",g+"PHISHING TOOLS:",b+"                              |")
    print(b+"|",g+"1.",r+"ZPHISHER",y+"       (shell)",b+"                   |")
    print(b+"|",g+"2.",r+"MAXPHISHER",y+"     (python)",b+"                  |")
    print(b+"|",g+"3.",r+"ADVPHISHING",y+"    (shell)",b+"                   |")
    print(b+"|",g+"4.",r+"GOPHISH",y+"        (golang)",b+"                  |")
    print(b+"|",g+"5.",r+"FIERCEPHISH",y+"    (php)",b+"                     |")
    print(b+"|",g+"6.",r+"SHELLPHISH",y+"     (shell)",b+"                   |")
    print(b+"|",g+"7.",r+"LORDPHISH",y+"      (shell)",b+"                   |")
    print(b+"|",g+"8.",r+"DARKPHISH",y+"      (python)",b+"                  |")
    print(b+"|",g+"9.",r+"T-PHISH",y+"        (shell)",b+"                   |")
    print(b+"|",g+"10.",r+"RAVANA",y+"        (shell)",b+"                   |")
    print(b+"•••••••••••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
               os.system("clear")
               os.system(" pkg install git -y")
               os.system(" sudo apt install git -y")
               os.system(" git clone --depth=1 https://github.com/htr-tech/zphisher.git")
               os.system("clear")
               os.chdir("zphisher")
               os.system(" bash zphisher.sh ")

    elif choice == "2":
               os.system("clear")
               os.system("pkg install git python3 php openssh -y")
               os.system("sudo apt install git python3 php openssh-client -y")
               os.system("git clone https://github.com/KasRoudra2/MaxPhisher")
               os.system("pip3 install -r MaxPhisher/files/requirements.txt")
               os.system("pip3 install maxphisher")
               os.system("sudo pip3 install maxphisher")
               os.system("clear")
               os.chdir("MaxPhisher")
               os.system("python3 maxphisher.py")

    elif choice == "3":
               os.system("clear")
               os.system("pkg install git -y")
               os.system("sudo apt install git -y")
               os.system("git clone https://github.com/Ignitetch/AdvPhishing.git")
               os.chdir("AdvPhishing")
               os.system("bash Android-Setup.sh")
               os.system("bash Linux-Setup.sh")
               os.system("bash AdvPhishing.sh")

    elif choice == "4":
               os.system("clear")
               os.system("pkg install git golang -y")
               os.system("apt install sudo -y")
               os.system("sudo apt install git golang-go -y")
               print("\033[32m")
               os.system("git clone https://github.com/gophish/gophish.git")
               os.chdir("gophish")
               os.system("go build")
               os.system("go run gophish.go")

    elif choice == "5":
               os.system("clear")
               os.system("wget https://raw.githubusercontent.com/Raikia/FiercePhish/master/install.sh")
               os.system("chmod +x install.sh")
               os.system("clear")
               os.system("bash install.sh")

    elif choice == "6":
               os.system("clear")
               os.system("apt install git wget php unzip curl -y")
               os.system("pkg install git wget php unzip curl -y")
               os.system("git clone https://github.com/AbirHasan2005/ShellPhish.git")
               os.system("clear")
               os.chdir("ShellPhish")
               os.system("bash shellphish.sh")

    elif choice == "7":
               os.system("clear")
               os.system("sudo apt install git php openssh wget -y")
               os.system("pkg install git php openssh wget -y")
               os.system("git clone https://github.com/therealelyayo/LordPhish-1.git")
               os.chdir("LordPhish-1")
               os.system("bash lord.sh")

    elif choice == "8":
               os.system("clear")
               os.system("sudo apt install python3 curl php git openssh nodejs npm python3-tk -y")
               os.system("pkg  install python3 curl php git openssh nodejs npm python3-tk -y")
               os.system("pip3 install requests wget pyshorteners")
               os.system("git clone https://github.com/Cyber-Anonymous/Dark-Phish.git")
               os.chdir("Dark-Phish")
               os.system("python3 dark-phish.py")

    elif choice == "9":
               os.system("clear")
               os.system("sudo apt install git unzip -y")
               os.system("pkg install git unzip -y")
               os.system("git clone https://github.com/Stefin-Franklin/T-Phish.git")
               os.chdir("T-Phish")
               os.system("unzip T-Phish.zip")
               os.chdir("T-Phish")
               os.system("bash start.sh")
               os.system("bash phish.sh")

    elif choice == "10":
               os.system("clear")
               os.system("sudo apt install git -y ")
               os.system("pkg install git -y")
               os.system("git clone https://github.com/princekrvert/Ravana.git")
               os.chdir("Ravana")
               os.system("bash ravana.sh")

    else:
          main()


# Create a URLHIDING tools page
def page_2():
    banner()
    print("____________________________________________________")
    print("| ------------- TOOL NAME : URLHIDING TOOLS ------- |")
    print("| ----------------- AUTHOR : LP777 ---------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________________")
    print(b+"|",g+"URLHIDING TOOLS:",b+"                             |")
    print(b+"|",g+"1.",r+"Facad1ng",y+"      (python)",b+"                   |")
    print(b+"|",g+"2.",r+"URLhider",y+"      (python)",b+"                   |")
    print(b+"|",g+"3.",r+"Mask-url",y+"      (python)",b+"                   |")
    print(b+"|",g+"4.",r+"Maskphish",y+"     (shell)",b+"                    |")
    print(b+"•••••••••••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == '1':
          os.system("clear")
          os.system("pkg install git python3 -y")
          os.system("apt install git python3 -y")
          os.system("git clone https://github.com/spyboy-productions/Facad1ng.git")
          os.chdir("Facad1ng")
          os.system("pip3 install -r requirements.txt")
          os.system("clear")
          os.system("python3 facad1ng.py")

    elif choice == '2':
          os.system("clear")
          os.system("pkg install git python3 -y")
          os.system("apt install git python3 -y")
          os.system("git clone https://github.com/IHA089/URLHider.git")
          os.chdir("URLHider")
          os.system("pip3 install -r requirements.txt")
          os.system("clear")
          os.system("python3 URLHider.py")

    elif choice == '3':
          os.system("clear")
          os.system("pkg install git python3 -y")
          os.system("apt install git python3 -y")
          os.system("git clone https://github.com/mishakorzik/mask-url.git")
          os.system("pip3 install requests")
          os.system("clear")
          os.chdir("mask-url")
          os.system("python3 mask.py")

    elif choice == '4':
          os.system("clear")
          os.system("pkg install git -y")
          os.system("apt install git -y ")
          os.system("git clone https://github.com/rsdraju99/maskphish.git")
          os.system("clear")
          os.chdir("maskphish")
          os.system("bash maskphish.sh")

    else:
          main()

# Create a password generator tools page
def page_3():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : PASSWORD GENERATOR  TOOLS ---- |")
    print("| -------------- AUTHOR : LP777  ------------------ |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________________")
    print(b+"|",g+"PASSWORD GENERATOR  TOOLS:",b+"                   |")
    print(b+"|",g+"1.",r+"Crunch",y+"                      (c)",b+"          |")
    print(b+"|",g+"2.",r+"Cupp",y+"                        (python)",b+"     |")
    print(b+"|",g+"3.",r+"W-list-gen",y+"                  (python)",b+"     |")
    print(b+"|",g+"4.",r+"Pydictor",y+"                    (python)",b+"     |")
    print(b+"|",g+"5.",r+"Psudohash",y+"                   (python)",b+"     |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == '1':
          os.system("clear")
          banner()
          print("")
          print(g)
          min = input("ENTER THE PASSWORD LENTH (min) : ")
          max = input("ENTER THE PASSWORD LENTH (max) : ")
          pas = input("ENTER THE PASSKEYWORD TO GENERATE PASSWORD : ")
          file = input("ENTER THE FILE NAME TO SAVE GENERATED PASSWORD : ")
          os.system(f"crunch {min} {max} {pas} > {file}")
          print("")
          print("")
          print(r+"YOUR PASSWORD WAS SAVED IN ",g+file)

    elif choice == '2':
          os.system("clear")
          os.system("pkg install git python3 -y")
          os.system("apt install git python3 -y")
          os.system("git clone https://github.com/Mebus/cupp.git")
          os.system("clear")
          print("\033[31m")
          os.chdir("cupp")
          os.system("python3 cupp.py -i")

    elif choice == "3":
               os.system("clear")
               os.system("sudo apt install git -y")
               os.system("pkg install git -y")
               os.system("git clone https://github.com/IHA089/W-list-gen.git")
               os.chdir("W-list-gen")
               os.system("python3 wlistgen.py")

    elif choice == "4":
               os.system("clear")
               os.system("sudo apt install git python3 -y")
               os.system("pkg install git python3 -y")
               os.system("git clone https://github.com/LandGrey/pydictor.git")
               os.chdir("pydictor")
               os.system("python3 pydictor.py")

    elif choice == "5":
               os.system("clear")
               os.system("sudo apt install git python3 -y")
               os.system("pkg install git python3 -y")
               os.system("git clone https://github.com/t3l3machus/psudohash.git")
               os.system("pip3 install tqdm")
               os.chdir("psudohash")
               os.system("python3 psudohash.py")

    else:
          main()

# Create a phone number osint tools page
def page_4():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : PHONE NUMBER OSINT TOOLS ----- |")
    print("| -------------- AUTHOR : LP777 ------------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________________")
    print(b+"|",g+"PHONE NUMBER OSINT TOOLS",b+"                     |")
    print(b+"|",g+"1.",r+"Truecallerjs",y+"      (java)",b+"                 |")
    print(b+"|",g+"2.",r+"Phoneinfoga",y+"       (python)",b+"               |")
    print(b+"|",g+"3.",r+"Owl-sint",y+"          (python)",b+"               |")
    print(b+"|",g+"4.",r+"Th3inspector",y+"      (perl)",b+"                 |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
               os.system("clear")
               os.system("sudo apt install git nodejs -y")
               os.system("pkg install git nodejs -y")
               os.system("npm install truecallerjs")
               os.system("npm install -g truecallerjs")
               os.system("git clone https://github.com/sumithemmadi/truecallerjs.git")
               os.chdir("truecallerjs")
               os.system("truecallerjs login")
               print(g)
               print("Use this tool must you be login with your phone number")
               print("You forget login run this command:")
               print("truecallerjs login ")
               print("truecallerjs -s [number]: Use this command to search for a phone number and retrieve the caller name and related information.")

    elif choice == "2":
               os.system("clear")
               os.system("sudo apt install git python3 -y")
               os.system("pkg install git python3 -y")
               os.system("git clone https://github.com/la-deep-web/Phoneinfoga.git")
               os.chdir("Phoneinfoga")
               os.system("pip3 install -r requirements.txt")
               os.system("python3 phoneinfoga.py -h ")

    elif choice == "3":
               os.system("clear")
               os.system("sudo apt install git python2 python3 -y")
               os.system("pkg install git python2 python3 -y")
               os.system("git clone https://github.com/IccTeam/Owl-sint.git")
               os.chdir("Owl-sint")
               os.system("bash module.sh")
               os.system("python3 owlsint.py")

    elif choice == "4":
               os.system("clear")
               os.system("sudo apt install git perl -y")
               os.system("pkg install git perl -y")
               os.system("git clone https://github.com/Moham3dRiahi/Th3inspector.git")
               os.chdir("Th3inspector")
               os.system("bash install.sh")
               os.system("perl Th3inspector.pl")

    else:
          main()

# Create a ip changer tools page
def page_5():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : IP CHANGER TOOLS ------------- |")
    print("| -------------- AUTHOR : LP777 --- --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________________")
    print(b+"|",g+"IP CHANGER TOOLS ",b+"                             |")
    print(b+"|",g+"1.",r+"Tor ip changer",y+"         (python)",b+"           |")
    print(b+"|",g+"2.",r+"Gr33n37-ip-changer",y+"     (shell)",b+"            |")
    print(b+"|",g+"3.",r+"Auto_Tor_IP_changer",y+"    (python)",b+"           |")
    print(b+"|",g+"4.",r+"PyTor-IP-Changer",y+"       (python)",b+"           |")
    print(b+"|",g+"5.",r+"Ip-changer",y+"             (shell)",b+"            |")
    print("••••••••••••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
               os.system("clear")
               os.system("sudo apt install git python3 -y")
               os.system("pkg  install git python3 -y")
               os.system("git clone https://github.com/isPique/Tor-IP-Changer.git")
               os.chdir("Tor-IP-Changer")
               os.system("pip3  install -r requiremkents.txt")
               os.system("python3 IP-Changer.py")

    elif choice == "2":
               os.system("clear")
               os.system("sudo apt install git -y")
               os.system("pkg install git -y")
               os.system("git clone https://github.com/gr33n37/gr33n37-ip-changer.git")
               os.chdir("gr33n37-ip-changer")
               os.system("bash ip-changer.sh")

    elif choice == "3":
               os.system("clear")
               os.system("sudo apt install git python3 -y")
               os.system("pkg install git python3 -y")
               os.system("git clone https://github.com/FDX100/Auto_Tor_IP_changer.git")
               os.chdir("Auto_Tor_IP_changer")
               os.system("python3 install.py")
               os.system("python3 autoTOR.py")

    elif choice == "4":
               os.system("clear")
               os.system("sudo apt install git python3 -y")
               os.system("pkg install git python3 -y")
               os.system("git clone https://github.com/G0ldenRat10/PyTor-IP-Changer.git")
               os.chdir("PyTor-IP-Changer")
               os.system("pip3 install -r requirements.txt")
               os.system("python3 pytor.py")

    elif choice == "5":
               ip_changer()

    else:
          main()

# Create a instagram tools page 
def page_6():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : INSTAGRAM  TOOLS ------------- |")
    print("| -------------- AUTHOR : LP777 --- --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________")
    print(b+"|",g+"Instagram tools:",b+"                     |")
    print(b+"|",g+"1.",r+"Osint tools",y+"       (3)",b+"            |")
    print(b+"|",g+"2.",r+"Passwordcracking",y+"  (1)",b+"            |")
    print(b+"|",g+"3.",r+"Mass report",y+"       (1)",b+"            |")
    print("•••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
         insta_osint()

    elif choice == "2":
         password_cracking()

    elif choice == "3":
         insta_mass_report()

    else:
          main()

def ip_changer():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : IP-CHANGER ------------------- |")
    print("| -------------- AUTHOR : LP777 ------------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________")
    print(b+"|",g+"IP-CHANGER:",b+"                          |")
    print(b+"|",g+"1.",r+"INSTALL TOOL",y+"        ",b+"             |")
    print(b+"|",g+"2.",r+"RUN TOOL",y+"   ",b+"                      |")
    print("•••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
         os.system("clear")
         os.system("sudo apt install curl -y")
         os.system("pkg install curl -y")
         os.system("curl -sL https://github.com/Anon4You/Ip-Changer/raw/main/installer.sh | bash")
         print("Tool installed")
         time.sleep(3)
         ip_changer()

    elif choice == "2":
         os.system("clear")
         sec = input("ENTER HOW MANY SECONDS TO CHANGE IP (min:5): ")
         banner()
         os.system(f"ip-changer -r {sec}")

    else:
          main()

# Create a osint tools page
def insta_osint():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : OSINT TOOLS ------------------ |")
    print("| -------------- AUTHOR : LP777 --- --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_____________________________________________")
    print(b+"|",g+"Osint tools:",b+"                              |")
    print(b+"|",g+"1.",r+"Ig-osint-v2",y+"                (python)",b+"   |")
    print(b+"|",g+"2.",r+"Ig-osint-tomxploit",y+"         (python)",b+"   |")
    print(b+"|",g+"3.",r+"Owl-sint",y+"                   (python)",b+"   |")
    print("••••••••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
       os.system("clear")
       os.system("sudo apt install git python3 -y")
       os.system("pkg install git python3 -y")
       os.system("git clone https://github.com/Achik-Ahmed/IG-OSINT-V2.git")
       os.chdir("IG-OSINT-V2")
       os.system("pip3 install instaloader")
       os.system("python3 ig.py")

    elif choice == "2":
       os.system("clear")
       os.system("sudo apt install git python3 -y")
       os.system("pkg install git python3 -y")
       os.system("git clone https://github.com/t0mxplo1t/IG-OSINT.git")
       os.chdir("IG-OSINT")
       os.system("pip3 install instaloader")
       os.system("python3 ig.py")

    elif choice == "3":
       os.system("clear")
       os.system("sudo apt install git python2 python3 -y")
       os.system("pkg install git python2 python3 -y")
       os.system("git clone https://github.com/IccTeam/Owl-sint.git")
       os.chdir("Owl-sint")
       os.system("bash module.sh")
       os.system("python3 owlsint.py")

    else:
          main()

# Create a password cracking tools page
def password_cracking():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : PASSWORD CRACKING TOOLS ------ |")
    print("| -------------- AUTHOR : LP777 --- --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"________________________________________")
    print(b+"|",g+"Password cracking  tools:",b+"           |")
    print(b+"|",g+"1.",r+"Instainsane",y+"           (shell)",b+"   |")
    """print(b+"|",g+"2.",r+"",y+"        ()",b+"        |")"""
    print("••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
        os.system("clear")
        os.system("sudo apt install git curl tor openssl -y")
        os.system("pkg install git curl tor openssl -y")
        os.system("git clone https://github.com/umeshshinde19/instainsane.git")
        os.chdir("instainsane")
        os.system("chmod +x install.sh")
        os.system("bash install.sh")
        os.system("bash instainsane.sh")

    else:
          main()

def insta_mass_report():
    banner()
    print("____________________________________________________")
    print("| ------ TOOL NAME : INSTA MASS REPORT TOOLS ------ |")
    print("| -------------- AUTHOR : LP777 --- --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"________________________________________")
    print(b+"|",g+"Insta mass report tools:",b+"            |")
    print(b+"|",g+"1.",r+"SMH",y+"              (python)",b+"       |") 
    print("••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
        os.system("clear")
        os.system("sudo apt install git python3 python3-pip -y")
        os.system("pkg install git python3 ")
        os.system("git clone https://github.com/rdWei/SocialMediaHackingToolkit.git")
        os.chdir("SocialMediaHackingToolkit")
        os.system("pip3 install -r requirements.txt")
        os.system("python3 cmd/main.py")

    else:
          main()

def page_7():
    banner()
    print("____________________________________________________")
    print("| ---------- TOOL NAME : WHATSAPP TOOLS ----------- |")
    print("| -------------- AUTHOR : LP777 --- --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"________________________________________")
    print(b+"|",g+"WHATSAPP TOOLS:",b+"                     |")
    print(b+"|",g+"1.",r+"QRL Hacking",y+"         (python)",b+"    |")
    print(b+"|",g+"2.",r+"unban method",y+"        ()",b+"          |")
    print("••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
           os.system("clear")
           os.system("sudo apt update && apt install git -y")
           os.system("apt update && pkg install git -y")
           os.system("sudo apt install python3 -y")
           os.system("pkg install python3 -y")
           os.system("pip install --upgrade pip")
           os.system("git clone https://github.com/OWASP/QRLJacking.git")
           os.chdir("QRLJacking")
           os.chdir("QRLJacker")
           os.system("chmod +x *")
           os.system("pip3 install -r requirements.txt")
           os.system("python3 QrlJacker.py")

    elif choice == "2":
           os.system("clear")
           os.system("sudo apt install figlet -y")
           os.system("pkg install figlet -y")
           banner()
           os.system("figlet whatsapp unban method")
           print(""" ❃ 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐔𝐍𝐁𝐀𝐍𝐍𝐈𝐍𝐆 ❃

➳ 𝙲𝚘𝚙𝚢 𝚝𝚑𝚒𝚜 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚊𝚗𝚍 𝚖𝚊𝚔𝚎 𝚜𝚞𝚛𝚎 𝚝𝚘 𝚛𝚎𝚙𝚕𝚊𝚌𝚎 𝚝𝚑𝚎 𝚕𝚊𝚜𝚝 𝚙𝚊𝚛𝚝 𝚠𝚒𝚝𝚑 𝚢𝚘𝚞𝚛 𝚋𝚊𝚗𝚗𝚎𝚍 𝚗𝚞𝚖𝚋𝚎𝚛.

Il mio numero è nuovo, e con quello ho appena aperto il settore e in questo gruppo ho davvero bisogno del mio account, non violo alcuna regola dell'informativa sulla privacy, quindi chiedo al team di supporto di whatsapp di agire il prima possibile in modo che Posso avere accesso al materiale dal mio gruppo è 2547𝚇𝚇𝚇𝚇𝚇𝚇𝚇𝚇

➳ 𝙿𝚊𝚜𝚝𝚎 𝚝𝚑𝚎 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚘𝚗 𝚋𝚘𝚝𝚑 𝚝𝚑𝚎 𝚜𝚞𝚋𝚓𝚎𝚌𝚝 𝚊𝚗𝚍 𝚌𝚘𝚖𝚙𝚘𝚜𝚎 𝚜𝚙𝚊𝚌𝚎𝚜.

➳ 𝚂𝚎𝚗𝚍 𝚝𝚑𝚎 𝚖𝚊𝚒𝚕 𝚝𝚘

smb@support.whatsapp.com

➳ 𝚆𝚊𝚒𝚝 𝚏𝚘𝚛 𝚆𝚑𝚊𝚝𝚜𝙰𝚙𝚙 𝚜𝚞𝚙𝚙𝚘𝚛𝚝 𝚝𝚘 𝚛𝚎𝚙𝚕𝚢
     ✼ 𝑻𝒉𝒆 𝒘𝒂𝒊𝒕𝒊𝒏𝒈 𝒅𝒖𝒓𝒂𝒕𝒊𝒐𝒏 𝒎𝒂𝒚 𝒗𝒂𝒓𝒚 𝒃𝒖𝒕 𝒔𝒉𝒐𝒖𝒍𝒅𝒏'𝒕 𝒕𝒂𝒌𝒆 𝒎𝒐𝒓𝒆 𝒕𝒉𝒂𝒏 24 𝒉𝒐𝒖𝒓𝒔.

✦•━━━━━━━━━━━━━━━━━•✦
  🥳 𝙷𝚊𝚙𝚙𝚢 𝙷𝚊𝚌𝚔𝚒𝚗𝚐 🥳
✦•━━━━━━━━━━━━━━━━━•✦ """)

    else:
           main()

def page_8():
    banner()
    print("____________________________________________________")
    print("| ----------- TOOL NAME : Cloud shell  ------------ |")
    print("| -------------- AUTHOR : LP777 --- --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"________________________________________")
    print(b+"|",g+"Cloud shell:",b+"                        |")
    print(b+"|",g+"1.",r+"Google cloud shell",y+"         ()",b+"   |")
    print("••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
           os.system("clear")
           os.system("pkg install curl -y")
           os.system("sudo apt install curl -y")
           os.system("curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz")
           os.system("clear")
           os.system("tar -xf google-cloud-cli-linux-x86_64.tar.gz")
           os.system("clear")
           os.system("./google-cloud-sdk/install.sh")
           os.system("clear")
           os.system("./google-cloud-sdk/install.sh --help")
           os.system("clear")
           os.system("./google-cloud-sdk/bin/gcloud init")
           os.system("clear")
           os.system("clear")
           os.system("gcloud init")
           os.system("clear")
           time.sleep(3)
           print("To run type : gcloud cloud-shell ssh")
           os.system("source ~/.bashrc")
           time.sleep(5)
           os.system("gcloud cloud-shell ssh")

    else:
           main()

def btc_1():
    banner()
    print("____________________________________________________")
    print("| --------- TOOL NAME : Btc brute-force  ---------- |")
    print("| -------------- AUTHOR : LP777 --- --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"_________________________________________")
    print(b+"|",g+"Btc brute-force:",b+"                     |")
    print(b+"|",g+"1.",r+"INSTALL Btc wallets",y+"        ",b+"      |")
    print(b+"|",g+"2.",r+"RUN TOOL",y+"   ",b+"                      |")
    print("•••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
         os.system("git clone https://github.com/lucidphantom777/Wallen-gen.git")
         os.system("cd Wallen-gen") 
         btc_1()

    elif choice == "2":
         os.system("./walletgen.sh")

    else:
          main()

def page_9():
    banner()
    print("____________________________________________________")
    print("| ----------- TOOL NAME : Btc brute-force  -------- |")
    print("| -------------- AUTHOR : LP777 --- --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"________________________________________")
    print(b+"|",g+"Btc brute-force:",b+"                    |")
    print(b+"|",g+"1.",r+"seed-phrase-generator",y+"  (shell)",b+"  |")
    print("••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
          os.system("apt install sudo -y")
          os.system("sudo apt update -y") 
          os.system("sudo apt install unzip -y") 
          os.system("sudo apt install git -y") 
          os.system("git clone https://github.com/lucidphantom777/Wallen-gen.git") 
          os.system("cd Wallen-gen") 
          os.system("unzip walletgen.Zip") 
          os.system("chmod +x walletgen.sh") 
          os.system("chmod +x walletgen") 
          os.system("./walletgen.Sh") 
          btc_1()

    else:
           main()


def page_10():
    banner()
    print("____________________________________________________")
    print("| ----------- TOOL NAME : DDOS-ATTACK tools  ------ |")
    print("| -------------- AUTHOR : LP777 --- --------------- |")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("")
    print(b+"________________________________________")
    print(b+"|",g+"DDOS-ATTACK tools:",b+"                  |")
    print(b+"|",g+"1.",r+"DDOS-RIPPER",y+"  (python)",b+"           |")
    print("••••••••••••••••••••••••••••••••••••••••")
    print('\033[32m')
    # Get users choice
    get_user_choice = input("Enter choices : ")
    # Store get_user_choice data  into choice variable
    choice = get_user_choice

    if choice == "1":
           os.system("clear")
           os.system("pkg install git python3 -y")
           os.system("sudo apt install git python3 python3-pip -y")
           os.system("git clone https://github.com/palahsu/DDoS-Ripper.git")
           os.chdir("DDoS-Ripper")
           os.system("python3 DRipper.py")


    else:
           main()

if __name__ == "__main__":
    main()
