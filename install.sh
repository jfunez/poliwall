#!/bin/bash
sudo pip install virtualenv virtualenvwrapper
cd $HOME
mkdir -p $HOME/demos/poliwall_demo/
cd $HOME/demos/poliwall_demo/
git clone https://github.com/jfunez/poliwall.git
cd poliwall
export WORKON_HOME="`pwd`/venvs/"
mkdir -p $WORKON_HOME
echo $WORKON_HOME
export VIRTUALENVWRAPPER_HOOK_DIR=$WORKON_HOME
export PIP_VIRTUALENV_BASE=$WORKON_HOME
export PIP_RESPECT_VIRTUALENV=true
export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv polienv
workon polienv
cd poliwall
./init.sh
