#!/usr/bin/env python3

##
# Script installs all of the dotfiles that I use into $HOME/.config/dotfiles folder.
##

import os

# Path variables
#
config_dir_path     = "$HOME/.config"
dotfile_dir_path    = config_dir_path  + "/dotfiles"
avim_dir_path       = config_dir_path  + "/nvim"
avim_user_path      = config_dir_path  + "/nvim/lua/user"
bspwm_config_path   = config_dir_path + "/bspwm"
sxhkd_config_path   = config_dir_path + "/sxhkd"
polybar_config_path = config_dir_path + "/polybar"
font_dir_path       = "$HOME/.fonts"

repo_config_path    = "configs"

# Symlink paths
#
zsh_dir_path     = dotfile_dir_path + "/zsh"
vim_dir_path     = dotfile_dir_path + "/vim"
nvim_dir_path    = dotfile_dir_path + "/nvim"

# Helper functions
#
def new_line():
    print("--\n")

def create_dir(dir):
    print("Creating folder:  {}...".format(dir))
    os.system("mkdir -p {}".format(dir))

def copy_file(src, dest):
    print("Copying {} to {}".format(src,dest))
    os.system("cp -r {} {}".format(src,dest))

def clone_repo(repo, dest):
    print("Git cloning {} to {}".format(repo,dest))
    os.system("git clone {} {}".format(repo,dest))

def create_symlink(src, dest):
    print("Creating symlink {} to {}".format(src,dest))
    os.system("ln -s -f {} {}".format(src,dest))

def remove(file):
    if os.path.exists(file):
        print("Removing {} \n".format(file))
        os.system("sudo rm -rf {}".format(file))
    else:
        print("{} not found, moving on.\n".format(file))
        new_line()


def install_configs():
    print("Installing dotfiles...")
    # Setup config files
    #
    create_dir(dotfile_dir_path)

    # ZSH
    #
    create_dir(zsh_dir_path)
    copy_file(".zshrc",    zsh_dir_path)
    copy_file("aliases",   zsh_dir_path)
    copy_file("variables", zsh_dir_path)
    create_symlink(zsh_dir_path + "/.zshrc", "$HOME/.zshrc")
    new_line()

    # VIM
    #
    create_dir(vim_dir_path)
    clone_repo("git@github.com:lukehayes/VimConfig.git", vim_dir_path)
    create_symlink(vim_dir_path + "/init.vim", "$HOME/.vimrc")
    new_line()

    # ASTRONVIM
    #
    clone_repo("https://github.com/AstroNvim/AstroNvim", "~/.config/nvim")
    create_dir(avim_user_path)
    create_symlink(avim_dir_path + "/init.lua", avim_user_path + "/init.lua")
    new_line()

    # NEOVIM
    #
    create_dir(nvim_dir_path)
    clone_repo("git@github.com:lukehayes/AstroNvimConfig.git", nvim_dir_path)
    new_line()

    # FONTS
    #
    create_dir(font_dir_path)
    copy_file("fonts/JetBrainsMono", font_dir_path)
    copy_file("fonts/ShareTech",     font_dir_path)
    new_line()

    # BSPWM
    #
    create_dir(bspwm_config_path)
    create_dir(bspwm_config_path + "/scripts")
    copy_file(repo_config_path + "/bspwm", dotfile_dir_path)
    create_symlink(dotfile_dir_path + "/bspwm/bspwmrc", bspwm_config_path + "/bspwmrc" )
    create_symlink(dotfile_dir_path + "/bspwm/keybindings", bspwm_config_path + "/keybindings" )
    create_symlink(dotfile_dir_path + "/bspwm/scripts/keybindings_rofi.sh", bspwm_config_path + "/scripts/keybindings_rofi.sh" )
    new_line()
    
    # SXHKD
    #
    create_dir(sxhkd_config_path)
    copy_file(repo_config_path + "/sxhkd", dotfile_dir_path)
    create_symlink(dotfile_dir_path + "/sxhkd/sxhkdrc", sxhkd_config_path + "/sxhkdrc" )
    new_line()

    # POLYBAR
    #
    create_dir(polybar_config_path)
    copy_file(repo_config_path + "/polybar", dotfile_dir_path)
    create_symlink(dotfile_dir_path + "/polybar/config.ini", polybar_config_path + "/config.ini" )
    create_symlink(dotfile_dir_path + "/polybar/launch.sh",  polybar_config_path + "/launch.sh" )
    new_line()

    # WALLPAPERS
    #
    copy_file("wallpapers", dotfile_dir_path)
    new_line()

    # Rofi
    #
    folder = "/rofi"
    copy_file(repo_config_path + folder, config_dir_path)

    # ASEPRITE COLOR PALETTES
    #
    folder = "palettes"
    copy_file(folder, config_dir_path + "/aseprite")

    # IMAC LIGHT HELPER SCRIPT
    #
    copy_file("scripts/light", "/usr/local/bin")

def nuke_all_configs():
        print("Nuking All Files...\n")
        remove("/home/luke/.config/dotfiles")
        remove("/home/luke/.zshrc")
        remove("/home/luke/.vimrc")
        remove("/home/luke/.vim")
        remove("/home/luke/.fonts")
        remove("/home/luke/.config/nvim")
        remove("/home/luke/.config/bspwm")
        remove("/home/luke/.config/sxhkd")
        remove("/home/luke/.config/polybar")
        remove("/home/luke/.config/rofi")
        remove("/usr/local/bin/light")
        print("All files removed.\n")

def run_config():
    choice = input("""
        1: Overwrite all configs.\n
        2: Remove and overwrite all files.\n
        3: Just Remove the all of the config/dot files.\n
        0: Do nothing and close.\n"""
    )
    if int(choice) == 3:
        nuke_all_configs()

    elif int(choice) == 2:
        nuke_all_configs()
        install_configs()

    elif int(choice) == 1:
        install_configs()

    elif int(choice) == 0:
        print("Nothing selected. Closing.")


run_config()

