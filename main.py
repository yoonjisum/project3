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
pip install streamlit
import streamlit as st

# --- 키워드 기반 분류 함수 ---
def classify_task_keywords(text):
    text = text.lower()

    if any(keyword in text for keyword in ["ppt", "슬라이드", "발표", "프레젠테이션", "설명자료"]):
        return "PPT 제작"
    elif any(keyword in text for keyword in ["검색", "자료", "논문", "정보", "조사", "리서치"]):
        return "자료 검색"
    elif any(keyword in text for keyword in ["그래프", "시각화", "차트", "도표", "데이터"]):
        return "시각화 자료 생성"
    else:
        return "기타"

# --- 추천 도구 사전 ---
ai_tools = {
    "PPT 제작": [
        {"name": "Gamma", "description": "글을 입력하면 자동으로 슬라이드 생성"},
        {"name": "Tome", "description": "스토리 기반 AI 프레젠테이션 도구"}
    ],
    "자료 검색": [
        {"name": "Perplexity", "description": "출처 기반 AI 검색 엔진"},
        {"name": "Consensus", "description": "논문 기반 AI 검색 요약 도구"}
    ],
    "시각화 자료 생성": [
        {"name": "ChatGPT + Python", "description": "프롬프트 기반 시각화 코드 생성"},
        {"name": "Tableau", "description": "코딩 없이 데이터 시각화"}
    ],
    "기타": []
}

# --- Streamlit App ---
st.set_page_config(page_title="키워드 기반 과제 도우미", page_icon="🧠", layout="centered")
st.title("🧠 키워드 기반 과제 도우미")
st.markdown("과제 내용을 입력하면, 키워드 기반으로 적절한 AI 도구를 추천해드립니다!")

user_input = st.text_area("📥 과제 내용을 자유롭게 입력하세요:")

if st.button("AI 도구 추천받기") and user_input:
    task_type = classify_task_keywords(user_input)
    st.success(f"✅ 분류된 과제 유형: **{task_type}**")

    if ai_tools[task_type]:
        st.markdown("### 🔍 추천 AI 도구:")
        for tool in ai_tools[task_type]:
            st.markdown(f"""
            **🔹 {tool['name']}**  
            - {tool['description']}
            """)
    else:
        st.warning("⚠️ 정확한 유형을 찾지 못했어요. 입력을 더 구체적으로 작성해 주세요.")

