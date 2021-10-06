from pytube import YouTube as YT
from pytube.cli import on_progress as P

Lista_Videos = [
    'https://www.youtube.com/watch?v=wcLNteez3c4',
    'https://www.youtube.com/watch?v=ASO_zypdnsQ'
]

for i in Lista_Videos:
    videoInfo = YT(i)
    videoFileDL = YT(i,on_progress_callback=P).streams\
        .filter(res="720p",progressive=True)\
        .first()
    videoFileDL.download()
    print(f"Downloado do vídeo '{videoInfo.title}' concluido com sucesso!")