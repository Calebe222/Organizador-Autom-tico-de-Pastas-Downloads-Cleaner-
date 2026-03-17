import os
import shutil 

pasta_downloads = '/Users\calebe\Downloads'
extensoes = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
    'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Musicas': ['.mp3', '.wav', '.flac'],
    'Compactados': ['.zip', '.rar', '.7z']
}

for arquivo in os.listdir(pasta_downloads):
    caminho_arquivo = os.path.join(pasta_downloads, arquivo)
    if os.path.isfile(caminho_arquivo):
        extensao = os.path.splitext(arquivo)[1].lower()
        for pasta, exts in extensoes.items():
            if extensao in exts:
                pasta_destino = os.path.join(pasta_downloads, pasta)
                os.makedirs(pasta_destino, exist_ok=True)
                shutil.move(caminho_arquivo, pasta_destino)
                print(f'Movido: {arquivo} -> {pasta}')
                break