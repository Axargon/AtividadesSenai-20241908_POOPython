
# Classe Endereço
from datetime import date

class Endereco:
    def __init__(self,logradouro =" ", numero =" ", endereco_comercial= False):
        # Inicializar os nosso atributos com valores padrão
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_comercial = endereco_comercial

# Classe Pessoa
class Pessoa:
    def __init__(self, nome ="", rendimento = 0.0, endereco = None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco
    def calcular_imposto( self, rendimento):
        return rendimento
        
# Classe Pessoa física
class PessoaFisica(Pessoa):
    def __init__(self, nome="", rendimento=0, endereco=None, cpf = "", dataNascimento =None):
        
        if endereco is None:
            #se nenhum endereco for fornecido, cria um endereco de objeto padrao
            endereco =Endereco()
        
        if dataNascimento is None:
            dataNascimento = date.today()
    
        super().__init__(nome, rendimento, endereco)
        #Chama o construtor da superclasse Pessoa para inicializar os atributos herdados

        self.cpf = cpf
        self.dataNascimento = dataNascimento
        
    def calcular_imposto(self, rendimento: float) -> float:
        if rendimento <= 1500:
            return 0 #sem imposto para rendimentos ate 1500
        elif 1500 < rendimento <= 3500:
            return ((rendimento/100) * 2) #imposto de 2% para rendimentos entre 1500 e 3500
        elif 3500 < rendimento <= 6000:
            return((rendimento/100)* 3.5) #imposto de 3.5% para rendimentos entre 3500 e 6000
        else:
            return ((rendimento/100) *5) #imposto de 5% para rendimentos acima de 6000
        
        #return super().calcular_imposto(rendimento)

# CLasse pessoa Jurídica
class PessoaJuridica(Pessoa):
    pass





        