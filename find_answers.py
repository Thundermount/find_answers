import requests
from bs4 import BeautifulSoup
import time

class TestSolver:
# Данные для поиска ответов на вопрос
# первое сам вопрос второе варианты ответа и последнее количество найденных
    question = ''
    options = []
    answers = dict()
    def __init__(self,q,o):
        self.question = q.lower()
        self.options = o.lower().split('\n')

    def __get_links(self):
        question = self.question
        response = requests.get(
            "https://www.google.com/search?newwindow=1&sxsrf=ALeKk00njbb0RN_mCmM3p5-uqFJBPI6ibw%3A1606825460067&source=hp&ei=9DXGX5LNAbqTwPAP_dGt-Ac&q=" + question + "&oq=a&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIECCMQJzIGCCMQJxATMgUIABCxAzIFCC4QsQMyBQgAELEDMgUIABCxAzICCAAyAggAMgUIABCxA1CcBFicBGCjCGgAcAB4AIABf4gBf5IBAzAuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwiSl4um46ztAhW6CRAIHf1oC38Q4dUDCAc&uact=5"
        )

        soup = BeautifulSoup(response.text, "html.parser")
        links_div = soup.select('div.kCrYT')
        links = []
        for link in links_div:
            for i in link.select('a[href]'):
                links.append(i['href'])
                break
        return links

    def get_answers(self):
        options = self.options
        answers = self.answers
        i = 0
        for o in options:
            answers[i+1] = 0
            i+=1

        sites = self.__get_links()
        for link in sites:
            try:
                res = requests.get('https://www.google.com' + link)
                page = res.text.lower()

                i = 0
                for option in options:
                    score = 0.0
                    opt = option.split(" ")
                    for word in opt:
                        if word in page:
                            score += 1.0
                    answers[i+1] += score
                    i+=1
            except Exception:
                pass
        return answers
