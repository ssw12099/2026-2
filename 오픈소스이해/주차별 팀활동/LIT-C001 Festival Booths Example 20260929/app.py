import base64
import json

import streamlit as st
from pathlib import Path
import random

try:
    import pandas as pd
except ImportError as error:
    st.error(
        "pandas를 불러오지 못했습니다. "
        "Windows의 DLL 차단 여부를 확인해 주세요."
    )
    st.code(str(error), language="text")
    st.stop()
st.set_page_config(page_title="축제 부스 길잡이", page_icon="🎪", layout="wide")

# =========================
# 변경사항 2. 학교 로고 및 상단 화면
# =========================
logo_path = Path(__file__).resolve().parent / "hallym_logo.jpg"

title_col, logo_col = st.columns([5, 1])

with title_col:
    st.title("축제 부스 길잡이")
    st.caption("관심 있는 부스를 찾고, 나만의 축제 코스를 만들어 보세요.")

with logo_col:
    try:
        logo_bytes = logo_path.read_bytes()
    except OSError:
        st.caption("학교 로고를 불러올 수 없습니다.")
    else:
        st.image(logo_bytes, width=180)

st.divider()

# 1. 검색·필터 및 대기시간 표시 - 김찬빈

# =========================
# Data Loading
def load_data():
    try:
        df = pd.read_csv(Path(__file__).resolve().parent / "booths.csv", encoding="utf-8-sig")
        # is_open 컬럼이 없을 경우 기본값 True 설정
        if "is_open" not in df.columns:
            df["is_open"] = True
        # wait_time 컬럼이 없거나 모든 대기시간 값이 0인 경우 예시 대기시간 자동 생성
        if "wait_time" not in df.columns or df["wait_time"].sum() == 0:
            random.seed(42)  # 새로고침해도 값이 변하지 않도록 고정
            wait_times = [5, 10, 15, 25, 30, 40, 50]
            df["wait_time"] = [random.choice(wait_times) for _ in range(len(df))]
        return df
    except FileNotFoundError:
        st.error("booths.csv 파일을 찾을 수 없습니다.")
        st.stop()
    except pd.errors.EmptyDataError:
        st.error("booths.csv가 비어 있습니다.")
        st.stop()
    except pd.errors.ParserError:
        st.error("CSV 형식이 올바르지 않습니다. 구분자와 따옴표를 확인해 주세요.")
        st.stop()
    except UnicodeDecodeError:
        st.error("booths.csv를 UTF-8 형식으로 저장해 주세요.")
        st.stop()
    except OSError:
        st.error("CSV 파일을 읽을 수 없습니다. 접근 권한을 확인해 주세요.")
        st.stop()

df = load_data()
filtered_df = df.copy()
# 대기시간 상태 뱃지 및 문구 반환 함수
def get_wait_time_info(wait_time, is_open):
    if not is_open:
        return "🔴 운영 종료"
    elif wait_time <= 10:
        return f"🟢 바로 입장 가능 ({wait_time}분)"
    elif wait_time <= 30:
        return f"🟡 보통 대기 ({wait_time}분)"
    else:
        return f"🔴 혼잡/대기 길음 ({wait_time}분)"
