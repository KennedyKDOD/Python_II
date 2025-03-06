# personalizador/layout.py
from rich.layout import Layout
from rich.console import Console

console = Console()

def split_layout(texto, isArquivo):
    """Exibe o texto em um layout dividido verticalmente.
    
    Args:
        texto (str): O texto a ser exibido ou caminho do arquivo.
        isArquivo (bool): Indica se o texto é um caminho para um arquivo.
    """
    layout = Layout()
    layout.split_column(Layout(name="superior"), Layout(name="inferior"))
    
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto
    
    layout["superior"].update(conteudo)
    layout["inferior"].update("Texto exibido acima!")
    console.print(layout)

def side_by_side(texto, isArquivo):
    """Exibe o texto em um layout lado a lado.
    
    Args:
        texto (str): O texto a ser exibido ou caminho do arquivo.
        isArquivo (bool): Indica se o texto é um caminho para um arquivo.
    """
    layout = Layout()
    layout.split_row(Layout(name="esquerda"), Layout(name="direita"))
    
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto
    
    layout["esquerda"].update(conteudo)
    layout["direita"].update("Texto ao lado!")
    console.print(layout)