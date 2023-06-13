from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file_already_exists = False
    returned_data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(txt_importer(path_file)),
        'linhas_do_arquivo': txt_importer(path_file)
    }
    for element in instance._data:
        if element['nome_do_arquivo'] == path_file:
            file_already_exists = True
            break
    if not file_already_exists:
        instance.enqueue(returned_data)
    print(returned_data)


def remove(instance):
    if instance.__len__() < 1:
        print('Não há elementos')
    else:
        removed_element = instance.dequeue()
        path_file = removed_element['nome_do_arquivo']
        print(f'Arquivo {path_file} removido com sucesso')


def file_metadata(instance, position):
    try:
        searching_file = instance.search(position)
        sys.stdout.write(str(searching_file))
    except IndexError:
        sys.stderr.write('Posição inválida')
