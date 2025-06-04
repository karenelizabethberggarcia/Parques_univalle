import tkinter as tk
import turtle

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Parqués - Juego de mesa")
ventana.geometry("800x400")
ventana.configure(bg="#000000")

etiquetas = tk.Label(ventana, text=" Hola, Bienveni@s al Juego ",
                     font=("OCR A Extended", 30),
                     fg="#ffffff", bg="#000000")
etiquetas.pack(pady=25)

n_jugadores = tk.Label(ventana, text="Ingresa el número de Jugadores :",
                       font=("OCR A Extended", 19),
                       fg="#ffffff", bg="#000000")
n_jugadores.pack(pady=20)

no_jugadores = tk.Entry(ventana, width=10, font=("OCR A Extended", 19))
no_jugadores.pack(pady=10)

mensaje = tk.Label(ventana, text="", font=("OCR A Extended", 15),
                   fg="yellow", bg="#000000")
mensaje.pack(pady=10)

def iniciar_tablero():
    ventana.destroy()

    def seguros(t, x, y,color):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color("black", color)
        t.begin_fill()
        t.setheading(270)
        t.circle(13)
        t.end_fill()
        t.penup()

    def dibujar_circulo_color(t, x, y, color, radio=100):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color("black", color)
        t.begin_fill()
        t.circle(radio)
        t.end_fill()
        t.penup()

    def colores_por_casa(t):
        # Color meta 1 - ROJO
        t.color("#ff0000")
        t.begin_fill()
        t.penup()
        t.goto(-33, 273)
        t.pendown()
        t.setheading(270)
        t.forward(88)
        t.setheading(180)
        t.forward(67)
        t.setheading(270)
        t.forward(29)
        t.setheading(0)
        t.forward(67)
        t.setheading(270)
        t.forward(86)
        t.setheading(180)
        t.forward(36)
        t.setheading(315)
        t.forward(99)
        t.setheading(45)
        t.forward(99)
        t.setheading(180)
        t.forward(37)
        t.setheading(90)
        t.forward(203)
        t.setheading(180)
        t.forward(67)
        t.end_fill()
        t.penup()

        # Color meta 2 - VERDE
        t.color("#82f06e")
        t.begin_fill()
        t.penup()
        t.goto(-272, -33)
        t.setheading(0)
        t.pendown()
        t.forward(88)
        t.setheading(270)
        t.forward(67)
        t.setheading(0)
        t.forward(29)
        t.setheading(90)
        t.forward(67)
        t.setheading(0)
        t.forward(85)
        t.setheading(270)
        t.forward(36)
        t.setheading(45)
        t.forward(99)
        t.setheading(135)
        t.forward(99)
        t.setheading(270)
        t.forward(37)
        t.setheading(180)
        t.forward(201)
        t.setheading(270)
        t.forward(66)
        t.end_fill()
        t.penup()

        # Color meta 3 - AMARILLO
        t.color("#f6ff00")
        t.begin_fill()
        t.penup()
        t.goto(33, -273)
        t.setheading(90)
        t.pendown()
        t.forward(86)
        t.setheading(0)
        t.forward(67)
        t.setheading(90)
        t.forward(29)
        t.setheading(180)
        t.forward(67)
        t.setheading(90)
        t.forward(88)
        t.setheading(0)
        t.forward(37)
        t.setheading(135)
        t.forward(99)
        t.setheading(225)
        t.forward(99)
        t.setheading(0)
        t.forward(37)
        t.setheading(270)
        t.forward(205)
        t.setheading(0)
        t.forward(70)
        t.end_fill()
        t.penup()

        # Color meta 4 - AZUL
        t.color("#746df2")
        t.begin_fill()
        t.penup()
        t.goto(274, 33)
        t.setheading(180)
        t.pendown()
        t.forward(87)
        t.setheading(90)
        t.forward(67)
        t.setheading(180)
        t.forward(29)
        t.setheading(270)
        t.forward(67)
        t.setheading(180)
        t.forward(86)
        t.setheading(90)
        t.forward(36)
        t.setheading(225)
        t.forward(99)
        t.setheading(315)
        t.forward(99)
        t.setheading(90)
        t.forward(37)
        t.setheading(0)
        t.forward(202)
        t.setheading(90)
        t.forward(67)
        t.end_fill()
        t.penup()

        t.speed(0)
        t.color("#000000")

    def dibujar_margen_exterior(t):
        t.penup()
        t.goto(-325, 325)
        t.pendown()
        t.pensize(30)
        t.color("#744103")
        for _ in range(4):
            t.forward(650)
            t.right(90)
        t.pensize(1)

    def dibujar_cuadro_interior(t):
        t.penup()
        t.goto(-300, 300)
        t.pendown()
        t.color("black")
        for _ in range(4):
            t.forward(600)
            t.right(90)
        t.penup()

    def dibujar_cruz(t):
        t.forward(200)
        t.right(90)
        t.pendown()
        t.forward(600)
        t.penup()
        t.left(90)
        t.pendown()
        t.forward(200)
        t.left(90)
        t.forward(600)
        t.right(90)
        t.penup()
        t.forward(200)
        t.right(90)
        t.forward(200)
        t.pendown()
        t.right(90)
        t.forward(600)
        t.penup()
        t.left(90)
        t.pendown()
        t.forward(200)
        t.left(90)
        t.forward(600)
        t.penup()

    def dibujar_centro(t):
        t.setheading(0)
        t.goto(-70, 70)
        t.pendown()
        for _ in range(4):
            t.forward(140)
            t.right(90)
        t.penup()

        t.goto(-100, 100)
        t.setheading(-45)
        t.pendown()
        t.forward(284)
        t.penup()

        t.goto(-100, -100)
        t.setheading(45)
        t.pendown()
        t.forward(284)
        t.penup()

    def casillas(t):
        t.speed(0)
        t.setheading(0)
        t.color("black")

        t.penup()
        t.goto(-100, 300)
        t.forward(67)
        t.pendown()
        t.right(90)
        t.forward(230)
        t.left(90)
        t.penup()
        t.forward(67)
        t.setheading(90)
        t.pendown()
        t.forward(230)
        t.setheading(0)
        t.forward(67)
        t.penup()

        t.goto(-100, -300)
        t.forward(67)
        t.pendown()
        t.left(90)
        t.forward(230)
        t.right(90)
        t.penup()
        t.forward(67)
        t.right(90)
        t.pendown()
        t.forward(230)
        t.setheading(0)
        t.penup()

        t.goto(-300, 100)
        for _ in range(3):
            t.pendown()
            t.forward(29)
            t.right(90)
            t.forward(200)
            t.left(90)
            t.forward(29)
            t.left(90)
            t.forward(200)
            t.right(90)
            t.penup()

        t.goto(100, 100)
        for _ in range(3):
            t.pendown()
            t.forward(29)
            t.right(90)
            t.forward(200)
            t.left(90)
            t.forward(29)
            t.left(90)
            t.forward(200)
            t.right(90)
            t.penup()

        t.goto(300, 100)
        t.setheading(270)
        t.forward(67)
        t.pendown()
        t.right(90)
        t.forward(230)
        t.left(90)
        t.penup()
        t.forward(67)
        t.pendown()
        t.setheading(0)
        t.forward(230)
        t.penup()

        t.goto(-300, 100)
        t.setheading(270)
        t.forward(67)
        t.pendown()
        t.left(90)
        t.forward(230)
        t.right(90)
        t.penup()
        t.forward(67)
        t.pendown()
        t.setheading(180)
        t.forward(230)
        t.penup()

        t.goto(-100, 300)
        for _ in range(3):
            t.pendown()
            t.setheading(270)
            t.forward(29)
            t.left(90)
            t.forward(200)
            t.right(90)
            t.forward(29)
            t.right(90)
            t.forward(200)
            t.penup()

        t.goto(-100, -100)
        for _ in range(3):
            t.pendown()
            t.color("black")
            t.setheading(270)
            t.forward(29)
            t.left(90)
            t.forward(200)
            t.right(90)
            t.forward(29)
            t.right(90)
            t.forward(200)
            t.penup()

        t.speed(0)

    wn = turtle.Screen()
    wn.title("Tablero de Parqués")
    wn.bgcolor("white")
    wn.setup(width=800, height=800)

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(1)

    dibujar_margen_exterior(t)
    colores_por_casa(t)
    t.setheading(0)
    dibujar_cuadro_interior(t)
    dibujar_cruz(t)
    
    dibujar_centro(t)
    casillas(t)
    t.setheading(180)

    circulos = [
        (-200, 300, "#ff0000"),
        (200, 300, "#746df2"),
        (-200, -100, "#82f06e"),
        (200, -100, "#f6ff00")
    ]

    seguro = [
        (-13, 286,"#a1a1a1"), (-80, 170,"#ff0000"), (56,  170,"#a1a1a1"),
        (-13, -286,"#a1a1a1"), (-80, -173,"#a1a1a1"), (56, -173,"#f6ff00"),
        (275, 6,"#a1a1a1"),(160,65,"#746df2"), (160, -65,"#a1a1a1"),
        (-298, 6,"#a1a1a1"), (-183, 65,"#a1a1a1"), (-183, -65,"#82f06e")
    ]

    for x, y ,color in seguro:
        seguros(t, x, y,color)

    for x, y, color in circulos:
        t.setheading(180)
        dibujar_circulo_color(t, x, y, color)

    t.hideturtle()
    wn.mainloop()

def seleccionar_jugadores():
    try:
        jugadores = int(no_jugadores.get())
        if jugadores < 2 or jugadores > 4:
            raise ValueError("Número de jugadores debe ser entre 2 y 4")
        mensaje.config(text=f"Seleccionaste {jugadores} jugadores", fg="lightgreen")
        ventana.after(100, iniciar_tablero)
    except ValueError as e:
        mensaje.config(text=f"Error: {e}", fg="#ff0000")
        no_jugadores.delete(0, tk.END)

iniciar_juego = tk.Button(ventana, text="Jugar",
                          font=("OCR A Extended", 29),
                          fg="white", bg="black",
                          activebackground="#FF0000",
                          activeforeground="#000000",
                          command=seleccionar_jugadores)
iniciar_juego.pack(pady=30)

ventana.mainloop()