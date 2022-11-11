import turtle
import time
import random
wnd = turtle.Screen()
wnd.title("Pong clase Urtzi")
#color fondo
wnd.bgcolor("black")
wnd.setup(width=800, height=600)
wnd.tracer(0)
# "Raqueta" Izquierda
raq_izq = turtle.Turtle()
raq_izq.speed(0)
raq_izq.shape("square")
raq_izq.color("grey")
raq_izq.penup()
raq_izq.goto(-350, -0)
raq_izq.shapesize(stretch_len=1, stretch_wid=5)
# "Raqueta" Derecha
raq_der = turtle.Turtle()
raq_der.speed(0)
raq_der.shape("square")
raq_der.color("grey")
raq_der.penup()
raq_der.goto(+350, -0)
raq_der.shapesize(stretch_len=1, stretch_wid=5)
# Pelotonsia
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("red")
pelota.goto(0,0)
pelota.penup()
#Marcador
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-0, 260)
pen.write("Jugador izq: 0 Jugador derecha: 0 ",align="center", font=("Calibri", 20, "bold"))
#Ibon tontaco
ibon = turtle.Turtle()
ibon.speed(0)
ibon.color("black")
ibon.penup()
ibon.hideturtle()
ibon.goto(230, -290)
ibon.write("Si ibon lo he hecho yo",align="center", font=("Calibri", 10, "bold"))
#Marcador números
puntos_izq = 0
puntos_der = 0
#Monimiento pelotil
pelota.dx = 0.25
pelota.dy = 0.25
#Movimiento raqueta izquierda
def raq_izq_arriba():
    y = raq_izq.ycor()
    y +=40
    raq_izq.sety(y)
def raq_izq_abajo():
    y = raq_izq.ycor()
    y -=40
    raq_izq.sety(y)
#Movimiento raqueta derecha
def raq_der_arriba():
    y = raq_der.ycor()
    y +=40
    raq_der.sety(y)
def raq_der_abajo():
    y = raq_der.ycor()
    y -=40
    raq_der.sety(y)
def pelota_vuelta():
    pelota.goto(0,0)
    pelota.dx *=-1
def pelota_vuelta1():
    pelota.goto(0,0)
    pelota.dx *=-1
def parar():
    time.sleep(1)
def parar1():
    time.sleep(1)
def lado():
    pelota.dx *=-1
    pelota.dy *=-1
def lado1():
    pelota.dx *=-1
    pelota.dy *=-1
#Parar al principio
time.sleep(2)
#teclas
wnd.listen()
wnd.onkeypress(raq_izq_arriba, "w")
wnd.onkeypress(raq_izq_abajo, "s")
wnd.onkeypress(raq_der_arriba, "Up")
wnd.onkeypress(raq_der_abajo, "Down")
wnd.onkeypress(pelota_vuelta, "d")
wnd.onkeypress(pelota_vuelta1, "1")
wnd.onkeypress(parar, "0")
wnd.onkeypress(parar1, "a")
wnd.onkeypress(lado , "q")
wnd.onkeypress(lado1, "7")
#Bucle actualizar pantalla
while True:
    wnd.update()
    #pelota movimiento
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    #Bordes (ARRIBA y ABAJO)
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1
    #Bordes (Derecha y izquierda)
    if pelota.xcor() > 400:
        pelota.goto (0, 0)
        pelota.dx *= -1
        puntos_izq += 1
        pen.clear()
        pen.write("Jugador izq: {} Jugador derecha: {}".format(puntos_izq, puntos_der),align="center", font=("Calibri", 20, "bold"))
    if pelota.xcor() < -400:
        pelota.goto (0, 0)
        pelota.dx *= -1
        puntos_der += 1
        pen.clear()
        pen.write("Jugador izq: {} Jugador derecha: {}".format(puntos_izq, puntos_der),align="center", font=("Calibri", 20, "bold"))
    #Raquetas hits
    if (pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < raq_der.ycor() + 40 and pelota.ycor() > raq_der.ycor() - 50):
        pelota.setx(340)
        pelota.dx *= -1
    if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < raq_izq.ycor() + 40 and pelota.ycor() > raq_izq.ycor() - 50):
        pelota.setx(-340)
        pelota.dx *= -1
    if puntos_der > 9:
        print("gana derecha")
        exit()
    if puntos_izq > 9:
        print("gana izquierda")
        exit()
