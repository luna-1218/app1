import streamlit as st
import random

# 대륙별 나라-수도 데이터
continent_data = {
    "아시아": {
        "네팔": "카트만두",
        "대한민국": "서울",
        "동티모르": "딜리",
        "라오스": "비엔티안",
        "레바논": "베이루트",
        "말레이시아": "쿠알라룸푸르",
        "몰디브": "말레",
        "몽골": "울란바토르",
        "미얀마": "네피도",
        "바레인": "마나마",
        "방글라데시": "다카",
        "베트남": "하노이",
        "부탄": "팀부",
        "북한": "평양",
        "브루나이": "반다르스리브가완",
        "사우디아라비아": "리야드",
        "스리랑카": "콜롬보",
        "시리아": "다마스쿠스",
        "싱가포르": "싱가포르",
        "아랍에미리트": "아부다비",
        "아르메니아": "예레반",
        "아제르바이잔": "바쿠",
        "아프가니스탄": "카불",
        "예멘": "사나",
        "오만": "무스카트",
        "요르단": "암만",
        "우즈베키스탄": "타슈켄트",
        "이라크": "바그다드",
        "이란": "테헤란",
        "이스라엘": "예루살렘",
        "인도": "뉴델리",
        "인도네시아": "자카르타",
        "일본": "도쿄",
        "조지아": "트빌리시",
        "중국": "베이징",
        "카자흐스탄": "아스타나",
        "카타르": "도하",
        "캄보디아": "프놈펜",
        "쿠웨이트": "쿠웨이트",
        "키르기스스탄": "비슈케크",
        "태국": "방콕",
        "타지키스탄": "두샨베",
        "투르크메니스탄": "아슈하바트",
        "튀르키예": "앙카라",
        "파키스탄": "이슬라마바드",
        "팔레스타인": ["알 쿠드스","예루살림","라말라"],
        "필리핀": "마닐라"
    },
    "아프리카": {
        "가나": "아크라",
        "가봉": "리브르빌",
        "감비아": "반줄",
        "기니": "코나크리",
        "기니비사우": "비사우",
        "나미비아": "빈트후크",
        "남수단": "주바",
        "남아프리카 공화국": ["프리토리아", "블룸폰테인", "케이프타운", "요하네스버그"],
        "나이지리아": "아부자",
        "니제르": "니아메",
        "라이베리아": "몬로비아",
        "레소토": "마세루",
        "르완다": "키갈리",
        "리비아": "트리폴리",
        "마다가스카르": "안타나나리보",
        "말라위": "릴롱궤",
        "말리": "바마코",
        "모로코": "라바트",
        "모리셔스": "포트루이스",
        "모리타니": "누악쇼트",
        "모잠비크": "마푸투",
        "베냉": "포르토노보",
        "보츠와나": "가보로네",
        "부룬디": "기테가",
        "부르키나파소": "와가두구",
        "상투메 프린시페": "상투메",
        "세네갈": "다카르",
        "세이셸": "빅토리아",
        "소말리아": "모가디슈",
        "수단": "하르툼",
        "시에라리온": "프리타운",
        "알제리": "알제",
        "앙골라": "루안다",
        "에리트레아": "아스마라",
        "에스와티니": ["음바바네", "로밤바"],
        "에티오피아": "아디스아바바",
        "우간다": "캄팔라",
        "이집트": "카이로",
        "잠비아": "루사카",
        "적도 기니": "말라보",
        "중앙아프리카공화국": "방기",
        "지부티": "지부티",
        "짐바브웨": "하라레",
        "차드": "은자메나",
        "카메룬": "야운데",
        "카보베르데": "프라이아",
        "케냐": "나이로비",
        "코모로": "모로니",
        "코트디부아르": "야무수크로",
        "콩고 공화국": "브라자빌",
        "콩고민주공화국": "킨샤사",
        "탄자니아": "도도마",
        "토고": "로메",
        "튀니지": "튀니스"
        
    },
    "유럽": {
        "그리스": "아테네",
        "네덜란드": "암스테르담",
        "노르웨이": "오슬로",
        "덴마크": "코펜하겐",
        "독일": "베를린",
        "라트비아": "리가",
        "러시아": "모스크바",
        "루마니아": "부쿠레슈티",
        "룩셈부르크": "룩셈부르크",
        "리투아니아": "빌뉴스",
        "리히텐슈타인": "파두츠",
        "모나코": "모나코",
        "몬테네그로": "포드고리차",
        "몰도바": "키시너우",
        "몰타": "발레타",
        "바티칸": "바티칸",
        "벨기에": "브뤼셀",
        "벨라루스": "민스크",
        "보스니아 헤르체고비나": "사라예보",
        "북마케도니아": "스코페",
        "불가리아": "소피아",
        "산마리노": "산마리노",
        "세르비아": "베오그라드",
        "슬로바키아": "브라티슬라바",
        "슬로베니아": "류블랴나",
        "스웨덴": "스톡홀름",
        "스위스": "베른",
        "스페인": "마드리드",
        "아이슬란드": "레이캬비크",
        "아일랜드": "더블린",
        "안도라": "안도라라베야",
        "알바니아": "티라나",
        "영국": "런던",
        "에스토니아": "탈린",
        "오스트리아": "빈",
        "우크라이나": "키이우",
        "이탈리아": "로마",
        "체코": "프라하",
        "크로아티아": "자그레브",
        "키프로스": "니코시아",
        "포르투갈": "리스본",
        "폴란드": "바르샤바",
        "프랑스": "파리",
        "핀란드": "헬싱키",
        "헝가리": "부다페스트"
    },
    "북아메리카": {
        "그레나다": "세인트조지스",
        "과테말라": "과테말라시티",
        "니카라과": "마나과",
        "도미니카 공화국": "산토도밍고",
        "도미니카 연방": "로조",
        "멕시코": "멕시코 시티",
        "미국": "워싱턴 D.C.",
        "바베이도스": "브리지타운",
        "바하마": "나소",
        "벨리즈": "벨모판",
        "세인트루시아": "캐스트리스",
        "세인트빈센트 그레나딘": "킹스타운",
        "세인트키츠 네비스": "바스테르",
        "아이티": "포르토프랭스",
        "앤티가 바부다": "세인트존스",
        "엘살바도르": "산살바도르",
        "온두라스": "테구시갈파",
        "자메이카": "킹스턴",
        "캐나다": "오타와",
        "코스타리카": "산호세",
        "쿠바": "아바나",
        "트리니다드 토바고": "포트오브스페인",
        "파나마": "파나마 시티"
    },
    "남아메리카": {
        "가이아나": "조지타운",
        "베네수엘라": "카라카스",
        "볼리비아": ["라파스","수크레"],
        "브라질": "브라질리아",
        "수리남": "파라마리보",
        "아르헨티나": "부에노스 아이레스",
        "에콰도르": "키토",
        "우루과이": "몬테비데오",
        "칠레": "산티아고",
        "콜롬비아": "보고타",
        "파라과이": "아순시온",
        "페루": "리마"
    },
    "오세아니아": {
        "나우루": "야렌",
        "뉴질랜드": "웰링턴",
        "마셜 제도": "마주로",
        "미크로네시아 연방": "팔리키르",
        "바누아투": "포트빌라",
        "사모아": "아피아",
        "솔로몬 제도": "호니아라",
        "키리바시": "사우스타라와",
        "통가": "누쿠알로파",
        "투발루": "푸나푸티",
        "파푸아뉴기니": "포트모르즈비",
        "팔라우": "응게룰무드",
        "피지": "수바",
        "호주": "캔버라"
    }
}

