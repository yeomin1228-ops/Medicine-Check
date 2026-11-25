
import streamlit as st

# 재고 상태 판별 함수
def check_stock(num):
    if num == 0:
        return "재고 없음"
    elif num < 30:
        return "재고 부족"
    else:
        return "재고 충분"

# 약품 리스트
drugs = [
    ["타이레놀", 0],
    ["이부프로펜", 0],
    ["항생제", 0],
    ["소화제", 0],
    ["감기약", 0],
    ["소염제", 0]
]

st.title("💊 약국 재고 확인기")

# 약품 개수 입력받기
for d in drugs:
    d[1] = st.number_input(d[0] + " 재고 개수", min_value=0, step=1)

# 재고 상태 한 번에 출력
if st.button("재고 상태 확인하기"):
    low_drugs = []

    for d in drugs:
        status = check_stock(d[1])

        if status != "재고 충분":
            low_drugs.append(d[0])

    st.subheader("📋 전체 재고 상태")

    for d in drugs:
        st.write(f"{d[0]}: {check_stock(d[1])}")

    st.warning(f"부족한 약품은 총 {len(low_drugs)}종입니다. ({', '.join(low_drugs)})")
