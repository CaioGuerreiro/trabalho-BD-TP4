import pyodbc 

conectarDados = "DRIVER={SQLite3 ODBC Driver};SERVER=Caio_Guerreiro;DATABASE=BDtrabalho.db;Trusted_connection=yes"
# estabelecendo conexão com o banco
conectar = pyodbc.connect(conectarDados)

cursor = conectar.cursor()


def checkPaciente():
    cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='Medico';""")
    result = cursor.fetchall()
    print(len(result) > 0)
    return len(result) > 0  # Retorna True se a tabela existir, False caso contrário

def checkMedico():
    cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name='Medico';""")
    result = cursor.fetchall()
    print(len(result) > 0) 
    return len(result) > 0  # Retorna True se a tabela existir, False caso contrário



# criando tabela paciente
if checkPaciente() == False:
    
    conectar = pyodbc.connect(conectarDados)
    
    cursor = conectar.cursor()
    queryPaciente = """CREATE TABLE Paciente (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, sexo TEXT); """
    
    print('-'*40)
    print('tabela Paciente criada')
    print('-'*40)

    cursor.execute(queryPaciente)
    cursor.commit()
# criando tabela Medico
if checkMedico() == False:
    
    queryMedico = """CREATE TABLE Medico(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, crm TEXT, paciente_id INTEGER, FOREIGN KEY (paciente_id) REFERENCES Paciente (id) ON DELETE SET NULL); """
    print('-'*40)
    print('tabela Paciente criada')
    print('-'*40)
    cursor.execute(queryMedico)
    cursor.commit()



print('Escolha sua ação')
print('qual tebela deseja consultar?')
print('1 - Paciente')
print('2 - Medico')
tabelaEscolhida = int(input())
if tabelaEscolhida == 1:
   

    print('1 - Inserir dado na tebela')
    print('2 - Deletar dado na tebela')
    print('3 - Atualizar dado na tebela')
    print('4 - Consultar dado na tebela')
    print('5 - Consultar por nome')

    opcaoEscolhida = int(input())

    if opcaoEscolhida == 1:
        print('nome:')
        nomePaciente = input()
        print('idade:')
        idadePaciente = int(input())
        print('sexo:')
        sexoPaciente = input()
        queryPaciente = f"""INSERT INTO Paciente (nome, idade, sexo) VALUES ('{nomePaciente}', {idadePaciente}, '{sexoPaciente}');"""
        print('Paciente inserido')
        
        cursor.execute(queryPaciente)
        cursor.commit()

    if opcaoEscolhida == 2:
        print('id:')
        idPaciente = input()
        queryPaciente = f"""DELETE FROM Paciente WHERE id={idPaciente};"""
        print('Paciente deletado')
        cursor.execute(queryPaciente)
        cursor.commit()
    
    if opcaoEscolhida == 3:
        print('id:')
        idPaciente = input()
        print('nome:')
        nomePaciente = input()
        print('idade:')
        idadePaciente = int(input())
        print('sexo:')
        sexoPaciente = input()
        queryPaciente = f"""UPDATE Paciente SET nome = '{nomePaciente}', idade = {idadePaciente}, sexo = '{sexoPaciente}' WHERE id = {idPaciente};"""
        print('Paciente atualizado')
        cursor.execute(queryPaciente)
        cursor.commit()

    if opcaoEscolhida == 4:
        queryPaciente = """SELECT * FROM Paciente;"""
        cursor.execute(queryPaciente)
        cursor.commit()
        consulta = cursor.fetchall()

        for linha in consulta:
            print(linha)

    if opcaoEscolhida == 5:
        print('nome:')
        nomePaciente = input()
        queryPaciente = f"""SELECT * FROM Paciente WHERE nome LIKE '%{nomePaciente}%';"""
        cursor.execute(queryPaciente)
        cursor.commit()
        consulta = cursor.fetchall()

        for linha in consulta:
            print(linha)


if tabelaEscolhida == 2:

  

    print('1 - Inserir dado na tebela')
    print('2 - Deletar dado na tebela')
    print('3 - Atualizar dado na tebela')
    print('4 - Consultar dado na tebela')

    opcaoEscolhida = int(input())

    if opcaoEscolhida == 1:
        print('nome:')
        nomeMedico = input()
        print('crm:')
        crm = input()
        print('id paciente:')
        idPaciente = int(input())
        queryMedico = f"""INSERT INTO Medico (nome, crm, paciente_id) VALUES ('{nomeMedico}', '{crm}', {idPaciente});"""
        print('Medico inserido')
        cursor.execute(queryMedico)
        cursor.commit()

    if opcaoEscolhida == 2:
        print('id:')
        idMedico = input()
        queryMedico = f"""DELETE FROM Medico WHERE id={idMedico};"""
        print('Medico deletado')
        cursor.execute(queryMedico)
        cursor.commit()
    
    if opcaoEscolhida == 3:
        print('id:')
        idMedico = input()
        print('nome:')
        nomeMedico = input()
        print('crm:')
        crm = int(input())
        print('id paciente:')
        idPaciente = int(input())
        queryMedico = f"""UPDATE Medico SET nome = '{nomeMedico}', crm = {crm}, paciente_id = '{idPaciente}' WHERE id = {idMedico};"""
        print('Paciente atualizado')
        cursor.execute(queryMedico)
        cursor.commit()

    if opcaoEscolhida == 4:
        queryMedico = """SELECT * FROM Medico;"""
        cursor.execute(queryMedico)
        cursor.commit()
        consulta = cursor.fetchall()

        for linha in consulta:
            print(linha)  
          
    if opcaoEscolhida == 5:
        print('nome:')
        nomeMedico = input()
        queryPaciente = f"""SELECT * FROM Medico WHERE nome LIKE '%{nomeMedico}%';"""
        cursor.execute(queryMedico)
        cursor.commit()
        consulta = cursor.fetchall()

        for linha in consulta:
            print(linha)

    







cursor.close()

