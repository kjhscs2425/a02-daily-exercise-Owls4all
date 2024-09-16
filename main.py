import turtle
#
#-setting up shortcuts-#
t=turtle
def L():
    t.left(90)
def go(d):
    t.forward(d)
def R():
    t.right(90)
#----------------------#
side=20
R()
for i in range(1,13):
    go(i*side)
    R()

t.exitonclick()