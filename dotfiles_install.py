#!/usr/bin/env python3

## 
# Script installs all of the dotfiles that I use into $HOME/.config/symlinks folder.
## 

import os

# Variables
# 
symlink_dir_path = "$HOME/.config/symlinks"
zsh_dir_path = symlink_dir_path + "/zsh"
vim_dir_path = symlink_dir_path + "/vim"

# Helper functions
# 
def create_dir(dir):
    print("Creating folder:  {}...".format(dir))
    os.system("mkdir -p {}".format(dir))

def copy_file(src, dest):
    print("Copying {} to {}".format(src,dest))
    os.system("cp {} {}".format(src,dest))

# Setup config files
# 
create_dir(symlink_dir_path)

# ZSH
# 
create_dir(zsh_dir_path)
copy_file(".zshrc", zsh_dir_path)
copy_file("aliases", zsh_dir_path)
copy_file("variables", zsh_dir_path)



