import turtle

t = turtle.Turtle()

def zeichne_boden():
    t.up()
    t.goto(-150, -150)
    t.down()
    t.forward(100)

def zeichne_senkrechten_balken():
    t.backward(50)
    t.left(90)
    t.forward(250)

def zeichne_waagerechten_balken():
    t.right(90)
    t.forward(100)

def zeichne_schraege():
    t.up()
    t.goto(-100, 50)
    t.left(45)
    t.down()
    t.forward(70)

def zeichne_schlaufe():
    t.up()
    t.goto(0, 100)
    t.right(135)
    t.down()
    t.forward(40)

def zeichne_kopf():
    t.up()
    t.goto(-20, 40)
    t.down()
    t.circle(20)

def zeichne_koerper():
    t.up()
    t.goto(0, 20)
    t.down()
    t.forward(80)

def zeichne_linken_arm():
    t.up()
    t.backward(60)
    t.right(-45)
    t.down()
    t.forward(40)

def zeichne_rechten_arm():
    t.up()
    t.backward(40)
    t.right(90)
    t.down()
    t.forward(40)

def zeichne_linkes_bein():
    t.up()
    t.backward(40)
    t.right(-45)
    t.forward(60)
    t.left(45)
    t.down()
    t.forward(40)

def zeichne_rechtes_bein():
    t.backward(40)
    t.right(90)
    t.down()
    t.forward(40)

def zeichne_stufe(fehler):
    if(fehler == 1):
        zeichne_boden()
    if(fehler == 2):
        zeichne_senkrechten_balken()
    if(fehler == 3):
        zeichne_waagerechten_balken()
    if(fehler == 4):
        zeichne_schraege()
    if(fehler == 5):
        zeichne_schlaufe()
    if(fehler == 6):
        zeichne_kopf()
        zeichne_koerper()
        zeichne_linken_arm()
        zeichne_rechten_arm()
        zeichne_linkes_bein()
        zeichne_rechtes_bein()


