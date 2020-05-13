import numpy as np
from plot_data import PlotData

class Ex2:


    #Os métodos implementados foram feitos para a resolução específica do exercício, não sendo válidos para caso geral.
    def resolver_euler(self, u0_in, f_in, g1_in, g2_in, N_in):
        
        delta_t = delta_x = 1/N_in
        lambda_calc = 1/delta_x
        
        a_diagonal, a_sub_diagonal = self.calc_decomp(self.gerar_matriz_euler(N_in, lambda_calc))

        ut = []
        for xi in range(1,N_in):
            ut.append(u0_in(xi*delta_x))

        contador_adicionar_novo_plot = 0
        PlotDatas = []

        for i in range(0, N_in):
            t=delta_t*i

            if contador_adicionar_novo_plot<=t:
                ut_aux = []
                ut_aux.append(g1_in(t))
                for x in range(0,N_in-1):
                    ut_aux.append(ut[x])
                ut_aux.append(g2_in(t))

                PlotDatas.append(PlotData(contador_adicionar_novo_plot, ut_aux.copy()))
                contador_adicionar_novo_plot = contador_adicionar_novo_plot + 0.1

            ut[0] = ut[0]+lambda_calc*g1_in(t+delta_t)
            ut[N_in-2] = ut[N_in-2]+lambda_calc*g2_in(t+delta_t)

            for x in range(0,N_in-1):
                ut[x] = ut[x] + delta_t*f_in(t+delta_t,(x+1)*delta_x)

            
            temp = self.substituicao_direta(a_sub_diagonal, ut)
            temp = self.resolver_diagonal(a_diagonal, temp)
            ut = self.substituicao_inversa(a_sub_diagonal, temp).copy()

        ut_final = []
        ut_final.append(g1_in(1))
        for x in range(0,N_in-1):
            ut_final.append(ut[x])
        ut_final.append(g2_in(1))

        return PlotDatas, ut_final

    def resolver_crank_nicolson(self, u0_in, f_in, g1_in, g2_in, N_in):
        
        delta_t = delta_x = 1/N_in
        lambda_calc = 1/delta_x
        
        a_diagonal, a_sub_diagonal = self.calc_decomp(self.gerar_matriz_crank_nicolson(N_in, lambda_calc))

        ut = []
        for xi in range(1,N_in):
            ut.append(u0_in(xi*delta_x))


        for i in range(0, N_in):
            t=delta_t*i

            ut_aux = [None]*(N_in-1)

            ut_aux[0] = ut[0]+(lambda_calc/2)*(g1_in(t)-2*ut[0]+ut[1]) + (delta_t/2)*(f_in(t,delta_x) + f_in(t+delta_t,delta_x)) + (lambda_calc/2)*g1_in(t+delta_t)
            ut_aux[N_in-2] = ut[N_in-2]+(lambda_calc/2)*(ut[N_in-3]-2*ut[N_in-2]+g2_in(t)) + (delta_t/2)*(f_in(t,(N_in-1)*delta_x) + f_in(t+delta_t,(N_in-1)*delta_x)) + (lambda_calc/2)*(g2_in(t+delta_t))
            for x in range(1,N_in-2):
                ut_aux[x] = ut[x]+(lambda_calc/2)*(ut[x-1]-2*ut[x]+ut[x+1]) + (delta_t/2)*(f_in(t,(x+1)*delta_x) + f_in(t+delta_t,(x+1)*delta_x))

            ut=ut_aux.copy()
            
            temp = self.substituicao_direta(a_sub_diagonal, ut)
            temp = self.resolver_diagonal(a_diagonal, temp)
            ut = self.substituicao_inversa(a_sub_diagonal, temp)

        ut_final = []
        ut_final.append(g1_in(1))
        for x in range(0,N_in-1):
            ut_final.append(ut[x])
        ut_final.append(g2_in(1))

        return ut_final


    #https://themadcreator.github.io/luqr/
    #usado para a função Ly=b
    def substituicao_direta(self, sub_diagonal, b):
        
        if(len(sub_diagonal) != len(b)-1):
            raise ValueError('Dimensoes impossiveis de serem resolvidas:'+str(len(sub_diagonal))+','+str(len(b))) 
        
        resolvido = [b[0]]

        for i in range(1,len(b)):
            resolvido.append(b[i]-sub_diagonal[i-1]*resolvido[i-1])


        return resolvido

    #usado para a função Dz =y
    def resolver_diagonal(self, diagonal, y):

        if(len(diagonal) != len(y)):
            raise ValueError('Dimensoes impossiveis de serem resolvidas:'+str(len(diagonal))+','+str(len(y))) 

        resolvido = []
        for i in range(len(diagonal)):
            resolvido.append(y[i]/diagonal[i])

        return resolvido

    #usado para a função (L^t)x=z
    def substituicao_inversa(self, sub_diagonal, z):
        
        if(len(sub_diagonal) != len(z)-1):
            raise ValueError('Dimensoes impossiveis de serem resolvidas:'+str(len(sub_diagonal))+','+str(len(z))) 
        
        resolvido = [z[len(z)-1]]

        for i in range(len(z)-2,-1,-1):
            resolvido.append(z[i]-sub_diagonal[i]*resolvido[len(resolvido)-1])

        resolvido.reverse()

        return resolvido
 
    def gerar_matriz_euler(self, N_in, lambda_in):
        A = np.identity(N_in-1)
        for i in range(0,len(A)):
            A[i][i] = 1+2*lambda_in

        for i in range(0,len(A)-1):
            A[i+1][i] = -lambda_in
            A[i][i+1] = -lambda_in
        
        return A

    def gerar_matriz_crank_nicolson(self, N_in, lambda_in):
        A = np.identity(N_in-1)
        for i in range(0,len(A)):
            A[i][i] = 1+lambda_in

        for i in range(0,len(A)-1):
            A[i+1][i] = -lambda_in/2
            A[i][i+1] = -lambda_in/2
        
        return A
        

    def calc_decomp(self,A_in):
        diagonal = []
        sub_diagonal = []
        
        for i in range(0,len(A_in)-1):
            aux_matriz = np.identity(len(A_in))
            aux_indice = A_in[i+1][i]/A_in[i][i]
            sub_diagonal.append(aux_indice)
            aux_matriz[i+1][i] = -aux_indice
            
            A_in = aux_matriz.dot(A_in)

        for i in range(0,len(A_in)):
            diagonal.append(A_in[i][i])

        #self.conferir_LDL(diagonal, sub_diagonal)

        return diagonal, sub_diagonal

    #Fiz mais para conferir o cálculo
    def conferir_LDL(self, diagonal, sub_diagonal):
        L = np.identity(len(diagonal))
        D = np.identity(len(diagonal))

        for i in range(0,len(diagonal)):
            D[i][i] = diagonal[i]

        for i in range(0,len(diagonal)-1):
            L[i+1][i] = sub_diagonal[i]

        print(L.dot(D).dot(L.transpose()))

        return None