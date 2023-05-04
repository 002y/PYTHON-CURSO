a = 2
c = 1
def soma(a=0, b=0, c=0):
    """
    -> soma "a" mais "b" e mostra na tela, se não der valor para "a,b,c", eles recebem 0
    """
    a = 5
    s = a + b + c
    print(s)



soma(1, a, 2)
help(soma)
####

def valor():
    global c #pegando o "c" do programa principal ou, escopo global
    c = 5
    print(c)


print(c)
valor()
