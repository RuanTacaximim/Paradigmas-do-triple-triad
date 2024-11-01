from classes import carta, player
import tkinter as UI

class triple_triad():
    def __init__(self):
        # inicia o tkinter 
        root = UI.Tk()
        #muda o nome
        root.title('Tripe triad')
        root.configure(bg="black")
        # Obtém a largura e altura da tela
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Cria um rótulo para mostrar o tamanho da tela
        label = UI.Label(root, text=f"Largura: {screen_width} px, Altura: {screen_height} px")
        label.pack(pady=20)


            
        def switch_window():
            

            switcher: bool
            def window_mode():
                #desativa fullscreen
                root.attributes("-fullscreen",False)
                if switcher == False:
                    switcher = True
                if switcher == True:
                    switcher = False
            window_mode()
        
        #botão sair
        window_button = UI.Button(root, text='[_]', command= switch_window)
        window_button.place(x= 1700,y=0)
        
        


        # o porgrama é uma função e termina aqui, volte para cima ☝️
        root.mainloop()
    def play_triple_triad():
        pass


triple_triad()









