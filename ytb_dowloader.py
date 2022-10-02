from pytube import YouTube
import screen_ytb_dowloader as s_ytb

# Pergunta pelo link do YouTube

# link = input("Entre com o link do YouTube:  ")
yt = YouTube(link)

# Mostra detalhes do vídeo
print("Título: ",yt.title)
print("Tempo do vídeo: ",yt.length, " segundos")
print("Tamando do vídeo: ",yt.streams.get_highest_resolution().filesize ,"em bytes")
print(yt.thumbnail_url)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download finalizado!!")
