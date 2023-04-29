import pytest
import os
from src.pre_built.counter import count_ocurrences


@pytest.fixture
def file_path():
    path = 'test_file.txt'
    with open(path, "w") as file:
        file.write(
            """
            Python é uma linguagem de programação popular e poderosa.
            Ela é utilizada em diversas áreas, como desenvolvimento web,
            análise de dados, inteligência artificial e automação de tarefas
            Python possui uma sintaxe clara e concisa, além de uma grande
            variedade de bibliotecas e ferramentas disponíveis, tornando-a
            uma opção versátil e eficiente para muitas aplicações. Python
            é amplamente utilizado por grandes empresas como Google, Amazon
            e Facebook, além de ser uma escolha popular para projetos de
            código aberto. PYTHON é uma palavra que representa o poder e a
            versatilidade dessa linguagem, e Python é a escolha de
            muitos programadores talentosos em todo o mundo."""
        )
    yield path
    os.remove(path=path)


def test_counter(file_path):
    assert count_ocurrences(file_path, "Python") == 5
    assert count_ocurrences(file_path, "python") == 5