# 세션 상태 초기화
if "continent" not in st.session_state:
    st.session_state.continent = None
if "country" not in st.session_state:
    st.session_state.country = None
if "score" not in st.session_state:
    st.session_state.score = 0
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "playing" not in st.session_state:
    st.session_state.playing = False
if "answered" not in st.session_state:
    st.session_state.answered = False
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False

st.set_page_config(page_title="수도 맞추기 게임", page_icon="🌍")

st.title("🌍 수도 맞추기 게임")

# --- 대륙 선택 ---
if not st.session_state.playing:
    st.write("게임을 시작하기 전에 대륙을 선택하세요!")
    continent = st.selectbox("대륙 선택", list(continent_data.keys()))

    if st.button("게임 시작"):
        st.session_state.continent = continent
        st.session_state.country = random.choice(list(continent_data[continent].keys()))
        st.session_state.score = 0
        st.session_state.attempts = 0
        st.session_state.playing = True
        st.session_state.answered = False
        st.session_state.show_hint = False
        st.success(f"🎮 {continent} 대륙 수도 맞추기 게임 시작!")

# --- 게임 진행 ---
if st.session_state.playing:

    st.subheader(f"❓ {st.session_state.country}의 수도는 어디일까요?")

    # 힌트 버튼
    if not st.session_state.answered and st.button("💡 힌트 보기"):
        st.session_state.show_hint = True

    if st.session_state.show_hint:
        correct = continent_data[st.session_state.continent][st.session_state.country]
        st.info(f"힌트: 수도의 첫 글자는 **{correct[0]}** 입니다.")

    # 문제마다 고유한 key → 입력창 자동 초기화
    answer = st.text_input(
        "수도를 입력하세요:",
        key=f"answer_{st.session_state.attempts}_{st.session_state.country}",
        disabled=st.session_state.answered
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        submit = st.button("제출", disabled=st.session_state.answered)
    with col2:
        skip = st.button("⏭️ 건너뛰기", disabled=st.session_state.answered)
    with col3:
        stop = st.button("🛑 게임 멈추기")

    if submit:
        correct = continent_data[st.session_state.continent][st.session_state.country]
        st.session_state.attempts += 1

        if answer.strip() == correct:
            st.success("🎉 정답입니다!")
            st.session_state.score += 1
        else:
            st.error(f"❌ 틀렸습니다! 정답은 {correct} 입니다.")

        st.write(f"현재 점수: {st.session_state.score} / {st.session_state.attempts} 문제")
        st.session_state.answered = True

    # 건너뛰기: 점수/시도 변화 없이 그냥 다음 문제
    if skip:
        st.session_state.country = random.choice(list(continent_data[st.session_state.continent].keys()))
        st.session_state.answered = False
        st.session_state.show_hint = False
        st.rerun()

    # 정답 확인 후 → 다음 문제 버튼
    if st.session_state.answered:
        if st.button("➡️ 다음 문제"):
            st.session_state.country = random.choice(list(continent_data[st.session_state.continent].keys()))
            st.session_state.answered = False
            st.session_state.show_hint = False
            st.rerun()

    # 게임 멈추기 버튼
    if stop:
        st.session_state.playing = False
        accuracy = (st.session_state.score / st.session_state.attempts * 100) if st.session_state.attempts > 0 else 0
        st.warning(f"게임이 종료되었습니다. ✅ 최종 점수: {st.session_state.score} / {st.session_state.attempts} "
                   f"(정답률: {accuracy:.1f}%)")

# --- 멈춘 상태에서 다시 시작 ---
if not st.session_state.playing and st.session_state.attempts > 0:
    if st.button("다시 시작하기"):
        st.session_state.continent = None
        st.session_state.country = None
        st.session_state.score = 0
        st.session_state.attempts = 0
        st.session_state.playing = False
        st.session_state.answered = False
        st.session_state.show_hint = False
        st.success("새 게임을 시작하세요! 먼저 대륙을 선택하세요.")
