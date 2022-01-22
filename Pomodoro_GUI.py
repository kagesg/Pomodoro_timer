import time
import tkinter as tk
import matplotlib.pyplot as plt

#Variáveis para cálculos:


#Fonte, cores e dimensões da interface
font1 = ('helvetica', 10, 'bold')
bgcolor_button = '#E67E22'
fgcolor_button = '#0000A7'

L_boxes = 8
H_boxes = 6

x1, y1 = 227, 670 #Coordenadas caixa 1
x2, y2 = x1, (y1 + 4*H_boxes) #Coordenadas caixa 2
x3, y3 = x1, 94 #Coordenadas caixa 3
x4, y4 = 340, 12 #Coordenadas caixa 4
xb_1, yb_1 = 900, 100 #Coordenadas botão de setup
xb_2, yb_2 = xb_1+100, 100 #Coordenadas botão de inicio
xb_3, yb_3 = xb_2+100, 100 #Coordenadas botão de cancelar
xd_1, yd_1 = 1200, 500 #Coordenadas Display valores


root = tk.Tk()

#Funções da interface:
def calcular():
    box_1 = field_1.get()
    box_2 = field_2.get()
    box_3 = field_3.get()
    box_4 = field_4.get()
    box_5 = field_5.get()
    box_6 = field_6.get()
    prompt["text"] = box_1, box_2, box_3, box_4


#https://stackoverflow.com/questions/51781651/showing-a-greyed-out-default-text-in-a-tk-entry
def exitfullscreen():
    root.attributes("-fullscreen", False)

def handle_focus_in():
    field_1.delete(0, tk.END)
    field_1.config(fg='black')

def handle_focus_out():
    field_1.delete(0, tk.END)
    field_1.config(fg='grey')
    field_1.insert(0, "Example: Joe Bloggs")

def handle_enter(txt):
    print(field_1.get())
    handle_focus_out('dummy')

#Funções matemáticas


#Frames
frame_q_ent = tk.Frame(root,width=100,highlightbackground='red',highlightthicknes=3)

frame_q_ent.grid(row=2,column=2,padx=20,pady=20,ipadx=20,ipady=20)
frame_q_ent.place(x=1000, y=500)
#frame_f_ent = Frame(root,width=100,highlightbackground='red',highlightthicknes=1)
#frame_f_sai = Frame()

#Imagem de fundo da caldeira
# background_image = tk.PhotoImage(file="2-Boiler800.png")
# background_label = tk.Label(root, image=background_image)
# background_label.place(x=0, y=0) #Adicionar ", relwidth=1, relheight=1" depois da variável y

#Campos para inserir variáveis
field_1 = tk.Entry(root,width=L_boxes, bg='#AED6F1', fg='black', font= font1)
field_1.place(x=x1-L_boxes, y=y1-H_boxes)
field_1.insert(tk.END,'Temperatura entrada')
field_1.bind("<FocusIn>", handle_focus_in)
field_1.bind("<FocusOut>", handle_focus_out)
field_1.bind("<Return>", handle_enter)

field_2 = tk.Entry(root,width=L_boxes, bg='#AED6F1', fg='black', font= font1)
field_2.place(x=x2-L_boxes, y=y2-H_boxes)
field_3 = tk.Entry(root,width=L_boxes, bg='#AED6F1', fg='black', font= font1)
field_3.place(x=x3-L_boxes, y=y3-H_boxes)
field_4 = tk.Entry(root,width=L_boxes, bg='#ABB2B9', fg='black', font= font1)
field_4.place(x=x4-L_boxes, y=y4-H_boxes)


#Botão para definir parâmetros do pomodoro
calculate_button = tk.Button(root, width=L_boxes, text="Setup", command=calcular, bg=bgcolor_button, fg=fgcolor_button, font= font1)
calculate_button.place(x=xb_1, y=yb_1)

#Botão para iniciar/pausar o pomodoro
calculate_button = tk.Button(root, width=L_boxes, text="Start/Pause", command=calcular, bg=bgcolor_button, fg=fgcolor_button, font= font1)
calculate_button.place(x=xb_2, y=yb_2)

#Botão para cancelar o pomodoro
calculate_button = tk.Button(root, width=L_boxes, text="Stop", command=calcular, bg=bgcolor_button, fg=fgcolor_button, font= font1)
calculate_button.place(x=xb_3, y=yb_3)

#Escrever o valor definido para cálculos
prompt = tk.Label(root, text="Display valores",bg='green', fg='white', font= font1)
prompt.place(x=xd_1, y=yd_1)

#Botão para sair do modo fullscreen
#a = tk.Button(root, width=10, text="Exit", command=exitfullscreen)
#a.place(x=1450, y=0)

root.state("zoomed")
root.mainloop()