if not df.empty:
    # Sidebar Filters
    st.sidebar.header("🔍 검색 및 필터")
    # 1. 키워드 검색
    search_term = st.sidebar.text_input("부스 이름/설명 검색", "")
    # 변경사항 1: 우천 시 실내 부스만 검색
    indoor_only = st.sidebar.checkbox(
        "실내 부스만 보기",
        value=False,
        key="search_indoor_only",
    )
    # 2. 카테고리 필터 (category 컬럼 체크)
    if "category" in df.columns:
        categories = ["전체"] + list(df["category"].dropna().unique())
        selected_category = st.sidebar.selectbox("카테고리 선택", categories)
    else:
        selected_category = "전체"
    # 3. 운영 상태 필터 (is_open 컬럼 체크)
    has_is_open = "is_open" in df.columns
    if has_is_open:
        status_option = st.sidebar.radio("운영 상태", ["전체", "운영 중만 보기", "마감 포함 전체"])
    # 3. 최대 대기시간 필터 (슬라이더)
    max_wait_filter = st.sidebar.slider(
        "⏱️ 최대 대기시간 필터 (분)",
        min_value=0,
        max_value=60,
        value=60,
        step=5,
        help="선택한 시간 이하로 대기하는 부스만 표시합니다."
    )
    # Filtering Logic
    filtered_df = df.copy()
    # 검색어 필터링
    if search_term:
        name_match = filtered_df["name"].astype(str).str.contains(search_term, case=False, na=False, regex=False) if "name" in filtered_df.columns else True
        desc_match = filtered_df["description"].astype(str).str.contains(search_term, case=False, na=False, regex=False) if "description" in filtered_df.columns else False
        filtered_df = filtered_df[name_match | desc_match]
    if selected_category != "전체" and "category" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["category"] == selected_category]
    if has_is_open and status_option == "운영 중만 보기":
        filtered_df = filtered_df[filtered_df["is_open"] == True]
    # 대기시간 조건 필터링 (운영 종료 부스도 함께 표시하려면 is_open 조건 추가)
    if "wait_time" in filtered_df.columns:
        filtered_df = filtered_df[
            (filtered_df["wait_time"] <= max_wait_filter) | (filtered_df["is_open"] == False)
        ]
    # 변경사항 1: 검색 결과에서 야외 부스 제외
    if indoor_only:
        filtered_df = filtered_df[
            filtered_df["indoor"] == True
        ].copy()
    # Result Metrics
    st.metric(label="검색된 부스 수", value=f"{len(filtered_df)}개")
    # Display Results
    if not filtered_df.empty:
        for _, row in filtered_df.iterrows():
            category_text = f"[{row['category']}] " if "category" in row and pd.notna(row["category"]) else ""
            is_open = row.get("is_open", True)
            wait_time = int(row.get("wait_time", 0))
            # 대기시간 정보 및 뱃지 가져오기
            wait_badge = get_wait_time_info(wait_time, is_open)
            booth_name = row.get("name", "이름 없음")
            with st.expander(f"{category_text}{booth_name} | {wait_badge}"):
                col1, col2 = st.columns([2, 1])
                with col1:
                    if "location" in row:
                        st.write(f"📍 **위치:** {row['location']}")
                    if "description" in row:
                        st.write(f"📝 **설명:** {row['description']}")
                with col2:
                    if is_open:
                        st.metric(label="⏱️ 예상 대기시간", value=f"{wait_time}분")
                    else:
                        st.caption("현재 운영이 종료된 부스입니다.")
    else:
        st.info("조건에 일치하는 부스가 없습니다.")

# =========================
# 2. 랜덤 추천 - 박현진

# =========================
booths = df
st.header("🎲 랜덤 부스 추천")
st.write("조건을 고르고 버튼을 누르면 조건에 맞는 부스 한 곳을 추천해 드려요.")
categories = sorted(booths["category"].unique())
selected_categories = st.multiselect(
    "관심 있는 카테고리 (비워 두면 전체)",
    categories,
)
place_type = st.radio(
    "실내/실외",
    ["상관없음", "실내", "실외"],
    horizontal=True,
)
# 변경사항 3: 검색 조건과 관계없이 운영 중단 부스는 추천 제외
candidates = filtered_df[
    filtered_df["is_open"] == True
].copy()
if selected_categories:
    candidates = candidates[candidates["category"].isin(selected_categories)]
if place_type == "실내":
    candidates = candidates[candidates["indoor"]]
elif place_type == "실외":
    candidates = candidates[~candidates["indoor"]]
recommend_signature = (
    tuple(candidates["id"].astype(str)),
    tuple(selected_categories),
    place_type,
)
if st.session_state.get("recommend_signature") != recommend_signature:
    st.session_state.pop("recommended", None)
    st.session_state["recommend_signature"] = recommend_signature
