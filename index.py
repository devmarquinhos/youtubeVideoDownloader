# Importando bibliotecas
from pytube import YouTube
from os import path, mkdir

# Função para verificar se o caminho onde será salvo o vídeo existe. Caso não exista, será criado.
def verificaCaminho(caminho):
    existeCaminho = path.exists(caminho)
    if existeCaminho != True:
        mkdir(caminho)

# Receber URL do vídeo e recebendo o caminho para salvar o arquivo baixado
link = input("Cole aqui a URL do vídeo que deseja baixar: ")
caminho = input('Cole aqui o diretório de onde deseja salvar: ')
if caminho == "":
    caminho = './videos'
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
