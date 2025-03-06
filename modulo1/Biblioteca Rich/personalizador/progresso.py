# personalizador/progresso.py
from rich.progress import Progress
from rich.console import Console
import time

console = Console()

def progress_bar(texto, isArquivo):
    """Exibe o texto com uma barra de progresso simulada.
    
    Args:
        texto (str): O texto a ser exibido ou caminho do arquivo.
        isArquivo (bool): Indica se o texto é um caminho para um arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto
    
    with Progress() as progress:
        task = progress.add_task("[green]Processando...", total=100)
        for _ in range(100):
            time.sleep(0.01)  # Simula processamento
            progress.update(task, advance=1)
        console.print(conteudo)

def spinning_wheel(texto, isArquivo):
    """Exibe o texto com um spinner de carregamento.
    
    Args:
        texto (str): O texto a ser exibido ou caminho do arquivo.
        isArquivo (bool): Indica se o texto é um caminho para um arquivo.
    """
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    else:
        conteudo = texto
    
    with Progress() as progress:
        task = progress.add_task("[cyan]Carregando...", total=None)  # Spinner
        time.sleep(2)  # Simula carregamento
        progress.update(task, completed=True)
        console.print(conteudo)