#!/bin/bash

echo "On what distro are you? (debian, arch)"
read distro

if [ "$distro" = "debian" ]; then
	echo "installing packages via apt"
	sudo apt update
	sudo apt -y install gcc g++
  sudo apt -y install python3
elif [ "$distro" = "arch" ]; then
	echo "installing packages via pacman"
	sudo pacman -Syu --noconfirm
	sudo pacman -S --noconfirm gcc g++
  sudo pacman -S --noconfirm python3
else
	echo "wrong input"
fi

echo "creating folder for cloning"
mkdir ~/.nullc

echo "cloning repo"
git clone https://www.github.com/Preclik02/nullc ~/.nullc

echo "compiling the cpp file via g++"
g++ ~/.nullc/nullc.cpp -o ~/.nullc/nullc
chmod +x ~/.nullc/install.sh

echo "what terminal do you use? (bash, zsh)"
read terminal


if [ "$terminal" = "bash" ]; then
	echo 'export PATH="$HOME/.nullc:$PATH"' >> ~/.bashrc
	echo "Added to PATH in ~/.bashrc. Please restart your terminal or run: source ~/.bashrc"
	echo "\n\nNow you need to restart the terminal and runt this line: source ~/.zshrc"
	read
elif [ "$terminal" = "zsh" ]; then
	echo 'export PATH="$HOME/.nullc:$PATH"' >> ~/.zshrc
	echo "Added to PATH in ~/.zshrc. Please restart your terminal or run: source ~/.zshrc"
	echo "\n\nNow you need to restart the terminal and run this line: source ~/.zshrc"
	read
fi

