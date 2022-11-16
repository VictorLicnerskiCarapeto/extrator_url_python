import re
url = "https://www.bytebank.com.br/cambio"
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
# o "()" dentro da expressão serve para ele buscar exatamente o item que está dentro
match = padrao_url.match(url)

if not match:
    raise ValueError("A url não é valida")

print("A URL é válida")