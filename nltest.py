#   Universidade de Brasília - Faculdade de Tecnologia
#   Instrumentação de controle - 2021/2
#   Gabriel Tambara Rabelo - 18/0017021

import random
from matplotlib import pyplot as plt

def simulacao():

    r = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000] # resistores de 1k
    rb = [2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000] # resistores de 2k
    rx = [2000] # resistor inicial no terra e resistores equivalentes

    # define a tolerancia
    tol = 0.00005

    # adiciona erro nos resistores com base na sua tolerancia

    for i in range(8):
        x = -1 + (2*(random.randrange(20)/20))
        r[i] = r[i]*(1+(tol*x))

    for i in range(9):
        x = -1 + (2*(random.randrange(20)/20))
        rb[i] = rb[i]*(1+(tol*x))

    # resistencia ligada ao terra sempre
    x = -1 + (2*(random.randrange(20)/20))
    rx[0] = rx[0]*(1+(tol*x))

    # resistencia que escala a tensão de saída para 10,23 como o maximo
    x = -1 + (2*(random.randrange(20)/20))
    rref = 2044*(1+(tol*x))

    # resistencias do amplificador inversor de ganho -1
    x = -1 + (2*(random.randrange(20)/20))
    rmenos = 1000*(1+(tol*x))

    x = -1 + (2*(random.randrange(20)/20))
    rmenosalt = 1000*(1+(tol*x))

    # calculo pelo equivalente de thevenin
    for i in range(8):
        req = (rb[i]*rx[i])/(rb[i]+rx[i]) + r[i]
        rx.append(req)
    req = (rb[8]*rx[8])/(rb[8]+rx[8])

    # calculo da tensão de saida para entrada máxima

    valormax = 1023
    vref = 5

    vout = (rref/req)*(rmenos/rmenosalt)*(valormax/1024)*vref

    print("req: " + str(req))
    print("rref: " + str(rref))
    print("valormax: " + str(vout))
    if vout > 10.210019:
        erro = vout - 10.210019
    else:
        erro = -vout + 10.210019
    return erro

limite = 0.001 #0.1%
resultados = []
p = []
iteradas = 0
for i in range(10000):
    p.append(i+1)
    resultado = simulacao()
    resultados.append(resultado)
    if(resultado > limite):
        iteradas = iteradas+1
print(100*iteradas/10000, '% de erros')

print("valor medio = ", 100*(sum(resultados)/len(resultados)), '%')
plt.xlabel("Iterações")
plt.ylabel("Não linearidade")
plt.scatter(p, resultados, s = 1.1, c = '#aa7a63')
plt.axhline(color = 'r', y = 0.001)
plt.title('Simulação Monte Carlo')
plt.show()