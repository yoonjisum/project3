# ai_helper_app.py

import streamlit as st
from PIL import Image

# 페이지 설정
st.set_page_config(page_title="AI 과제 도우미", page_icon="🤖", layout="centered")

st.title("🎓 AI 과제 도우미")
st.write("많은 과제를 빠르고 효율적으로 처리할 수 있도록 인공지능 도구를 추천해드립니다.")

# 과제 유형 선택
task_type = st.selectbox(
    "어떤 과제를 도와드릴까요?",
    ["선택하세요", "PPT 제작", "자료 검색", "시각화 자료 생성", "에세이 작성", "프로그래밍 과제", "기타"]
)

# 인공지능 도구 추천 DB
ai_tools = {
    "PPT 제작": {
        "이름": "Gamma, Tome",
        "설명": "AI 기반으로 자동 디자인과 내용 요약을 통해 빠르게 PPT를 생성할 수 있습니다.",
        "링크": ["https://gamma.app", "https://tome.app"]
    },
    "자료 검색": {
        "이름": "Perplexity, Consensus",
        "설명": "질문에 대한 최신 논문, 웹 정보 등을 AI가 요약해 제공해주는 검색 도구입니다.",
        "링크": ["https://www.perplexity.ai", "https://consensus.app"]
    },
    "시각화 자료 생성": {
        "이름": "ChatGPT + Python, Canva, Flourish",
        "설명": "데이터 시각화를 위해 ChatGPT와 파이썬 코드를 활용하거나, 템플릿 기반 툴을 사용할 수 있습니다.",
        "링크": ["https://flourish.studio", "https://canva.com"]
    },
    "에세이 작성": {
        "이름": "ChatGPT, Grammarly",
        "설명": "초안 작성부터 문법 교정까지 글쓰기를 도와주는 AI 도구입니다.",
        "링크": ["https://chat.openai.com", "https://grammarly.com"]
    },
    "프로그래밍 과제": {
        "이름": "GitHub Copilot, ChatGPT Code Interpreter",
        "설명": "코드 자동 완성, 코드 리뷰, 디버깅 등을 도와주는 AI 코딩 도구입니다.",
        "링크": ["https://github.com/features/copilot", "https://chat.openai.com"]
    },
    "기타": {
        "이름": "ChatGPT",
        "설명": "과제 유형을 구체적으로 입력하면 그에 맞는 도구를 추천해드릴 수 있습니다.",
        "링크": ["https://chat.openai.com"]
    }
}

# 도구 추천 결과 출력
if task_type != "선택하세요":
    tool = ai_tools[task_type]
    st.subheader(f"✅ 추천 인공지능 도구: {tool['이름']}")
    st.write(tool["설명"])
    for link in tool["링크"]:
        st.markdown(f"[🔗 도구 바로가기]({link})")

ai_tools = {
    "PPT 제작": {
        "이름": "Gamma, Tome",
        "설명": "AI 기반으로 자동 디자인과 내용 요약을 통해 빠르게 PPT를 생성할 수 있습니다.",
        "링크": ["https://gamma.app", "https://tome.app"],
        "이미지": [
            "https://assets.gamma.app/homepage/Gamma_Logo.svg",  # Gamma 공식 로고 URL 예시
            "https://tome.app/static/media/tome-logo.a55a0d9e.svg"  # Tome 공식 로고 URL 예시
        ]
    },
    "자료 검색": {
        "이름": "Perplexity, Consensus",
        "설명": "질문에 대한 최신 논문, 웹 정보 등을 AI가 요약해 제공해주는 검색 도구입니다.",
        "링크": ["https://www.perplexity.ai", "https://consensus.app"],
        "이미지": [
            "https://www.perplexity.ai/static/media/logo.4e836e56.svg",
            "https://consensus.app/favicon.ico"
        ]
    },
    # ... 나머지 도구들도 동일하게 이미지 URL 추가
}

# 추천 결과 출력 예시
if task_type != "선택하세요":
    tool = ai_tools[task_type]
    st.subheader(f"✅ 추천 인공지능 도구: {tool['이름']}")
    st.write(tool["설명"])
    
    # 이미지와 링크를 같이 출력
    cols = st.columns(len(tool["이미지"]))
    for idx, img_url in enumerate(tool["이미지"]):
        with cols[idx]:
            st.image(img_url, width=100)
            st.markdown(f"[🔗 바로가기]({tool['링크'][idx]})")
