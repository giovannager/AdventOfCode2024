import re

def read_txt_file(foldername: str, file: str):
    f = open(foldername + '/' + file, "r")
    return f.read()

def split_input_into_lists(input_txt: str) -> tuple:
    list1, list2 = [], []
    input_txt_lines = input_txt.split('\n')
    for line in input_txt_lines:
        parse_line = re.split('\s+', line)
        list1.append(parse_line[0])
        list2.append(parse_line[1])
    return (list1, list2)

if __name__ == '__main__': 
    __init__.py.bin