url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
print (url)
contador_url = url.find('?')
url_base = url[:contador_url]
print(url_base)
url_parametro = url [contador_url + 1:]
print (url_parametro)