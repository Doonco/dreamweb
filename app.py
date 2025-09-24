import streamlit as st
import pandas as pd

st.title("간단한 Pandas + Streamlit 앱")

# 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # Pandas로 CSV 읽기
    df = pd.read_csv(uploaded_file)
    
    st.subheader("데이터 미리보기")
    st.write(df.head())  # 상위 5개 행 출력

    st.subheader("기본 통계 정보")
    st.write(df.describe())  # 기본 통계 정보 출력
else:
    st.info("먼저 CSV 파일을 업로드하세요.")
