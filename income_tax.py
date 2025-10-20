# 소득(income)과 세금(tax) 변수 선언
income = 3500  # 단위: 만원
tax = 0

# 소득 수준에 따라 세율 결정
if income <= 1000:
    tax = income * 0.05
    level = "저소득층"
elif income <= 3000:
    tax = income * 0.25   # ✅ 중간소득층 25%
    level = "중간소득층"
else:
    tax = income * 0.50   # ✅ 고소득층 50%
    level = "고소득층"

# 결과 출력
print(f"소득: {income}만원")
print(f"세금: {tax:.1f}만원")
print(f"소득 수준: {level}")
