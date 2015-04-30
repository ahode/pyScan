#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
import socket
import subprocess
import sys
from datetime import datetime

root = Tk()
def submit():
    port1 = int(port.get())
    if port1==0:
        PortRangeScan()    
    else:
        singlePortscan()
        
def singlePortscan():
    port1 = int(port.get())
    host1 = str(host.get())
    remoteServerIP  = socket.gethostbyname(host1)
    l1r = ttk.Label(root, text = 'Scanning host %s at port ' %remoteServerIP).grid(row = 5, column = 0, columnspan = 2)
    t1 = datetime.now()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServerIP, port1))
    if result == 0:
        l2r = ttk.Label(root, text = 'port %s open' %port1).grid(row = 6, column = 0, columnspan = 2)
    else:
        l2r = ttk.Label(root, text = 'port %s closed' %port1).grid(row =6, column = 0, columnspan = 2)
    sock.close()
    t2 = datetime.now()
    total =  t2 - t1
    l3r = ttk.Label(root, text = 'scan completed in %s: ' %total).grid(row =7, column = 0, columnspan = 2)

def PortRangeScan():
    host1 = str(host.get())
    remoteServerIP  = socket.gethostbyname(host1)
    lr0 = ttk.Label(root, text ='scanning host %s for ports in range 0 to 1024' %remoteServerIP).grid(row = 5, column = 0, columnspan = 2)
    for port2 in range(20, 26):
        for r in range(6, 15):            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            resultr = sock.connect_ex((remoteServerIP, port2))
            if resultr == 0:
                lr1= Label(root, text = 'Port %s Open' %port2).grid(row = 6, column = 0, columnspan = 2)
            sock.close()
        lr2 =ttk.Label(root, text = 'scan completed in ...').grid(row = 7, column = 0, columnspan = 2)
    
  
    
    
root.config(padx = 10, pady = 10)
root.title('pyScan ~ PORT SCANNER')
host = StringVar()
port = StringVar()

logo = ttk.Label(root, text = 'pyScan', font = ('courier', 18, 'bold')).grid(row = 0, column = 0)

label1 = ttk.Label(root, text = 'Hostname/IP : ').grid(row = 1, column = 0)
entry1 = ttk.Entry(root, width = 40, textvariable = host)
entry1.grid(row = 1, column = 1)
label2 = ttk.Label(root, text = 'Port : ').grid(row = 2, column = 0)
entry2 = ttk.Entry(root, width = 40, textvariable = port)
entry2.insert(0, 0)
entry2.grid(row = 2, column = 1)
button = ttk.Button(root, text = 'START SCAN' , width = 20, command = submit).grid(row = 4, column = 1)

root.mainloop()
