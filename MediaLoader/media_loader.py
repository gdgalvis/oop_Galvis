import abc


#Los parametros del constructor No son attributos de la clase

class MediaLoader(abc.ABC):
    """
    Abrstract Classes
    
    """
    @abc.abstractmethod
    def play(self) -> None:
        ...
    
    @property
    @abc.abstractmethod
    def ext(self) -> str:
        ...
    
class Wav(MediaLoader):
    pass

class Ogg(MediaLoader):
    ext= ".ogg"
    def play(self) -> None:
        print("Playing OGG")

class MP3(MediaLoader):
    def __init__(self,only_Jazz,only_rock=True) -> None:
        self.only_Jazz = True