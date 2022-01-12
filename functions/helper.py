def read_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            data = file.read()
    except FileNotFoundError:
        print('File Not Found')
        exit()
    return data


def write_file(new_file_name, write_pack):
    with open(new_file_name, 'w+b') as file:
        file.write(bytes(write_pack))
    print('File was written')


def read_description():
    try:
        with open('description.md') as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print('File Not Found')
        exit()


def to_bits(text):
    result = []
    for i in bytearray(text, 'utf-8'):
        result.append(i)
    return result


def from_bits(bits):
    result = []
    for x in bits:
        result.append(int(x))
    result = bytearray(result).decode()
    return result
