#!/usr/bin/env bash
# This file is used to make a new release

echo -e "\e[31m /!\ Make sure you have updated the version number /!\ \e[0m"
read -p "New release ? (y/n) " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo -n Password:
    read -s password
    echo
    rm -r dist build
    python setup.py sdist
    python setup.py bdist_wheel
    if [[ $1 = "-t" || $1 = "--test" ]]
    then
        twine upload -r pypitest -p $password dist/*
    else
        twine upload -r pypi -p $password dist/*
    fi
fi