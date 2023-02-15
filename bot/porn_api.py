import requests
from pornhub_api import PornhubApi
from bs4 import BeautifulSoup as BS
#с-76 gay sex(https://www.pornhub.com/video?c=76) c-80 orgy(https://www.pornhub.com/video?c=80)
#  c-17 ebony(https://www.pornhub.com/video?c=17) c-1 asia(https://www.pornhub.com/video?c=1)



#это пока не надо
api = PornhubApi()

#временная функция, надо заменить на нормальную
def getporn_from_request(s: str) -> str:
    
    return('суперпорно с конями и ' + s)

def getporn_from_category(s: str) -> str:
   # category = dict ([('gay_sex', 1), ('orgy', 2), ('ebony', 3), ('asia', 4)])
    
    
    
    #category = urllib.request.urlopen("https://www.pornhub.com/video?c=76")    <------- (stackoverflow) будет, вроде как, сёрчить в данной категории на одной странице 
   # soup = BeautifulSoup(html_page, "html.parser")
    #for link in soup.findAll('a'):
      #  print(link.get('href'))
    pass

#че блять?       бл я тупой          мой мозк поплыл при попытке присвоить ссылки значениям 1,2,3,4  мне нужна твоя помощьб мома (つ﹏⊂)