#!/usr/bin/env python3
import os
import shutil
import argparse
from datetime import datetime

PASTA_ORIGEM_DEFAULT = r"C:\Users\nome_usuario\Teste_Projeto_Organizador_Arquivos"
LOG_FILENAME = "organizador_log.txt"

MAPEAMENTO = {
    ".txt": "Documentos",
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".doc": "Documentos",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".mp3": "Musicas",
    ".mp4": "Videos",
    ".zip": "Arquivos_Comprimidos",
    ".rar": "Arquivos_Comprimidos"
}

# Funções Usadas
def registrar_log(pasta_origem, mensagem):
    caminho_log = os.path.join(pasta_origem, LOG_FILENAME)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{ts}] {mensagem}\n"
    with open(caminho_log, "a", encoding="utf-8") as f:
        f.write(linha)

def obter_extensao(nome_arquivo):
    return os.path.splitext(nome_arquivo)[1].lower()

def pasta_destino_para_extensao(extensao):
    return MAPEAMENTO.get(extensao)

def gerar_nome_unico(pasta_destino, nome_arquivo):
    base, ext = os.path.splitext(nome_arquivo)
    candidato = nome_arquivo
    i = 1
    while os.path.exists(os.path.join(pasta_destino, candidato)):
        candidato = f"{base} ({i}){ext}"
        i += 1
    return candidato

def mover_arquivo(caminho_origem, pasta_destino, pasta_origem, dry_run=False):
    os.makedirs(pasta_destino, exist_ok=True)
    nome_arquivo = os.path.basename(caminho_origem)
    nome_final = gerar_nome_unico(pasta_destino, nome_arquivo)
    destino = os.path.join(pasta_destino, nome_final)
    try:
        if dry_run:
            print(f"[DRY RUN] {nome_arquivo} -> {pasta_destino}/{nome_final}")
            registrar_log(pasta_origem, f"[DRY RUN] Pretendia mover: {nome_arquivo} -> {pasta_destino}/{nome_final}")
        else:
            shutil.move(caminho_origem, destino)
            print(f"Movido: {nome_arquivo} -> {pasta_destino}/{nome_final}")
            registrar_log(pasta_origem, f"Movido: {nome_arquivo} -> {pasta_destino}/{nome_final}")
    except Exception as e:
        print(f"ERRO ao mover {nome_arquivo}: {e}")
        registrar_log(pasta_origem, f"ERRO ao mover {nome_arquivo}: {e}")

def organizar(pasta_origem, dry_run=False, move_unknown=False):
    if not os.path.isdir(pasta_origem):
        raise ValueError(f"Pasta não existe: {pasta_origem}")

    for nome in os.listdir(pasta_origem):
        caminho = os.path.join(pasta_origem, nome)
        if not os.path.isfile(caminho):
            continue
        if nome == LOG_FILENAME:
            continue
        if nome.startswith("."):
            continue

        extensao = obter_extensao(nome)
        pasta_rel = pasta_destino_para_extensao(extensao)

        if pasta_rel:
            pasta_destino = os.path.join(pasta_origem, pasta_rel)
            mover_arquivo(caminho, pasta_destino, pasta_origem, dry_run=dry_run)
        else:
            if move_unknown:
                pasta_destino = os.path.join(pasta_origem, "Outros")
                mover_arquivo(caminho, pasta_destino, pasta_origem, dry_run=dry_run)
            else:
                registrar_log(pasta_origem, f"Pulado (sem mapeamento): {nome}")

# ===== CLI simples =====
def parse_args():
    parser = argparse.ArgumentParser(description="Organizador automático de arquivos por extensão.")
    parser.add_argument("-s", "--source", default=PASTA_ORIGEM_DEFAULT, help="Pasta a ser organizada")
    parser.add_argument("-n", "--dry-run", action="store_true", help="Não move arquivos, apenas mostra o que faria")
    parser.add_argument("-u", "--move-unknown", action="store_true", help='Mover extensões desconhecidas para a pasta "Outros"')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print("Organizador iniciado.")
    print("Pasta:", args.source)
    print("Dry run:", args.dry_run)
    print("Mover desconhecidos para 'Outros':", args.move_unknown)
    organizar(args.source, dry_run=args.dry_run, move_unknown=args.move_unknown)
    print("Concluído. Veja o log em", os.path.join(args.source, LOG_FILENAME))
