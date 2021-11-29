from PyQt5 import QtCore, QtMultimedia
import configuration
import os

dirname = os.path.dirname(__file__)
music_folder = os.path.join(dirname, "../musics")


def playBackground():
    musics = configuration.musics
    file = musics['background']
    configuration.music.setSource(QtCore.QUrl.fromLocalFile(
        os.path.join(music_folder, "./" + file)))
    configuration.music.play()


def playCorrect():
    musics = configuration.musics
    file = musics['correct']
    music = QtMultimedia.QSoundEffect(QtCore.QCoreApplication.instance())
    music.setSource(QtCore.QUrl.fromLocalFile(
        os.path.join(music_folder, ":" + file)))
    music.play()


def playWrong():
    musics = configuration.musics
    file = musics['wrong']
    music = QtMultimedia.QSoundEffect(QtCore.QCoreApplication.instance())
    music.setSource(QtCore.QUrl.fromLocalFile(
        os.path.join(music_folder, ":" + file)))
    music.play()
