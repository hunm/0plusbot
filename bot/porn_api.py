import requests
from bs4 import BeautifulSoup as BS

#скидывает порно по запросу
def getporn_from_request(s: str) -> list:
  url: str = 'https://pornhub.com/video/search?search=' + s
  return makepornlist(url)


def getbestporn() -> list:
  return makepornlist('https://pornhub.com/video?o=tr')


def getporn_from_category(s: str):
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
  return makepornlist(url)
  

#формирует массив со ссылками на порно для любого полученного адреса
def makepornlist(url: str) -> list:
  page = requests.get(url)
  soup = BS(page.text, "html.parser")
  ans = []
  #парсит все видео со страницы
  for video in soup.findAll(class_='pcVideoListItem js-pop videoblock videoBox'):
    if video.get('data-video-vkey') is not None:
      #формирует ссылку на каждое видео со страницы
      ans.append('https://pornhub.com/view_video.php?viewkey=' + video.get('data-video-vkey'))
  return ans



if __name__ == '__main__':
  #print(getporn_from_category('orgy'))
  pass