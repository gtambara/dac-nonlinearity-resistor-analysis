import random
from matplotlib import pyplot as plt


def v_ideal(r, n, vref):
    v = vref*n/(16)
    return v

def dif(x, y):
    if x >= y:
        result = x - y
    else:
        result = y - x
    return result

def simul(vref, r, tol):
    resists = []
    tensoes_ideais = []
    tensoes_reais = []
    errors = []
    for n in range(1, 17):
        resists.append((1+random.uniform(-tol, tol))*r)
        tensoes_ideais.append(v_ideal(r, n, vref))
    den = sum(resists)
    for i in range(1, 17):
        soma = 0
        for a in range(i):
            soma = soma + resists[a]
        tensoes_reais.append(vref*(soma/den))

    for i in range(16):
        erro = dif(tensoes_ideais[i], tensoes_reais[i])
        erro = erro*(i+1)/(16*vref)
        errors.append(erro)
    nl = max(errors)
    return nl
    


def monte_carlo():
    aux = 0
    vref = 5
    r = 10
    tol  = 0.008 # +-0.8%
    rep = 10000
    nl_req = 0.001 #0.1%
    nls = []
    x = []
    for i in range(rep):
        x.append(i+1)
        nl = simul(vref, r, tol)
        nls.append(nl)
        if(nl > nl_req):
            aux = aux+1
    print(aux)
    print(100*aux/rep, '% de erros')

    if(aux > rep*0.05):
        print('Projeto não cumpre requisito de não-linearidade')
    else:
        print('Não-linearidade menor que 0.1% para ', 100*(1-(aux/rep)) , '% das simulações')
    print('Não-linearidade média = ', 100*(sum(nls)/len(nls)), '%')
    plt.scatter(x, nls, s = 1.1, c = '#ffbe00')
    plt.axhline(color = 'r', y = 0.001, linestyle = ':')
    plt.xlabel('Simulações')
    plt.ylabel('Não-linearidade')
    plt.title('Resultado das simulações')
    plt.show()
    
monte_carlo()

Rb[]
for i in range(10):
    x = -1+(2*( random.randint(0,10) / 10 ))
    Rb[i] = 2000*(1 + tolerancia*x)
    