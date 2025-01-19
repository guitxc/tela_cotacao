# pip install requests
import requests
# importar o tkinter
from tkinter import *

# função principal
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotações["text"] = texto

# Criar janela
janela = Tk()
# Titulo
janela.title("Cotação atual das Moedas")
# Tamanho da janela
janela.geometry("250x200")
# Texto inical
texto_orientação = Label(janela, text="Clique para ver as contações das moedas")
# Localização do texto
texto_orientação.grid(column=0, row=0, padx=10, pady=10)

# Botao
botao = Button(janela, text="Buscar cotações do DOLAR/EURO/BTC", fg="blue", command=pegar_cotacoes)
# Localização do botão
botao.grid(column=0, row=1, padx=10, pady=10)

# Cotação
texto_cotações = Label(janela, text="")
# Localização da cotação
texto_cotações.grid(column=0, row=2, padx=10, pady=10)

# Sempre a ultima janela de codigo
janela.mainloop()