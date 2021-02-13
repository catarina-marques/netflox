import psycopg2
from datetime import date
conn = psycopg2.connect(host="localhost", dbname="netflox", user="postgres", password="postgres")
cur = conn.cursor()

def menuCliente(name, idcli, conn, cur):
    print("\n\nSessão iniciada como Cliente: ",name)

    c = input("\n\n1 - Listar todos os artigos\n2 - Ver detalhes de um artigo\n3 - Alugar um artigo"
              "\n4 - Ver a lista de artigos alugados\n5 - Mostrar o valor gasto"
              "\n6 - Consultar mensagens\n7 - Pesquisa\n8 - Logout\n\nSelecione uma opcção: ")

    while (c != 1 or c != 2 or c != 3 or c != 4 or c != 5 or c != 6):

        if c == "1":
            listarTodos(name,idcli,cur,conn)
        elif c == "2":
            detalhesArtigo(name, idcli, cur, conn)
        elif c == "3":
            while True:
                idarticle=input("\n\nInsira o id do artigo:")
                if Representint(idarticle):
                    cur.execute("Select * from article where id = %s",[idarticle])
                    if cur.rowcount!=0:
                        rent(name, idcli, idarticle, cur, conn)
                    else:
                        continue
        elif c == "4":
            listaHistoricoAlugados(name, idcli,cur,conn)
        elif c == "5":
            valorGasto(name,idcli,cur,conn)
        elif c == "6":
            consultarMensagens(name, idcli,cur,conn)
        elif c == "7":
            pesquisa(name,idcli,cur,conn)
        elif c == "8":
            logout(name, idcli,cur,conn)
        else:
            print("\nOpçao invalida")
            continue

def listarTodos(name, idcli,cur,conn):
    print("\n\nSessão iniciada como Cliente: ", name)
    print("\n\nLista de todos os artigos")
    cur.execute("Select * from article")
    for i in cur.fetchall():
        print("\nID - ",i[0]," Nome - ", i[1])

    c = input("\n1 - Ver detalhes de um artigo\n2 - Alugar um artigo \n3 - Voltar ao menu\n4: Logout\n\nnSelecione uma opçao:")
    while (c != 1 or c != 2 or c != 3):
        #c = input("\n1 - Ver detalhes de um artigo\n2 - Alugar um artigo \n3 - Voltar ao menu\n3: Logout\n\nnSelecione uma opçao:")
        if c == "1":
            detalhesArtigo(name, idcli,cur,conn)
        elif c == "2":
            while True:
                idarticle=input("\n\nDe-me o id do artigo:")
                if Representint(idarticle):
                    cur.execute("Select * from article where id = %s",[idarticle])
                    if cur.rowcount!=0:
                        rent(name, idcli, idarticle, cur, conn)
                    else:
                        continue

        elif c == "3":
            menuCliente(name, idcli,cur,conn)
        elif c == "4":
            logout(name, idcli,cur,conn)
        else:
            print("\n\nOpçao invalida:")
            continue

def Representint(s):
    try:
        int(s)
        return  True
    except:
        return  False

