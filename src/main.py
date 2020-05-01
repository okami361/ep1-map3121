import math
import numpy as np
import matplotlib.pyplot as plt
from ex1 import Ex1

def main():

    #Ex1
    f = lambda t,x : 10*x*x*(x-1) - 60*x*t + 20*t
    u0 = lambda x : 0
    g1 = lambda t : 0
    g2 = lambda t : 0

    f_exato = lambda t,x : 10*t*x*x*(x-1)

    print("\nN:")
    N_in = int(input())

    print("\nlambda:")
    lambda_in = float(input())

    M = pow(N_in,2)/lambda_in

    ex1 = Ex1()
    y_estimado = ex1.resolver(u0,f,N_in,M,lambda_in,g1,g2)
    x = np.linspace(0,1,N_in+1)
    plt.scatter(x,y_estimado)
    
    y_exato = []
    for xi in x:
        y_exato.append(f_exato(1, xi))
      
    plt.scatter(x,y_exato)
    
    plt.show()
if __name__ == "__main__":
    main()