st.caption(f"조건에 맞는 부스: {len(candidates)}곳")
if st.button("랜덤으로 추천받기", type="primary"):
    if candidates.empty:
        st.session_state.pop("recommended", None)
        st.warning("조건에 맞는 부스가 없어요. 조건을 바꿔서 다시 시도해 보세요.")
    else:
        st.session_state["recommended"] = candidates.sample(1).iloc[0].to_dict()
recommended = st.session_state.get("recommended")
if recommended:
    st.subheader(f"✨ {recommended['name']}")
    st.write(recommended["description"])
    left, right = st.columns(2)
    left.metric("카테고리", recommended["category"])
    right.metric("장소", "실내" if recommended["indoor"] else "실외")
    st.write(f"📍 위치: {recommended['location']}")

# =========================
# 3. 방문 코스  - 소선웅

# =========================
st.subheader("🗺️ 방문 코스")
# 검색 기능과 연결할 때 df를 실제 검색 결과 변수로 변경합니다.
# 변경사항 3: 운영 중인 부스만 새 방문 코스에 추가 가능
course_source_df = filtered_df[
    filtered_df["is_open"] == True
].copy()
course_columns = [
    "id", "name", "category", "location", "indoor", "description"
]
# 5번 기능에 전달할 결과: 선택이 없거나 오류가 있으면 빈 DataFrame
course_df = pd.DataFrame(columns=course_columns)
course_ready = True
# 필요한 컬럼과 자료형 확인
if not isinstance(course_source_df, pd.DataFrame):
    st.error("방문 코스에 연결된 데이터가 DataFrame이 아닙니다.")
    course_ready = False
elif not course_source_df.columns.is_unique:
    st.error("중복된 컬럼명이 있습니다. 연결된 데이터를 확인해 주세요.")
    course_ready = False
else:
    course_missing_columns = [
        column
        for column in course_columns
        if column not in course_source_df.columns
    ]
    if course_missing_columns:
        st.error(
            "필요한 컬럼이 없습니다: "
            + ", ".join(course_missing_columns)
        )
        course_ready = False
# 팀원의 원본 DataFrame을 변경하지 않도록 복사
if course_ready:
    course_source_df = course_source_df[course_columns].copy()
    course_source_df["id"] = (
        course_source_df["id"].astype("string").str.strip()
    )
    course_bad_ids = (
        course_source_df["id"].isna()
        | course_source_df["id"].eq("")
    )
    course_bad_names = (
        course_source_df["name"]
        .fillna("")
        .astype(str)
        .str.strip()
        .eq("")
    )
    if course_bad_ids.any():
        st.error("ID가 없는 부스가 있습니다.")
        course_ready = False
    elif course_source_df["id"].duplicated().any():
        st.error("부스 ID가 중복되어 있습니다.")
        course_ready = False
    elif course_bad_names.any():
        st.error("이름이 없는 부스가 있습니다.")
        course_ready = False
