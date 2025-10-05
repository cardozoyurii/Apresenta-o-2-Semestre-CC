# DOCS BR 

# Lista de ações disponíveis
listaAcoes = [
    "Tirar passaporte",
    "Se alistar",
    "Tirar título de eleitor",
    "Abrir empresa",
    "CNH"
]

print("Bem-vindo ao Guia de Documentos Brasileiros(DOCS BR)")


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


print(f"\nOlá {nome}, seja bem-vindo(a) ao DOCS BR, nosso guia inteligente de documentos, feito para que você possa se informar, de forma simples, em relação à alguns documentos brasileiros :D")
print("Este código ganhou vida com a ajuda de Gustavo, Hendrick, Higor, Lucas e Yuri")


if idade <= 17:
    print("\nAtenção!!! Abrir uma empresa e tirar a CNH só podem ser realizadas após os 18 anos de idade. \nO alistamento militar é necessário, e só pode ser realizado, no ano em que a pessoa for completar 18 anos de idade. \nJá o título de eleitor pode ser feito a partir dos 16 anos, porém é obrigatório a partir dos 18.")


print("\nEscolha uma das ações:")
for i in range(len(listaAcoes)):
    print(f"{i} - {listaAcoes[i]}")


buscar = int(input("\nDigite o número correspondente à ação desejada: "))


if buscar == 0:
    print("\nDocumentos necessarios para tirar passaporte:")
    print("- RG")
    print("- CPF")
    print("- Certidão de nascimento ou casamento")
    print("- Comprovante de pagamento da taxa")
    print("\nPara tirar um passaporte, preencha o formulário online no site da Polícia Federal, pague a taxa (GRU) gerada, agende um atendimento presencial na PF, compareça no local e dia agendado com todos os documentos necessários, e acompanhe o processo para retirar o passaporte pronto no posto selecionado\n")
elif buscar == 1:

    print("\nDocumentos para alistamento militar:")
    print("- RG")
    print("- CPF")
    print("- Comprovante de residência")
    print("Para fazer o alistamento militar, acesse o site www.alistamento.eb.mil.br entre janeiro e junho do ano em que completa 18 anos, usando seus dados do Gov.br.você será convocado para as próximas etapas, que podem incluir exames médicos e físicos, e, dependendo do resultado, poderá ser dispensado (pagando uma taxa e jurando à Bandeira) ou seguirá para a incorporação")

elif buscar == 2:

    print("\nDocumentos para título de eleitor:")
    print("- RG")
    print("- CPF")
    print("- Comprovante de residência")
    print("\nPara tirar o título de eleitor, a maneira mais prática é fazer a solicitação pela internet, usando o serviço Título Net da Justiça Eleitoral. No entanto, quem for tirar o documento pela primeira vez e não tiver biometria cadastrada deverá comparecer a um cartório eleitoral")

elif buscar == 3:
        
    print("\nDocumentos para abrir uma empresa:")
    print("- RG")
    print("- CPF")
    print("- Comprovante de residência")
    print("- Contrato social ou MEI")
    print("\nPara abrir uma empresa, você deve elaborar um plano de negócios, definir o tipo de empresa (como MEI, ME ou EPP), escolher o regime tributário e as atividades (CNAE). \nEm seguida, realize a consulta de viabilidade do nome e local, elabore o contrato social, registre-se na Junta Comercial ou Cartório, obtenha o CNPJ, faça as inscrições Estadual e Municipal necessárias, e solicite os alvarás de funcionamento")

elif buscar == 4:
    
    print("\nDocumentos para tirar CNH")
    print("- RG, CNH provisória de outro estado, passaporte, carteira de trabalho, etc.(com foto)")
    print("- CPF")
    print("- Comprovante de residência")
    print("- Foto 3x4")
    print("\nPara tirar a CNH, você deve fazer a inscrição no Detran e numa autoescola, realizar o exame médico e psicológico, concluir o curso teórico e ser aprovado na prova de legislação, fazer as aulas práticas e aprovar no exame de direção veicular. Após todas essas etapas, você poderá solicitar a emissão da sua primeira CNH")

else:
    print("\nOpção inválida, tente novamente.")