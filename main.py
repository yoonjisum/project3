import streamlit as st

# --- 인공지능 도구 데이터 정의 ---
ai_tools = {
    "PPT 제작": [
        {
            "name": "Gamma",
            "description": "AI 기반 슬라이드 자동 생성 도구. 글 입력만으로 시각적으로 멋진 프레젠테이션 생성 가능."
        },
        {
            "name": "Tome",
            "description": "AI 프레젠테이션 제작 도구. 간단한 프롬프트로 스토리텔링 기반 PPT 생성."
        }
    ],
    "자료 검색": [
        {
            "name": "Perplexity AI",
            "description": "최신 정보와 출처를 함께 제공하는 AI 검색 도구. 과제에 필요한 신뢰성 높은 자료를 빠르게 검색."
        },
        {
            "name": "Consensus",
            "description": "논문 요약 AI 도구. 논문 중심의 정보가 필요할 때 유용함."
        }
    ],
    "시각화 자료 생성": [
        {
            "name": "ChatGPT + Python",
            "description": "프롬프트 기반 데이터 시각화 코드 생성. matplotlib, seaborn, plotly 등을 활용."
        },
        {
            "name": "Tableau Public",
            "description": "코딩 없이 시각화 자료를 만들 수 있는 무료 툴."
        }
    ]
}

# --- Streamlit App ---
st.set_page_config(page_title="AI 과제 도우미", page_icon="🤖", layout="centered")
st.title("🎓 AI 기반 과제 도우미")
st.subheader("많은 과제를 효율적으로 해결할 수 있도록, 적절한 인공지능을 추천해드립니다.")

st.markdown("#### 📌 어떤 과제를 도와줄까요?")
task_type = st.selectbox("과제 유형을 선택하세요:", list(ai_tools.keys()))

if task_type:
    st.markdown(f"### 🧠 추천 AI 도구 ({task_type})")
    for tool in ai_tools[task_type]:
        st.markdown(f"""
        #### 🔹 {tool['name']}
        - {tool['description']}
        """)

st.markdown("---")
st.markdown("💡 **Tip**: 다양한 도구를 조합해 사용하면 과제 효율을 극대화할 수 있어요!")
