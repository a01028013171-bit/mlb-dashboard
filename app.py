import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(
    page_title="MLB Kids 토들러 사이즈 분석",
    page_icon="👕",
    layout="wide"
)

# 타이틀
st.title("👕 MLB Kids 토들러 사이즈 핏 분석 대시보드")
st.markdown("**하의 사이즈 105~120 체감 조사 결과 (총 60명 응답)**")
st.divider()

# 데이터 준비
overview_data = pd.DataFrame({
    'size': ['105', '110', '120'],
    '크다': [46, 29, 15],
    '적당하다': [13, 31, 44],
    '작다': [1, 0, 1]
})

size_105 = pd.DataFrame({'응답': ['크다', '적당하다', '작다'], '인원': [46, 13, 1]})
size_110 = pd.DataFrame({'응답': ['크다', '적당하다'], '인원': [29, 31]})
size_120 = pd.DataFrame({'응답': ['크다', '적당하다', '작다'], '인원': [15, 44, 1]})

# 탭 생성
tab1, tab2, tab3, tab4 = st.tabs(["📊 전체 개요", "📈 사이즈별 상세", "💡 개선 제안", "💬 상세 피드백"])

# ========== 탭 1: 전체 개요 ==========
with tab1:
    st.header("핵심 인사이트")
    
    # 3개의 컬럼으로 인사이트 카드 표시
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("105 사이즈", "77%", "크다고 응답", delta_color="inverse")
        with st.expander("상세 이슈"):
            st.markdown("""
            - 바지 기장이 너무 길다 (2-3cm 조정 필요)
            - 허리둘레가 크다
            - 밑위가 길다
            - 100 사이즈 기준 필요
            """)
    
    with col2:
        st.metric("110 사이즈", "48%", "크다고 응답", delta_color="normal")
        with st.expander("상세 이슈"):
            st.markdown("""
            - 바지 기장 조정 필요 (1-2cm)
            - 전반적으로 가장 적절한 핏
            - 일부 품번 밑위 길이 이슈
            """)
    
    with col3:
        st.metric("120 사이즈", "25%", "크다고 응답", delta_color="off")
        with st.expander("상세 이슈"):
            st.markdown("""
            - 대체로 적절한 사이즈
            - 일부 바지 기장 조정 필요
            - 상의 대비 하의 기장 긴 편
            """)
    
    st.divider()
    
    # 전체 응답 분포 차트
    st.subheader("📊 사이즈별 응답 분포")
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='크다', x=overview_data['size'], y=overview_data['크다'], 
                         marker_color='#ef4444'))
    fig.add_trace(go.Bar(name='적당하다', x=overview_data['size'], y=overview_data['적당하다'], 
                         marker_color='#10b981'))
    fig.add_trace(go.Bar(name='작다', x=overview_data['size'], y=overview_data['작다'], 
                         marker_color='#3b82f6'))
    
    fig.update_layout(
        barmode='group',
        height=400,
        xaxis_title="사이즈",
        yaxis_title="응답 수 (명)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # 주요 발견사항
    st.subheader("🔍 주요 발견사항")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 사이즈 체감 트렌드")
        st.info("""
        작은 사이즈일수록 크다는 응답이 압도적으로 많습니다. 105 사이즈는 77%가 크다고 응답했으며, 
        120 사이즈는 73%가 적당하다고 응답했습니다. 이는 작은 사이즈의 패턴 조정이 시급함을 나타냅니다.
        """)
    
    with col2:
        st.markdown("#### 공통 이슈")
        st.warning("""
        모든 사이즈에서 바지 기장이 길다는 의견이 가장 많았습니다. 특히 105 사이즈의 경우 
        허리둘레와 밑위 길이도 함께 문제로 지적되었습니다. 경쟁 브랜드 대비 전반적으로 여유 있는 핏입니다.
        """)

# ========== 탭 2: 사이즈별 상세 ==========
with tab2:
    st.header("사이즈별 상세 분석")
    
    size_tab1, size_tab2, size_tab3 = st.tabs(["105 사이즈", "110 사이즈", "120 사이즈"])
    
    # 105 사이즈
    with size_tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            fig_105 = px.pie(size_105, values='인원', names='응답', 
                            color='응답',
                            color_discrete_map={'크다':'#ef4444', '적당하다':'#10b981', '작다':'#3b82f6'},
                            title='105 사이즈 응답 분포')
            fig_105.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_105, use_container_width=True)
        
        with col2:
            st.markdown("### 📊 응답 통계")
            st.dataframe(size_105.assign(비율=lambda x: (x['인원']/60*100).round(1).astype(str)+'%'), 
                        hide_index=True, use_container_width=True)
            st.error("**77%가 크다고 응답** - 긴급 조치 필요")
    
    # 110 사이즈
    with size_tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            fig_110 = px.pie(size_110, values='인원', names='응답',
                            color='응답',
                            color_discrete_map={'크다':'#ef4444', '적당하다':'#10b981'},
                            title='110 사이즈 응답 분포')
            fig_110.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_110, use_container_width=True)
        
        with col2:
            st.markdown("### 📊 응답 통계")
            st.dataframe(size_110.assign(비율=lambda x: (x['인원']/60*100).round(1).astype(str)+'%'), 
                        hide_index=True, use_container_width=True)
            st.warning("**48%가 크다고 응답** - 부분 수정 필요")
    
    # 120 사이즈
    with size_tab3:
        col1, col2 = st.columns(2)
        
        with col1:
            fig_120 = px.pie(size_120, values='인원', names='응답',
                            color='응답',
                            color_discrete_map={'크다':'#ef4444', '적당하다':'#10b981', '작다':'#3b82f6'},
                            title='120 사이즈 응답 분포')
            fig_120.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_120, use_container_width=True)
        
        with col2:
            st.markdown("### 📊 응답 통계")
            st.dataframe(size_120.assign(비율=lambda x: (x['인원']/60*100).round(1).astype(str)+'%'), 
                        hide_index=True, use_container_width=True)
            st.success("**73%가 적당하다고 응답** - 현행 유지")