def detalhesArtigo(name,idcli,cur,conn):
    print("\n\nSessão iniciada como Cliente: ", name)
    while True:
        id = input("\n\n1 - Introduzir o ID do artigo que pretende visualizar\n2-Voltar ao menu anterior\n\nSelecione uma das opçoes ")
        if id == "2":
            menuCliente(name,idcli,cur,conn)

        if Representint(id):
           temArtigo = verificaArtigo(id)
           if temArtigo == False:
                print("\nO ID nao corresponde a nenhum artigo da lista. Tente novamente ")
                continue
           else:
                cur.execute("select * from article where id = %s",[id])
                for i in cur.fetchall():
                    print("\nID do artigo: ", i[0], "\nNome do artigo: ", i[1], "\nPreço: ", i[2], "euros", "\nStock:",i[3],"unidades ","\nValidade:",i[4])

                    cur.execute("select genre_id from article_genre where article_id = %s",[id])
                    idtipo = cur.fetchone()

                    cur.execute("select name from genre where id = %s",[idtipo])
                    for i in cur.fetchall():
                        print("\n\nTipo de artigo ",i[1])

                        cur.execute("select actor_id from article_actor where article_id = %s", [id])
                        idactor = cur.fetchone()
                        cur.execute("select name from actor where id = %s", [idactor])
                        for i in cur.fetchall():
                            print("\n\nAtores: ", i[1])

                            cur.execute("select director_id from article_director where article_id = %s", [id])
                            idDirector = cur.fetchone()
                            cur.execute("select name from director where id = %s", [idDirector])
                            for i in cur.fetchall():
                                print("\n\nRealizadores: ", i[1])

                                cur.execute("select producer_id from article_producer where article_id = %s", [id])
                                idproducer = cur.fetchone()
                                cur.execute("select name from producer where id = %s", [idproducer])
                                for i in cur.fetchall():
                                    print("\n\nProdutores: ", i[1])
                                break



