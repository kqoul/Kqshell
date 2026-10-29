
import verdata
import banner
def help(arg):
        print(banner.help_banner)
        return

def calc(arg):
    try:
        user_input_n1 = input("Number 1: ")
        user_input_n1_helper = float(user_input_n1)
        user_input_n2 = input("Number 2: ")
        user_input_n2_helper = float(user_input_n2)

        user_input_oper = input("operation (+,-,/,*): ")

        if user_input_oper == "+":
            result = user_input_n1_helper + user_input_n2_helper
            print (result)
            return
        elif user_input_oper == "*":
            result = user_input_n1_helper * user_input_n2_helper
            print(result)
            return
        elif user_input_oper == "/":
            result = user_input_n1_helper / user_input_n2_helper
            print(result)
            return
        elif user_input_oper == "-":
            result = user_input_n1_helper - user_input_n2_helper
            print(result)
            return
        else:
            print("Invalid Operation!")
            return
    except:
        print("invalid syntax!")

def kqshell_kernel_info(arg):
    kernel = os.uname().release
    print("Kernel version:",kernel)

def kqshell_distro(arg):
    with open ("/etc/os-release") as f:
        os_info = dict(
            line.strip().split("=", 1)
            for line in f
            if "=" in line

        )
    distro = os_info.get("PRETTY_NAME","Unknown").strip('"')
    print("Distro:",distro)

def about(arg):
    kernel = os.uname().release
    with open ("/etc/os-release") as f:
        os_info = dict(
            line.strip().split("=", 1)
            for line in f
            if "=" in line

        )
    distro = os_info.get("PRETTY_NAME","Unknown").strip('"')

    print ("kqshell Version :", verdata.ver ,"Kernel version:" ,kernel,"Distro:",distro,",shell Made with love by kqoul!")
    return

import os
def pwd(arg):
    print(os.getcwd())
    return

import getpass
product_code = ""
with open("/sys/devices/virtual/dmi/id/product_name") as f:
    product_code = f.read().strip()
def whoami(arg):
    print(f"{getpass.getuser()}@{product_code}")
    return

def aboutv(arg):
    print(verdata.ver)
    return

def abouti(arg):
    print("""
Shell: kqshell
langage: python
shell ver:
""", verdata.ver)
    return

def abouth(arg):
    print("""
about -> Check basic info
aboutv -> check only version number
abouti -> Prints more advanced info
abouth -> prints this text
""")
    return

def ls(arg):
    print(os.listdir())

import sys
def exit(arg):
    print("exiting...")
    sys.exit()

def ihatekqoul(arg):
    print("me too haha")
    return
def iluvkqoul(arg):
    print("me too lmao")
    return

def xdg_session(arg):
    print(os.environ.get("XDG_SESSION_TYPE"))
    return
def xdg_desktop(arg):
    print(os.environ.get("XDG_CURRENT_DESKTOP"))
    return
def xdg_session_desktop(arg):
    print(os.environ.get("XDG_SESSION_DESKTOP"))
    return
def shell_home(arg):
    print(os.environ.get("HOME"))
    return

def shell_user(arg):
    print(os.environ.get("USER"))
    return
def shell_primary_shell(arg):
    print(os.environ.get("SHELL"))
    return

def shell_path(arg):
    print(os.environ.get("PATH"))
    return

def shell_diplay_x11(arg):
    print(os.environ.get("DISPLAY"))
    return
def shell_diplay_wayland(arg):
    print(os.environ.get("WAYLAND_DISPLAY"))
    return
import webbrowser
def browser(arg):
    query = " ".join(arg)

    if query.startswith("http://") or query.startswith("https://") or query.startswith("www."):
        print("Opening URL:", query)
        webbrowser.open(query)
        print("back")
        return
    elif "." in query and " " not in query:
        print("Opening URL:", "http://" + query)
        webbrowser.open("http://" + query)
        return
    else:
        url = "https://www.google.com/search?q=" + query.replace(" ", "+")
        print("Searching Google for:", query)
        webbrowser.open(url)
        return
with open ("/sys/devices/virtual/dmi/id/product_name") as f:
    product_code = f.read().strip()

def title_window():
     while True:
          cwd = os.getcwd()
          print(f"\033]0;kqshell.V{verdata.ver}-{product_code}@{cwd}\007", end="", flush=True)
          return


import subprocess

def ff_kitty(arg):
    ff_kitty = [
        "fastfetch","--logo-type","kitty"
    ]
    subprocess.run(ff_kitty)
    return

def whatsnew(arg):
    print(banner.whats_new_banner)


def build_nixos(arg):
    subprocess.run("cd /etc/nixos/")
    subprocess.run("sudo nixos-rebuild switch --flake /etc/nixos#$(hostname)")

import platform
def OS(arg):
    info = platform.uname()
    print(f"OS:{info.system}")
    print(f"OS release{info.release}")
