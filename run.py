#primary imports
from datetime import datetime
from datetime import date
import time
import os
import sys
import winsound
import json
import urllib.request
from urllib.request import urlopen
from tkinter import filedialog
from tkinter import *

from import_pro import *
from paths_list import *


#################################
os.chdir(error_messages_path)   #
temp = open("import_error", 'r')#
import_error = temp.read()      #
temp.close()                    #
#################################


today = datetime.today()
#def encrypt(password):
#def decrypt(password):
def title():
    os.chdir(texts_path)
    title_file = open("title", 'r')
    title = title_file.read()
    title_file.close()
    return title
def playsound(frequency, duration):
    winsound.Beep(frequency, duration)
def version():
    os.chdir(patch_path)
    version_file = open("version", 'r')
    version = version_file.read()
    version_file.close()
    return version
def presentation():
    os.chdir(texts_path)
    presentation_file = open("presentation", 'r')
    presentation = presentation_file.read()
    presentation_file.close()
    return presentation
def patch_notes():
    os.chdir(patch_path)
    patch_notes_file = open("patch_notes", 'r')
    patch_notes = patch_notes_file.read()
    patch_notes_file.close()
    return patch_notes
def requirements_():
    os.chdir(texts_path)
    requirements_file = open("requirements", 'r')
    requirements = requirements_file.read()
    requirements_file.close()
    return requirements
def new_admin():
    os.chdir(admins_path)
    admin_name = input("Enter the username you want:")
    admin_pass = input("Enter the password you want:")
    os.mkdir("admin_account[" + admin_name + "]")
    os.chdir("admin_account[" + admin_name + "]")
    user = open("admin_name", 'w')
    user.write(admin_name)
    user.close()
    password = open("admin_password", 'w')
    password.write(admin_pass)
    password.close()
    if (encrypt('admin_password') == False):
        print("#ERROR#\nDue to the fact that the library needed for this process (cryptography)\n"
              "isn't installed, the password will not be encrypted, but the security of\n"
              "the personal information will be compromised.")
    return admin_name
def encrypt(file_name):
    requirements = requirements_status()
    if (requirements == True):
        key = Fernet.generate_key()
        mykey = open('mykey', 'wb')
        mykey.write(key)
        mykey.close()
        f = Fernet(key)
        original_file = open(file_name, 'rb')
        original = original_file.read()
        original_file.close()
        encrypted = f.encrypt(original)
        os.unlink(file_name)
        encrypted_file = open (f'enc_{file_name}', 'wb')
        encrypted_file.write(encrypted)
        encrypted_file.close()
        return True
    if (requirements == False):
        return False
def decrypt(file_name):
    mykey = open('mykey', 'rb')
    key = mykey.read()
    f = Fernet(key)
    encrypted_file = open(file_name, 'rb')
    encrypted = encrypted_file.read()
    encrypted_file.close()
    return (f.decrypt(encrypted))
    
        
def help():
    os.chdir(texts_path)
    help_file = open("help", 'r')
    help = help_file.read() #'help' variable may appear in a different color, but it's still a normal variable
    help_file.close()
    return(help)
def error(x):
    os.chdir(error_messages_path)
    temp = open(str(x), 'r')
    error = temp.read()
    temp.close()
    return error
