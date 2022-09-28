import threading
import signal
import sys
import os
print("Usage Python3 blackeyes.py /url/here")
print("Require dnsutils, sudo apt install dnsutils, or wsl apt install dnsutils")
print("requires GAU")
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
        print("website: "+website+"; "+rootserver1+"---------"+rootserver2+"  provide different answers")
    else:
        print("website: "+website+"; "+rootserver1+"---------"+rootserver2+"  provide the same answer")

def threads(ip):
    t0 = threading.Thread(target=check, args=(ip,"192.175.48.6",sys.argv[1]))
    t1 = threading.Thread(target=check, args=(ip,"192.175.48.42",sys.argv[1]))
    t2 = threading.Thread(target=check, args=(ip,"192.175.48.1",sys.argv[1]))
    t0.start()
    t1.start()
    t2.start()
    t0.join()
    t1.join()
    t2.join()
if __name__ =="__main__":
    ips = ["192.175.48.6", "192.175.48.42", "192.175.48.1"]
    for i in range(3):
        print("Choice"+str(i)+" :"+str(ips[i]))
    for ipd in ips: 
        threads(ipd)

    print("Which blackhole server dimension would you like to be in? pick 0 through 2")
    x = input()
    while True:
        os.popen("dig +trace "+str(ips[x])).read()
        print("Connected to:"+str(ips[x]), end="\r", flush=True)
