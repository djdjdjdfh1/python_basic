from abc import ABC, abstractmethod

class Parents(ABC):
    def make_money(self):
        raise NotImplementedError
    
    @abstractmethod
    def save_money(self):
        print('저축')

class Child(Parents):
    def make_money(self): # 부모의 make_moeny 재정의(override)
        print('장사')
    def save_money(self):
        print('투자')

c = Child() # 부모의 추상메서드를 상속받으면 클래스에서 반드시 재정의 안하면 객체생성 불가
c.make_money() # 다형성, 자식클래스에서 재정의 안하면 예외 발생하도록 설계
c.save_money() # 추상화