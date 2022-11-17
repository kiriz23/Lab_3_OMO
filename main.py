import numpy as np
import math

# Kirill Krocha OM-3, Variant 4


def first_l(x,y):
    return (0.9+math.cos(y))/3


def second_l(x, y):
    return math.sin(x-0.6)-1.6


def phi_1_y(y):
    return -(math.sin(y))/3


def phi_1_x():
    return 0


def phi_2_x(x):
    return math.cos(x-(3/5))


def phi_2_y():
    return 0


def viznachnik(x,y):
    return -(phi_1_y(y)*phi_2_x(x))


def algo_1(x_start, y_start, eps):
    k=0
    x= first_l(x_start,y_start)
    y = second_l(x_start,y_start)
    print("Determinant = "+str(viznachnik(x_start,y_start)))
    if(abs(viznachnik(x_start,y_start)) > 1):
        print(" Method is not converged!!!")
    print("         x_k                     y_k", "           step", sep="                   ")
    print(str(x_start).center(20) + str(y_start).center(30) + str(k).center(35))

    while max(abs(first_l(x,y)-x),abs(second_l(x,y)-y)) > eps :
        k += 1
        print(str(x).center(20) + str(y).center(30) + str(k).center(35))
        x_k = first_l(x,y)
        y_k = second_l(x,y)
        if max(x-x_k,y-y_k) <= eps:
            return x_k, y_k
        x = x_k
        y = y_k


A = np.array([(2.1,1.0,1.1),(1.0,2.6,1.1),(1.1,1.1,3.1)])


def algo_2(x1, x2, x3, eps):
    x_start = np.array([x1,x2,x3])
    k = 0
    x_k = x_start
    x_k = x_k/math.sqrt(x_k.dot(x_k))
    print("            mu_k+1", "        step", sep="                   ")

    while k > -1:
        k += 1
        x_k = np.matmul(x_k.T, A)
        x_k = x_k/math.sqrt(x_k.dot(x_k))
        x_k_plus = np.matmul(x_k.T, A)
        mu_k = x_k_plus.dot(x_k)
        x_k_plus = x_k_plus/math.sqrt(x_k_plus.dot(x_k_plus))
        mu_k_plus = np.matmul(x_k_plus.T, A).dot(x_k_plus)
        print(str(mu_k_plus).center(30) + str(k).center(35))
        if mu_k_plus-mu_k < eps:
            return mu_k_plus


algo_1(1.25,0,0.001)
print("Second task")
algo_2(1,1,1,0.001)




