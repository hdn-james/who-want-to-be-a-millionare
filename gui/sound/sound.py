from PyQt5 import QtCore, QtMultimedia
import configuration

current_dir = "./who-want-to-be-a-millionare/gui/musics/" 
    
def playBackground():
    musics = configuration.musics
    file = musics['background']
    configuration.music.setSource(QtCore.QUrl.fromLocalFile(current_dir + file))
    configuration.music.play()
    
def playCorrect():
    musics = configuration.musics
    file = musics['correct']
    music = QtMultimedia.QSoundEffect(QtCore.QCoreApplication.instance())
    music.setSource(QtCore.QUrl.fromLocalFile(current_dir + file))
    music.play()
    
def playWrong():
    musics = configuration.musics
    file = musics['wrong']
    music = QtMultimedia.QSoundEffect(QtCore.QCoreApplication.instance())
    music.setSource(QtCore.QUrl.fromLocalFile(current_dir + file))
    music.play()