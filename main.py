"""
Usage:
    main.py compress <name1> <name2>
    main.py decompress <name1> <name2>
    main.py text -c
    main.py text -d
    main.py description
    main.py (-h | --help)

Arguments:
    <operation>  Math Operation
    <num1>       First Number
    <num2>       Second Number


Options:

    -h, --help          Show this screen.
    -v, --version       Show version
"""

from docopt import docopt
import functions.compression as cs
import functions.decompression as dcs
import functions.helper as hp


def run_compress():
    pack = hp.read_file(file_name)
    data = cs.compress(pack)
    hp.write_file(new_file_name, data)


def run_decompress():
    unpack = hp.read_file(file_name)
    data = dcs.decompress(unpack)
    hp.write_file(new_file_name, data)


def run_text_compress():
    data = cs.compress(text)
    print('\n' + data)


def run_text_decompress():
    data = dcs.decompress(text)
    print('\n' + data)


def description():
    hp.read_description()


if __name__ == '__main__':
    arguments = docopt(__doc__, version='LZ 1.2')
    file_name = arguments['<name1>']
    new_file_name = arguments['<name2>']

    if arguments['compress']:
        run_compress()
    elif arguments['decompress']:
        run_decompress()
    elif arguments['text']:
        if arguments['-c']:
            text = input()
            run_text_compress()
    elif arguments['text']:
        if arguments['-c']:
            text = input()
            run_text_decompress()
    elif arguments['description']:
        description()
    else:
        print(arguments)
