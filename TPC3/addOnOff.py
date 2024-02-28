import re
import sys


def addOnAndOff(texto):
    '''
    This function parses the string and parses all the integer numbers,
    the words 'On' and 'Off' to able/disable the sum of the numbers and the '='
    to print the sum of the numbers.
    '''
    values = re.findall(r'[-+]?\d+|Off|On|=',texto,flags=re.IGNORECASE)

    print(values)

    on = True
    sum = 0
    for value in values:
        value = value.lower()
        if value == 'off':
            on = False
        elif value == 'on':
            on = True
        elif value == '=':
            print(f"Soma = {sum}")
        elif on:
            sum += int(value)



def main():
    readFile = sys.stdin
    if len(sys.argv) > 1:
        readFile = open(sys.argv[1], 'r')
    
    texto = readFile.read()
    
    addOnAndOff(texto)


if __name__ == "__main__":
    main()

