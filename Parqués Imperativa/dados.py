import turtle
import tkinter as tk
from tkinter import *
import random

ventana = turtle.Screen()
ventana.title("¡¡¡ Tira Los Dados !!!")
ventana.bgcolor("white")
ventana.setup(width = 400, height = 300)
ventana.screensize(400, 400)
ventana.tracer(0)
ventana.setworldcoordinates(-200, -200, 200, 200)



dado1 = [   [(-150, 150, "white"), (-100, 100, "black"), (-50, 50, "white"), (-50, 150, "white"), 
             (-150, 50, "white"), (-150, 100, "white"), (-50, 100, "white")],



            [(-150, 150, "black"), (-100, 100, "white"), (-50, 50, "black"), (-50, 150, "white"), 
             (-150, 50, "white"), (-150, 100, "white"), (-50, 100, "white")],


             [(-150, 150, "black"), (-100, 100, "black"), (-50, 50, "black"), (-50, 150, "white"), 
             (-150, 50, "white"), (-150, 100, "white"), (-50, 100, "white")],

             [(-150, 150, "black"), (-100, 100, "white"), (-50, 50, "black"), (-50, 150, "black"), 
             (-150, 50, "black"), (-150, 100, "white"), (-50, 100, "white")],

             [(-150, 150, "black"), (-100, 100, "black"), (-50, 50, "black"), (-50, 150, "black"), 
             (-150, 50, "black"), (-150, 100, "white"), (-50, 100, "white")],

             [(-150, 150, "black"), (-100, 100, "white"), (-50, 50, "black"), (-50, 150, "black"), 
             (-150, 50, "black"), (-150, 100, "black"), (-50, 100, "black")]

         ]

dado2 = [   [(-150, 150, "white"), (-100, 100, "black"), (-50, 50, "white"), (-50, 150, "white"), 
             (-150, 50, "white"), (-150, 100, "white"), (-50, 100, "white")],



            [(-150, 150, "black"), (-100, 100, "white"), (-50, 50, "black"), (-50, 150, "white"), 
             (-150, 50, "white"), (-150, 100, "white"), (-50, 100, "white")],


             [(-150, 150, "black"), (-100, 100, "black"), (-50, 50, "black"), (-50, 150, "white"), 
             (-150, 50, "white"), (-150, 100, "white"), (-50, 100, "white")],

             [(-150, 150, "black"), (-100, 100, "white"), (-50, 50, "black"), (-50, 150, "black"), 
             (-150, 50, "black"), (-150, 100, "white"), (-50, 100, "white")],

             [(-150, 150, "black"), (-100, 100, "black"), (-50, 50, "black"), (-50, 150, "black"), 
             (-150, 50, "black"), (-150, 100, "white"), (-50, 100, "white")],

             [(-150, 150, "black"), (-100, 100, "white"), (-50, 50, "black"), (-50, 150, "black"), 
             (-150, 50, "black"), (-150, 100, "black"), (-50, 100, "black")]

            ]
         
         
def generar_dados(x, y):
        print(f"¡Haz hecho click en las coordenadas {x} y {y}!")  
        if boton_x <= x <= boton_x + ancho_boton:
            if boton_y <= y <= boton_y + alto_boton:
                cont = 0         
                while cont < 2:
                    lado1 = random.randrange(1, 7)
                    tortugas = [turtle.Turtle() for _ in range(7)]

                    for i in range(7):
                        tortugas[i].shape("circle")
                        tortugas[i].color(dado1[lado1 - 1][i][2])
                        tortugas[i].penup()
                        tortugas[i].goto(dado1[lado1 - 1][i][0], dado1[lado1 - 1][i][1])
                        ventana.update()
                    cont += 1
                    if cont == 1:
                        lado2 = random.randrange(1, 7)
                        if lado2 == lado1:
                             print("¡¡¡ PAR !!!")
                        tortugas = [turtle.Turtle() for _ in range(7)]
                        for i in range(7):
                            tortugas[i].shape("circle")
                            tortugas[i].color(dado2[lado2-1][i][2])
                            tortugas[i].penup()
                            tortugas[i].goto(dado2[lado2 - 1][i][0] + 200, dado2[lado2 - 1][i][1])
                            ventana.update()
                        cont += 1
                        


boton = turtle.Turtle()
boton.hideturtle()

boton_x = -50
boton_y = -70
ancho_boton = 180
alto_boton = 50


def dibujar_boton(boton1):
    boton1.penup()
    boton1.fillcolor("#BBA9BB")
    boton1.begin_fill()
    boton1.goto(boton_x, boton_y)
    boton1.goto(boton_x + ancho_boton, boton_y)
    boton1.goto(boton_x + ancho_boton, boton_y + alto_boton)
    boton1.goto(boton_x, boton_y + alto_boton)
    boton1.goto(boton_x, boton_y)
    boton1.end_fill()
    boton1.goto(boton_x + 15, boton_y + 15)
    boton1.write("Lanzar dados", font = ("Arial", 12, "bold"))

dibujar_boton(boton)



ventana.onclick(generar_dados)
ventana.update()
ventana.mainloop()