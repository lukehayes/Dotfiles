#!/usr/bin/env python3

## 
# Script installs all of the dotfiles that I use into $HOME/.config/dotfiles folder.
## 

import os

# Variables
# 
dotfile_dir_path = "$HOME/.config/dotfiles"
zsh_dir_path = dotfile_dir_path + "/zsh"
vim_dir_path = dotfile_dir_path + "/vim"

# Helper functions
# 
def create_dir(dir):
    print("Creating folder:  {}...".format(dir))
    os.system("mkdir -p {}".format(dir))

def copy_file(src, dest):
    print("Copying {} to {}".format(src,dest))
    os.system("cp {} {}".format(src,dest))

def clone_repo(repo, dest):
    print("Git cloning {} to {}".format(repo,dest))
    os.system("git clone {} {}".format(repo,dest))

def create_symlink(src, dest):
    print("Creating dotfile {} to {}".format(src,dest))
    os.system("ln -s {} {}".format(src,dest))

# Setup config files
# 
create_dir(dotfile_dir_path)

# ZSH
# 
create_dir(zsh_dir_path)
copy_file(".zshrc", zsh_dir_path)
copy_file("aliases", zsh_dir_path)
copy_file("variables", zsh_dir_path)
create_symlink(zsh_dir_path + "/.zshrc", "$HOME/.zshrc")

# VIM
# 
create_dir(vim_dir_path)
clone_repo("git@github.com:lukehayes/VimConfig.git", vim_dir_path)
create_symlink(vim_dir_path + "/init.vim", "$HOME/.vimrc")
