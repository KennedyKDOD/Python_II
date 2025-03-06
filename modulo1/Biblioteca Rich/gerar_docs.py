# gerar_docs.py
import os
import sys

# Adiciona o diretório atual ao sys.path
sys.path.append(os.path.abspath('.'))

modulos = ['layout', 'painel', 'progresso', 'estilo']
for modulo in modulos:
    nome_modulo = f"personalizador.{modulo}"
    print(f"Gerando documentação para {nome_modulo}...")
    os.system(f"python -m pydoc -w {nome_modulo}")
    # Verifica se o arquivo foi criado (já com o nome correto)
    if os.path.exists(f"{nome_modulo}.html"):
        print(f"Documentação gerada: {nome_modulo}.html")
    else:
        print(f"Erro: {nome_modulo}.html não foi gerado!")

print("Gerando documentação do pacote personalizador...")
os.system("python -m pydoc -w personalizador")