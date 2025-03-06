# personalizador/estilo.py
from rich.console import Console
from rich.text import Text

console = Console()

def bold_colored(texto, isArquivo):
    """Exibe o texto em negrito e colorido.
    
    Args:
        texto (str): O texto a ser exibido ou caminho do arquivo.
        isArquivo (bool): Indica se o texto é um caminho para um arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto
    
    texto_formatado = Text(conteudo, style="bold red")
    console.print(texto_formatado)

def underlined_italic(texto, isArquivo):
    """Exibe o texto sublinhado e em itálico.
    
    Args:
        texto (str): O texto a ser exibido ou caminho do arquivo.
        isArquivo (bool): Indica se o texto é um caminho para um arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto
    
    texto_formatado = Text(conteudo, style="underline italic blue")
    console.print(texto_formatado)