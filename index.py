# Importando bibliotecas
from pytube import YouTube
import os
from time import sleep
from tkinter import *

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

# Função para imprimir o título
def titlePrint():
    print("="*50)
    print("Youtube Downloader | v1.2a")
    print("="*50)
    
# Receber URL do vídeo e recebendo o caminho para salvar o arquivo baixado
def dataCollect():
    videoURL = str(input("Cole aqui a URL do vídeo que deseja baixar: "))
    dirPath = str(input("Cole aqui o endereço da pasta onde deseja salvar: "))
    if dirPath == "":
        dirPath = 'videos'
    verificaCaminho(dirPath)
    
    collectedData = [videoURL, dirPath]
    return collectedData

# Recebendo as informações do vídeo e baixando o vídeo
def downloadVideo(videoURL, dirPath):
    yt = YouTube(videoURL)
    videoInfo = [yt.title, yt.author]
    print(f'{videoInfo[0]} | {videoInfo[1]}')
    
    ytDownload = yt.streams.get_highest_resolution()
    print("Baixando...")
    ytDownload.download(dirPath)
    print("Vídeo baixado com sucesso!")
    
# Imprimindo o título
titlePrint()

# Coletando os dados do vídeo e o diretório
videoUrl, dirPath = dataCollect()

# Fazendo o download do vídeo
downloadVideo(videoUrl, dirPath)

# Abrindo o diretório
openDir(dirPath)
