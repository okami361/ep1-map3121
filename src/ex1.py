class Ex1:
    def resolver(self, u0, f, N_in, M_in, lambda_in, g1_in, g2_in):
        
        
        delta_t = lambda_in/pow(N_in,2)
        delta_x = 1/N_in

        ut = []
        t=0
        ut.append(g1_in(t))

        for xi in range(1,N_in):
            ut.append(u0(xi))

        ut.append(g2_in(t))

        for y in range(0, int(M_in)):
            ut_next = ut
            for xi in range(1,N_in):
                ut_next[xi] =ut[xi] + delta_t*((ut[xi-1]-2*ut[xi]+ut[xi+1])*pow(N_in,2) + f(xi*delta_x,t))

            ut= ut_next
            t=t+delta_t
            ut[0] = g1_in(t)
            ut[N_in] = g2_in(t)

        return ut
            