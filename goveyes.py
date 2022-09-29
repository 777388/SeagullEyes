import threading
import signal
import sys
import os
print("Usage Python3 goveyes.py /url/here")
print("Require dnsutils, sudo apt install dnsutils, or wsl apt install dnsutils")
print("requires GAU")
def sigint_handler(signal, frame):
    print("Unlocked from dimensional trace")
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
        print("website: "+website+"; "+rootserver1+"---------"+rootserver2+"  provide different answers")
    else:
        print("website: "+website+"; "+rootserver1+"---------"+rootserver2+"  provide the same answer")

def threads(ip):
    t0 = threading.Thread(target=check, args=(ip,"13.227.74.97",sys.argv[1]))
    t1 = threading.Thread(target=check, args=(ip,"104.125.44.111",sys.argv[1]))
    t2 = threading.Thread(target=check, args=(ip,"65.116.218.50",sys.argv[1]))
    t3 = threading.Thread(target=check, args=(ip,"104.16.149.244",sys.argv[1]))
    t4 = threading.Thread(target=check, args=(ip,"23.59.195.36",sys.argv[1]))
    t5 = threading.Thread(target=check, args=(ip,"192.0.66.168",sys.argv[1]))
    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t0.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
if __name__ =="__main__":
    ips = ["13.227.74.97", "104.125.44.111", "65.116.218.50", "104.16.149.244", "23.59.195.36", "192.0.66.168"]
    ipf = ["0.DOE", "1.DOD", "2.ARMY", "3.FBI", "4.CIA", "5.White House"]
    for i in range(6):
        print("Choice"+str(i)+" :"+str(ips[i]))
        print(str(ipf[i]))
    for ipd in ips: 
        threads(ipd)

    print("Which gov server dimension would you like to be in? pick 0 through 5")
    x = input()
    while True:
        os.popen("wsl dig +trace "+str(ips[int(x)])).read()
        print("Connected to:"+str(ips[int(x)])+"  "+str(ipf[int(x)]), end="\r", flush=True)
