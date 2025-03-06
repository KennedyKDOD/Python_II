# personalizador/painel.py
from rich.panel import Panel
from rich.console import Console

console = Console()

def bordered_panel(texto, isArquivo):
    """Exibe o texto em um painel com borda.
    
    Args:
        texto (str): O texto a ser exibido ou caminho do arquivo.
        isArquivo (bool): Indica se o texto é um caminho para um arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto
    
    painel = Panel(conteudo, title="Texto Formatado", border_style="blue")
    console.print(painel)

def colored_panel(texto, isArquivo):
    """Exibe o texto em um painel colorido.
    
    Args:
        texto (str): O texto a ser exibido ou caminho do arquivo.
        isArquivo (bool): Indica se o texto é um caminho para um arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto
    
    painel = Panel(conteudo, title="Texto Colorido", style="bold green on black")
    console.print(painel)