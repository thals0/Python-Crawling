import requests
import bs4

list=[['G마켓 랭크 순','판매 인기 순','낮은 가격 순','높은 가격 순'],['&s=7','&s=8','&s=1','&s=2']]
#print(list[0])
#print(len(list[0]))

while True:
    keyword=input("검색 상품:")
    if keyword =="0":
        break

    print("<G마켓의", keyword, "상품 정보>")

    for i in range(len(list[1])):
        URL="https://browse.gmarket.co.kr/search?keyword="+keyword+"&s="+ list[1][i]
        raw=requests.get(URL)
        html=bs4.BeautifulSoup(raw.text,'html.parser')
        box=html.find('div',{'class':'section__module-wrap','module-design-id':'15'})
        items=box.find_all('div',{"class":'box__item-container'})

        print("<",list[0][i],">")

        for item in items[:4]:
            title=item.find('span',{'class':'text__item'})
            price=item.find('strong',{'class':'text__value'})
            print("이름:",title.text)
            print("가격:",price.text)
            print()
