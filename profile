echo "$0: Login shell"

alias ls='ls --color=auto'
alias patch='patch --binary'
alias idvad='pageant ~/id/vadmium.ssh2.rsa.ppk &'
alias xp='putty -X'
alias less='less -r'

[ -e ~/.env ] && . ~/.env
