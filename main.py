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
    data = hp.read_file(file_name)
    pack = cs.compress(data)
    hp.write_file(new_file_name, pack)


def run_decompress():
    data = hp.read_file(file_name)
    unpack = dcs.decompress(data)
    hp.write_file(new_file_name, unpack)


def run_text_compress():
    code_text = hp.to_bits(text)
    data = cs.compress(code_text)
    print(" ".join(map(str, data)))


def run_text_decompress():
    code_text = text.split()
    data = dcs.decompress(code_text)
    result = hp.from_bits(data)
    print(result)


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
            print()
            run_text_compress()

        elif arguments['-d']:
            text = input()
            print()
            run_text_decompress()
        else:
            print('view the documentation')
            print(arguments)

    elif arguments['description']:
        description()
    else:
        print('view the documentation')
        print(arguments)