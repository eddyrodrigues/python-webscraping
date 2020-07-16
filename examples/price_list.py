import requests
from bs4 import BeautifulSoup

r = requests.get("http://testing-ground.scraping.pro/blocks?ver=1")
if(r.status_code != 200):
    None
else:
    website = r.text
    web_bs4 = BeautifulSoup(website, features="html.parser")

    #print(web_bs4.select_one("#case1").find("div"))
    divs_produtos = [web_bs4.select_one("#case1").find("div")]

    for div in web_bs4.select_one("#case1").find("div").findNextSiblings():
        divs_produtos = divs_produtos + [div]

    #print(divs_produtos[0]['class'])
    for item in divs_produtos:
        if ("ads" in item['class']):
            divs_produtos.remove(item)

    produtos = []
    nomes = []
    precos = []
    

    #print(div.select_one(".name").text);

    for div in divs_produtos:
        nomes = nomes + [div.select_one(".name").text]
        precos = precos + [div.find("span").findNextSibling().text]
        produtos = produtos + [(div.select_one(".name").text, div.find("span").findNextSibling().text)]
    
    for nome, preco in produtos:
        print("Nome do produto: ", nome)
        print("Preco do produto: ", preco)

    
#tip: use the open method to create a file and save all products to a single file!
