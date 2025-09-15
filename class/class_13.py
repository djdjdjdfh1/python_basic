# 클래스
# 클래스 변수, 인스턴스 변수
# 생성자 __init__
# 메소드 __str__, __eq__, __ne__, __lt__, __gt__
# property, getter, setter, deleter --> 함수를 변수처럼 사용
# 객체생성

# 상품관리
# 상품명, 가격, 재고

class Product:
    def __init__(self, name, price, stock):
        self._name = name
        self._price = price
        self._stock = stock
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value
    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, value):
        self._stock = value

    def __str__(self):
        return f'상품명: {self._name}, 가격: {self._price}, 재고: {self._stock}'

p1 = Product('삼다수', 500, 20)
p1.name = '제주삼다수'
print(p1.name)
products = [
    Product('삼다수', 500, 20),
    Product('칸타타', 1500, 50),
    Product('비락식혜', 1200, 30)
]
# 가격 20% 인하
# 가격 10% 인상
# 제품 출력