from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica, PessoaJuridica


def main ():
    lista_pf =[]
    while True:
        opcao = int(input("Escolha uma opção: \n1-Pessoa Física \n2-Pessoa Jurídica \n0-Sair "))
        if opcao ==1:
            while True:
                opcao_pf= int(input("Escolha uma opção: \n1-Cadastrar Pessoa física \n2-Listar Pessoa física \n3-Remover Cadastro \n0-Voltar ao Menu anterior  "))
                if opcao_pf == 1 :
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input( "Digite o nome da pessoa física: ")
                    novapf.cpf = input( "Ditite o cpf: ")
                    novapf.rendimento = float(input("Digite o rendimento mensal (somente números): "))
                    
                    data_nascimento = input("Digite a data de Nasximento (dd/MM/aaaa): ")
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retornando ao menu...")
                        continue # Retornar ao inicio do loop

                    novo_end_pf.logradouro = input("Digite o logradouro: ")
                    novo_end_pf.numero = input("Digite o número: ")
                    end_comercial = input("Este endereço é comercial? S/N: ")
                    novo_end_pf.endereco_comercial = end_comercial.strip().upper() == 'S'

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)
                    print("Cadastro realizado com sucesso!! ")
                elif opcao_pf ==2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome}")
                            print(f"CPF: {cada_pf.cpf}")
                            print(f"Endereço: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}")
                            print(f"Data Nascimento: {cada_pf.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista Vazia")
                elif opcao_pf==3:
                    remov = input("Informe o cpf da pessoa a ser removida: ")
                    validacao = False
                    for pf in lista_pf:
                        if pf.cpf == remov:
                            lista_pf.remove(pf)
                            print("Pessoa removida")
                            validacao = True
                            break
                    if validacao == False:
                        print("Pessoa não encontrada")                   
                elif opcao_pf == 0:
                    print("Voltando ao menu  anterior")
                    break
                else:
                    print("Opção inválida, por favor digite uma das opções indicadas")
        elif opcao ==2 :
            lista_pj=[]
            while True:
                opcao_pj= int(input("Escolha uma opção: \n1-Cadastrar Pessoa Juriídica \n2-Listar Pessoa Jurídica \n3-Remover Cadastro \n0-Voltar ao Menu anterior  "))
                if opcao_pj == 1 :
                    novapj = PessoaJuridica()
                    novo_end_pj = Endereco()
                    
                    novapj.nome = input( "Digite o nome da pessoa jurídica: ")
                    novapj.cnpj = input( "Ditite o cnpj: ")
                    novapj.rendimento = float(input("Digite o rendimento mensal (somente números): "))

                    novo_end_pj.logradouro = input("Digite o logradouro: ")
                    novo_end_pj.numero = input("Digite o número: ")
                    end_comercial = input("Este endereço é comercial? S/N: ")
                    novo_end_pj.endereco_comercial = end_comercial.strip().upper() == 'S'

                    novapj.endereco = novo_end_pj

                    lista_pj.append(novapj)
                    print("Cadastro realizado com sucesso!! ")
                elif opcao_pj ==2:
                    if lista_pj:
                        for cada_pj in lista_pj:
                            print(f"Nome: {cada_pj.nome}")
                            print(f"CNPF: {cada_pj.cnpj}")
                            print(f"Endereço: {cada_pj.endereco.logradouro}, {cada_pj.endereco.numero}")
                            print(f"Imposto a ser pago: {cada_pj.calcular_imposto(cada_pj.rendimento)}")
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista Vazia")
                elif opcao_pj==3:
                    remov = input("Informe o CNPJ da pessoa a ser removida: ")
                    validacao = False
                    for pj in lista_pj:
                        if pj.cnpj == remov:
                            lista_pj.remove(pj)
                            print("Pessoa Juridica removida")
                            validacao = True
                            break
                    if validacao == False:
                        print("Pessoa Juridica não encontrada") 
                elif opcao_pj == 0:
                    print("Voltando ao menu  anterior")
                    break
                else:
                    print("Opção inválida, por favor digite uma das opções indicadas")
        elif opcao ==0:
            print("Obrigdo por utiliza o nosso sistema! Valeu! ")
            break

if __name__ == "__main__":
    main()