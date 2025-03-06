# main.py
import argparse
from personalizador import layout, painel, progresso, estilo

# Dicionários para mapear módulos e funções
MODULOS = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo
}

FUNCOES = {
    "layout": {"split": layout.split_layout, "side": layout.side_by_side},
    "painel": {"bordered": painel.bordered_panel, "colored": painel.colored_panel},
    "progresso": {"bar": progresso.progress_bar, "spinner": progresso.spinning_wheel},
    "estilo": {"bold": estilo.bold_colored, "underline": estilo.underlined_italic}
}

def main():
    parser = argparse.ArgumentParser(description="Personaliza a exibição de texto com a biblioteca rich.")
    
    parser.add_argument("texto", help="Texto a ser exibido ou caminho do arquivo.")
    parser.add_argument("-a", "--arquivo", action="store_true",
                        help="Indica que o argumento 'texto' é um caminho para um arquivo.")
    parser.add_argument("-m", "--modulo", default="layout",
                        choices=MODULOS.keys(),
                        help="Módulo a ser usado: layout, painel, progresso, estilo (padrão: layout).")
    parser.add_argument("-f", "--funcao", default=list(FUNCOES["layout"].keys())[0],
                        choices=[f for funcs in FUNCOES.values() for f in funcs.keys()],
                        help="Função a ser usada: split, side, bordered, colored, bar, spinner, bold, underline (padrão: split).")
    
    args = parser.parse_args()

    # Selecionar o módulo e a função
    modulo = MODULOS[args.modulo]
    funcao = FUNCOES[args.modulo].get(args.funcao, FUNCOES["layout"]["split"])
    
    # Executar a função escolhida
    funcao(args.texto, args.arquivo)

if __name__ == "__main__":
    main()