import threading
import signal
import sys
import os
print("Usage Python3 seagulleyes.py /url/here")
print("Requires GAU,  https://github.com/lc/gau")
print("Require dnsutils, sudo apt install dnsutils, or wsl apt install dnsutils")
print("If running on linux, be sure to remove all instances of wsl in the code")
def sigint_handler(signal, frame):
    print("Unlocked from dimensional connection")
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

def opener(rootserver, website):
    os.popen("wsl dig +trace "+rootserver).read()
    this = os.popen("wsl gau "+website+" 2>&1").read()
    return this

def check(rootserver1, rootserver2, website):
    a = opener(rootserver1, website)
    b = opener(rootserver2, website)
    if a == b:
        print("website: "+website+"; "+rootserver1+"---------"+rootserver2+"  are in different dimensions")
    else:
        print("website: "+website+"; "+rootserver1+"---------"+rootserver2+"  are in the same dimension")

def threads(ip):
    t0 = threading.Thread(target=check, args=(ip,"198.41.0.4",sys.argv[1]))
    t1 = threading.Thread(target=check, args=(ip,"199.9.14.201",sys.argv[1]))
    t2 = threading.Thread(target=check, args=(ip,"192.33.4.12",sys.argv[1]))
    t3 = threading.Thread(target=check, args=(ip,"199.7.91.13",sys.argv[1]))
    t4 = threading.Thread(target=check, args=(ip,"192.203.230",sys.argv[1]))
    t5 = threading.Thread(target=check, args=(ip,"192.5.5.241",sys.argv[1]))
    t6 = threading.Thread(target=check, args=(ip,"192.112.36.4",sys.argv[1]))
    t7 = threading.Thread(target=check, args=(ip,"198.97.190.53",sys.argv[1]))
    t8 = threading.Thread(target=check, args=(ip,"192.36.148.17",sys.argv[1]))
    t9 = threading.Thread(target=check, args=(ip,"192.58.128.30",sys.argv[1]))
    t10 = threading.Thread(target=check, args=(ip,"193.0.14.129",sys.argv[1]))
    t11 = threading.Thread(target=check, args=(ip,"199.7.83.42",sys.argv[1]))
    t12 = threading.Thread(target=check, args=(ip,"202.12.27.33",sys.argv[1]))
    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t0.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
if __name__ =="__main__":
    ips = ["198.41.0.4", "199.9.14.201", "192.33.4.12", "199.7.91.13", "192.203.230", "192.5.5.241", "192.112.36.4", "198.97.190.53", "192.36.148.17", "192.58.128.30", "193.0.14.129", "199.7.83.42", "202.12.27.33"]
    for i in range(13):
        print("Choice"+str(i)+" :"+str(ips[i]))
    for ipd in ips: 
        threads(ipd)

    print("Which dimension would you like to be in? pick 0 through 12")
    x = input()
    while True:
        os.popen("wsl dig +trace "+str(ips[x])).read()
        print("Connected to:"+str(ips[x]), end="\r", flush=True)

