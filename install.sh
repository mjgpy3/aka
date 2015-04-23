#!/bin/bash

install_path="$HOME/.aka"

echo "Installing at $install_path"

mkdir -p $install_path

cp ./src/* $install_path

export AKA_ALIASES=$install_path/aliases.json

for command_name in sdfa fads fsad safd afsd asfd dsfa fdas dfsa sfad dfas fsda asdf adfs fasd dsaf adsf dafs dasf sfda afds fdsa sadf sdaf
do
	alias $command_name="$install_path/aka.py"
done
