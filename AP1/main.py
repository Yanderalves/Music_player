import os
from tkinter import filedialog
import platform

try:
    from tkinter import *
except:
    from Tkinter import *

try:
    import pygame
except:
    os.system('pip3 install pygame')
    import pygame

SO = platform.system()

if SO == 'Windows':
    IMAGES_PATH = os.getcwd() +  '\\Images\\'
    barra = '\\'
else:
    IMAGES_PATH = os.getcwd() + "/Images/"
    barra = '/'

pygame.init()
pygame.mixer.init()

class App():
    
    def __init__(self, master=None):
        self.font = ('Arial', '12')
        self.master = master
        self.master.title("Music Player")
        self.master.configure(background='#6c67c9')
        self.master.geometry("300x420") # Largura x Altura
        self.master.resizable(width=False, height=False)
        
        self.foto = PhotoImage(file=IMAGES_PATH + 'pylot.png').subsample(2, 2)
        self.saida = Label(self.master, text="Foto do Albúm", image=self.foto)
        # self.saida['bg'] = '#000000'
        # self.saida['fg'] = '#ffffff'
        self.saida.place(x=65, y=30)

        self.lista_musicas = []
        self.musica_tocando = 0
        self.tocando = False
        self.formatos_permitidos = ['mp3', 'wav', 'ogg']
        
        self.progresso = Button(self.master)
        self.photo=PhotoImage(file=IMAGES_PATH + 'play.png')
        self.progresso.config(image=self.photo,width="200",height="3",activebackground="black",bg="black", bd=0)
        self.progresso.place(x=50, y=275)

        self.play = Button(self.master)
        imagem_play = PhotoImage(file=IMAGES_PATH + 'play.png').subsample(10,10)
        self.play.config(image=imagem_play)
        self.play.image = imagem_play
        self.play['command'] = self.tocar_musica
        self.play['highlightbackground'] = '#6c67c9'
        self.play['activebackground'] = '#6c67c9'
        self.play['bg'] = '#6c67c9'
        self.play['cursor'] = 'hand2'
        self.play['borderwidth'] = 0
        self.play.place(x=123, y=300)

        self.pause = Button(self.master)
        imagem_pause = PhotoImage(file=IMAGES_PATH + 'pause.png').subsample(10,10)
        self.pause.config(image=imagem_pause)
        self.pause.image = imagem_pause
        self.pause['command'] = self.pausar
        self.pause['highlightbackground'] = '#6c67c9'
        self.pause['activebackground'] = '#6c67c9'
        self.pause['bg'] = '#6c67c9'
        self.pause['cursor'] = 'hand2'
        self.pause['borderwidth'] = 0

        self.prox = Button(self.master)
        imagem_prox = PhotoImage(file=IMAGES_PATH + 'prox.png').subsample(10,10)
        self.prox.config(image=imagem_prox)
        self.prox.image = imagem_prox
        self.prox['command'] = self.passar_musica
        self.prox['highlightbackground'] = '#6c67c9'
        self.prox['borderwidth'] = 0
        self.prox['activebackground'] = '#6c67c9'
        self.prox['bg'] = '#6c67c9'
        self.prox['cursor'] = 'hand2'
        self.prox.place(x=186, y=300)

        self.ant = Button(self.master)
        imagem_ant = PhotoImage(file=IMAGES_PATH + 'ant.png').subsample(10,10)
        self.ant.config(image=imagem_ant)
        self.ant.image = imagem_ant
        self.ant['command'] = self.voltar_musica
        self.ant['borderwidth'] = 0
        self.ant['highlightbackground'] = '#6c67c9'
        self.ant['bg'] = '#6c67c9'
        self.ant['cursor'] = 'hand2'
        self.ant['activebackground'] = '#6c67c9'
        self.ant.place(x=60, y=300)

        self.nome_musica = Label(self.master, font=self.font)
        self.nome_musica['bg'] = '#6c67c9'
        self.nome_musica['fg'] = '#ffffff'
        self.nome_musica['width'] = 17
        self.nome_musica.place(x=70, y=230)

        self.master.withdraw()
        self.folder_selected = filedialog.askdirectory(title="Selecione sua pasta de músicas")
        self.master.deiconify()
        self.carrega_musicas()

    def carrega_musicas(self):
        if self.folder_selected != ():
            for musica in os.listdir(self.folder_selected):
                if musica.split('.')[-1] in self.formatos_permitidos:
                    self.lista_musicas.append(musica)
            if len(self.lista_musicas) == 0:
                print("Nenhuma música encontrada")
                self.master.destroy()
        else:
            print("Nenhuma pasta selecionada")
            self.master.destroy()

    def verifica(self):
        if self.musica_tocando >= len(self.lista_musicas) or self.musica_tocando < 0:
            self.musica_tocando = 0
     
    def passar_musica(self):
        self.musica_tocando += 1
        self.verifica()
        self.tocar_musica()

    def pausar(self):
        self.play.place(x=123, y=300)
        self.pause.place_forget()
        self.tocando = False
        pygame.mixer.music.pause()

    def voltar_musica(self):
        self.musica_tocando -= 1
        self.verifica()
        self.tocar_musica()

    def tocar_musica(self):
        if self.tocando == False:    
            self.verifica()
            pygame.mixer.music.load(self.folder_selected + barra + self.lista_musicas[self.musica_tocando])
            pygame.mixer.music.play()
            self.lista_musicas[self.musica_tocando]
            self.nome_musica['text'] = self.lista_musicas[self.musica_tocando].split('.')[0]
            self.pause.place(x=123, y=300)
        else:
            pygame.mixer.music.unpause()
            self.tocando = True


root = Tk()
App(root)
root.mainloop()
