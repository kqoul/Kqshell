import os
import subprocess
import startup
import sys
import verdata
import getpass
import readline
from commands import help, calc, about, pwd, whoami, aboutv, abouth, abouti, about, ls, exit, ihatekqoul, iluvkqoul, xdg_session, xdg_session_desktop, shell_diplay_wayland, shell_diplay_x11, shell_home, shell_path, shell_primary_shell, shell_user, xdg_desktop, browser, title_window, kqshell_distro, kqshell_kernel_info, ff_kitty, whatsnew, build_nixos, OS
with open ("/sys/devices/virtual/dmi/id/product_name") as f:
    product_code = f.read().strip()



def welcome():
       startup.startup_programs()
       print("'help' for command list")
       main()

def main():
    while True:
         #try:
            title_window()
            user_loaction = os.getcwd()
            username = getpass.getuser()
            user_input = f"{username}@{product_code}{user_loaction}> "
            user_input_helper = input(user_input)
            user_input_splitter = user_input_helper.split()
            try:
                command = user_input_splitter[0]
                arg = user_input_splitter[1:]
            except IndexError:
                continue
            def cd(arg):
                try:
                    os.chdir(os.path.expanduser(arg[0]))
                    title_window()
                    return
                except:
                     print("No such file or directory!")
            def mkdir(arg):
                 os.mkdir(arg[0])
                 return
            def echo(arg):
                 print(" ".join(arg[0:]))
                 
                 return
            
            def pkg(arg):
               #try:
               osinfo = " ".join(arg)
               if osinfo == "nixos":
                    subprocess.run("nix-store -q --references /run/current-system/sw | cut -d- -f2-")
               elif osinfo == "arch":
                    pkg = [
          "sudo", "pacman", "-Qs",
          ]
                    subprocess.run(pkg)    
                    return
               #except 
            commands = {
                 "help": help,
                 "calc": calc,
                 "about":about,
                 "pwd": pwd,
                 "whoami": whoami,
                 "aboutv": aboutv,
                 #"abouth":abouth,
                 "abouti": abouti,
                 "about": about,
                 "ls": ls,
                 "exit": exit,
                 "cd": cd,
                 "mkdir": mkdir,
                 "echo": echo,
                 "ihatekqoul": ihatekqoul,
                 "iluvkqoul": iluvkqoul,
                 "kqshell.xdg.session": xdg_session,
                 #works
                 "kqshell.xdg.desktop.session": xdg_session_desktop,
                 #works
                 "kqshell.shell.display.wayland": shell_diplay_wayland,
                 #works
                 "kqshell.xdg.desktop": xdg_desktop,
                 #works
                 "kqshell.shell.display.x11": shell_diplay_x11,
                 #dont know if it works i am on wayland
                 "kqshell.shell.home": shell_home,
                 #works
                 "kqshell.shell.path": shell_path,
                 #works
                 "kqshell.primary.shell": shell_primary_shell,
                 #works
                 "kqshell.shell.user": shell_user,
                 #works
                 "browser": browser,
                 "kqshell.kernel.ver":kqshell_kernel_info,
                 "kqshell.kernel.distro":kqshell_distro,
                 "ff": ff_kitty,
                 "whatsnew":whatsnew,
                 "pkg": pkg,
                 #"build-nixos":build_nixos
                 #nixos build command sucks and crashes the whole fucking shell
                 "kqshell.sysinfo":OS,
               

                 
                 
            
            }
            
            if command in commands:
                 commands[command](arg)
            else:
                 try:
                    sub_arg = [command] + arg
                    subprocess.run(sub_arg)

                    main()
                 except:
                    print("No such program or command!")
                    main()


           
                 

                 
         #except :
          #   print("invalid syntax")



welcome()


            
                