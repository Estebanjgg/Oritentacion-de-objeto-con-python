endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rios de Janeiro, RJ, 23440-120"


import re # Regular Expreession -- RegEx

# 5 digitos + - (opcional) + 3 


padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)-9*6