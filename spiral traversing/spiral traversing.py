import random
import turtle
turtle.bgcolor("black")

oviya = turtle.Turtle()
widht = 5
height  = 7
dot_distance = 25
oviya.penup()
list_colors=["blue","red","green","orange","pink","violet","yellow","purple","white"]
oviya.setpos(-250,250)

def spiral(k,l):
    '''
       k=no of rows
       l=no of columns
       a=matrix
    '''
    m=0  #starting index of row
    n=0  #starting index of column
    f=0
    color=random.randint(0,10)
    oviya.color(list_colors[color])

    while(m<k and n<l):

        if(f==1):
            oviya.right(90)

        for i in range(n , l):
            oviya.dot()
            oviya.forward(dot_distance)
            #print(a[m][i], end=" ")
        m+=1
        f=1
        color=random.randint(0,10)
        oviya.color(list_colors[color])

        oviya.right(90)

        for i in range(m, k):
            oviya.dot()
            oviya.forward(dot_distance)
            #print(a[i][l-1], end=" ")
        l-=1
        color=random.randint(0,10)
        oviya.color(list_colors[color])
        oviya.right(90)

        if(n<l):
            for i in range(l-1, n-1, -1):
                oviya.dot()
                oviya.forward(dot_distance)
                #print(a[k-1][i], end=" ")
            k-=1
        color=random.randint(0,10)
        oviya.color(list_colors[color])
        oviya.right(90)
    
        if(m<k):
            for i in range(k-1, m-1, -1):
                oviya.dot()
                oviya.forward(dot_distance)
                #print(a[i][n],end=" ")
            n+=1        


spiral(20,20)
turtle.done()

#try to do the same using recursion


