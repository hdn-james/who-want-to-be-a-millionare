from PyQt5 import QtCore, QtMultimedia

def init():    
    global musics
    musics = {
        'background': 'test.wav',
        'correct': 'correct.wav',
        'wrong': 'wrong.wav'
    }
    
    global music
    music = QtMultimedia.QSoundEffect(QtCore.QCoreApplication.instance())
    music.setLoopCount(QtMultimedia.QSoundEffect.Infinite)
    music.setVolume(0.5)