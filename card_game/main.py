from classes import carta, player
import customtkinter as UI

class triple_triad():
    def __init__(self):
        # inicia o tkinter 
        root = UI.CTk()
        #muda o nome
        root.title('Tripe triad')
        root.configure(bg="black")
        # Obtém a largura e altura da tela
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        

        # Cria um rótulo para mostrar o tamanho da tela
        label = UI.CTkLabel(root, text=f"Largura: {screen_width} px, Altura: {screen_height} px")
        label.pack(pady=20)


            
        def switch_window():
            nonlocal root
            root.attributes("-fullscreen", not root.attributes("-fullscreen"))

        switch_window()
                

            

            

        
        #botão sair
        window_button = UI.CTkButton(root, text='[__]', command= switch_window)
        window_button.place(x= 1700,y=0)
        
        


        # o porgrama é uma função e termina aqui, volte para cima ☝️
        root.mainloop()
    def play_triple_triad():
        pass


triple_triad()









