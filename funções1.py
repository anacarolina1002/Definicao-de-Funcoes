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
