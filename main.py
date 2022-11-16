# url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url = " "
#Sanitização da URL
url = url.strip()
#Validação da URL
if url == "":
    raise ValueError("A URL está vazia")

#Separar base e os parâmetros
indice_interrogação = url.find("?")
url_base = url[:indice_interrogação]#fatiamento de strings(slicing em inglês)
url_parametros = url[indice_interrogação+1:]#pode omitir um dos parametros do fatiamento
print(url_parametros)

#Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)#passando uma string para o find, e retorna a primeira posição
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)