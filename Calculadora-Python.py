import tkinter as tk 

janela = tk.Tk();
janela.title("Calculadora Python");
janela.geometry("400x600");

botao0 = tk.Button (janela, text="0",width=12, height=8);
botao1 = tk.Button (janela, text="1",width=12, height=8);
botao2 = tk.Button (janela, text="2",width=12, height=8);
botao3 = tk.Button (janela, text="3",width=12, height=8);
botao4 = tk.Button (janela, text="4",width=12, height=8);
botao5 = tk.Button (janela, text="5",width=12, height=8);
botao6 = tk.Button (janela, text="6",width=12, height=8);
botao7 = tk.Button (janela, text="7",width=12, height=8);
botao8 = tk.Button (janela, text="8",width=12, height=8);
botao9 = tk.Button (janela, text="9",width=12, height=8);

botao1.place(x=0, y=469);
botao4.place(x=0, y=340);
botao7.place(x=0, y=211);
botao2.place(x=94, y=469);
botao3.place(x=188, y=469);
botao5.place(x=94, y=340);
botao6.place(x=188, y=340);
botao8.place(x= 94,y=211);
botao9.place(x=188, y=211);


janela.mainloop();