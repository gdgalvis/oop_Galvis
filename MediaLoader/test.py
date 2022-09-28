from media_loader import MediaLoader,Wav,Ogg

#No pudes instanciar una clase abstracta
#media=MediaLoader()

#La clase neceista atributos y metodos para ser intanciado
#wav=Wav()

ogg=Ogg()
ogg.play()
print(ogg.ext)
ogg.ext=".mp3"
print(ogg.ext)