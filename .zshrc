# Path to your oh-my-zsh installation.
export ZSH="/home/luke/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="mgutz"

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)

source $ZSH/oh-my-zsh.sh

# Make Ruby Gems (Rails specifically) work
export GEM_HOME="$(ruby -e 'puts Gem.user_dir')"
export PATH="$PATH:$GEM_HOME/bin"

#source $HOME/.config/luke-config/bashrc-aliases

SYMLINK_PATH=$HOME/.config/luke-symlinks/ZSH

source $SYMLINK_PATH/aliases
source $SYMLINK_PATH/variables

# Swap the escape key with the capslock key.
setxkbmap -option caps:swapescape # Swap capslock with ESC.
setxkbmap -option caps:escape # Make capslock another ECS.

./.fehbg
