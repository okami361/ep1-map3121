import math
import numpy as np
import matplotlib.pyplot as plt
from ex1 import Ex1

def main():

    #Ex1
    #a
    # f = lambda t,x : 10*x*x*(x-1) - 60*x*t + 20*t
    # u0 = lambda x : 0
    # g1 = lambda t : 0
    # g2 = lambda t : 0

    #a'
    f = lambda t,x : 10*math.cos(10*t)*pow(x,2)*pow(1-x,2) - (1+math.sin(10*t))*(12*pow(x,2) - 12*x +2)
    u0 = lambda x : pow(x,2)*pow(1-x,2)
    g1 = lambda t : 0
    g2 = lambda t : 0

    f_exato = lambda t,x : (1+math.sin(10*t))*pow(x,2)*pow(1-x,2)

    print("\nN:")
    N_in = int(input())

    print("\nlambda:")
    lambda_in = float(input())

    M = pow(N_in,2)/lambda_in

    ex1 = Ex1()
    y_estimado = ex1.resolver(u0,f,N_in,M,lambda_in,g1,g2)
    x = np.linspace(0,1,N_in+1)
    plt.plot(x,y_estimado, color='#0000FF') # cor azul

    y_exato = []
    for xi in x:
        y_exato.append(f_exato(1, xi))

    plt.plot(x,y_exato,color='#808080')  # cor cinza

    plt.title('Distribuição do Calor em t=1')
    plt.xlabel('x: Comprimento da Barra')
    plt.ylabel('u(1,x)')

    erro = 0
    for i in range(len(y_estimado)):
        e = abs (y_estimado[i] - y_exato[i])
        if e > erro: 
            erro = e
    print("\nErro Máximo: ", erro)

    plt.show()

if __name__ == "__main__":
    continuar = "s"
    while continuar == "s": 
        main()
        print("\nContinuar? (s/n) ")
        continuar = input()