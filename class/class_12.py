class Person:
    def __init__(self, name, age):
        self._name = name # private 변수로 설정
        self._age = age # private 변수로 설정
    # 데코레이터를 이용한 setter, getter 설정
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def age(self):
        return self._age
    @name.setter
    def age(self, age):
        if age < 0:
            raise ValueError('나이는 음수가 될수 없습니다.')
        self._age = age
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    
a = Person("홍길동", 20)
print(a._name)
print(a.age)
a.name = '김철수'
a.age = 30