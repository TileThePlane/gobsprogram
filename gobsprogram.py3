#!/usr/bin/env python3
from colorama import init


def main():
    init()
    print("\033[1;32;40m")
    print("Gob's Program:  Y/N?")
    choice = input('? ')
    if choice.upper() == 'Y':
            while True:
                print('Penus  ' * 5 + 'Penus')

if __name__ == '__main__':
    main()
