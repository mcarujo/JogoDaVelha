from Board import Board

tabela = Board()
tabela.print()
retorno = tabela.where_i_lose()
if(isinstance(retorno, list)):
    print('é array')
else:
    print('é falso')




