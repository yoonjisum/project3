import streamlit as st

# AI 도구 추천 데이터
ai_tools = {
    "PPT 제작": [
        {"name": "Gamma", "description": "글을 입력하면 자동으로 슬라이드 생성", "url": "https://gamma.app"},
        {"name": "Tome", "description": "스토리 기반 AI 프레젠테이션 도구", "url": "https://tome.app"}
    ],
    "자료 검색": [
        {"name": "Perplexity", "description": "출처 기반 AI 검색 엔진", "url": "https://www.perplexity.ai"},
        {"name": "Consensus", "description": "논문 기반 AI 요약 도구", "url": "https://consensus.app"}
    ],
    "시각화 자료 생성": [
        {"name": "ChartGPT", "description": "프롬프트로 그래프 생성", "url": "https://chartgpt.dev"},
        {"name": "Tableau", "description": "코딩 없이 데이터 시각화", "url": "https://public.tableau.com"}
    ]
}

def simple_summarize(text, max_sentences=2):
    sentences = text.split(". ")
    return ". ".join(sentences[:max_sentences]) + ("..." if len(sentences) > max_sentences else "")

st.set_page_config(page_title="📚 AI 과제 도우미", layout="centered")
st.title("📚 AI 과제 도우미 & 도구 바로가기")
st.markdown("과제 유형에 맞는 AI 도구를 추천하고, 실제로 바로 사용할 수 있게 연결해 드립니다.")

task_type = st.selectbox("📝 과제 유형을 선택하세요:", list(ai_tools.keys()))

if task_type:
    st.subheader(f"🔍 추천 AI 도구 - {task_type}")
    for tool in ai_tools[task_type]:
        col1, col2 = st.columns([0.7, 0.3])
        with col1:
            st.markdown(f"**{tool['name']}** - {tool['description']}")
        with col2:
            st.markdown(f"[바로가기 🔗]({tool['url']})")

st.markdown("---")

st.subheader("🧠 ChatGPT 스타일 간단 요약기 (로컬 처리)")
text_input = st.text_area("과제 내용을 붙여넣으면 요약해 드릴게요:")

if st.button("요약하기"):
    if text_input.strip():
        summary = simple_summarize(text_input)
        st.success("요약 결과:")
        st.markdown(f"> {summary}")
    else:
        st.warning("요약할 내용을 먼저 입력해 주세요.")

st.markdown("---")

st.subheader("🔎 Perplexity 검색하기")
search_query = st.text_input("검색할 키워드를 입력하세요:")

if st.button("Perplexity로 검색"):
    if search_query.strip():
        search_url = f"https://www.perplexity.ai/search?q={search_query.replace(' ', '+')}"
        st.markdown(f"[👉 Perplexity에서 '{search_query}' 검색하기]({search_url})")
    else:
        st.warning("검색어를 입력해 주세요.")
