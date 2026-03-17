# 📂 Organizador Automático de Pastas (Downloads Cleaner)

Este script automatiza a organização de pastas bagunçadas (como a pasta Downloads), movendo automaticamente os arquivos para subpastas específicas com base nas suas extensões (ex: .pdf vai para 'Documentos', .jpg vai para 'Imagens').

Ideal para manter o ambiente de trabalho limpo e facilitar a localização de arquivos no dia a dia do serviço público.

## 🚀 Funcionalidades
- **Classificação por Extensão:** Identifica o tipo de arquivo e decide o destino correto.
- **Criação Dinâmica de Pastas:** Se a pasta de destino (ex: 'Planilhas') não existir, o script a cria automaticamente.
- **Movimentação Segura:** Utiliza a biblioteca `shutil` para garantir que o arquivo seja movido sem corromper.

## 🛠️ Bibliotecas Utilizadas
Este projeto utiliza apenas bibliotecas nativas do Python, não sendo necessário instalar pacotes externos:
- `os`: Para manipulação de caminhos e listagem de arquivos.
- `shutil`: Para a movimentação física dos arquivos entre diretórios.

## 📖 Como usar

1.  Abra o arquivo `organizador.py`.
2.  Configure o caminho da pasta que você deseja organizar:
    ```python
    caminho_da_pasta = r"C:\Usuarios\SeuNome\Downloads"
    ```
3.  Execute o script.
4.  Veja seus arquivos serem movidos para as pastas:
* **🖼️ Imagens:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`
* **📄 Documentos:** `.pdf`, `.doc`, `.docx`, `.txt`, `.xlsx`
* **🎬 Vídeos:** `.mp4`, `.avi`, `.mov`, `.mkv`
* **🎵 Músicas:** `.mp3`, `.wav`, `.flac`
* **📦 Compactados:** `.zip`, `.rar`, `.7z`