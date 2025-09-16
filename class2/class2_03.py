# 직원 Employee - 아이디, 이름, 급여
class Employee:
    def __init__(self, id, name, base_salary):
        self.id = id
        self.name = name
        self._base_salary = base_salary # private 의미로 사용
    @property
    def base_salary(self):
        return self._base_salary
    @base_salary.setter
    def base_salary(self, money):
        if money > 0:
            self._base_salary = money
        else:
            raise ValueError('금액은 양수입니다')
    def emp(self):
        print('직원 클래스')    
    def __str__(self):
        return f'아이디:{self.id}, 이름:{self.name}, 급여:{self._base_salary}'

# 정규직 - FullTimeEmployee - 보너스
class FullTimeEmployee(Employee):
    def __init__(self, id, name, base_salary, bonus):
        super().__init__(id, name, base_salary)
        self.bonus = bonus
    # 보너스도 마이너스 입력 불가
    def fte(self):
        print('정규직 클래스')
    def __str__(self):
        return super().__str__() + f', 보너스: {self.bonus}'

# 계약직 - PartTimeEmployee - 시간당 급여, 기본급 없음
class PartTimeEmployee(Employee):
    def __init__(self, id, name, per_hours, hours):
        super().__init__(id, name, 0)
        self.per_hours = per_hours
        self.hours = hours
    def pte(self):
        print('계약직 클래스')
    def __str__(self):
        return super().__str__() + f', 시간당 페이:{self.per_hours}, 시간:{self.hours}'

# 인턴 - Intern - 고정수당
class Intern(Employee):
    def __init__(self, id, name, fixed_salary):
        super().__init__(id, name, 0)
        self.fixed_salary = fixed_salary
    def it(self):
        print('인턴 클래스')
    def __str__(self):
        return super().__str__() + f', 고정급여: {self.fixed_salary}'

p1 = FullTimeEmployee('1', '홍', 40000, 300)
p2 = PartTimeEmployee('2', '길', 3000, 5)
p3 = Intern('3', '동', 20000)
emp = [p1,p2,p3]

for i in emp:
    print(i)
    if isinstance(i, FullTimeEmployee):
        i.fte()
    elif isinstance(i, PartTimeEmployee):
        i.pte()
    elif isinstance(i, Intern):
        i.it()
    else:
        print('오류입니다')