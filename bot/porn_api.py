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
   # словарь, в котором категория является ключом, а циферка категории - значением
   # в функцию можно закидывать только строку - одну из этих категорий
  category: dict = {
                  'asia': 1,
                  'ebony': 17,
                  'gay_sex': 76,
                  'orgy': 80
                  }

  #формирование адреса для нашей категории
  url: str = 'https://www.pornhub.com/video?c=' + str(category[s])
    
  page = requests.get(url)   
  #print(page.status_code) оно работает

  soup = BS(page.text, "html.parser")

  ans = []
  for link in soup.findAll('a'):
    ans.append(link.get('href'))
  return ans
#че блять?       бл я тупой          мой мозк поплыл при попытке присвоить ссылки значениям 1,2,3,4  мне нужна твоя помощьб мома (つ﹏⊂)

if __name__ == '__main__':
  print(getporn_from_category('orgy'))