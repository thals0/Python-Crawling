import requests 
import bs4

while True:
    keyword=input("검색을 원하는 키워드를 입력하세요.(0을 입력하면 종료)")
    if keyword =="0":
        break

    URL = "https://browse.gmarket.co.kr/search?keyword="+keyword 
    raw=requests.get(URL)
    html=bs4.BeautifulSoup(raw.text,'html.parser')
    box=html.find('div',{'class':'section__module-wrap','module-design-id':'15'})
    items=box.find_all('div',{"class":'box__item-container'})

    print("<G마켓의",keyword,"상품 정보>")
    for item in items[:3]:
        title=item.find('span',{'class':'text__item'})
        price=item.find('strong',{'class':'text__value'})
        print("이름:",title.text)
        print("가격:",price.text)
        print()
