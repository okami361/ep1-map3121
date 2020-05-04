import numpy as np

#https://www.youtube.com/watch?v=1Fl4PjbD2Y8

class Ex2:

    def resolver(self,lambda_in,A_in):
        diagonal_a = []
        sub_diagonal_a = []
        
        for i in range(0,len(A_in)-1):
            aux_matriz = np.identity(len(A_in))
            aux_indice = A_in[i+1][i]/A_in[i][i]
            sub_diagonal_a.append(aux_indice)
            aux_matriz[i+1][i] = -aux_indice
            
            A_in = aux_matriz.dot(A_in)

        for i in range(0,len(A_in)):
            diagonal_a.append(A_in[i][i])

        self.calc_LDL(diagonal_a, sub_diagonal_a)

        return None

    def calc_LDL(self, diagonal, sub_diagonal):
        L = np.identity(len(diagonal))
        D = np.identity(len(diagonal))

        for i in range(0,len(diagonal)):
            D[i][i] = diagonal[i]

        for i in range(0,len(diagonal)-1):
            L[i+1][i] = sub_diagonal[i]

        print(L.dot(D).dot(L.transpose()))

        return None

    def resolver_euler(self,lambda_in,A_in):

        return None