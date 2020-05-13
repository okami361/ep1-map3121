import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from ex1 import Ex1
from ex2 import Ex2
from plot_data import PlotData


def main():

    #Ex1
    # # a
    f = lambda t,x : 10*x*x*(x-1) - 60*x*t + 20*t
    u0 = lambda x : 0
    g1 = lambda t : 0
    g2 = lambda t : 0

    f_exato = lambda t,x : 10*t*pow(x,2)*(x-1)

    # a'
    # f = lambda t,x : 10*math.cos(10*t)*pow(x,2)*pow(1-x,2) - (1+math.sin(10*t))*(12*pow(x,2) - 12*x +2)
    # u0 = lambda x : pow(x,2)*pow(1-x,2)
    # g1 = lambda t : 0
    # g2 = lambda t : 0


    # f_exato = lambda t,x : (1+math.sin(10*t))*pow(x,2)*pow(1-x,2)

    #Ex2
    ex2 = Ex2()

    #c
    # dx = 1/N_in
    # f = lambda t,x : 0 if x>(0.25+(dx/2)) else ( 0 if (x<0.25-(dx/2)) else ((10000*(1-(2*(t**2))))/dx) )
    # u0 = lambda x : 0
    # g1 = lambda t : 0
    # g2 = lambda t : 0

    Ns = [10,20,80,160]


    for N_atual in Ns:
        plt.clf()
        plt.figure(figsize=(10,4))

        x = np.linspace(0,1,N_atual+1)

        plt.subplot2grid((1,2), (0,0))
        PlotDatas, ut_final = ex2.resolver_euler(u0,f,g1,g2,N_atual)
        colors = cm.rainbow(np.linspace(0, 1, len(PlotDatas)))

        for i in range(len(PlotDatas)):
            plt.plot(x,PlotDatas[i].datas, color=colors[i], label = 'Tempo='+str(round(PlotDatas[i].tempo,2)))

        plt.plot(x,ut_final, color='#000000', label = 'Tempo=1')

        plt.legend(loc='best')
        plt.title('Distribuição de Calor N='+str(N_atual))
        plt.xlabel('x: Comprimento da Barra')
        plt.ylabel('u(t,x)')

        plt.subplot2grid((1,2), (0,1))

        y_exato = []
        for xi in x:
            y_exato.append(f_exato(1, xi))

        plt.plot(x,ut_final, color='#808080', label = 'Função Exata')
        plt.plot(x,y_exato, color='#0000FF', label = 'Função Estimada')

        plt.legend(loc='best')
        plt.title('Distribuição de Calor N='+str(N_atual))
        plt.xlabel('x: Comprimento da Barra')
        plt.ylabel('u(t,x)')

        plt.savefig('images\euler_n_'+str(N_atual))

        plt.clf()



if __name__ == "__main__":
    continuar = "s"
    while continuar == "s":
        main()
        print("\nContinuar? (s/n) ")
        continuar = input()