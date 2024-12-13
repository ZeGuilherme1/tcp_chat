import os
import platform


def client_side_title():
    print(ascii)
    print(" " * 10, "Client-side\n", " " * 10)
    print("https://github.com/ZeGuilherme1\n")

def server_side_title():
    print(ascii)
    print(" " * 10, "Server-side\n", " " * 10)
    print("https://github.com/ZeGuilherme1\n")

def clean_terminal():
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

with open("tcp_chat.txt", "r", encoding="utf-8") as title:
    ascii = title.read()




