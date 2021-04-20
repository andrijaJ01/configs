source /usr/share/instantshell/zshrc

export EDITOR=vim

alias nnn='nnn -deH'

#wal -R
clear

autoload -Uz compinit
zstyle ':completion:*' menu select
fpath+=~/.zfunc
