def altera(vet, tam):
    for i in range(tam):
        if vet[i] < 0:
            vet[i] = 0
        elif vet[i] < 10:
            vet[i] = 1
        else:
            v[i] = 2
    return vet

tam = 39

v = [0]*tam
for i in range(tam):
    v[i] = input('Digite um valor: ')
altera(v,tam)
print("v")