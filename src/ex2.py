import numpy as np

#https://www.youtube.com/watch?v=1Fl4PjbD2Y8

class Ex2:


    #TODO: segundo o roteiro é para ser usado N-1, mas não penso que faça sentido. Conferir quando possível
    def resolver_euler(self, u0_in, f_in, g1_in, g2_in, N_in):
        
        delta_t = delta_x = 1/N_in
        lambda_calc = 1/delta_x
        
        a_diagonal, a_sub_diagonal = self.calc_decomp(self.gerar_matriz(N_in, lambda_calc))

        ut = []
        ut.append(g1_in(0))
        for xi in range(1,N_in-1):
            ut.append(u0_in(xi*delta_x))
        ut.append(g2_in(0))


        for t in range(0, 1, delta_t):
            ut[0] = ut[0] + lambda_calc*g1_in(t+delta_t)
            ut[N_in-1] = ut[N_in-1] + lambda_calc*g2_in(t+delta_t)

            for x in range(0,N_in):
                ut[x] = ut[x] + delta_t*f_in(t+delta_t,x*delta_x)
            
            temp = self.substituicao_direta(a_sub_diagonal, ut)
            temp = self.resolver_diagonal(a_diagonal, temp)


        return None


    #https://themadcreator.github.io/luqr/
    #Ax=B, usado para a função L
    def substituicao_direta(self, sub_diagonal, b):
        
        if(len(sub_diagonal-1) != len(b)):
            raise ValueError('Dimensoes impossiveis de serem resolvidas') 
        
        resolvido = [b[0]]

        for i in range(1,len(b)):
            resolvido.append(b[i]-sub_diagonal[i-1])


        return resolvido

    def resolver_diagonal(self, diagonal, y):

        if(len(diagonal) != len(y)):
            raise ValueError('Dimensoes impossiveis de serem resolvidas') 

        resolvido = []
        for i in range(len(diagonal)):
            resolvido.append(y[i]/diagonal[i])

        return resolvido



    def gerar_matriz(self, N_in, lambda_in):
        A = np.identity(N_in -1)
        for i in range(0,len(A)):
            A[i][i] = 1+2*lambda_in

        for i in range(0,len(A)-1):
            A[i+1][i] = -lambda_in
            A[i][i+1] = -lambda_in
        
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

        self.conferir_LDL(diagonal, sub_diagonal)

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