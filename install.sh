#!/bin/bash

install_path="$HOME/.aka"

echo "Installing at $install_path"

mkdir -p $install_path

cp ./src/* $install_path

export AKA_ALIASES=$install_path/aliases.json
