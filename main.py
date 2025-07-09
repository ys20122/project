import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    # 프로젝트 폴더 내 waste_data.csv 파일을 읽습니다.
    return pd.read_csv("waste_data.csv")

data = load_data()

st.title("♻️ 분리도우미")
st.markdown("쓰레기의 **정확한 분리배출 방법**과 **환경 영향**을 알아보세요!")

query = st.text_input("🔍 분리배출 방법이 궁금한 쓰레기를 입력하세요 (예: 페트병, 종이컵 등)").strip()

if query:
    # 이름 컬럼에서 검색어 포함된 행을 찾음 (대소문자 구분 안 하고, 정규식 끔)
    result = data[data['name'].str.contains(query, case=False, na=False, regex=False)]

    if not result.empty:
        for _, row in result.iterrows():
            st.subheader(f"🗑️ {row['name']}")
            st.write(f"**📂 분류:** {row['category']}")
            st.write(f"**🏷️ 라벨 분리 필요:** {row['label_separation']}")
            st.write(f"**🔩 뚜껑 분리 필요:** {row['cap_separation']}")
            st.write(f"**🧼 세척 필요:** {row['wash_required']}")
            st.write(f"**♻️ 재활용 가능 여부:** {row['recyclable']}")
            st.write(f"**🔬 재질:** {row['material']}")
            st.info(f"🕒 분해 시간: {row['decompose_time']}")
            st.success(f"🌍 환경 메시지: {row['eco_note']}")
    else:
        st.warning("일치하는 쓰레기 정보를 찾을 수 없습니다. 다른 이름으로 검색해보세요.")
