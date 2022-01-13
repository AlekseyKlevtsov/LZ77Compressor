# data byte read function

def read_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            data = file.read()
    except FileNotFoundError:
        print('File Not Found')
        exit()
    return data


# data byte read function

def write_file(new_file_name, write_pack):
    with open(new_file_name, 'w+b') as file:
        file.write(bytes(write_pack))

    return print('File was written')


# documentation opening function

def read_documentation():
    try:
        with open('description.md') as file:
            data = file.read()
    except FileNotFoundError:
        print('File Not Found.')
        exit()
    return print(data)

# function to convert string to byte array

def to_bits(text):
    result = []
    for i in bytearray(text, 'utf-8'):
        result.append(i)
    return result

# byte array to string conversion function

def from_bits(bits):
    result = []
    for x in bits:
        result.append(int(x))
    result = bytearray(result).decode()
    return result
