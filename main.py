pip install streamlit
import streamlit as st

# --- 과제 유형별 추천 도구 사전 ---
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

# --- Streamlit 앱 구성 ---
st.set_page_config(page_title="📚 AI 과제 도우미", layout="centered")
st.title("📚 AI 기반 과제 도우미")
st.markdown("많은 과제를 효율적으로 처리할 수 있도록 적절한 AI 도구를 추천해드립니다!")

# --- 자연어 입력 분류 섹션 ---
st.header("🧠 자연어 입력으로 과제 분석하기")
user_input = st.text_area("자유롭게 과제 내용을 입력하세요:")

if st.button("AI 도구 추천받기 (자연어 입력)") and user_input:
    task_type = classify_task_keywords(user_input)
    st.success(f"✅ 분류된 과제 유형: **{task_type}**")

    if ai_tools[task_type]:
        st.markdown("### 🔍 추천 AI 도구:")
        for tool in ai_tools[task_type]:
            st.markdown(f"**🔹 {tool['name']}**\n- {tool['description']}")
    else:
        st.warning("⚠️ 과제 유형을 정확히 파악하지 못했어요. 입력을 더 구체적으로 작성해 주세요.")

st.markdown("---")

# --- 기존 선택형 추천 기능 유지 ---
st.header("🎯 과제 유형을 직접 선택해서 추천받기")
task_choice = st.selectbox("과제 유형을 선택하세요:", list(ai_tools.keys())[:-1])  # '기타' 제외

if task_choice:
    st.markdown(f"### 🧠 선택한 유형: **{task_choice}**")
    st.markdown("### 🔍 추천 AI 도구:")
    for tool in ai_tools[task_choice]:
        st.markdown(f"**🔹 {tool['name']}**\n- {tool['description']}")
