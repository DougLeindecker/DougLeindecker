def desv(*args):
    med=round(sum(args)/len(args), 2)
    contador = 0
    k = 0
    z = 0
    for i in range(len(args)):
        y = (round(args[i]-med, 4))
        x = y**2
        k += x
        contador += 1
        if contador == len(args):
            w = (k)/len(args)
            z += (w**0.5)
            l = round(z, 5)
    return l
print(desv(1,2,3,4,5))
