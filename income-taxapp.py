import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="소득·세금 계산기", page_icon="💰", layout="centered")

st.title("💰 소득·세금 계산기")
st.caption("조건: 저소득 5%, 중간소득 25%, 고소득 50% (단위: 만원)")

# 사용자 입력
income = st.number_input("소득을 입력하세요 (만원)", min_value=0, step=50, value=3500)

# 소득 수준 분류 및 세금 계산
if income <= 1000:
    tax = income * 0.05
    level = "저소득층"
elif income <= 3000:
    tax = income * 0.25
    level = "중간소득층"
else:
    tax = income * 0.50
    level = "고소득층"

# 결과 표시
st.subheader("📊 계산 결과")
st.metric("소득", f"{income:,.0f} 만원")
st.metric("세금", f"{tax:,.1f} 만원")
st.metric("소득 수준", level)

# 참고 정보 (선택)
with st.expander("계산 기준 보기"):
    st.write("""
- 저소득층: 소득 ≤ 1,000만원 → 세율 5%
- 중간소득층: 소득 ≤ 3,000만원 → 세율 25%
- 고소득층: 소득 > 3,000만원 → 세율 50%
""")
