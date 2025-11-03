from empresa.models import Estado, Cidade, Logradouro, CEP, Empresa, Funcionario
def run():
    if Estado.objects.exists():
        print('Dados já populados.')
        return
    est = Estado.objects.create(nome='Alagoas', sigla='AL')
    cid = Cidade.objects.create(nome='Maceió', estado=est)
    log = Logradouro.objects.create(nome='Rua Exemplo', cidade=cid)
    cep = CEP.objects.create(codigo='57000-000', logradouro=log)
    emp = Empresa.objects.create(nome='Empresa Exemplo', cnpj='00.000.000/0000-00', cidade=cid)
    for i in range(1,6):
        Funcionario.objects.create(nome=f'Funcionario {i}', cpf=f'000.000.000-0{i}', empresa=emp, cargo='Analista')
    print('População concluída.')
if __name__=='__main__':
    run()