def secure_pdf(path, file, password, final_path):
    parser = PdfFileWriter()
    os.chdir(path)
    pdf = PdfFileReader(file)
    os.chdir(final_path)
    #read
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    #encrypt
    parser.encrypt(password)
    #opens the file
    with open(f"encrypted_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print("> " + f"encrypted_{file} created <")
def sound_check():
    os.chdir(personalization_path)
    while True:
        try:
            temp = open('sound_check', 'r')
            sound_check = temp.read()
            temp.close()
            if (sound_check == 'true'):
                sound_check = True
            if (sound_check == 'false'):
                sound_check = False
            return sound_check
            break
        except:
            temp = open('sound_check', 'w')
            temp.write('true')
            temp.close()
            print("> file 'souncheck' was not found, it has now been created, try again <\n"
                  "if this message is printed more then once, see technical support")
def entry_sound_pro(): #(protocol)
    souncheck = sound_check()
    if (souncheck == True):
        playsound(500, 500)
        playsound(700, 500)
        playsound(1000, 500)
def exit_sound_pro(): #(protocol)
    souncheck = sound_check()
    if (souncheck == True):
        playsound(1000, 500)
        playsound(700, 500)
        playsound(500, 500)
def error_sound():
    souncheck = sound_check()
    if (souncheck == True):
        playsound(160, 500)
def activation_pro(): #(protocol)
    souncheck = sound_check()
    if (souncheck == True):
        playsound(700, 500)
def internet_check():
    host='http://google.com'
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False
def dir_GUI():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected


def login():
    ############################################
    def login_slf():#security level friendly
        os.chdir(last_access_path)
        last_user_file = open('last_user', 'r')
        last_user = last_user_file.read()
        last_user_file.close()
        #checking if the last user was an admin
        name_admin_dir = ("admin_account["+last_user+"]")
        user_admin_path = os.path.join(admins_path, name_admin_dir)
        os.chdir(user_admin_path)
        #getting username
        username_file = open("admin_name", 'r')
        username = username_file.read()
        username_file.close()
        print("welcome back, " + str(username) + ".                          ")
    #############################################

    os.chdir(data_path)
    security_lvl_file = open("security_level", 'r')
    security_lvl = security_lvl_file.read()
    security_lvl_file.close()
    print(">>> ", end='')

    if (security_lvl == 'friendly'):
        login_slf()
        
    if (security_lvl == 'medium'):
        print("enter your username:                             ", end="\r")
        while True:
            while True:
                username = input(">>> enter your username:")
                name_admin_dir = ("admin_account["+username+"]")
                user_admin_path = os.path.join(admins_path, name_admin_dir)
                try:
                    os.chdir(user_admin_path)
                    break
                except:
                    print("user not found.")
            username_file = open("admin_name", 'r')
            username_check = username_file.read()
            username_file.close()
            if (username == username_check):
                print("welcome back, "+username+".                          ")
                #change last_user to current one
                os.chdir(last_access_path)
                file = open("last_user", 'w')
                file.write(username)
                break
            else:
                print("<ERROR> " + error("error_3"))

    if (security_lvl == 'high'):
        print("enter your username:                             ", end="\r")
        while True:
            while True:
                username = input(">>> enter your username:")
                password = input(">>> enter the password:")
                name_admin_dir = ("admin_account["+username+"]")
                user_admin_path = os.path.join(admins_path, name_admin_dir)
                try:
                    os.chdir(user_admin_path)
                    break
                except:
                    print("<ERROR> " + error("error_4"))
            username_file = open("admin_name", 'r')
            username_check = username_file.read()
            username_file.close()
            password_check = str(decrypt("enc_admin_password"))
            password_final = ("b'"+password+"'")
            if ((username == username_check) and (password_final == password_check)):
                print("welcome back, "+username+".                          ")
                #change last_user to current one
                os.chdir(last_access_path)
                file = open("last_user", 'w')
                file.write(username)
                break
            else:
                print("<ERROR> " + error("error_4"))

def menu():
    while True:
        print(Fore.BLUE+"[MENU]>"+Style.RESET_ALL, end='')
        menu_input = input()
        #
        if ((menu_input == 'help') or (menu_input == 'h')):
            print(help())
        #
        if (menu_input == 'exit'):
            exit_sound_pro()
            break
        #
        if (menu_input == 'quit'):
            print(">the right command to exit the menu is 'exit'<")
        #
        if (menu_input == 'sec_lvl'):
            os.chdir(data_path)
            temp = open("security_level", 'r')
            sec_lvl = temp.read()
            print("the current security level is " + str(sec_lvl) + '.')
            print("to change it use the command 'chg_sec_lvl'")
        #
        if (menu_input == 'chg_sec_lvl'):
            print("enter the kind of security level you would like to use:\n"
                  "(1)friendly: it never asks for username or password, but it logs in with the last user used.\n"
                  "(2)medium: it asks for the username every time.\n"
                  "(3)high: it asks for username and password every time.")
            while True:
                sec_lvl = input(">")
                os.chdir(data_path)
                if (sec_lvl == '1'):
                    file = open("security_level", 'w')
                    file.write("friendly")
                    file.close()
                    print(">security level set as: friendly<")
                    activation_pro() #activation sound
                    break
                if (sec_lvl == '2'):
                    file = open("security_level", 'w')
                    file.write("medium")
                    file.close()
                    print(">security level set as: medium<")
                    activation_pro() #activation sound
                    break
                if (sec_lvl == '3'):
                    file = open("security_level", 'w')
                    file.write("high")
                    file.close()
                    print(">security level set as: high<")
                    activation_pro() #activation sound
                    break
        #
        if (menu_input == 'users_list'):
            os.chdir(users_path)
            temp = open("users_list", 'r')
            users_list = temp.readlines()
            for x in users_list:
                print(x, end="")
            print('')
            temp.close()
            
        #
        if (menu_input == 'new_admin'):
            new_admin()
            
        #
        if (menu_input == 'cmd'):
            os.chdir(programs_path)
            os.system('cmd.bat')
            
        #
        if (menu_input == "wi-fi_prof"):
            os.chdir(programs_path)
            os.system("wi_fi_profiles.bat")
            
        #
        if (menu_input == "wi-fi_profinfo"):
            print("< press 'ctrl + c' or type 'exit' to exit the program >")
            while True:
                try:
                    profile_name = input(">Enter the name of the profile:")
                    if (profile_name == 'exit'):
                        break
                    command = "netsh wlan show profile name=" + profile_name + " key=clear \npause"
                    os.chdir(programs_path)
                    file = open("wi_fi_profinfo.bat", 'w')
                    file.write(command)
                    file.close()
                    os.system("wi_fi_profinfo.bat")
                except:
                    break
            print('')
            
        #
        if ((menu_input == 'cpu') or (menu_input == 'CPU')):
            try:
                # cpu frequencies
                cpufreq = psutil.cpu_freq()
                # data structure
                table = [[("Physical Cores:"), (psutil.cpu_count(logical=False))],
                        [("Total Cores:"), (psutil.cpu_count(logical=True))],
                        [("Max Frequency:"), (f"{cpufreq.max:.2f}Mhz")],
                        [("Min Frequency:"), (f"{cpufreq.min:.2f}Mhz")],
                        [("Current Frequency:"), (f"{cpufreq.current:.2f}Mhz")]]
                print(tabulate(table))
                # CPU usage
                time.sleep(0.1)
                print("CPU usage per core:")
                for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                    print(f"Core {i}: {percentage}%")
                    time.sleep(0.1)
                print("< press 'ctrl + c' to interrupt the function >")
                print("< TOTAL CPU USAGE >")
                try:
                    while True:
                        today = datetime.today()
                        table = ("[" + str(today.time())+ " | " +
                                  str(psutil.cpu_percent())+"%]  ")
                        print(table, end="\r")
                        time.sleep(1)
                except:
                    print(">function interrupted<   ")

                
            except:
                print("<ERROR> " + error("error_5"))
                print(error("error_function_requirements"))
                print("- psutil\n"
                      "- tabulate")

        #
        if (menu_input == 'pdf_crypt'):
            requirements = requirements_status()
            if (requirements == True):
                while True:
                    path = input("Enter the path of the file's folder:")
                    if (path == 'exit'):
                        break
                    try:
                        os.chdir(path)
                        break
                    except:
                        print("> invalid path <")
                while True:
                    file = input("Enter the pdf file's name:")
                    if (file == 'exit'):
                        break
                    try:
                        temp = open(file, 'r')
                        temp.close()
                        break
                    except:
                        print("> file not found <")
                password = input("Enter the password with which you want to encrypt the file:")
                if (password == 'exit'):
                    break
                while True:
                    final_path = input("enter the path where you want the encrypted file saved:")
                    if (file_path == 'exit'):
                        break
                    try:
                        os.chdir(final_path)
                        break
                    except:
                        print("> invalid path <")
                try:
                    secure_pdf(path, file, password, final_path)
                except:
                    print(error("error_1"))
            if (requirements == False):
                print("<ERROR> " + error("error_5"))
                print(error("error_function_requirements"))
                print("- fpdf\n"
                      "- PyPDF2")
        #
        if ((menu_input == 'sound_on') or (menu_input == 'sound_ON')):
            os.chdir(personalization_path)
            temp = open("sound_check", 'w')
            temp.write("true")
            temp.close()
            print("< the sound is now [ON] >")
            activation_pro() #activation sound

        #
        if ((menu_input == 'sound_off') or (menu_input == 'sound_OFF')):
            os.chdir(personalization_path)
            temp = open("sound_check", 'w')
            temp.write("false")
            temp.close()
            print("< the sound is now [OFF] >")
            
        #
        if (menu_input == 'net_loc'):
            requirements = requirements_status()
            if (requirements == True):
                url = "http://ipinfo.io/json" # link to get json info
                try: #verifying if http://ipinfo.io/json is reachable
                    response = urlopen(url)
                    data = json.load(response)
                    table = [["IP Address:", data["ip"]],
                             ["Server:", data["org"]],
                             ["City:", data["city"]],
                             ["Country:", data["country"]],
                             ["Region:", data["region"]]]
                    print(tabulate(table))
                except:
                    print("< ERROR >\nAn error has occurred while extracting json data from 'http://ipinfo.io/json'.\n"
                          "Make sure you have an internet connection, otherwise it could be a problem of the source and\n"
                          "a maintenance may be happening. Try again later.")
            if (requirements == False):
                print("<ERROR> " + error("error_5"))
                print(error("error_function_requirements"))
                print("- tabulate")

        #
        if (menu_input == 'net_add'):
            requirements = requirements_status()
            if (requirements == True):
                class Network_Details(object):
                    def __init__(self):
                        self.parser = psutil.net_if_addrs()
                    def __repr__(self):
                        self.interfaces = []
                        self.address_ip = []
                        self.netmask_ip = []
                        self.broadcast_ip = []
                        for interface_name, interface_addresses in self.parser.items():
                            self.interfaces.append(interface_name)
                            for address in interface_addresses:
                                if str(address.family) == 'AddressFamily.AF_INET':
                                    self.address_ip.append(address.address)
                                    self.netmask_ip.append(address.netmask)
                                    self.broadcast_ip.append(address.broadcast)
                        data = {"interface" : [*self.interfaces],
                                "IP-address" : [*self.address_ip],
                                "Netmask" : [*self.netmask_ip],
                                "BroadCast-IP" : [*self.netmask_ip]}
                        return tabulate(data, headers="keys", tablefmt='github')
                if __name__=="__main__":
                    print("\n")
                    print(Network_Details())
                    print("\n")
        
            if (requirements == False):
                print("<ERROR> " + error("error_5"))
                print(error("error_function_requirements"))
                print("- tabulate\n"
                        "- psutil\n")

        #
        if (menu_input == 'net_ver'):
            print('internet:', Fore.GREEN+"[CONNECTED]"+Style.RESET_ALL if internet_check()==True else Fore.RED+"[NOT CONNECTED]"+Style.RESET_ALL)

        #
        if (menu_input == 'net_spd'):
            requirements = requirements_status()
            internet = internet_check()
            print(">>> checking internet connection...", end="\r")
            time.sleep(0.3)
            if (internet == True):
                print(">>> checking internet connection... "+Fore.GREEN+"[CONNECTED]"+Style.RESET_ALL, end="\r")
                time.sleep(0.3)
                if (requirements == True):
                    class Network_Details(object):
                        def __init__(self):
                            self.tester = psutil.net_if_addrs()
                            self.speed = speedtest.Speedtest()
                            self.interface = self.interfaces()[0]
                            print(">>> getting download speed...                               ", end="\r")
                            self.download_speed = self.speeds()["download"]
                            print(">>> getting download speed... [DONE]                         ", end="\r")
                            time.sleep(0.3)
                            print(">>> getting upload speed...                                 ", end="\r")
                            self.upload_speed = self.speeds()["upload"]
                            print(">>> getting upload speed... [DONE]                           ", end="\r")
                            time.sleep(0.3)
                            
                        def __str__(self):
                            data = {"Interface:" : [self.interface],
                                    "Download:" : [str(self.download_speed) + " Mbps"],
                                    "Upload:" : [str(self.upload_speed) + " Mbps"]}
                            table = tabulate(data, headers="keys", tablefmt="pretty")
                            return str(table)
                        def interfaces(self):
                            interfaces = []
                            for interface_name, _ in self.tester.items():
                                interfaces.append(str(interface_name))
                                return interfaces
                        def speeds(self):
                            download_speed = round(self.speed.download() / 1_000_000, 2)
                            upload_speed = round(self.speed.upload() / 1_000_000, 2)
                            return {"download": download_speed, "upload": upload_speed}
                    if __name__=="__main__":
                        print(Network_Details())
  
                if (requirements == False):
                    print("<ERROR> " + error("error_5"))
                    print(error("error_function_requirements"))
                    print("- tabulate\n"
                          "- psutil\n"
                          "- speedtest-cli\n")
            if (internet == False):
                print(">>> checking internet connection... "+Fore.RED+"[NOT CONNECTED]"+Style.RESET_ALL, end="\r")
                time.sleep(0.5)
                print("#ERROR#                                            \n" + error("internet_error"))

        #
        if (menu_input == 'clock'):
            try:
                while True:
                    now = datetime.now()
                    print(now.strftime("%H:%M:%S"),end="\r")
                    time.sleep(1)
            except:
                print("")

        #
        if (menu_input == 'clear'):
            os.system('cls')

        #
        if (menu_input == 'phonfo'):
            def number_scanner(phone_number):
                number = phonenumbers.parse(phone_number)
                description = geocoder.description_for_number(number, "it")
                print(description)
                supplier = carrier.name_for_number(number, "it")
                info = [["Country", "Supplier"],
                        [description, supplier]]
                data = str(tabulate(info, headers="firstrow", tablefmt="github"))
                return data
            while __name__=="__main__":
                try:
                    number = input("Enter Number (with the prefix and a '+'):")
                    print(number_scanner(number))
                    print("\n")
                except:
                    print("\n")
                    break
        #
        if (menu_input == "yt_dl"):
            while True:
                try:
                    url = input("url>")
                    data = YouTube(url)
                    video = data.streams.get_highest_resolution()
                    download_dir = dir_GUI()
                    try:
                        video.download(download_dir)
                        print("> downloaded succesfully <")
                    except:
                        print("> download failed <")
                    break
                except:
                    if ((url == 'exit') or (url == '')):
                        break
                        break
                    else:
                        print("> url not valid <")
                
                
def main():        
    def first_time_check():
        os.chdir(data_path)
        try:
            file = open('first_time_check', 'r')
            file.close()
            first_time = False
        except:
            first_time = True
            file = open('first_time_check', 'w')
            file.close()
        return first_time
    def first_time_protocol():
        print('')
        pres = presentation()
        print(pres)
        p_notes = patch_notes()
        print(">latest patch notes<\n" + p_notes)
        print("it's now time to create an admin account")
        admin_name = (new_admin())
        os.chdir(last_access_path)
        file = open('last_user', 'w')
        file.write(admin_name)
        time.sleep(0.5)
        print("<the new account has been created succesfully!>")
        #writing user name in new winton/data/users/users_list
        os.chdir(users_path)
        temp = open('users_list', 'a')
        temp.write(admin_name + '\n')
        time.sleep(0.5)
        print("enter the kind of security level you would like to use:\n"
              "(as everything, you'll be able to change it from the menu)\n\n"
              "(1)friendly: it never asks for username or password, but it logs in with the last user used.\n"
              "(2)medium: it asks for the username every time.\n"
              "(3)high: it asks for username and password every time.")
        while True:
            sec_lvl = input(">")
            os.chdir(data_path)
            file = open("security_level", 'w')
            if (sec_lvl == '1'):
                print(">security level set as: friendly<")
                file.write("friendly")
                file.close
                break
            if (sec_lvl == '2'):
                print(">security level set as: medium<")
                file.write("medium")
                file.close
                break
            if (sec_lvl == '3'):
                print(">security level set as: high<")
                file.write("high")
                file.close
                break
        requirements = requirements_status()
        if (requirements == False):
            print("To have your version of Winston runnin without bugs at with the maximum of the funcionalities,"
                  "make sure to have downloaded on your system or virtual environment the latest versions of the"
                  "following libraries.")
            print(">requirements needed<\n", requirements_())
            print(">requirements yet to install<")
            if (psutil_lib == False):
                print("- psutil")
            if (fpdf_lib == False):
                print("- fpdf")
            if (PyPDF2_lib == False):
                print("- PyPDF2")
            if (tabulate_lib == False):
                print("- tabulate")
            if (speedtest_lib == False):
                print("- speedtest-cli")
            if (cryptography_lib == False):
                print("- cryptography")
            if (phonenumbers_lib == False):
                print("- phonenumbers")
            if (colorama_lib == False):
                print("- colorama")
            if (pytube_lib == False):
                print("- pytube")
            print("")
    
    def existence_check_pro(): #(protocol)
    # this protocol checks if every file or directory that is necessary
    # for the correct working of winston exists.
        def dir_check():
            def check(dir):
                try:
                    os.chdir(dir)
                    return True
                except:
                    return False
            if (check(error_messages_path) == False):
                print("#ERROR# 'error_messages' directory not found")
                return False
            
            if (check(patch_path) == False):
                print("#ERROR# 'patch' directory not found\n")
                return False
            
            if (check(personalization_path) == False):
                print("#ERROR# 'personalization' directory not found")
                return False
        
            if (check(programs_path) == False):
                print("#ERROR# 'programs' directory not found")
                return False
        
            if (check(texts_path) == False):
                print("#ERROR# 'texts' directory not found")
                return False

            if (check(users_path) == False):
                print("#ERROR# 'users' directory not found")
                return False
            else:
                return True
                
        if (dir_check() == False):
            return False
        if (dir_check() == True):
            return True

    def main_check_pro(): #(protocol)
        print(">>> checking directiories existence...                  ", end="\r")
        time.sleep(0.5)
        if(existence_check_pro() == True):
            print(">>> checking directiories existence..."+Fore.GREEN+"[SUCCESS]     "+Style.RESET_ALL, end="\r")
            time.sleep(0.3)
        elif(existence_check_pro() == False):
            print(">>> checking directiories existence..."+Fore.RED+"[FAILED]      "+Style.RESET_ALL, end="\r")
            error_sound()
            time.sleep(1)

    def import_check_pro(): #(protocol)
        print(">>> checking imports status...                          ", end="\r")
        time.sleep(0.5)
        stat = requirements_status()
        if(stat == True):
            print(">>> checking imports status..."+Fore.GREEN+"[SUCCESS]             "+Style.RESET_ALL, end="\r")
            time.sleep(0.3)
        elif(stat == False):
            print(">>> checking imports status..."+Fore.RED+"[FAILED]              "+Style.RESET_ALL, end="\r")
            error_sound()
            time.sleep(1)
            # prints the requirements needed in the eventuality that one or more aren't installed
            print(import_error)
            time.sleep(1)
            print(">requirements<")
            if (psutil_lib == False):
                print("- psutil")
            if (fpdf_lib == False):
                print("- fpdf")
            if (PyPDF2_lib == False):
                print("- PyPDF2")
            if (tabulate_lib == False):
                print("- tabulate")
            if (speedtest_lib == False):
                print("- speedtest-cli")
            if (cryptography_lib == False):
                print("- cryptography")
            if (phonenumbers_lib == False):
                print("- phonenumbers")
            if (colorama_lib == False):
                print("- colorama")
            if (pytube_lib == False):
                print("- pytube")
            print("")

    first_time = first_time_check()
    if (first_time == True):
        first_time_protocol()
        import_check_pro()
        main_check_pro()
        login()
        entry_sound_pro()
        menu()
    if (first_time == False):
        import_check_pro()
        main_check_pro()
        login()
        entry_sound_pro()
        menu()

    
if __name__=="__main__":
    #######
    init()# need this to use colorama
    #######
    title_screen = title()
    version_number = version()
    print(Fore.MAGENTA+title_screen+Style.RESET_ALL)
    time.sleep(0.5)
    print("WINSTON™team 2019-"+str(today.year)+"     version -- " + version_number)
    time.sleep(0.1)
    print('\ninternet:', Fore.GREEN+"[CONNECTED]"+Style.RESET_ALL if internet_check()==True else Fore.RED+"[NOT CONNECTED]"+Style.RESET_ALL)
    time.sleep(0.1)
    now = datetime.now()
    today = date.today()
    print(""+now.strftime("%H:%M:%S") + ' | ' + str(today))
    time.sleep(0.1)
    time.sleep(0.3)
    main()