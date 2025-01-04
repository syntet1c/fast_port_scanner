import socket
import multiprocessing
import argparse
import pyfiglet

f = pyfiglet.figlet_format("Syntetic", font="slant")
print(f)

def arguments():
    args = argparse.ArgumentParser()
    args.add_argument("-t", "--target", dest="target", help="Your target, eg. example.com")
    args.add_argument("-p", "--ports", dest="port", help="port range, eg. -p 1-1024")
    argument = args.parse_args()
    port = str(argument.port).split("-")
    port = range(int(port[0]), int(port[1]))
    
    return [argument.target, port]

h = socket.gethostbyname(arguments()[0])
def scann_port(port):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    
    r = s.connect_ex((h, port))
    if r == 0:
        print(f"Port Open: {port}")
    s.close()

with multiprocessing.Pool(processes=70) as p:
    p.map(scann_port, arguments()[1])
