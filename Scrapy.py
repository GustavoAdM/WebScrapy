from scrapy import Spider, Request
from scrapy.crawler import CrawlerProcess
from bancodados import BancodeDados


class ScrapyNet(Spider):

    name = 'filmesNet'
    url_start = 'https://www.imdb.com/list/ls530915139/'
    user_agent = {
        'user': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36'}

    def start_requests(self, url=url_start, agent=user_agent):
        yield Request(url, headers=agent)

    def parse(self, response):
        list_filme = []

        # retorna uma lista
        for qntfilmes in range(1, 101):
            rating = response.css(
                f'.mode-detail:nth-child({qntfilmes}) .ipl-rating-star.small .ipl-rating-star__rating::text').get()
            filmes = response.css(
                f'.mode-detail:nth-child({qntfilmes}) .lister-item-header a::text').get()
            anos = response.css(
                f'.mode-detail:nth-child({qntfilmes}) .text-muted.unbold::text').get()
            genero = response.css(f'.genre::text').getall()

            if rating == None:
                list_filme.append(
                    {'Filme': filmes, 'Ano': anos, 'Rating': '0', 'Genero': genero[qntfilmes-1]})
            else:
                list_filme.append(
                    {'Filme': filmes, 'Ano': anos, 'Rating': rating, 'Genero': genero[qntfilmes-1]})

        for qntlista in range(0, len(list_filme)):
            c_filme = list_filme[qntlista]['Filme']
            c_ano = list_filme[qntlista]['Ano']
            c_rating = list_filme[qntlista]['Rating']
            c_genero = list_filme[qntlista]['Genero']
            BancodeDados().inserirdados(c_filme, c_ano, c_rating, c_genero)


proc = CrawlerProcess()
proc.crawl(ScrapyNet)
proc.start()
