#!/usr/bin/env python3

import os

print("Copying Grub File...")
os.system("sudo cp grub /etc/default/grub")

print("Runing grub-mkconfig...")
os.system("grub-mkconfig -o /boot/grub/grub.cfg")

print("Setting up archlinux-keyring...")
os.system("sudo acman -Sy archlinux-keyring")

print("Copying pacman.conf...")
os.system("sudo cp pacman.conf /etc/")

print("Updating System...")
os.system("sudo pacman -Su")

print("Copying .Xresources file to $HOME ...")
os.system("sudo cp .Xresources $HOME")

print("Updating .Xresources file for correct screen sizing on 5k monitor...")
os.system("xrdb -merge ~/.Xresources")
