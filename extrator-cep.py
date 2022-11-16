import re #Regular Expression -- RegEX

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
#ao colocar "?" ao lado do padrão, indica que ele pode ou não aparecer na sequencia
#quantificadores "{}" mostram quantas vezes o padrão irá se repetir
#inervalos "-" pega o intervalo entre o primeiro e o ultimo numero ou letra

busca = padrao.search(endereco) #objeto Match
if busca:
    cep = busca.group()
    print(cep)
