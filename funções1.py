#sintaxe de função em python
def inicioCodigo():
    print("Minha primeira função em python!")
inicioCodigo()   
#Passando parametro definido
def passandoParametro (nome,sobrenome):
    print("Meu nome é",nome,sobrenome)
passandoParametro(True, "Ana")
passandoParametro("Ana Carolina","Machado")
passandoParametro(1.50,1)
#Passando parametro indefinido
def parametroIndefinido(*nome):
    print("Meu nome é:",nome[0],nome[1],nome[2])
parametroIndefinido("Ana","Carolina","Machado")
#Passando parametro definido com chave
def parametroChave(nome,idade,cpf):
    print("Meu nome é:",nome,"\nMinha idade é:",idade,"\nMeu cpf é:",cpf)
parametroChave(nome="Ana Carolina Machado",idade="16",cpf="1234")
#Passando parametro indefinido com chave
def parametroChaveInd(**dados):
    print("Informações do Usuário:",dados["nome"] +"\n"+dados["idade"])
parametroChaveInd(nome="Ana Carolina Machado",idade="16",cpf="1234")
#Passando parametro com valor padrao
def parametroPadrao (nome="sem nome"):
    print("Bem-vindo!",nome)
parametroPadrao("Ana")
parametroPadrao()
#Passando LISTA por parametro
def parametroLista(lista):
    for i in lista:
        print(i)
minhaLista = ["Ana Carolina","Machado"]
parametroLista(minhaLista)
#Parametro vazio, só passa reto por ele
def funcaoVazia():
    pass
#Função com retorno
def funcRetorno(nome):
    if nome=="Ana":
        return True
    else:
        return False
recebeRetorno=funcRetorno("Ana")#Se mudar o nome aqui, a função se torna falsa!
if recebeRetorno==True:
    print("Okay")
else:
    print("Não é.")
    
#chamada da função com retorno direto no if
if retornaValor("Francine") == True:
    print("Correto")
else:
    print("Incorreto")

#Recursividade: é recurso onde podemos chamar a função dentro dela mesma.
def funcaoRecursiva(numero):
    if numero > 0:
        resultado = numero + funcaoRecursiva(numero - 1)
    else:
        resultado = 0
    return resultado

funcaoRecursiva(5)
