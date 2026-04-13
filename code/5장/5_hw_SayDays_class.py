# 5_hw_SayDays_class.py

class SayDay:
    def __init__(self, year, month, day):
        # 속성 초기화
        self.year = year
        self.month = month
        self.day = day
    
    def is_leap(self):
        # 윤년 여부 확인
        y = self.year
        return ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0))
        
    def days(self): # 당해년도 1월 1일 기준으로 몇째 날인지 알려줌
        # 1월 1일부터 지난 날짜
        # 윤년이면 2월이 29일, 평년이면 28일까지 존재
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
    
    def days_left(self): #당해년도 12월 31일 기준 남은 일수 알려줌
        # 12월 31일까지 남은 날짜
        # 윤년이면 1년이 366일, 평년이면 365일
        total_days = 366 if self.is_leap() else 365
        return total_days - self.days()
    def weekday(self): # 숫자로 요일을 알려줌
        # Zeller 공식으로 요일 계산
        y = self.year
        m = self.month
        d = self.day
        
        if m < 3:
            m += 12
            y -= 1
        
        k = y % 100
        j = y // 100 # 정수 필수
        h =  (d + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
        
        return h
    def weekday_name(self): # 요일을 한글로 알려줌 (0 -> 토요일)
        # 요일 이름 반환
        names = ["토요일", "일요일", "월요일",
                 "화요일", "수요일", "목요일", "금요일"]
        return names[self.weekday()]

# 클래스 사용하는 프로그램

while True:
    # 날짜 입력
    year = int(input("년도를 입력하세요: "))
    month = int(input("월을 입력하세요: "))
    day = int(input("일을 입력하세요: "))
    
    date = SayDay(year, month, day)
    
    # 결과 출력
    print("몇 번째 날: ", date.days())
    print("남은 일수: ", date.days_left())
    print("요일 숫자: ", date.weekday())
    print("요일 이름: ", date.weekday_name())