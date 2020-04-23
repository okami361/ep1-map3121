import math
from ex1 import Ex1

def main():

    #Ex1
    f = lambda t,x : 10*x*x*(x-1) - 60*x*t + 20*t
    u0 = lambda x : 0
    g1 = lambda t : 0
    g2 = lambda t : 0

    print("\nN:")
    N_in = int(input())

    print("\nlambda:")
    lambda_in = float(input())

    M = pow(N_in,2)/lambda_in

    ex1 = Ex1()
    ex1.resolver(u0,f,N_in,M,lambda_in,g1,g2)

if __name__ == "__main__":
    main()