lista1 = [1,2,3,4,5]
lista2 = [4,5,6,7,8]
comuns = [i for i in lista1 if i in lista2]
listasemcomum = []
for i in lista1:
        if i not in lista2:
            listasemcomum.append(i)
        
for i in lista2:
        if i not in lista1:
            listasemcomum.append(i)

print(listasemcomum)

texto = "Vivia há já não poucos anos algures num concelho do Ribatejo um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"
lista3 = [i for i in texto.split(" ") if len(i) > 3]
print(lista3)

lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = [(lista.index(i),i) for i in lista]
print(listaRes)


def strCount(s,subs):
    occurences = [i for i in range(len(s)) if s.startswith(subs, i)]
    return  len(occurences)


def produtoM3(lista):
    lista.sort()
    return lista[0] * lista[1] * lista[2]

def reduxInt(n):
    soma = sum([int(i) for i in str(n)])
    if n < 10:
        return n
    else:
        return reduxInt(soma)
def myIndexOf(s1,s2):
    if s2 in s1:
        return s1.find(s2)
    else:
        return -1

def quantosPost(redeSocial):
    return len(redeSocial)

def postsAutor(redeSocial,autor):
    posts = list()
    for i in redeSocial:
        if i["autor"] == autor:
            posts.append(i)

    return posts

def autores(redeSocial):
    autores = set()
    for i in redeSocial:
        autores.append(i["autor"])
    return sorted(autores)        

def insPost(redeSocial,conteudo,autor,dataCriacao,comentarios):
    max_id = 0
    for i in redeSocial:
        if int(i["id"][1:]) > max:
            max = int(i["id"][1:])
    redeSocial.append({"id":"p"+str(max + 1),"conteudo":conteudo,"autor":autor,"dataCriacao":dataCriacao,"comentarios":comentarios})
    return redeSocial

def remPost(redeSocial,id):
    del redeSocial[id]
    return redeSocial

def postsPorAutor(redeSocial):
    autores = autores(redeSocial)
    posts = dict()
    for i in redeSocial:
        for j in autores:
            if i["autor"] == j:
                posts[j] = posts.get(j,0) + 1
    return posts

def comentadoPor(redeSocial,autor):
    posts = list()
    for i in redeSocial:
        for j in i["comentarios"]:
            if j["autor"] == autor:
                posts.append(i)
    return posts
