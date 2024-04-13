import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
#barra da janela
ctk.set_appearance_mode('dark')
#corpo da janela
janela = ctk.CTk('white')
janela.geometry('600x400')
janela.title('app de combustível')

#funcaçao de calculo -----
def calculo():
    di=int(distancia.get())
    co=int(consumo.get())
    pr=float(preco.get())

    valor = (di/co)*pr
    
    messagebox.showinfo('resultado',f'o gasto da viagem foi de R$ {valor:.2f}')
#--------------
#tela de inicio
ctk.CTkLabel(janela,text='App viagem x Consumo', font=('arial',22,'bold'),text_color='#1C1C1C').pack(pady=20)
#distância
ctk.CTkLabel(janela,text='Distância(KM)', font=('arial',18,'bold'),text_color='#8B2500').pack(pady=5)
distancia=ctk.CTkEntry(janela,placeholder_text='Digite a Distância percorrida',width=400)
distancia.pack()
#consumo
ctk.CTkLabel(janela,text='Consumo(L)', font=('arial',18,'bold'),text_color='#8B2500').pack(pady=5)
consumo=ctk.CTkEntry(janela,placeholder_text='Digite o consumo ',width=400)
consumo.pack()
#preoço do Conbustivel
ctk.CTkLabel(janela,text='Preço do Combustível', font=('arial',18,'bold'),text_color='#8B2500').pack(pady=5)
preco=ctk.CTkEntry(janela,placeholder_text='Digite o preço do combistível',width=400)
preco.pack()
#botão
btn= ctk.CTkButton(janela,text='Calcular', width=150,fg_color='#7A378B',text_color='white',command=calculo)
btn.pack(pady=15)

janela.mainloop()