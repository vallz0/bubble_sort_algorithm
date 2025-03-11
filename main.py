def bubble(lista:list):
    for step in range(len(lista)-1,0,-1):
        for i in range(step):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista [i]
        print(lista)

if __name__ == '__main__':
    bubble([4,3,1,9,8,7,2,5])
