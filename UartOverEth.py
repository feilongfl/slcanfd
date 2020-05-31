#!/usr/bin/env python3
#coding = utf-8
'''
@Author: feilong
@LastEditors: feilong
@Description: 
@email: feilongphone@gmail.com
'''
 
import pty
import os
import select
import socket
import argparse

def mkpty(ip, port):
    uart, tty = pty.openpty()
    uartname = os.ttyname(tty)
    print (uartname)
    s = socket.socket()
    s.bind((ip, port))
    s.listen(5)
    return uart, s

def main(): 
    uart, s = mkpty('127.0.0.1',8891)
    r_list = [uart, s]
    while True:
        rl, wl, el = select.select(r_list, [], [], 1)
        for master in rl:
            # uart
            if master == uart: 
                data = os.read(master, 128)
                for c in r_list:
                    if c != uart and c!= s:
                        c.sendall(data)
                        pass
            #socket
            elif master == s:
                conn, addr = master.accept()
                r_list.append(conn)
                data = conn.recv(128)
                os.write(uart, data)
            #socket
            else:
                try:
                    data = master.recv(128)
                    os.write(uart, data)
                except ConnectionAbortedError:
                    r_list.remove(master)
                    

if __name__ == "__main__":
    main()
    