from classes import carta, player
import tkinter as UI

class triple_triad():
    def __init__(self):
        # inicia o tkinter 
        root = UI.Tk()
        #muda o nome
        root.title('Tripe triad')
    
        # Obtém a largura e altura da tela
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Cria um rótulo para mostrar o tamanho da tela
        label = UI.Label(root, text=f"Largura: {screen_width} px, Altura: {screen_height} px")
        label.pack(pady=20)

        def controle_de_janela():
            if window_mode == True:
                fullscreen()
            elif fullscreen == True:
                window_mode()
            
        def fullscreen():
            #ativa fullscreen
            root.attributes("-fullscreen",True)
        def window_mode():
            #desativa fullscreen
            root.attributes("-fullscreen",False)
        
        #botão sair
        window_button = UI.Button(root, text='sair da tela cheia', command= window_mode)
        window_button.place(x= 1700,y=0)
        fullscreen_button = UI.Button(root,text="[_]", command= controle_de_janela)
        fullscreen_button.place(x= 1600,y=10)


        # o porgrama é uma função e termina aqui, volte para cima ☝️
        root.mainloop()
    def play_triple_triad():
        pass


triple_triad()









