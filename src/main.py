import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
from ex1 import Ex1
from ex2 import Ex2
from plot_data import PlotData
from exercicio_data import ExercicioData


def main():

    exercicios = []

    exercicios.append(ExercicioData('a',
        lambda t,x,dx : 10*x*x*(x-1) - 60*x*t + 20*t,
        lambda x : 0,
        lambda t : 0,
        lambda t : 0,
        f_exato = lambda t,x : 10*t*pow(x,2)*(x-1)))

    exercicios.append(ExercicioData('a_linha',
        lambda t,x,dx : 10*math.cos(10*t)*(x**2)*((1-x)**2) - (1+math.sin(10*t))*(12*x**2 - 12*x +2),
        lambda x : (x**2)*((1-x)**2),
        lambda t : 0,
        lambda t : 0,
        lambda t,x : (1+math.sin(10*t))*(x**2)*((1-x)**2)))

    exercicios.append(ExercicioData('b',
        lambda t,x,dx : math.exp(t-x)*math.cos(5*t*x)-(-25*math.exp(t-x)*(t**2)*math.cos(5*t*x)+10*math.exp(t-x)*t*math.sin(5*t*x)),
        lambda x : math.exp(-x),
        lambda t :math.exp(t),
        lambda t : math.exp(t-1)*math.cos(5*t),
        lambda t,x : math.exp(t-x)*math.cos(5*t*x)))

    exercicios.append(ExercicioData('c',
        lambda t,x,dx :  0 if x > (0.25+(dx/2)) else (0 if (x <0.25-(dx/2)) else ((10000*(1-(2*(t**2))))/dx)),
        lambda x : 0,
        lambda t : 0,
        lambda t : 0,
        None))

    Ns = [10, 20, 40, 80, 160, 320]

    ex2 = Ex2()

    for exercicio_atual in exercicios:
        print('\n---------------------------------------------------------------------------------------')
        print('Exercicio:'+exercicio_atual.nome)
        for N_atual in Ns:
            print('\nN:'+str(N_atual))
            x = np.linspace(0, 1, N_atual+1)

            PlotDatas_euler, y_estimado_euler = ex2.resolver_euler(exercicio_atual.u0, exercicio_atual.f, exercicio_atual.g1, exercicio_atual.g2, N_atual)
            PlotDatas_crank, y_estimado_crank = ex2.resolver_crank_nicolson(exercicio_atual.u0, exercicio_atual.f, exercicio_atual.g1, exercicio_atual.g2, N_atual)


            y_exato = None
            if not exercicio_atual.f_exato is None:
                y_exato = []
                for xi in x:
                    y_exato.append(exercicio_atual.f_exato(1, xi))

            plot(y_exato, y_estimado_euler, PlotDatas_euler, N_atual, 'Euler_'+exercicio_atual.nome+'_'+str(N_atual))
            plot(y_exato, y_estimado_crank, PlotDatas_crank, N_atual, 'Crank_'+exercicio_atual.nome+'_'+str(N_atual))

            if not exercicio_atual.f_exato is None:
                print('Euler:')
                calc_erro(y_exato,y_estimado_euler, N_atual)
                print('Crank:')
                calc_erro(y_exato,y_estimado_crank, N_atual)


def plot(y_exato, y_estimado, PlotDatas, N, nome):
    plt.figure(figsize=(10, 4))

    x = np.linspace(0, 1, N+1)
    plt.subplot2grid((1, 2), (0, 0))
    colors = cm.rainbow(np.linspace(0, 1, len(PlotDatas)))

    for i in range(len(PlotDatas)):
        plt.plot(x, PlotDatas[i].datas, color=colors[i],
                    label='Tempo='+str(round(PlotDatas[i].tempo, 2)))

    plt.plot(x, y_estimado, color='#000000', label='Tempo=1')

    plt.legend(loc='best')
    plt.title('Distribuição de Calor N='+str(N))
    plt.xlabel('x: Comprimento da Barra')
    plt.ylabel('u(t,x)')

    plt.subplot2grid((1, 2), (0, 1))

    if not y_exato is None:
        plt.plot(x,y_exato, color='#808080', label = 'Função Exata')

    plt.plot(x, y_estimado, color='#0000FF', label='Função Estimada')

    plt.legend(loc='best')
    plt.title('Distribuição de Calor N='+str(N))
    plt.xlabel('x: Comprimento da Barra')
    plt.ylabel('u(t,x)')

    plt.savefig('images\\'+nome)
    plt.clf()
    plt.close()



def calc_erro(y_exato,y_estimado, N):
    erro = 0
    erro_percentual=0
    for i in range(len(y_estimado)):
        e = abs (y_exato[i]-y_estimado[i])
        if e > erro: 
            erro = e
            erro_percentual = 100*abs((y_exato[i]-y_estimado[i])/y_exato[i])

    print("Erro Máximo: ", erro)

if __name__ == "__main__":
    main()