def verificaArtigo(id):
    conn = psycopg2.connect(host="localhost", dbname="netflox", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.execute("select * from article where id = %s",[id])
    if cur.rowcount!= 0:
            return(True)
    return (False)

def rent(name,idcli,idarticle,cur,conn):
    while True:

        cur.execute("Select * from article where id=%s", [idarticle])
        rent = cur.fetchone()
        today = date.today()
        rent_date = today.strftime("%Y-%m-%d")
        id_rent = cur.fetchone()
        cur.execute("select price from rent where id = %s", [id_rent])
        #for i in cur.fetchall():
        while True:
            price = cur.fetchall()
            cur.execute("select * from client")
            balance = cur.fetchone()
            if (balance >= price):
                balance = (balance - price)
                try:
                    cur.execute("Insert into rent(purchase_date,price,user_id) values(%s,%s,%s)",
                                (rent_date, rent[3], idcli))
                    conn.commit()
                    cur.execute("Insert into rent_article(rent_id,article_id) values(%s,%s)", (id_rent, idarticle))
                    conn.commit()
                    cur.execute("update client set balance = %s where user_id=%s ", (balance, idcli))
                    conn.commit()
                    print("\nArtigo alugado")

                except psycopg2.error:
                    conn.rollback()
                    print("\nAlguma coisa esta errada")

                break
            else:
                print("\nNão é possivel alugar. Saldo insuficiente")
                continue


def listaHistoricoAlugados(name, idcli,cur,conn):
    print("\n\nSessão iniciada como Cliente: ", name)
    print("\nArtigos disponiveis: ")
    cur.execute("select * from rent where user_id=%s", (idcli,))
    idrent = cur.fetchone()[0]

    cur.execute ("select article_id from rent_article where rent_id=%s",(idrent))
    idarticle = cur.fecthone()

    cur.execute("select name from article where id=%s",(idarticle))
    for i in cur.fetchall():
        print("\n\nId do artigo: ", i[0],"\tNome do artigo: ",i[1])
        break


def valorGasto(name, idcli,cur,conn):
    print("\n\nSessão iniciada como Cliente: ", name)
    while (c != 1 or c != 2 or c != 3 or c != 4):
        c = input("\n1 - Ver valor gasto em alugueres passados\n2 - Ver valor gasto por cada tipo de artigo"
                  "\n3-Voltar ao menu\n4: Logout\n\nSelecione uma opcao:")

        if c == "1":
            valorGastoAlugures(name,idcli,cur,conn)
        elif c == "2":
            valorGastoGenre(name, idcli,cur,conn)
        elif c == "3":
            menuCliente(name, idcli,cur,conn)
        elif c == "4":
            logout(name, idcli,cur,conn)
        else:
            print("\n\nOpção invalida")
            continue

def valorGastoAlugures(name,idcli,cur,conn):
    total=0
    cur.execute("select price from rent where user_id=%s",(idcli,))
    for i in cur.fetchall():
        total += i[2]
        print("\nTotal gasto: ",total)
        break

def valorGastoGenre(name, idcli,cur,conn):
    totalGenre = 0
    print("\n\nTotal gasto por tipo de artigo: ")
    cur.execute("select name from genre where id=%s",idcli)
    genres = cur.fetchone()

    cur.execute("select id from article where name=%s",genres)
    idarticle = cur.fetchone()

    cur.execute("select rent_id from rent_article where article_id=%",idarticle)
    idrent=cur.fetchone()

    cur.execute("select price from rent where id=%",idrent)
    for i in cur.fetchall():
        totalGenre +=i[2]
        print("\nTotal gasto por tipo de artigo: ",totalGenre)
        break


def consultarMensagens(name, idcli,cur,conn):
    print("\nSessão iniciada como Cliente: ", name)
    c = input("\n\n1 - Consultar mensagens lidas\n2 - Consultar mensagens não lidas"
              "\n3 - Selecionar uma mensagem\n4 - Voltar ao menu\n5 - Logout\n\nEscreva uma opçao: ")
    while (c != 1 or c != 2 or c != 3 or c != 4):

        if c == "1":
            mensagensLidas(name, idcli,cur,conn)
        elif c == "2":
            mensagensNaoLidas(name, idcli,cur,conn)
        elif c == "3":
            selecionarMensagem(name,idcli,cur,conn)
        elif c == "4":
            menuCliente(name, idcli,cur,conn)
        elif c == "5":
            logout(name, idcli)
        else:
            print("\nOpçao Invalida")
            continue

def mensagensLidas(name, user_id,cur,conn):
    verifica = verificaMensagemLida(user_id)
    if verifica == False:
        print("\nNão há mensagens lidas.")
        consultarMensagens(name, user_id)

    print("\nSessão iniciada como Cliente: ", name, "\nMensagens lidas:")
    cur.execute("select * from flag_message")
    for i in cur.fetchall():
        if user_id == i[2]:
            if True == i[0]:
                message_id = i[1]

                cur.execute("select * from message")
                for j in cur.fetchall():
                    if message_id == j[0]:
                        print("Mensagem", j[0], " - Assunto: ", j[1])
                        consultarMensagens(name, user_id, cur, conn)

def mensagensNaoLidas(name,user_id,cur,conn):
    verifica = verificaMensagemNaoLida(user_id)
    if verifica == False:
        print("Não há mensagens não lidas.")
        consultarMensagens(name, user_id,cur,conn)

    print("\nSessão iniciada como Cliente: ", name, "\nMensagens não lidas:")
    cur.execute("select * from flag_message")
    for i in cur.fetchall():
        if user_id == i[2]:
            if False == i[0]:
                message_id = i[1]

                cur.execute("select * from message")
                for j in cur.fetchall():
                    if message_id == j[0]:
                        print("ID Mensagem: ", j[0], " - Assunto: ", j[1])

def selecionarMensagem(name,user_id,cur,conn):

    id = input("\n\nID da mensagem que prentende ver:" )
    temMensagem = verificaMensagem(id, user_id)
    if temMensagem == False:
        print("\nA mensagem não existe")
        consultarMensagens(name, user_id, cur, conn)

    cur.execute("update flag_message set read_check = %s where message_id = %s and user_id = %s", (True, id, user_id))
    conn.commit()
    cur.execute("select * from message where id = %s",[id])
    for i in cur.fetchall():
        print("\n\nID da mensagem:", i[0], "\nAssunto:", i[1], "\nTexto:", i[2])
    consultarMensagens(name, user_id)

def verificaMensagem(id, user_id):
    cur.execute("select * from message where id = %s", [id]) #possivel erro porque tem o mesmo nome id
    for linha in cur.fetchall():
        return (True)
    return (False)

def verificaMensagemLida(user_id,cur,conn):
    cur.execute("select * from flag_message")
    for i in cur.fetchall():
        if user_id == i[2]:
            if i[0] == True:
                return (True)
    return (False)

def verificaMensagemNaoLida(user_id,cur,conn):
    cur.execute("select * from flag_message")
    for i in cur.fetchall():
        if user_id == i[2]:
            if i[0] == False:
                return (True)
    return (False)

def pesquisa(name, idcli,cur,conn):
    print("\n\nSessão iniciada como Cliente: ", name)

    c = input("\n\n1 -Pesquisar todos os artigos no sistema\n2 Pesquisar artigos no historico"
              "\n3 - Menu anterior\n4 - Logout\nSelecione uma opçao: ")
    while (c != 1 or c != 2 or c != 3 or c != 4):

        if c == "1":
            pesquisaTodosArtigos(name,idcli,cur,conn)
        elif c == "2":
            pesquisarHistoryrent(name,idcli,cur,conn)
        elif c == "3":
            menuCliente(name,idcli,cur,conn)
        elif c == "4":
            logout(name,idcli)
        else:
            print("\nOpcao invalida")
            continue

def pesquisaTodosArtigos(name, idcli,cur,conn):

    print("\n\nSessão iniciada como cliente: ", name)

    c = input("\n\n1 - Pesquisar por tipo de artigo\n2 - Titulo\n3 - Ator\n4 - Realizador"
              "\n5 - Produtor\n6 - Voltar ao menu\n7 - Logout\nSelecione uma opcao: ")

    while (c != 1 or c != 2 or c != 3 or c != 4 or c != 5 or c != 6 or c != 7):


        if c == "1":
            pesquisaGenre(name, cur)
        elif c == "2":
            pesquisarName(name, cur)
        elif c == "3":
            pesquisaActor(name, cur)
        elif c == "4":
            pesquisaDirector(name, cur)
        elif c == "5":
            pesquisaProducer(name, cur)
        elif c == "6":
            menuCliente(name, idcli, cur, conn)
        elif c == "7":
           logout(name, idcli)
        else:
            print("\nOpçao invalida")
            continue

def pesquisaGenre(name, cur):
    while True:

        print('\n\nSessao Iniciada como cliente: ', name)
        genre = input ("\n\nIntroduza o tipo de artigo: ")

        cur.execute("select id from genre where name = %s",(genre))
        if cur.rowcount == 0:
         print("\nNão existe artigo")
         continue

        else:
            print("\n\nResultado de pesquisa: ")
            cur.execute("select id from genre where name = %s",(genre))
            idgenre = cur.fetchone()[0]
            print("\nTipo de artigo: ", genre)

            cur.execute("select article_id from article_genre where genre_id = %s",(idgenre))

            for i in cur.fetchall():
                cur.execute("select name from article where id = %s",(i[0]))
                genrename = cur.fetchone()[0]
                print("\nNome: ",genrename)
            break

def pesquisarName(name, cur ):
    while True:

        print("\n\nSessao iniciada como cliente: ", name)
        nameArticle = input("\n\nIntroduza o nome do artigo: ")
        cur.execute("select id from article where name = %s",(nameArticle))

        if cur.rowcount == 0:
            print("\nNão existe artigo")
            continue

        else:
            print("\nResultado de pesquisa: ")
            cur.execute("select id from article where name = %s", (nameArticle))
            idArticle = cur.fetchone()[0]

            cur.execute("select name from article where id = %s", (idArticle))
            articlename = cur.fetchone()[0]
            print("\nNome do artigo: ", articlename)
        break

def pesquisaActor(name, cur):
    while True:

        print('\n\nSessao Iniciada como cliente: ', name)
        actor = input ("\n\nIntroduza o nome do ator: ")
        cur.execute("select id from actor where name = %s",(actor))

        if cur.rowcount == 0:
         print("\nNão existe artigo")
         continue

        else:
            print("\nResultado de pesquisa: ")
            cur.execute("select id from actor where name = %s",(actor))
            idactor = cur.fetchone()[0]

            cur.execute("select article_id from article_actor where actor_id = %s",(idactor))
            for i in cur.fetchall():
                cur.execute("select name from article where id = %s",(i[0]))
                articlename = cur.fetchone()[0]
                print("\nNome do artigo: ",articlename)
            break

def pesquisaDirector(name, cur):

    while True:

        print('\n\nSessao Iniciada como cliente: ', name)
        director = input("\n\nIntroduza o nome do director: ")
        cur.execute("select id from director where name = %s", (director))

        if cur.rowcount == 0:
            print("\nNão existe artigo")
            continue

        else:
            print("\nResultado de pesquisa: ")
            cur.execute("select id from director where name = %s", (director))
            idDirector = cur.fetchone()[0]

            cur.execute("select article_id from article_director where director_id = %s", (idDirector))
            for i in cur.fetchall():
                cur.execute("select name from article where id = %s", (i[0]))
                articlename = cur.fetchone()[0]
                print("\nNome do artigo: ", articlename)
            break

def pesquisaProducer(name, cur):
    while True:

        print('\n\nSessao Iniciada como cliente: ', name)
        producer = input ("\n\nIntroduza o nome do produtor: ")
        cur.execute("select id from producer where name = %s",(producer))

        if cur.rowcount == 0:
         print("\nNão existe artigo")
         continue

        else:
            print("\nResultado de pesquisa: ")
            cur.execute("select id from producer where name = %s",(producer))
            idProducer = cur.fetchone()[0]
            print("\nNome do produtor ", producer)

            cur.execute("select article_id from article_producer where producer_id = %s",(idProducer))
            for i in cur.fetchall():

                cur.execute("select name from article where id = %s",(i[0]))
                articlename = cur.fetchone()[0]
                print("\nNome do artigo: ",articlename )
            break


def pesquisarHistoryrent(name,idcli,cur,conn):
    print("\n\nSessão iniciada como Cliente: ", name)
    c = input("\n\n1 - Pesquisar por tipo de artigo\n2 - Titulo\n3 - Ator\n4 - Realizador"
              "\n5 - Produtor\n6 - Voltar ao menu\n7 - Logout\nSelecione uma opcao: ")
    while (c != 1 or c != 2 or c != 3 or c != 4 or c != 5 or c != 6 or c != 7):

        if c == "1":
            pesquisarGenreHistory(name,cur)
        elif c == "2":
            pesquisarNameHistory(name,idcli,cur,conn)
        elif c == "3":
            pesquisarActorHistory(name,idcli,cur,conn)
        elif c == "4":
            pesquisarDirectorHistory(name,idcli,cur,conn)
        elif c == "5":
            pesquisarProducerHistory(name, idcli,cur,conn)
        elif c == "6":
            menuCliente(name, idcli,cur,conn)
        elif c == "7":
            logout(name, idcli,cur,conn)
        else:
            continue

def pesquisarGenreHistory(name, cur):
    while True:

        print('\nSessao Iniciada como cliente: ', name)
        genre = input("\n\nIntroduza o tipo de aritigo  neste momento alugado: ")
        cur.execute("select id from genre where name = %s", (genre))

        if cur.rowcount == 0:
            print("\nNão existe artigo")
            continue

        else:
            print("\n\nResultados de pesquisa: ")
            cur.execute("select id from genre where name = %s", (genre))
            idgenre = cur.fetchone()[0]
            print("\n\nTipo de artigo: ", genre)

            cur.execute("select article_id from article_genre where genre_id = %s", (idgenre))
            idarticle = cur.fetchone()

            cur.execute("select rent_id from rent_article where article_id=%s",idarticle)
            #idrent=cur.fetchone()

            for i in cur.fetchall():
                cur.execute("select name from article where id=%s",i[0])
                articlename = cur.fetchone()[0]
                print("\nNome do artigo: ", articlename)
            break


def pesquisarNameHistory(name, idcli,cur):
    while True:

        print("\n\nSessao iniciada como cliente: ", name)
        nameArticle = input("\nIntroduza o nome do artigo: ")
        cur.execute("select id from article where name = %s",(nameArticle))

        if cur.rowcount == 0:
            print("\nNão existe artigo")
            continue

        else:
            print("\nResultado de pesquisa: ")
            cur.execute("select id from article where name = %s", (nameArticle))
            idArticle = cur.fetchone()[0]

            cur.execute("select rent_id from rent_article where article_id=%s",(idArticle))
            idrent = cur.fetchone()[0]

            cur.execute("select name from article where id = %s", (idrent))
            articlename = cur.fetchone()[1]
            print("\nNome do artigo: ", articlename)
        break

def pesquisarActorHistory(name, cur):
    while True:

        print('\n\nSessao Iniciada como cliente: ', name)
        actor = input("\n\nIntroduza o nome do artigo neste momento alugado que pretende pesquisar: ")
        cur.execute("select id from actor where name = %s", (actor))

        if cur.rowcount == 0:
            print("\nNão existe artigo")
            continue

        else:
            print("\nResultados de pesquisa: ")
            cur.execute("select id from actor where name = %s", (actor))
            idactor = cur.fetchone()[0]
            print("\nNome do ator: ", actor)

            cur.execute("select article_id from article_actor where actor_id = %s", (idactor))
            idarticle = cur.fetchone()[0]

            cur.execute("select rent_id from rent_article where article_id=%s",(idarticle))

            for i in cur.fetchall():
                cur.execute("select name from article where id=%s", i[0])
                articlename = cur.fetchone()[0]
                print("\nNome do artigo: ", articlename)
                break

def pesquisarDirectorHistory(name,cur):
    while True:

        print('\nSessao Iniciada como cliente: ', name)
        director = input("\n\nIntroduza o nome do realizador no artigo neste momento alugado: ")
        cur.execute("select id from director where name = %s", (director))

        if cur.rowcount == 0:
            print("\nNão existe artigo")
            continue

        else:
            print("\nResultados de pesquisa: ")
            cur.execute("select id from director where name = %s", (director))
            idDirector = cur.fetchone()[0]
            print("\nNome do Realizafor: ", director)

            cur.execute("select article_id from article_director where director_id = %s", (idDirector))
            idarticle = cur.fetchone()[0]

            cur.execute("select rent_id from rent_article where article_id=%s", (idarticle))

            for i in cur.fetchall():
                cur.execute("select name from article where id=%s", i[0])
                articlename = cur.fetchone()[0]
                print("\nNome do artigo: ", articlename)
            break

def pesquisarProducerHistory(name,cur):
    while True:

        print('\nSessao Iniciada como cliente: ', name)
        producer = input("\n\nIntroduza o noem do produtor do artigo neste momento alugado: ")
        cur.execute("select id from producer where name = %s", (producer))

        if cur.rowcount == 0:
            print("\nNão existe artigo")
            continue

        else:
            print("\nResultados de pesquisa: ")
            cur.execute("select id from producer where name = %s", (producer))
            idProducer = cur.fetchone()[0]
            print("\nNome do produtor: ", producer)

            cur.execute("select article_id from article_producer where producer_id = %s", (idProducer))
            idarticle = cur.fetchone()[0]

            cur.execute("select rent_id from rent_article where article_id=%s", (idarticle))

            for i in cur.fetchall():
                cur.execute("select name from article where id=%s", i[0])
                articlename = cur.fetchone()[0]
                print("\nNome do artigo: ", articlename)
            break

def logout(name, idcli):
    print("Logout.")
    #funcoes.menu()

cur.close()
conn.close()
