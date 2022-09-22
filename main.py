url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

parame_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parame_busca)
indice_valor = indice_parametro + len(parame_busca) + 1
indice_e_comercial = url_parametros.find('&')
valor = url_parametros[indice_valor:indice_e_comercial]
print(valor) 