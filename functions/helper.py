def read_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            data = file.read()
    except FileNotFoundError:
        print('File Not Found')
        exit()
    return data


def write_file(new_file_name, data):
    with open(new_file_name, 'w+b') as file:
        write_pack = []
        for x in data:
            write_pack.append(x)
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
