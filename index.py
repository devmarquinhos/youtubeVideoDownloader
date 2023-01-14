# Importando bibliotecas
from pytube import YouTube
import os
from time import sleep

# Função para verificar se o caminho onde será salvo o vídeo existe. Caso não exista, será criado.
def verificaCaminho(caminho):
    existeCaminho = os.path.exists(caminho)
    if not existeCaminho:
        os.mkdir(caminho)
        
# Função para abrir a pasta
def openDir(caminho):
    for i in range(1, 4):
        print(f'Abrindo diretório em {i}...')
        sleep(1)
    os.startfile(caminho)

# Imprimindo o título
print("="*50)
print("Youtube Downloader | v1.1")
print("="*50)

# Receber URL do vídeo e recebendo o caminho para salvar o arquivo baixado
link = input("Cole aqui a URL do vídeo que deseja baixar: ")
caminho = input('Cole aqui o diretório de onde deseja salvar: ')
if caminho == "":
    caminho = 'videos'
verificaCaminho(caminho)

# Coletando dados da URL inserida
yt = YouTube(link)
result = [yt.title, yt.author]
print(f'{result[0]} by {result[1]}')

# Baixando vídeo e salvando na pasta "videos"
ys = yt.streams.get_highest_resolution()
print("Baixando...")
ys.download(caminho)
print("Video baixado com sucesso!")

# Abrindo a pasta onde foi salvo o vídeo
openDir(caminho)
