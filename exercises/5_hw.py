# 5_hw.py

class SayDay:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def is_leap(self):
        y = self.year
        return ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0))
        
    def days(self):
        days_in_month = [
            31, 29 if self.is_leap() else 28, 31, 30,
            31, 30, 31, 31,
            30, 31, 30, 31,]
        total = 0
        m = 0
        while m < self.month - 1:
            total += days_in_month[m]
            m += 1
            
        total += self.day
        return total
    
    def days_left(self):
        total_days = 366 if self.is_leap() else 365
        return total_days - self.days()
    def weekday(self):
        y = self.year
        m = self.month
        d = self.day
        
        if m < 3:
            m += 12
            y -= 1
        
        k = y % 100
        j = y // 100
        h =  (d + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
        
        return h
    def weekday_name(self):
        names = ["토요일", "일요일", "월요일",
                 "화요일", "수요일", "목요일", "금요일"]
        return names[self.weekday()]

while True:
    year = int(input("년도를 입력하세요: "))
    month = int(input("월을 입력하세요: "))
    day = int(input("일을 입력하세요: "))
    
    date = SayDay(year, month, day)
    
    print("몇 번째 날: ", date.days())
    print("남은 일수: ", date.days_left())
    print("요일 숫자: ", date.weekday())
    print("요일 이름: ", date.weekday_name())