# 방문할 부스 선택 및 코스 관리
if course_ready:
    # 검색 결과: 지금 추가할 수 있는 부스
    course_options = course_source_df["id"].tolist()
    course_name_by_id = (
        course_source_df.set_index("id")["name"].to_dict()
    )
    # 전체 원본: 이미 담은 코스의 정보를 찾는 데 사용
    course_catalog_df = df[course_columns].copy()
    course_catalog_df["id"] = (
        course_catalog_df["id"].astype("string").str.strip()
    )
    if (
        course_catalog_df["id"].isna().any()
        or course_catalog_df["id"].eq("").fillna(True).any()
        or course_catalog_df["id"].duplicated().any()
    ):
        st.error("전체 부스 데이터의 ID가 비어 있거나 중복되어 있습니다.")
        st.stop()
    course_catalog_by_id = course_catalog_df.set_index("id")
    if "course_visit_ids" not in st.session_state:
        st.session_state["course_visit_ids"] = []
    # 원본에서 삭제된 부스가 있다면 코스에서도 정리
    course_catalog_ids = set(course_catalog_by_id.index)
    st.session_state["course_visit_ids"] = [
        booth_id
        for booth_id in st.session_state["course_visit_ids"]
        if booth_id in course_catalog_ids
    ]
    def course_add_selected():
        booth_id = st.session_state.get("course_pick_id")

        # 선택창을 초기화해 같은 부스를 다시 선택할 수 있게 함
        st.session_state["course_pick_id"] = None

        if booth_id is None:
            return

        # 추가하는 순간 CSV를 다시 읽어 현재 운영 상태 확인
        latest_booths = load_data()

        latest_ids = (
            latest_booths["id"].astype("string").str.strip()
        )

        selected_booth = latest_booths[
            latest_ids == booth_id
        ]

        if selected_booth.empty:
            st.warning("해당 부스가 없어 방문 코스에 추가하지 않았습니다.")
            return

        if not selected_booth["is_open"].eq(True).all():
            st.warning("운영이 중단된 부스는 방문 코스에 추가할 수 없습니다.")
            return

        st.session_state["course_visit_ids"].append(booth_id)

    def course_remove_visit(position):
        # 같은 부스가 여러 번 있어도 해당 순서의 방문만 삭제
        st.session_state["course_visit_ids"].pop(position)
    def course_clear_visits():
        st.session_state["course_visit_ids"].clear()
    # 검색 조건이 바뀌어 선택 대상에서 빠진 부스는 입력창에서 해제
    if (
        "course_pick_id" in st.session_state
        and st.session_state["course_pick_id"] not in course_options
    ):
        st.session_state["course_pick_id"] = None
    if course_options:
        st.selectbox(
            "다음에 방문할 부스를 선택하세요.",
            options=course_options,
            index=None,
            placeholder="부스를 선택하세요",
            format_func=lambda booth_id: (
                f"{course_name_by_id[booth_id]} ({booth_id})"
            ),
            key="course_pick_id",
            on_change=course_add_selected,
        )
    else:
        st.info("현재 조건에서 추가할 수 있는 부스가 없습니다.")
    visit_ids = st.session_state["course_visit_ids"]
    if visit_ids:
        st.button(
            "코스 전체 초기화",
            key="course_clear_all",
            on_click=course_clear_visits,
        )
    # 5번 CSV 다운로드 기능에 전달할 DataFrame
    # 같은 부스를 여러 번 방문하면 해당 행도 여러 번 들어감
    if visit_ids:
        course_df = (
            course_catalog_by_id.loc[visit_ids]
            .reset_index()
            [course_columns]
            .copy()
        )
    else:
        course_df = pd.DataFrame(columns=course_columns)
    st.write(f"코스에 담긴 방문: {len(course_df)}회")
    if course_df.empty:
        st.info("부스를 선택하면 방문 순서가 여기에 표시됩니다.")
    else:
        course_indoor_labels = (
            course_df["indoor"]
            .astype("string")
            .str.strip()
            .str.lower()
            .map({"true": "실내", "false": "야외"})
            .fillna("정보 없음")
        )
        if course_indoor_labels.eq("정보 없음").any():
            st.warning(
                "실내 여부가 잘못된 부스는 '정보 없음'으로 표시합니다."
            )
        # Streamlit의 데이터 표 안에는 개별 삭제 버튼을 넣기 어려워
        # 각 방문을 한 줄씩 표시합니다.
        header = st.columns([1, 2, 2, 1, 1])
        header[0].write("**순서**")
        header[1].write("**부스 이름**")
        header[2].write("**위치**")
        header[3].write("**실내 여부**")
        header[4].write("**삭제**")
        for position, (_, booth) in enumerate(course_df.iterrows()):
            row = st.columns([1, 2, 2, 1, 1])
            location = booth["location"]
            if pd.isna(location) or not str(location).strip():
                location = "위치 정보 없음"
            row[0].write(position + 1)
            row[1].write(booth["name"])
            row[2].write(location)
            row[3].write(course_indoor_labels.iloc[position])
            row[4].button(
                "삭제",
                key=f"course_delete_{position}",
                on_click=course_remove_visit,
                args=(position,),
            )

