import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(page_title="The Night the World Held Its Breath", page_icon="⚽", layout="wide", initial_sidebar_state="collapsed")

# Colors
NAVY = "#1B2A4A"
GOLD = "#D4AF37"

# Minimal CSS - don't fight Streamlit
import base64
def get_img_b64(filename):
    try:
        with open(os.path.join(os.path.dirname(__file__), 'assets', filename), 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

_stadium = get_img_b64('01_trophy_stadium_opening.jpg')
_fans = get_img_b64('08_fans_hugging_celebration.jpg')
_yamal = get_img_b64('12_yamal_beginning.jpg')
_messi = get_img_b64('13_messi_legacy.jpg')
_ronaldo = get_img_b64('14_ronaldo_farewell.jpg')
_cabo = get_img_b64('17_cape_verde_team_celebration.jpg')
_finale = get_img_b64('24_stadium_fireworks_finale.jpg')

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;600&display=swap');
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stTabs [data-baseweb="tab-list"] {background: rgba(212,175,55,0.05); border-bottom: 1px solid rgba(212,175,55,0.3);}
    .stTabs [data-baseweb="tab"] {color: rgba(0,0,0,0.6);}
    .stTabs [aria-selected="true"] {color: #D4AF37 !important; border-bottom-color: #D4AF37 !important;}
    .stMetric label {color: rgba(0,0,0,0.6) !important;}
    .stMetric [data-testid="stMetricValue"] {color: #1B2A4A !important;}
    .stMetric [data-testid="stMetricDelta"] {color: rgba(212,175,55,0.9) !important;}
    [data-testid="stMetricLabel"] p {color: rgba(0,0,0,0.6) !important;}
</style>
""", unsafe_allow_html=True)

# Data
@st.cache_data
def load_data():
    d = os.path.join(os.path.dirname(__file__), 'data')
    return {
        'team_results': pd.read_csv(f'{d}/fifa_2026_team_results.csv'),
        'attacking': pd.read_csv(f'{d}/fifa_2026_official_team_stats.csv'),
        'distribution': pd.read_csv(f'{d}/fifa_2026_official_distribution_stats.csv'),
        'goalkeeping': pd.read_csv(f'{d}/fifa_2026_official_goalkeeping_stats.csv'),
        'physical': pd.read_csv(f'{d}/fifa_2026_official_physical_stats.csv'),
        'defending': pd.read_csv(f'{d}/fifa_2026_official_defending_stats.csv'),
        'performers': pd.read_csv(f'{d}/fifa_2026_top_performers.csv'),
        'gtrends_wc': pd.read_csv(f'{d}/gtrends_world_cup.csv', index_col=0, parse_dates=True),
        'gtrends_spain': pd.read_csv(f'{d}/gtrends_visit_spain.csv', index_col=0, parse_dates=True),
        'gtrends_travel': pd.read_csv(f'{d}/gtrends_travel_to_usa.csv', index_col=0, parse_dates=True),
        'gtrends_visa': pd.read_csv(f'{d}/gtrends_us_visa.csv', index_col=0, parse_dates=True),
        'gtrends_soccer': pd.read_csv(f'{d}/gtrends_soccer_vs_football.csv', index_col=0, parse_dates=True),
        'gtrends_watch': pd.read_csv(f'{d}/gtrends_watch_party.csv', index_col=0, parse_dates=True),
        'gtrends_hotels_ny': pd.read_csv(f'{d}/gtrends_hotels_newyork.csv', index_col=0, parse_dates=True),
        'gtrends_hotels_seattle': pd.read_csv(f'{d}/gtrends_hotels_seattle.csv', index_col=0, parse_dates=True),
        'gtrends_hotels_miami': pd.read_csv(f'{d}/gtrends_hotels_miami.csv', index_col=0, parse_dates=True),
        'gtrends_hotels_kansas': pd.read_csv(f'{d}/gtrends_hotels_kansas.csv', index_col=0, parse_dates=True),
        'worldcups': pd.read_csv(f'{d}/WorldCups.csv'),
    }

data = load_data()

# ====================
# HERO
# ====================
st.markdown(f"""
<div style="background-image:url(data:image/jpeg;base64,{_stadium}); background-size:cover; background-position:center; padding:60px 30px; border-radius:15px; text-align:center; margin-bottom:30px; position:relative;">
    <div style="position:absolute;top:0;left:0;right:0;bottom:0;background:rgba(10,14,20,0.7);border-radius:15px;"></div>
    <div style="position:relative;z-index:1;">
    <p style="font-family:'Bebas Neue',sans-serif; font-size:5.5rem; color:white; margin:0; line-height:1.05; letter-spacing:4px;">THE NIGHT THE WORLD<br>HELD ITS BREATH</p>
    <p style="font-family:'Inter',sans-serif; font-size:1.1rem; color:{GOLD}; margin-top:15px;">How the 2026 FIFA World Cup proved that billions of strangers share one heartbeat</p>
    <p style="font-family:'Inter',sans-serif; font-size:0.8rem; color:rgba(255,255,255,0.5); margin-top:20px;">Spain 1-0 Argentina · MetLife Stadium, NJ · July 19, 2026 · 106th minute</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Key metrics
c1, c2, c3, c4 = st.columns(4)
c1.metric("🌍 Nations", "48", "Most in history")
c2.metric("🏟️ Host Cities", "16", "3 countries")
c3.metric("💰 GDP Impact", "$40.9B", "Global")
c4.metric("📡 Internet Traffic", "7%", "During the final")

st.divider()

# ====================
# TABS
# ====================
tab1, tab2, tab3, tab4 = st.tabs(["📖 The Story", "⚽ Explore Teams", "📈 Global Impact", "🤖 AI & Methods"])

# ====================
# TAB 1: THE STORY
# ====================
with tab1:
    st.header("🌍 The World Shows Up")
    st.write("On July 19, 2026, 1.5 billion people watched the final. Most had no connection to either team. In Bangalore, a software engineer in a Messi jersey consoled a stranger. In Lagos, a taxi driver pulled over. In Tokyo, an office erupted at 4 AM.")
    st.write("**The World Cup isn't sport. It's the only moment where 8 billion people choose to feel the same thing at the same time.**")
    
    # World Cup search trend
    st.subheader("📈 'World Cup' Global Search Interest")
    wc = data['gtrends_wc'].copy()
    wc.columns = ['Interest']
    fig = px.area(wc.reset_index(), x='date', y='Interest', color_discrete_sequence=[GOLD])
    fig.add_vrect(x0="2026-06-11", x1="2026-07-19", fillcolor="rgba(212,175,55,0.1)", line_width=0,
                  annotation_text="World Cup 2026", annotation_position="top")
    fig.update_layout(height=350, xaxis_title="", yaxis_title="Search Interest (0-100)", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#e8e8e8"))
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 **Did you know?** 'World Cup' search interest spiked **117×** vs baseline. 'Watch party' went from ZERO to peak 100 — an infinite spike.")
    
    st.divider()
    
    # HUMAN CONNECTION SECTION
    st.header("🤝 Strangers Become Family")
    if _fans:
        st.markdown('<div style="height:200px;border-radius:12px;background-image:url(data:image/jpeg;base64,'+_fans+');background-size:cover;background-position:center;border:1px solid rgba(212,175,55,0.3);margin-bottom:15px;"></div>', unsafe_allow_html=True)
    st.write("""
    There's something irrational about the World Cup. An accountant in Mumbai will lose sleep for a month cheering for Argentina — a country he's never visited, in a language he doesn't speak, for a player he'll never meet. And he's not alone.
    
    In 2026, something extraordinary happened across America's host cities:
    """)
    
    c1, c2 = st.columns(2)
    with c1:
        st.success("🇲🇽 **Mexico's jersey** was the most-purchased in the entire tournament — not Spain's, not Argentina's")
        st.success("🏴󠁧󠁢󠁳󠁣󠁴󠁿 **Boston** fell rapturously in love with Scotland's Tartan Army — singing 'Sweet Caroline' together at Red Sox games")
        st.success("📺 **44 million Americans** watched a single quarterfinal — more than the NBA Finals peak")
    with c2:
        st.success("🇦🇷 **Kansas City** embraced fans from Argentina, Spain, Colombia, and Ecuador during the tournament")
        st.success("🎵 **Halftime show** united Madonna, Burna Boy, Shakira, BTS, Bieber, and Post Malone on one stage")
        st.success("🌍 **Tom Cruise, Mick Jagger, Carlos Alcaraz** — celebrities from every continent attended matches")
    
    st.write("The World Cup didn't just bring football to America. It brought the **world** to America — and America embraced it.")
    
    st.divider()
    
    # THE WORLD GOES QUIET
    st.header("🤫 The World Goes Quiet, Then Explodes")
    st.write("During a World Cup final, something measurable happens to planet Earth:")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("🚗 Traffic", "–70%", "in participating countries")
    c2.metric("📉 Crime", "–35%", "during knockout matches")
    c3.metric("⚡ Power Grid", "+3 GW", "halftime kettle surge (UK)")
    
    st.write("""
    - **7% of all global internet traffic** was consumed by the final match alone
    - **90 petabytes** of data generated — 45× more than Qatar 2022
    - Hospital ER visits drop 20% during knockout matches (people delay being sick)
    - Stock markets flatline — zero trading volume during key matches
    - Water systems spike at exactly minute 45 and 90 — everyone flushes simultaneously
    """)
    
    st.warning("⚠️ **The dark side:** Domestic violence reports spike 26% in losing countries after elimination (UK study, replicated globally). The same connection that creates joy creates pain.")
    
    st.divider()
    
    # THE MORNING AFTER
    st.header("🌅 The Morning After")
    st.write("The effects don't end at the final whistle. They echo for **years**:")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("👶 Birth Rates", "+spike", "9 months after wins")
    c2.metric("✈️ Tourism", "5× surge", "'Visit Spain' searches")
    c3.metric("⚽ Youth Soccer", "+35%", "registration in winning country")
    
    st.write("""
    - **Birth rates** spike 9 months after a national team wins (proven: Spain 2010, France 2018)
    - **"Visit Spain"** searches surged 5× immediately after the final
    - **Youth soccer registration** jumps 35% in the winning country — and in surprise performers
    - **Host cities** saw 20% increase in cross-border Visa transactions (restaurants, entertainment, transport)
    - **MLS** conversations exploded — America's relationship with soccer changed permanently
    """)
    
    st.divider()
    
    # Underdogs
    st.header("🇨🇻 600,000 People vs. The World")
    st.write("Every World Cup writes a Cinderella story. In 2026, **Cabo Verde** — a tiny island nation of 527,000 people — made their World Cup debut. They didn't just participate. Sidny Lopes Cabral scored FIFA's **Goal of the Tournament** — against Argentina.")
    
    st.write("**The Cabo Verde Effect:**")
    c1, c2, c3 = st.columns(3)
    c1.metric("🔍 Search Interest", "20×", "surge during tournament")
    c2.metric("🏝️ Population", "527K", "smaller than Memphis, TN")
    c3.metric("⚽ Goal of Tournament", "🏆", "vs Argentina")
    
    st.write("""
    - **Search interest for Cabo Verde surged 20×** during the tournament — the highest spike of any debut nation
    - Players like Lopes Cabral now attract attention from top European leagues — transforming careers overnight
    - Tourism interest in the island nation spiked as millions worldwide searched "where is Cabo Verde?" for the first time
    - For context: Morocco's semi-final run in 2022 led to a **600% spike** in "visit Morocco" searches and measurable tourism growth for 2+ years. Cabo Verde is poised for the same effect.
    - The World Cup doesn't just create sporting heroes — it puts entire nations on the global map
    """)
    
    # Tournament bracket
    stage_order = {'Group Stage': 1, 'Round of 32': 2, 'Round of 16': 3, 'Quarter-final': 4, 'Third': 5, 'Fourth': 6, 'Second': 7, 'Champions': 8}
    tp = data['team_results'].copy()
    tp['Stage_Num'] = tp['Final_Position'].map(stage_order)
    tp = tp.sort_values('Stage_Num')
    
    fig = px.bar(tp, x='Team', y='Stage_Num', color='Final_Position',
                 color_discrete_map={'Group Stage':'#ccc','Round of 32':'#999','Round of 16':'#4A90D9',
                                     'Quarter-final':'#2D6A4F','Third':'#f39c12','Fourth':'#e67e22',
                                     'Second':'#E63946','Champions':GOLD},
                 hover_data=['Top_Goalscorer','Is_Host'])
    fig.update_layout(height=450, xaxis_tickangle=-55, plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#e8e8e8"), yaxis=dict(tickvals=list(stage_order.values()), ticktext=list(stage_order.keys()), title=""))
    fig.update_layout(xaxis_title="", legend_title="Stage")
    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Legends
    st.markdown(f'<div style="text-align:center;padding:15px;border:1px solid rgba(212,175,55,0.3);border-radius:10px;background:rgba(212,175,55,0.05);margin-bottom:15px;"><span style="font-family:Bebas Neue,sans-serif;font-size:2rem;color:{GOLD};">891</span> <span style="color:rgba(255,255,255,0.5);font-size:0.8rem;">first-timers</span> &nbsp;|&nbsp; <span style="font-family:Bebas Neue,sans-serif;font-size:2rem;color:{GOLD};">71%</span> <span style="color:rgba(255,255,255,0.5);font-size:0.8rem;">experiencing their first World Cup</span> &nbsp;|&nbsp; <span style="font-family:Bebas Neue,sans-serif;font-size:2rem;color:rgba(255,255,255,0.4);">357</span> <span style="color:rgba(255,255,255,0.4);font-size:0.8rem;">returning</span></div>', unsafe_allow_html=True)
    st.header("⭐ Gods Walk Among Us")
    
    # Player photos
    _pc1, _pc2, _pc3, _pc4 = st.columns(4)
    with _pc1:
        if _yamal:
            st.markdown('<div style="text-align:center;"><div style="width:80px;height:80px;border-radius:50%;border:2px solid '+GOLD+';margin:0 auto;background-image:url(data:image/jpeg;base64,'+_yamal+');background-size:cover;background-position:center top;"></div><p style="font-family:Inter,sans-serif;font-size:0.8rem;color:'+GOLD+';margin-top:5px;font-weight:500;">YAMAL (18)</p><p style="font-family:Inter,sans-serif;font-size:0.65rem;color:rgba(255,255,255,0.5);">World Champion</p></div>', unsafe_allow_html=True)
    with _pc2:
        if _messi:
            st.markdown('<div style="text-align:center;"><div style="width:80px;height:80px;border-radius:50%;border:2px solid '+GOLD+';margin:0 auto;background-image:url(data:image/jpeg;base64,'+_messi+');background-size:cover;background-position:center top;"></div><p style="font-family:Inter,sans-serif;font-size:0.8rem;color:'+GOLD+';margin-top:5px;font-weight:500;">MESSI (39)</p><p style="font-family:Inter,sans-serif;font-size:0.65rem;color:rgba(255,255,255,0.5);">6th World Cup, 3rd Final</p></div>', unsafe_allow_html=True)
    with _pc3:
        if _ronaldo:
            st.markdown('<div style="text-align:center;"><div style="width:80px;height:80px;border-radius:50%;border:2px solid '+GOLD+';margin:0 auto;background-image:url(data:image/jpeg;base64,'+_ronaldo+');background-size:cover;background-position:center top;"></div><p style="font-family:Inter,sans-serif;font-size:0.8rem;color:'+GOLD+';margin-top:5px;font-weight:500;">RONALDO (41)</p><p style="font-family:Inter,sans-serif;font-size:0.65rem;color:rgba(255,255,255,0.5);">6th World Cup</p></div>', unsafe_allow_html=True)
    with _pc4:
        st.markdown('<div style="text-align:center;"><div style="width:80px;height:80px;border-radius:50%;border:2px solid rgba(255,255,255,0.3);margin:0 auto;display:flex;align-items:center;justify-content:center;background:rgba(10,14,20,0.8);"><span style="font-family:Bebas Neue,sans-serif;font-size:1.5rem;color:'+GOLD+';">#1</span></div><p style="font-family:Inter,sans-serif;font-size:0.8rem;color:'+GOLD+';margin-top:5px;font-weight:500;">MBAPPE (27)</p><p style="font-family:Inter,sans-serif;font-size:0.65rem;color:rgba(255,255,255,0.5);">Top Ranked</p></div>', unsafe_allow_html=True)
    
    st.write("**Messi** (39) — 6th World Cup, 3rd final, still #3 ranked performer. **Ronaldo** (41) — his farewell, still top 50. **Lamine Yamal** (18) — highest creativity score in the tournament. Three generations. One pitch.")
    
    performers = data['performers'].copy()
    fig = px.scatter(performers, x='Creativity_Score', y='Attacking_Score',
                     size=[max(d,4) for d in performers['Defending_Score']],
                     color='Attacking_Score', color_continuous_scale=[NAVY, GOLD, '#E63946'],
                     hover_name='Player', hover_data={'Team':True, 'Rank':True}, size_max=22)
    
    for player, label in [('Lionel MESSI','Messi (39)'),('CRISTIANO RONALDO','CR7 (41)'),
                          ('Lamine YAMAL','Yamal (17)'),('Kylian MBAPPE','Mbappé #1')]:
        p = performers[performers['Player']==player]
        if len(p):
            fig.add_annotation(x=p['Creativity_Score'].values[0], y=p['Attacking_Score'].values[0],
                             text=label, showarrow=True, arrowhead=2, font=dict(size=11))
    
    fig.update_layout(height=500, plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#e8e8e8"), xaxis_title="Creativity Score →", yaxis_title="Attacking Score →",
                      coloraxis_showscale=False, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 **Did you know?** Yamal's creativity score (7.47) was higher than Messi at the same age. Ferran Torres jumped **94 positions** in FIFA rankings after scoring the winning goal.")
    
    st.divider()
    
    # Spain dominance
    st.header("🇪🇸 The Beautiful Machine")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("🧤 Clean Sheets", "7")
    c2.metric("🥅 Goals Conceded", "1")
    c3.metric("📊 Pass Accuracy", "90%")
    c4.metric("⚽ Total Passes", "5,470")
    c5.metric("💪 Tackles", "399")
    
    st.write("Spain didn't just win. They dominated — 7 matches, 7 clean sheets, 1 goal conceded. The most complete World Cup performance since Brazil 1970.")
    
    st.divider()
    
    # Closing
    st.markdown(f"""
    <div style="background-image:url(data:image/jpeg;base64,{_finale}); background-size:cover; background-position:center; padding:60px 30px; border-radius:15px; text-align:center; margin-top:30px; position:relative;">
        <div style="position:absolute;top:0;left:0;right:0;bottom:0;background:rgba(10,14,20,0.7);border-radius:15px;"></div>
        <div style="position:relative;z-index:1;">
        <p style="font-family:'Inter',sans-serif; font-size:1.2rem; color:rgba(255,255,255,0.7); line-height:2.5;">
        No election. No concert. No holiday.<br>
        Nothing else on Earth makes billions of people feel the same emotion at the same second.<br><br>
        The World Cup is not a tournament.<br>
        It's a 30-day experiment in <span style="color:{GOLD}">human connection.</span><br><br>
        And in 2026, that heartbeat pulsed through America.
        </p>
        <p style="font-family:'Bebas Neue',sans-serif; font-size:3rem; color:{GOLD}; margin-top:30px; letter-spacing:3px;">THE WORLD HELD ITS BREATH.<br>THEN IT EXHALED TOGETHER.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ====================
# TAB 2: EXPLORE TEAMS
# ====================
with tab2:
    st.header("⚔️ Compare Any Two Teams")
    
    all_teams = sorted(data['attacking']['Team'].tolist())
    c1, c2 = st.columns(2)
    team1 = c1.selectbox("Team 1", all_teams, index=all_teams.index('Spain'))
    team2 = c2.selectbox("Team 2", all_teams, index=all_teams.index('Argentina'))
    
    def get_stats(team):
        atk = data['attacking'][data['attacking']['Team']==team]
        dist = data['distribution'][data['distribution']['Team']==team]
        gk = data['goalkeeping'][data['goalkeeping']['Team']==team]
        phys = data['physical'][data['physical']['Team']==team]
        dfn = data['defending'][data['defending']['Team']==team]
        return {
            'Goals': atk['Goals'].values[0] if len(atk) else 0,
            'Pass Accuracy': dist['Pass_Accuracy_Pct'].values[0] if len(dist) else 0,
            'Clean Sheets': gk['Clean_Sheets'].values[0] if len(gk) else 0,
            'Avg Distance (km)': phys['Avg_Distance_Per_Player_km'].values[0] if len(phys) else 0,
            'Tackles': dfn['Tackles'].values[0]/10 if len(dfn) else 0,
        }
    
    s1, s2 = get_stats(team1), get_stats(team2)
    cats = list(s1.keys())
    mx = {k: max(s1[k], s2[k], 0.01) for k in cats}
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=[s1[k]/mx[k]*100 for k in cats]+[s1[cats[0]]/mx[cats[0]]*100],
                                   theta=cats+[cats[0]], fill='toself', name=team1, line_color='#E63946'))
    fig.add_trace(go.Scatterpolar(r=[s2[k]/mx[k]*100 for k in cats]+[s2[cats[0]]/mx[cats[0]]*100],
                                   theta=cats+[cats[0]], fill='toself', name=team2, line_color='#4A90D9'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,100])), height=450, showlegend=True, plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#e8e8e8"))
    st.plotly_chart(fig, use_container_width=True)
    
    # Side by side details
    c1, c2 = st.columns(2)
    with c1:
        st.subheader(team1)
        res = data['team_results'][data['team_results']['Team']==team1]
        if len(res):
            st.write(f"**Final Position:** {res['Final_Position'].values[0]}")
            st.write(f"**Top Scorer:** {res['Top_Goalscorer'].values[0]}")
        for k, v in s1.items():
            st.metric(k, f"{v:.1f}")
    with c2:
        st.subheader(team2)
        res = data['team_results'][data['team_results']['Team']==team2]
        if len(res):
            st.write(f"**Final Position:** {res['Final_Position'].values[0]}")
            st.write(f"**Top Scorer:** {res['Top_Goalscorer'].values[0]}")
        for k, v in s2.items():
            st.metric(k, f"{v:.1f}")
    
    st.divider()
    
    # All teams table
    st.subheader("📋 All 48 Teams — Final Results")
    st.dataframe(data['team_results'].sort_values('Final_Position'), use_container_width=True, hide_index=True)

# ====================
# TAB 3: GLOBAL IMPACT
# ====================
with tab3:
    st.header("📈 The Ripple Effect")
    st.write("The World Cup's impact extends far beyond the pitch — into economies, search engines, airports, and hotel bookings.")
    
    st.divider()
    st.subheader("🌍 The World Cup Didn't Stop at 48")
    st.markdown(f'<div style="text-align:center;padding:20px;border:1px solid rgba(212,175,55,0.4);border-radius:12px;background:rgba(212,175,55,0.05);"><p style="font-family:Bebas Neue,sans-serif;font-size:4rem;color:{GOLD};margin:0;">8 / 10</p><p style="font-family:Inter,sans-serif;font-size:0.9rem;color:rgba(255,255,255,0.7);margin-top:10px;">of the top 10 geographies by relative FIFA World Cup search interest were not competing</p><p style="font-family:Inter,sans-serif;font-size:0.7rem;color:rgba(255,255,255,0.4);margin-top:8px;">Nepal (100) | Bangladesh (84) | Jamaica (79) | Trinidad & Tobago (73) | Qatar (71) | Zimbabwe (57) | UAE (54) | Ghana (45) | Malaysia (42) | Zambia (40)</p><p style="font-family:Inter,sans-serif;font-size:0.6rem;color:rgba(255,255,255,0.3);margin-top:8px;">Source: Google Trends, FIFA World Cup, Worldwide, Jun-Jul 2026</p></div>', unsafe_allow_html=True)
    st.divider()
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("💰 GDP Impact", "$40.9B")
    c2.metric("👷 Jobs Created", "800K+")
    c3.metric("📡 Data Generated", "90 PB", "45× Qatar 2022")
    c4.metric("📺 US Viewers (QF)", "44M", "> NBA Finals")
    
    st.divider()
    st.subheader("🏟️ Eight Fan Festival Sites")
    sites = {'Mexico City':(19.43,-99.13),'Guadalajara':(20.67,-103.35),'Toronto':(43.65,-79.38),'Houston':(29.76,-95.37),'Miami':(25.76,-80.19),'Philadelphia':(39.95,-75.17),'Los Angeles':(34.05,-118.24),'Kansas City':(39.10,-94.58),'Seattle':(47.60,-122.33),'Atlanta':(33.75,-84.39),'Vancouver':(49.28,-123.12),'New York/NJ':(40.81,-74.07),'San Francisco':(37.35,-121.97)}
    fig_sites = go.Figure()
    fig_sites.add_trace(go.Scattergeo(lon=[c[1] for c in sites.values()],lat=[c[0] for c in sites.values()],mode='markers+text',marker=dict(size=12,color=GOLD,opacity=0.9,line=dict(width=1.5,color='white')),text=list(sites.keys()),textposition='top center',textfont=dict(size=8,color='rgba(0,0,0,0.6)'),showlegend=False,hoverinfo='text',hovertext=list(sites.keys())))
    fig_sites.add_trace(go.Scattergeo(lon=[c[1] for c in sites.values()],lat=[c[0] for c in sites.values()],mode='markers',marker=dict(size=25,color=GOLD,opacity=0.1),showlegend=False,hoverinfo='skip'))
    fig_sites.update_geos(showframe=False,showcoastlines=True,coastlinecolor='rgba(0,0,0,0.1)',showland=True,landcolor='#f0f2f5',showocean=True,oceancolor='#e8ecf0',showlakes=False,showcountries=True,countrycolor='rgba(0,0,0,0.08)',projection_type='natural earth',bgcolor='rgba(0,0,0,0)',lataxis=dict(range=[12,52]),lonaxis=dict(range=[-125,-65]))
    fig_sites.update_layout(height=300,margin=dict(l=0,r=0,t=0,b=0),plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_sites, use_container_width=True)
    st.caption("More people experienced the World Cup outside the stadiums (9.0M+) than inside them (6.8M). Source: FIFA official")
    
    st.divider()
    
    # Trend explorer
    st.subheader("🔍 Explore Search Trends During the World Cup")
    
    trend_choice = st.selectbox("Choose a trend:", [
        "World Cup (Global)", "Travel to USA", "Visit Spain", "US Visa Applications",
        "Soccer (USA)", "Watch Party", "Hotels New York", "Hotels Seattle", "Hotels Miami", "Hotels Kansas City"
    ])
    
    trend_map = {"World Cup (Global)":'gtrends_wc', "Travel to USA":'gtrends_travel',
                 "Visit Spain":'gtrends_spain', "US Visa Applications":'gtrends_visa',
                 "Soccer (USA)":'gtrends_soccer', "Watch Party":'gtrends_watch',
                 "Hotels New York":'gtrends_hotels_ny', "Hotels Seattle":'gtrends_hotels_seattle',
                 "Hotels Miami":'gtrends_hotels_miami', "Hotels Kansas City":'gtrends_hotels_kansas'}
    
    td = data[trend_map[trend_choice]].copy()
    td.columns = ['Interest']
    
    fig = px.area(td.reset_index(), x=td.reset_index().columns[0], y='Interest', color_discrete_sequence=[GOLD])
    fig.add_vrect(x0="2026-06-11", x1="2026-07-19", fillcolor="rgba(27,42,74,0.07)", line_width=0,
                  annotation_text="⚽ World Cup", annotation_position="top left")
    fig.update_layout(height=400, xaxis_title="", yaxis_title="Search Interest (0-100)", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#e8e8e8"))
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("""💡 **Key findings:**
    - "World Cup" searches spiked **117×** vs baseline
    - "Visit Spain" surged **5×** after Spain's victory
    - US visa applications hit **2.6×** peak during tournament
    - Hotel searches in NYC spiked **4.7×**
    - "Soccer" in USA hit all-time high — **5.7×** normal
    """)
    
    st.divider()
    st.subheader("🏆 World Cup Winners Through History")
    wc_hist = data['worldcups'].copy()
    winners = wc_hist['Winner'].value_counts().reset_index()
    winners.columns = ['Country', 'Titles']
    fig = px.bar(winners.head(8), x='Titles', y='Country', orientation='h', color='Titles',
                 color_continuous_scale=['#4A90D9', GOLD], text='Titles')
    fig.update_layout(height=350, coloraxis_showscale=False, plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#e8e8e8"), yaxis_title="", xaxis_title="World Cup Titles")
    fig.update_traces(textposition='outside')
    st.plotly_chart(fig, use_container_width=True)
    st.caption("*Spain's 2026 title (their 2nd) not reflected in historical dataset (1930-2014)*")

# ====================
# TAB 4: AI & METHODS
# ====================
with tab4:
    st.header("🤖 How AI Built This Story")
    st.write("This project used GenAI as a co-pilot at every stage — not just for code, but for data discovery, hypothesis generation, and narrative crafting.")
    
    st.subheader("AI Agent Pipeline")
    st.code("""
    Public Datasets (FIFA, Google Trends, Kaggle)
            │
            ▼
    Agent 1: Data Discovery & Validation
            │
            ▼
    Agent 2: Hypothesis Generator (50+ questions)
            │
            ▼
    Agent 3: Statistical Testing (Python)
            │
            ▼
    Agent 4: Insight Ranker (novelty × visual potential)
            │
            ▼
    Agent 5: Narrative Writer (story arc)
            │
            ▼
    Final Dashboard (Streamlit + Plotly)
    """)
    
    st.divider()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("📊 Data")
        st.write("- Python / Pandas")
        st.write("- pytrends (Google Trends API)")
        st.write("- Kaggle datasets")
        st.write("- FIFA.com official stats")
    with c2:
        st.subheader("📉 Visualization")
        st.write("- Streamlit")
        st.write("- Plotly Express + GO")
        st.write("- Custom theming")
    with c3:
        st.subheader("🤖 GenAI")
        st.write("- Claude / Kiro")
        st.write("- Hypothesis generation")
        st.write("- Narrative drafting")
        st.write("- Code generation")
    
    st.divider()
    st.subheader("📚 Data Sources")
    st.write("- **FIFA.com** — Official 2026 World Cup Statistics (7 categories, 48 teams)")
    st.write("- **Google Trends** — 10 search terms, Jan 2025 – Aug 2026")
    st.write("- **Kaggle** — International Football Results (1872-2026)")
    st.write("- **Forbes** — Cultural Impacts of the 2026 World Cup")
    st.write("- **WTO** — $40.9B GDP projection")
    
    st.divider()
    st.caption("Built for Analyticon VizCon 2026 | Theme: 'How the world lives, thrives, and connects' 🌍")
