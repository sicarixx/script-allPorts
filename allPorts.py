#!/usr/bin/python3
# Created by F1neg4n

import os

def welcome():
    welc = 'NMAP Port Scanner'
    info = '[INFO] Python script with NMAP to scan ports'
    os.system('clear')
    print(welc + '\n' + '*' * len(welc))
    print(info + '\n' + '-' * len(info))
    return

def getAddress():
    welcome()
    try:
        ipAddress = input('[+] Enter the IP Address: ')
        while(ipAddress == ''):
            ipAddress = input('[+] Please, enter the IP Address: ')
    except(KeyboardInterrupt):
        os.system('clear')
        welcome()
        print('[-] Interrupted by user!')
        exit()
    return ipAddress

def newScann():
    host = getAddress()
    try:
        print('[+] Scanning open ports: ' + host)
        print('-' * 44)
        scann = os.system('sudo nmap -p- -sS --min-rate 5000 --open -vvv -n -Pn ' + host + ' -oG allPorts')
        print('-' * 23)
        print('[+] Check file allPorts')
        print('-' * 23)
    except(KeyboardInterrupt):
        os.system('clear')
        welcome()
        print('[-] Interrupted by user!')
        exit()
    return scann

if __name__ == '__main__':
    newScann()