# =========================
# 4. 스탬프 미션 - 이준

# =========================
VISITS_FILE = Path(__file__).resolve().parent / "visits.csv"
# 전체 부스 이름과 3번에서 만든 방문 코스 사용
booth_names = dict(zip(df["id"].astype(str).str.strip(), df["name"]))
# 같은 부스를 여러 번 담아도 스탬프는 부스당 한 개
selected_ids = course_df["id"].drop_duplicates().tolist()
st.subheader("✅ 스탬프 미션")
visitor = st.text_input(
    "방문자 이름 또는 ID",
    key="stamp_visitor",
).strip()
if not visitor:
    st.info("스탬프 미션은 방문자 이름 또는 ID를 입력하면 사용할 수 있습니다.")
else:
    stamp_ready = True
    stamp_columns = ["visitor", "booth_id", "visited"]
    try:
        if VISITS_FILE.exists() and VISITS_FILE.stat().st_size > 0:
            visits = pd.read_csv(
                VISITS_FILE,
                encoding="utf-8-sig",
                dtype={
                    "visitor": str,
                    "booth_id": str,
                    "visited": str,
                },
                keep_default_na=False,
            )
        else:
            visits = pd.DataFrame(columns=stamp_columns)
    except (OSError, UnicodeError, pd.errors.ParserError, pd.errors.EmptyDataError):
        st.error("방문 기록을 읽지 못했습니다. visits.csv를 확인해 주세요.")
        stamp_ready = False
    if stamp_ready:
        if not set(stamp_columns).issubset(visits.columns):
            st.error("visits.csv에 필요한 컬럼이 없습니다.")
            stamp_ready = False
    if stamp_ready:
        my_visits = visits[visits["visitor"] == visitor]
        saved_status = {
            str(row.booth_id).strip():
                str(row.visited).strip().lower() in ("1", "true")
            for row in my_visits.itertuples(index=False)
        }
        if not selected_ids:
            st.info("위의 방문 코스에서 부스를 먼저 추가해 주세요.")
        else:
            completed_ids = []
            for booth_id in selected_ids:
                # 방문자와 부스를 함께 사용해 체크박스 구분
                checkbox_key = f"stamp_completed_{(visitor, booth_id)!r}"
                if checkbox_key not in st.session_state:
                    st.session_state[checkbox_key] = saved_status.get(
                        booth_id, False
                    )
                if st.checkbox(
                    f"{booth_names[booth_id]} 방문 완료",
                    key=checkbox_key,
                ):
                    completed_ids.append(booth_id)
            st.metric(
                "현재 코스에서 방문 완료한 부스",
                f"{len(completed_ids)}개",
            )
            if st.button("스탬프 현황 저장", key="stamp_save"):
                # 코스에서 빠진 부스의 기존 완료 기록은 보존
                updated_status = saved_status.copy()
                updated_status.update({
                    booth_id: booth_id in completed_ids
                    for booth_id in selected_ids
                })
                other_visits = visits[visits["visitor"] != visitor]
                new_visits = pd.DataFrame(
                    [
                        {
                            "visitor": visitor,
                            "booth_id": booth_id,
                            "visited": int(completed),
                        }
                        for booth_id, completed in updated_status.items()
                    ],
                    columns=stamp_columns,
                )
                updated = pd.concat(
                    [other_visits, new_visits],
                    ignore_index=True,
                )
                try:
                    updated.to_csv(
                        VISITS_FILE,
                        index=False,
                        encoding="utf-8-sig",
                    )
                except (OSError, UnicodeError):
                    st.error("방문 기록을 저장하지 못했습니다.")
                else:
                    st.success("스탬프 현황을 저장했습니다.")
