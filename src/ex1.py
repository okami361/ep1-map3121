class Ex1:
    def resolver(self, u0, f, N_in, M_in, lambda_in, g1_in, g2_in):
        
        
        delta_t = lambda_in/pow(N_in,2)

        ut = []
        t=0
        ut.append(g1_in(t))

        for x in range(1,N_in):
            ut.append(u0(x))

        ut.append(g2_in(t))

        for y in range(0, int(M_in)):
            ut_next = ut
            for x in range(1,N_in):
                ut_next[x] = delta_t*((ut[x-1]-2*ut[x]+ut[x+1])*pow(N_in,2) + f(x,t))

            ut= ut_next
            t=t+delta_t
            ut[0] = g1_in(t)
            ut[N_in] = g2_in(t)

        print(ut)
            