import sys

def txt_importer(path_file):
    if not path_file.endwith('.txt'):
        print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file, mode='r') as file:
            file_line = []
            for line in file.readlines():
                file_line.append(line.strip('\n'))
            return file_line
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