# 5. CSV 다운로드

# =========================
st.subheader("📥 방문 코스 CSV 다운로드")
# 5번 브랜치만 실행하면 아직 course_df가 없을 수 있습니다.
if "course_df" not in globals():
    st.info(
        "방문 코스 기능 연결이 필요합니다. "
        "3번 기능에서 만든 course_df를 연결하면 다운로드할 수 있습니다."
    )
elif not isinstance(course_df, pd.DataFrame):
    st.error("방문 코스 데이터가 DataFrame이 아닙니다.")
elif course_df.empty:
    st.info("방문할 부스를 먼저 선택해 주세요.")
else:
    course_export_columns = [
        "id", "name", "category", "location", "indoor", "description"
    ]
    course_export_missing = [
        column
        for column in course_export_columns
        if column not in course_df.columns
    ]
    if not course_df.columns.is_unique:
        st.error("방문 코스에 중복된 컬럼명이 있습니다.")
    elif course_export_missing:
        st.error(
            "CSV 저장에 필요한 컬럼이 없습니다: "
            + ", ".join(course_export_missing)
        )
    else:
        # 다른 기능이 추가한 컬럼은 제외하고 부스 정보만 저장
        course_export_df = course_df[course_export_columns].copy()
        # Excel에서 수식으로 해석될 수 있는 문자열 확인
        course_csv_risky = False
        for course_column in course_export_columns:
            for course_value in course_export_df[course_column]:
                if isinstance(course_value, str):
                    if (
                        course_value.startswith(("\t", "\r", "\n"))
                        or course_value.lstrip().startswith(
                            ("=", "+", "-", "@", "＝", "＋", "－", "＠")
                        )
                    ):
                        course_csv_risky = True
                        break
            if course_csv_risky:
                break
        if course_csv_risky:
            st.error(
                "Excel 수식으로 해석될 수 있는 문자열이 있습니다. "
                "부스 데이터를 확인한 뒤 다운로드해 주세요."
            )
        else:
            try:
                course_csv = course_export_df.to_csv(
                    index=False
                ).encode("utf-8-sig")
            except (TypeError, ValueError, UnicodeError):
                st.error(
                    "CSV 변환에 실패했습니다. 부스 데이터를 확인해 주세요."
                )
            else:
                st.download_button(
                    label="방문 코스 CSV 다운로드",
                    data=course_csv,
                    file_name="festival_course.csv",
                    mime="text/csv",
                    key="course_csv_download",
                )


# =========================
# 7. 방문 코스 공유 - 박현진
# =========================


st.header("📤 CSV 파일 공유")
st.caption("CSV 파일을 올리고 공유 버튼을 누르면 카카오톡, 메시지, DM 등 기기의 공유 창이 열려요.")

uploaded = st.file_uploader("공유할 CSV 파일을 업로드하세요", type="csv")

