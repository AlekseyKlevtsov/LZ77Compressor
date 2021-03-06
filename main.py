"""
Usage:
    main.py compress <name1> <name2>
    main.py decompress <name1> <name2>
    main.py text -c
    main.py text -d
    main.py documentation
    main.py (-h | --help)

Arguments:
    <num1>       First Number
    <num2>       Second Number

Options:
    -h, --help          Show this screen.
    -v, --version       Show version

"""

# import library docopt for using terminal
from docopt import docopt

# import functions used
import functions.compression as cs
import functions.decompression as dcs
import functions.helper as hp


# function compression file

def compress():
    data = hp.read_file(file_name)
    pack = cs.compress(data)
    hp.write_file(new_file_name, pack)


# function decompression file

def decompress():
    data = hp.read_file(file_name)
    unpack = dcs.decompress(data)
    hp.write_file(new_file_name, unpack)


# function compression text

def run_text_compress():
    text = input()
    print()
    code_text = hp.to_bits(text)
    data = cs.compress(code_text)
    print(" ".join(map(str, data)))


# function decompression text

def run_text_decompress():
    text = input()
    print()
    code_text = text.split()
    data = dcs.decompress(code_text)
    result = hp.from_bits(data)
    print(result)


#  function output documentation

def documentation():
    hp.read_documentation()


if __name__ == '__main__':
    arguments = docopt(__doc__, version='LZ 1.2.1')
    file_name = arguments['<name1>']
    new_file_name = arguments['<name2>']

    # choice using function

    if arguments['compress']:
        compress()

    elif arguments['decompress']:
        decompress()

    elif arguments['text']:
        if arguments['-c']:
            run_text_compress()

        elif arguments['-d']:
            run_text_decompress()
        else:
            print('View the documentation')
            print(arguments)

    elif arguments['documentation']:
        documentation()
    else:
        print('View the documentation')
        print(arguments)
