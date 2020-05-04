class Ex1:
    def resolver(self, u0, f, N_in, M_in, lambda_in, g1_in, g2_in,x, plt):
        
        t_counter = 0

        delta_t = 1/M_in
        delta_x = 1/N_in

        ut = []

        ut.append(g1_in(0))
        for xi in range(1,N_in):
            ut.append(u0(xi*delta_x))
        ut.append(g2_in(0))

        for y in range(1, int(M_in+1)):
            ut_next = ut.copy()
            for xi in range(1,N_in):
                ut_next[xi] = ut[xi] + delta_t*((ut[xi-1]-2*ut[xi]+ut[xi+1])/pow(delta_x,2) + f(y*delta_t,xi*delta_x))

            ut= ut_next.copy()
            ut[0] = g1_in(y*delta_t)
            ut[N_in] = g2_in(y*delta_t)

            if t_counter<y*delta_t*10:
                plt.plot(x,ut, label = ('t='+str(y*delta_t)))
                t_counter = t_counter+1

        return ut
            