if uploaded is not None:
    # 파일 내용은 base64로, 파일 이름은 </script> 등이 끼어들지 못하게 '<'를 이스케이프해 넘긴다.
    file_b64 = base64.b64encode(uploaded.getvalue()).decode("ascii")
    file_name = json.dumps(uploaded.name).replace("<", "\\u003c")

    # 컴포넌트 iframe에는 web-share 권한이 없어서, 같은 출처인 상위 창의 navigator.share를 사용한다.
    # 공유 창을 지원하지 않는 브라우저에서는 파일을 내려받는다.
    st.iframe(
        f"""
        <button id="share">📤 CSV 공유하기</button>
        <span id="msg"></span>
        <style>
          #share {{
            padding: 0.5rem 1rem; font-size: 1rem; cursor: pointer;
            border: 1px solid #ccc; border-radius: 0.5rem; background: #fff;
          }}
          #msg {{ margin-left: 0.5rem; font-family: sans-serif; color: #666; }}
        </style>
        <script>
          const name = {file_name};
          const bytes = Uint8Array.from(atob("{file_b64}"), (c) => c.charCodeAt(0));
          const msg = document.getElementById("msg");

          function download(blob) {{
            const a = document.createElement("a");
            a.href = URL.createObjectURL(blob);
            a.download = name;
            a.click();
            msg.textContent = "공유 창을 지원하지 않는 브라우저라 파일로 내려받았어요.";
          }}

          document.getElementById("share").onclick = async () => {{
            const win = window.parent;
            const blob = new Blob([bytes], {{ type: "text/csv" }});
            const file = new win.File([blob], name, {{ type: "text/csv" }});
            const data = {{ files: [file], title: name }};

            if (!win.navigator.canShare || !win.navigator.canShare(data)) {{
              download(blob);
              return;
            }}
            try {{
              await win.navigator.share(data);
              msg.textContent = "";
            }} catch (e) {{
              if (e.name !== "AbortError") download(blob);
            }}
          }};
        </script>
        """,
        height=60,
    )
import csv
from datetime import datetime
from pathlib import Path

import streamlit as st

REVIEWS_FILE = Path(__file__).resolve().parent / "reviews.csv"
COLUMNS = ["booth_id", "nickname", "rating", "content", "created_at"]


# =========================
# 6. 부스 별점 및 후기 - 이준
# =========================


def show_reviews(booths):
    st.subheader("⭐ 부스 후기·별점")

    booth_by_id = {row["id"]: row for row in booths.to_dict("records")}
    if not booth_by_id:
        st.info("등록된 부스가 없습니다.")
        return

    selected_id = st.selectbox(
        "후기를 확인하거나 작성할 부스",
        options=list(booth_by_id),
        format_func=lambda booth_id: booth_by_id[booth_id]["name"],
        key="review_booth"
    )
    booth = booth_by_id[selected_id]
    st.write(f"📍 {booth['location']} · {booth['category']}")
    st.write(booth["description"])

    if REVIEWS_FILE.exists() and REVIEWS_FILE.stat().st_size > 0:
        with REVIEWS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
            reviews = list(csv.DictReader(file))
    else:
        reviews = []

    with st.form("review_form", clear_on_submit=True):
        nickname = st.text_input("닉네임", max_chars=30)
        rating = st.slider("별점", min_value=1, max_value=5, value=5)
        content = st.text_area("후기", max_chars=300)
        submitted = st.form_submit_button("후기 저장")

    if submitted:
        if not nickname.strip() or not content.strip():
            st.warning("닉네임과 후기를 모두 입력하세요.")
        else:
            new_review = {
                "booth_id": selected_id,
                "nickname": nickname.strip(),
                "rating": str(rating),
                "content": content.strip(),
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            new_file = not REVIEWS_FILE.exists() or REVIEWS_FILE.stat().st_size == 0
            encoding = "utf-8-sig" if new_file else "utf-8"
            with REVIEWS_FILE.open("a", encoding=encoding, newline="") as file:
                writer = csv.DictWriter(file, fieldnames=COLUMNS)
                if new_file:
                    writer.writeheader()
                writer.writerow(new_review)
            reviews.append(new_review)
            st.success("후기가 저장되었습니다.")

    booth_reviews = [
        review for review in reviews if review["booth_id"] == selected_id
    ]
    st.write(f"**후기 {len(booth_reviews)}개**")

    if not booth_reviews:
        st.info("아직 작성된 후기가 없습니다.")
        return

    average = sum(int(review["rating"]) for review in booth_reviews) / len(booth_reviews)
    st.metric("평균 별점", f"{average:.1f} / 5")

    for review in reversed(booth_reviews):
        st.write(f"**{review['nickname']}** · {'⭐' * int(review['rating'])}")
        st.write(review["content"])
        st.caption(review["created_at"])
        st.divider()

    # 후기 화면 표시
st.divider()
show_reviews(df)