# ========== 탭 3: 개선 제안 ==========
with tab3:
    st.header("💡 개선 제안")
    
    # HIGH 우선순위
    st.markdown("### 🔴 HIGH - 105 사이즈")
    with st.container():
        st.markdown("#### 사이즈 체계 개선")
        st.markdown("""
        **구체적 실행 방안:**
        1. 105 사이즈를 100 사이즈로 변경 검토
        2. 바지 총기장 2-3cm 단축
        3. 허리둘레 1-2cm 조정
        4. 밑위 길이 1-2cm 단축
        5. 참고 브랜드: 캉골 100 사이즈
        """)
    
    st.divider()
    
    # MEDIUM 우선순위
    st.markdown("### 🟡 MEDIUM - 110 사이즈")
    with st.container():
        st.markdown("#### 부분 수정")
        st.markdown("""
        **구체적 실행 방안:**
        1. 바지 총기장 1-2cm 단축
        2. 특정 품번(7FS2H0356 등) 밑위 조정
        3. 현재 가장 밸런스가 좋은 사이즈
        """)
    
    st.divider()
    
    # LOW 우선순위
    st.markdown("### 🟢 LOW - 120 사이즈")
    with st.container():
        st.markdown("#### 미세 조정")
        st.markdown("""
        **구체적 실행 방안:**
        1. 바지 기장 1cm 정도 단축 고려
        2. 전반적으로 적절한 핏 유지
        3. 상의 대비 하의 비율 체크
        """)
    
    st.divider()
    
    # STRATEGIC 우선순위
    st.markdown("### 🟣 STRATEGIC - 전체")
    with st.container():
        st.markdown("#### 사이즈 라인업 재구성")
        st.markdown("""
        **구체적 실행 방안:**
        1. 100/110/120 사이즈 체계로 개편 검토
        2. 유아복 브랜드(캉골, 블루독, 노스키즈, 뉴발) 벤치마킹
        3. 105 사이즈 대신 100 사이즈 도입
        4. 하의 기장 전반적으로 짧게 조정
        """)

# ========== 탭 4: 상세 피드백 ==========
with tab4:
    st.header("💬 상세 피드백")
    
    feedback_105 = [
        "기장이 너무 길어요 (2cm 조정)",
        "밑위가 너무 길어요",
        "총기장 2cm 줄임, 통도 큽니다",
        "캉골 100 사이즈 기준으로 핏과 기장 원함",
        "바지 허리가 105 기준에서 너무 커요",
        "100 사이즈에 맞춰주세요. 105는 애매합니다",
        "전체 길이 3cm 정도 줄어들어야 함",
        "총장 2cm 줄어들면 좋겠어요"
    ]
    
    feedback_110 = [
        "바지기장이 길어요",
        "바지기장이 길다고 이야기 하십니다",
        "밑위가 길어요",
        "기장 1-2cm 줄이면 좋을 것 같아요",
        "바지기장을 1cm 정도 줄이면 좋겠습니다",
        "대부분 적당하다는 의견"
    ]
    
    feedback_120 = [
        "상의에 비해 바지 기장이 조금 길어요",
        "바지기장 1cm 정도 조정",
        "대체로 적절한 사이즈",
        "가장 만족도 높은 사이즈"
    ]
    
    # 105 사이즈 피드백
    st.subheader("🔴 105 사이즈 상세 피드백")
    col1, col2 = st.columns(2)
    for i, feedback in enumerate(feedback_105):
        if i % 2 == 0:
            with col1:
                st.info(f"**{i+1}.** {feedback}")
        else:
            with col2:
                st.info(f"**{i+1}.** {feedback}")
    
    st.divider()
    
    # 110 사이즈 피드백
    st.subheader("🟡 110 사이즈 상세 피드백")
    col1, col2 = st.columns(2)
    for i, feedback in enumerate(feedback_110):
        if i % 2 == 0:
            with col1:
                st.info(f"**{i+1}.** {feedback}")
        else:
            with col2:
                st.info(f"**{i+1}.** {feedback}")
    
    st.divider()
    
    # 120 사이즈 피드백
    st.subheader("🟢 120 사이즈 상세 피드백")
    col1, col2 = st.columns(2)
    for i, feedback in enumerate(feedback_120):
        if i % 2 == 0:
            with col1:
                st.success(f"**{i+1}.** {feedback}")
        else:
            with col2:
                st.success(f"**{i+1}.** {feedback}")
    
    st.divider()
    
    # 벤치마킹 브랜드
    st.subheader("🎯 벤치마킹 권장 브랜드")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("### 캉골\n**(100 사이즈)**")
    with col2:
        st.markdown("### 블루독")
    with col3:
        st.markdown("### 노스키즈")
    with col4:
        st.markdown("### 뉴발")

# 하단 요약
st.divider()
st.header("📋 디자인팀 액션 아이템 요약")

col1, col2, col3 = st.columns(3)

with col1:
    st.error("**긴급 (105)**")
    st.markdown("바지 기장 2-3cm 단축, 허리둘레 조정, 105→100 사이즈 전환 검토")

with col2:
    st.warning("**중요 (110)**")
    st.markdown("바지 기장 1-2cm 단축, 특정 품번 밑위 조정")

with col3:
    st.success("**모니터링 (120)**")
    st.markdown("현행 유지, 일부 바지 기장 1cm 조정 고려")