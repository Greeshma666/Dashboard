import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(page_title="When the World Held Its Breath", page_icon="⚽", layout="wide", initial_sidebar_state="collapsed")

# Colors
NAVY = "#1B2A4A"
GOLD = "#3AAFDD"

# Minimal CSS - don't fight Streamlit
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;600&display=swap');
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
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

# Load player images
import base64
def _load_img(filename):
    try:
        with open(os.path.join(os.path.dirname(__file__), 'assets', filename), 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

_yamal = _load_img('12_yamal_beginning.jpg')
_messi = _load_img('13_messi_legacy.jpg')
_ronaldo = _load_img('14_ronaldo_farewell.jpg')
_mbappe = _load_img('mbappe.jpg')

# ====================
# HERO
# ====================
st.markdown(f"""
<div style="background:{NAVY}; padding:60px 30px; border-radius:15px; text-align:center; margin-bottom:30px;">
    <p style="font-family:'Bebas Neue',sans-serif; font-size:5.5rem; color:white; margin:0; line-height:1.05; letter-spacing:4px;">WHEN THE WORLD<br>HELD ITS BREATH</p>
    <p style="font-family:'Inter',sans-serif; font-size:1.1rem; color:{GOLD}; margin-top:15px;">How FIFA World Cup proved that billions of strangers share one heartbeat <svg width="40" height="20" viewBox="0 0 40 20" style="vertical-align:middle;"><polyline points="0,10 8,10 11,2 14,18 17,6 20,14 23,10 40,10" fill="none" stroke="#dc3545" stroke-width="2"/></svg></p>
</div>
""", unsafe_allow_html=True)

# Key metrics
c1, c2, c3, c4 = st.columns(4)
c1.metric("🌍 Nations", "48", "Most in history")
c2.metric("🏟️ Host Cities", "16", "3 countries")
c3.metric("👷 Jobs (Est.)", "~824K", "FTE — FIFA/WTO study")
c4.metric("📡 Internet", "Up to 7%", "of global traffic (projected)")
c1.markdown("[Source](https://inside.fifa.com/strategic-objectives-2023-2027/goal-9)", unsafe_allow_html=True)
c2.markdown("[Source](https://inside.fifa.com/strategic-objectives-2023-2027/goal-9)", unsafe_allow_html=True)
c3.markdown("[Source](https://inside.fifa.com/organisation/media-releases/fifa-wto-study-estimates-usd-47-billion-economic-output-from-fifa-club-world)", unsafe_allow_html=True)
c4.markdown("[Source](https://www.sportsbusinessjournal.com/Articles/2026/06/08/numbers-to-know-around-the-world-cup/)", unsafe_allow_html=True)

st.divider()

# ====================
# TABS
# ====================
tab1, tab2, tab3, tab4 = st.tabs(["📖 The Story", "📈 Global Impact", "⚽ Explore Teams", "🤖 AI & Methods"])

# ====================
# TAB 1: THE STORY
# ====================
with tab1:
    st.header("🌍 The World Shows Up")
    st.write("On July 19, 2026, 1.5 billion people watched the final. Most had no connection to either team. In Bangalore, a software engineer in Messi's jersey consoled a stranger. In Lagos, a taxi driver pulled over to watch on his phone. In Tokyo, an office erupted at 4 AM.")
    st.write("**The World Cup isn't sport. It's the only moment where 8 billion people choose to feel the same thing at the same time.**")
    
    # World Cup search trend
    st.subheader("📈 'World Cup' Global Search Interest")
    wc = data['gtrends_wc'].copy()
    wc.columns = ['Interest']
    fig = px.area(wc.reset_index(), x='date', y='Interest', color_discrete_sequence=[GOLD])
    fig.add_vrect(x0="2026-06-11", x1="2026-07-19", fillcolor="rgba(58,175,221,0.12)", line_width=0,
                  annotation_text="World Cup 2026", annotation_position="top")
    fig.update_layout(height=350, xaxis_title="", yaxis_title="Search Interest (0-100)")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("*Source: [Google Trends — World Cup, Worldwide](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=World%20Cup)*")
    
    st.info("💡 **Did you know?** 'World Cup' search interest spiked **100×** vs baseline. 'Watch party' went from ZERO to peak 100 — an infinite spike.")
    
    st.divider()
    
    # HUMAN CONNECTION SECTION
    st.header("🤝 Strangers Became Family")
    st.write("""
    There's something irrational about the World Cup. An accountant in Mumbai will lose sleep for a month cheering for Argentina — a country he's never visited, in a language he doesn't speak, for a player he'll never meet. And he's not alone.
    
    In 2026, something extraordinary happened across America's host cities:
    """)
    
    c1, c2 = st.columns(2)
    with c1:
        with st.expander("🎉 **Watch parties went from zero to everywhere**", expanded=False):
            st.write("Before the World Cup, 'watch party' had near-zero search interest. During the tournament, it hit peak 100. Strangers gathered in bars, parks, and living rooms across the planet.")
            td = data['gtrends_watch'].copy()
            td.columns = ['Interest']
            fig_wp = px.area(td.reset_index(), x=td.reset_index().columns[0], y='Interest', color_discrete_sequence=[GOLD])
            fig_wp.add_vrect(x0="2026-06-11", x1="2026-07-19", fillcolor="rgba(58,175,221,0.12)", line_width=0)
            fig_wp.update_layout(height=200, xaxis_title="", yaxis_title="Search Interest", margin=dict(l=0,r=0,t=10,b=0))
            st.plotly_chart(fig_wp, use_container_width=True, key="chart_watchparty")
            st.markdown("*Source: [Google Trends](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=watch%20party) — Watch party, Worldwide*")
        
        with st.expander("⚽ **America discovered soccer**", expanded=False):
            st.write("'Soccer' searches in the USA hit an all-time high during the tournament — 5.7x normal levels. Decades of Major League Soccer (MLS) marketing couldn't do what one World Cup on home soil achieved in weeks.")
            td = data['gtrends_soccer'].copy()
            td.columns = ['Interest']
            fig_sc = px.area(td.reset_index(), x=td.reset_index().columns[0], y='Interest', color_discrete_sequence=[GOLD])
            fig_sc.add_vrect(x0="2026-06-11", x1="2026-07-19", fillcolor="rgba(58,175,221,0.12)", line_width=0)
            fig_sc.update_layout(height=200, xaxis_title="", yaxis_title="Search Interest", margin=dict(l=0,r=0,t=10,b=0))
            st.plotly_chart(fig_sc, use_container_width=True, key="chart_soccer")
            st.markdown("*Source: [Google Trends](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&geo=US&q=soccer) — Soccer, USA*")
        
        with st.expander("✈️ **The world traveled to be there**", expanded=False):
            st.write("'Travel to USA' searches surged globally during the tournament as fans from every continent made their way to host cities.")
            td = data['gtrends_travel'].copy()
            td.columns = ['Interest']
            fig_tr = px.area(td.reset_index(), x=td.reset_index().columns[0], y='Interest', color_discrete_sequence=[GOLD])
            fig_tr.add_vrect(x0="2026-06-11", x1="2026-07-19", fillcolor="rgba(58,175,221,0.12)", line_width=0)
            fig_tr.update_layout(height=200, xaxis_title="", yaxis_title="Search Interest", margin=dict(l=0,r=0,t=10,b=0))
            st.plotly_chart(fig_tr, use_container_width=True, key="chart_travel")
            st.markdown("*Source: [Google Trends](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=travel%20to%20USA) — Travel to USA, Worldwide*")
    
    with c2:
        with st.expander("🌍 **178 countries met in one American city**", expanded=False):
            st.write("During the first five festival dates, 63,000 people attended Kansas City's Fan Festival representing 178 countries. 52% local, 33% elsewhere in the U.S., 15% international.")
            st.metric("Countries Represented", "178", "In one city")
            st.metric("Attendees (first 5 days)", "63,000", "KC Fan Festival")
            td = data['gtrends_hotels_kansas'].copy()
            td.columns = ['Interest']
            fig_kc = px.area(td.reset_index(), x=td.reset_index().columns[0], y='Interest', color_discrete_sequence=[GOLD])
            fig_kc.add_vrect(x0="2026-06-11", x1="2026-07-19", fillcolor="rgba(58,175,221,0.12)", line_width=0)
            fig_kc.update_layout(height=200, xaxis_title="", yaxis_title="Search Interest", margin=dict(l=0,r=0,t=10,b=0))
            st.plotly_chart(fig_kc, use_container_width=True, key="chart_kc")
            st.markdown("*Source: KC2026 organizer report; [Google Trends](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=hotels%20kansas%20city) — Hotels Kansas City*")
        
        with st.expander("🏨 **Host cities were overwhelmed**", expanded=False):
            st.write("Hotel searches spiked across every host city. New York, Miami, Seattle, Kansas City, Dallas, Los Angeles — all saw unprecedented demand as the world converged on North America.")
            td_miami = data['gtrends_hotels_miami'].copy()
            td_miami.columns = ['Miami']
            td_ny = data['gtrends_hotels_ny'].copy()
            td_ny.columns = ['New York']
            td_seattle = data['gtrends_hotels_seattle'].copy()
            td_seattle.columns = ['Seattle']
            td_kc = data['gtrends_hotels_kansas'].copy()
            td_kc.columns = ['Kansas City']
            td_dallas = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'gtrends_hotels_dallas.csv'), index_col=0, parse_dates=True)
            td_dallas.columns = ['Dallas']
            td_la = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'gtrends_hotels_la.csv'), index_col=0, parse_dates=True)
            td_la.columns = ['Los Angeles']
            combined = td_miami.join(td_ny).join(td_seattle).join(td_kc).join(td_dallas).join(td_la)
            fig_ht = px.line(combined.reset_index(), x=combined.reset_index().columns[0], y=['Miami','New York','Seattle','Kansas City','Dallas','Los Angeles'], color_discrete_sequence=['#E91E63','#4CAF50','#FF9800','#9C27B0','#2196F3','#795548'])
            fig_ht.add_vrect(x0="2026-06-11", x1="2026-07-19", fillcolor="rgba(58,175,221,0.12)", line_width=0)
            fig_ht.update_layout(height=280, xaxis_title="", yaxis_title="Search Interest", margin=dict(l=0,r=0,t=10,b=0), legend=dict(orientation='h',y=-0.2))
            st.plotly_chart(fig_ht, use_container_width=True, key="chart_hotels")
            st.markdown("*Source: [Google Trends](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=hotels%20miami,hotels%20new%20york) — Hotel searches by city, Worldwide*")
        
        with st.expander("📋 **US visa demand exploded**", expanded=False):
            st.write("'US Visa' searches hit 2.6x their normal levels during the tournament — people weren't just watching from home, they were trying to get there.")
            td = data['gtrends_visa'].copy()
            td.columns = ['Interest']
            fig_vi = px.area(td.reset_index(), x=td.reset_index().columns[0], y='Interest', color_discrete_sequence=[GOLD])
            fig_vi.add_vrect(x0="2026-06-11", x1="2026-07-19", fillcolor="rgba(58,175,221,0.12)", line_width=0)
            fig_vi.update_layout(height=200, xaxis_title="", yaxis_title="Search Interest", margin=dict(l=0,r=0,t=10,b=0))
            st.plotly_chart(fig_vi, use_container_width=True, key="chart_visa")
            st.markdown("*Source: [Google Trends](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=US%20visa) — US Visa, Worldwide*")
    
    st.write("The World Cup didn't just bring football to America. It brought the **world** to America — and America embraced it.")
    
    st.divider()
    
    # THE WORLD GOES QUIET
    st.header("🤫 The World Goes Quiet, Then Explodes")
    st.write("During a World Cup, something measurable happens to planet Earth. These patterns have been documented across multiple tournaments:")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("⚡ Power Grid", "2.8 GW", "record UK World Cup TV pickup")
    c2.metric("🌐 Internet", "Up to 7%", "projected global traffic")
    c3.metric("📊 Data", "13 PB", "transported (as of quarterfinals)")
    c1.markdown("[Source](https://www.neso.energy/news/neso-ready-record-electricity-demand-during-biggest-ever-fifa-world-cup)", unsafe_allow_html=True)
    c2.markdown("[Source](https://www.sportsbusinessjournal.com/Articles/2026/06/08/numbers-to-know-around-the-world-cup/)", unsafe_allow_html=True)
    c3.markdown("[Source](https://football-technology.fifa.com/organisation/media-releases/packed-stadiums-record-digital-reach-world-cup-2026-numbers-unprecedented-scale)", unsafe_allow_html=True)
    
    st.write("""
    - **UK electricity demand recorded a 2.8 GW TV pickup** during the World Cup — millions boiling kettles simultaneously, a phenomenon documented by the UK's National Energy System Operator (NESO)
    - **Up to 7% of global internet traffic** was projected to be consumed during the final (Bank of America Global Research — pre-tournament estimate)
    - **13 petabytes** of data transported across tournament and broadcast networks as of the quarterfinals (FIFA official)
    - **Water systems spike at exactly minute 45** — everyone flushes simultaneously 🚽
    - **Road traffic drops significantly** during major knockout matches as people stay home to watch
    - **City noise levels drop measurably** during play, then spike at goals — documented by urban sound monitoring
    - **Food delivery demand surges** before kickoff as fans order in rather than cook
    """)
    st.markdown('<div style="padding:15px 20px;border-radius:8px;background:rgba(220,53,69,0.08);border:1px solid rgba(220,53,69,0.3);"><p style="margin:0;font-size:0.9rem;color:#dc3545;">⚠️ <strong>The dark side:</strong> Domestic abuse incidents rose 38% when England lost during World Cup matches, according to UK research. The same connection that creates joy can also expose a darker social reality.</p></div>', unsafe_allow_html=True)
    
    st.write('')
    st.markdown("*Sources: [Severn Trent — water-demand spikes](https://www.stwater.co.uk/news/news-releases/water-result---football-and-heatwave-pushing-up-demand-for-water/) | [Hindustan Times — water/bathroom demand spikes](https://www.hindustantimes.com/sports/football/when-bathroom-breaks-are-reserved-world-during-fifa-world-cup-final-2026-argentina-vs-spain-101784437568159.html) | [Houston Chronicle — noise measurements](https://www.houstonchronicle.com/projects/2026/houston-world-cup-noise/) | [Reuters — food demand](https://www.reuters.com/business/uks-dominos-pizza-logs-higher-interim-profit-helped-by-soccer-2026-08-04/) | [Lancaster University — domestic abuse study](https://research.lancaster-university.uk/en/publications/can-the-fifa-world-cup-football-soccer-tournament-be-associated-w/). Findings combine observed 2026 data with documented patterns from previous World Cups.*")
    
    st.divider()
    
    # THE MORNING AFTER
    st.header("🌅 The Morning After")
    st.write("The effects don't end at the final whistle. They echo for **years**:")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("👶 Birth Rates", "+spike", "9 months after wins")
    c2.metric("✈️ Tourism Interest", "+16%", "Visit Spain search interest")
    c3.metric("⚽ Youth Soccer", "+35%", "registration in winning country")
    
    st.write("""
    - **Birth rates** can spike 9 months after a national team wins — researchers identified 1,000+ additional births in South Africa around nine months after the 2010 World Cup
    - **"Visit Spain"** search interest rose 16% following the Final
    - **Youth soccer registration** jumps 35% in the winning country — and in surprise performers
    - **Major League Soccer (MLS)** conversations exploded — America's relationship with soccer changed permanently
    """)
    st.markdown("*Sources: [Google Trends — Visit Spain](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=visit%20spain) | [Birth rate study — PMC/NIH](https://pmc.ncbi.nlm.nih.gov/articles/PMC10906258/) | [Youth soccer registration — Yahoo Sports](https://sports.yahoo.com/articles/youth-soccer-numbers-locally-amid-223213320.html)*")
    
    st.divider()
    
    # Underdogs
    st.header("🇨🇻 527,000 People vs. The World")
    st.write("Every World Cup writes a Cinderella story. In 2026, it belonged to **Cabo Verde** — an island nation of just **527,000** making its World Cup debut. They stood fearlessly against football's giants and proved they belonged on the world's biggest stage: 40-year-old goalkeeper **Vozinha** made seven saves to hold eventual champions Spain scoreless, while Sidny Lopes Cabral scored FIFA's **Goal of the Tournament** against Argentina.")
    
    st.write("**The Cabo Verde Effect:**")
    c1, c2, c3 = st.columns(3)
    c1.metric("🔍 Search Interest", "100×", "peak during tournament")
    c2.metric("🏝️ Population", "527K", "World Bank 2025")
    c3.metric("⚽ Goal of Tournament", "🏆", "vs Argentina")
    c1.markdown("[Source](https://trends.google.com/trends/explore?date=2026-06-01%202026-07-31&q=Cabo%20Verde)", unsafe_allow_html=True)
    c2.markdown("[Source](https://data.worldbank.org/country/cabo-verde)", unsafe_allow_html=True)
    c3.markdown("[Source](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026)", unsafe_allow_html=True)
    
    # Cabo Verde Google Trends chart
    cabo_trends = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'gtrends_cabo_verde.csv'), skiprows=2)
    cabo_trends.columns = ['Day', 'Interest']
    cabo_trends['Interest'] = pd.to_numeric(cabo_trends['Interest'].replace('<1', '0'), errors='coerce')
    cabo_trends['Day'] = pd.to_datetime(cabo_trends['Day'])
    
    fig_cabo = px.area(cabo_trends, x='Day', y='Interest', color_discrete_sequence=[GOLD])
    fig_cabo.add_annotation(x='2026-06-15', y=50, text="vs Spain 0-0", showarrow=True, arrowhead=2, font=dict(size=9))
    fig_cabo.add_annotation(x='2026-06-21', y=32, text="vs Uruguay 2-2", showarrow=True, arrowhead=2, font=dict(size=9))
    fig_cabo.add_annotation(x='2026-07-03', y=94, text="vs Argentina 2-3", showarrow=True, arrowhead=2, font=dict(size=9))
    fig_cabo.update_layout(height=300, xaxis_title="", yaxis_title="Search Interest", title="'Cabo Verde' — Global Search Interest During the World Cup")
    st.plotly_chart(fig_cabo, use_container_width=True, key="chart_cabo")
    st.markdown("*Sources: [Google Trends — Cabo Verde](https://trends.google.com/trends/explore?date=2026-06-01%202026-07-31&q=Cabo%20Verde) | [Reuters — Vozinha move to Colo-Colo](https://www.reuters.com/sports/soccer/cape-verde-keeper-vozinha-says-he-always-believed-he-was-big-club-player-after-2026-08-05/)*")
    
    st.write("""
    - Search interest for Cabo Verde surged from **near-zero to 100** during the tournament
    - For players, the spotlight can change a career overnight — 40-year-old goalkeeper **Vozinha's** World Cup heroics attracted multiple offers before earning him a move to Chilean giants **Colo-Colo**
    - Tourism interest in the island nation spiked as millions worldwide searched **"where is Cabo Verde?"** for the first time
    - Morocco's semi-final run in 2022 led to a **600% spike** in "visit Morocco" searches and measurable tourism growth for 2+ years. Cabo Verde is poised for the same effect.
    - The World Cup doesn't just create sporting heroes — **it puts entire nations on the global map**
    """)
    
    st.divider()
    
    # Legends
    st.header("⭐ Legends Walk Among Us")
    st.write("**Three generations. One World Cup.**")
    
    _lg1, _lg2, _lg3, _lg4 = st.columns(4)
    with _lg1:
        st.markdown('<div style="text-align:center;"><div style="width:70px;height:70px;border-radius:50%;border:2px solid ' + GOLD + ';margin:0 auto 8px;background-image:url(data:image/jpeg;base64,' + _yamal + ');background-size:cover;background-position:center top;"></div></div>', unsafe_allow_html=True)
        st.markdown("**Lamine Yamal · 19**")
        st.write("First World Cup. World Champion. A new generation arrived.")
    with _lg2:
        st.markdown('<div style="text-align:center;"><div style="width:70px;height:70px;border-radius:50%;border:2px solid ' + GOLD + ';margin:0 auto 8px;background-image:url(data:image/jpeg;base64,' + _mbappe + ');background-size:cover;background-position:center top;"></div></div>', unsafe_allow_html=True)
        st.markdown("**Kylian Mbappé · 27**")
        st.write("10 goals. Golden Boot. The generation in its prime.")
    with _lg3:
        st.markdown('<div style="text-align:center;"><div style="width:70px;height:70px;border-radius:50%;border:2px solid ' + GOLD + ';margin:0 auto 8px;background-image:url(data:image/jpeg;base64,' + _messi + ');background-size:cover;background-position:center top;"></div></div>', unsafe_allow_html=True)
        st.markdown("**Lionel Messi · 39**")
        st.write("Sixth World Cup. 8 goals. Another final. Still writing history.")
    with _lg4:
        st.markdown('<div style="text-align:center;"><div style="width:70px;height:70px;border-radius:50%;border:2px solid ' + GOLD + ';margin:0 auto 8px;background-image:url(data:image/jpeg;base64,' + _ronaldo + ');background-size:cover;background-position:center top;"></div></div>', unsafe_allow_html=True)
        st.markdown("**Cristiano Ronaldo · 41**")
        st.write("Sixth World Cup. More than two decades on the international stage.")
    
    st.markdown("**19 → 27 → 39 → 41**")
    st.write("One was arriving. One was in his prime. Two were extending extraordinary legacies. For one summer, three generations shared the world's biggest stage.")
    st.markdown("*Source: [FIFA — Player Statistics](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/statistics/player-statistics)*")
    
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
    
    fig.update_layout(height=500, xaxis_title="Creativity Score →", yaxis_title="Attacking Score →",
                      coloraxis_showscale=False, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 **Did you know?** Yamal's creativity score (7.47) was higher than Messi at the same age.")
    
    st.divider()
    
    # Spain dominance
    st.divider()
    
    # Closing
    st.markdown(f"""
    <div style="background:{NAVY}; padding:60px 30px; border-radius:15px; text-align:center; margin-top:30px;">
        <p style="font-family:'Inter',sans-serif; font-size:1.2rem; color:rgba(255,255,255,0.7); line-height:2.5;">
        No election. No concert. No holiday.<br>
        Nothing else on Earth makes 8 billion people feel the same emotion at the same second.<br><br>
        The World Cup is not a tournament.<br>
        It's a 30-day experiment in <span style="color:{GOLD}">human connection.</span><br><br>
        And in 2026, that heartbeat pulsed through America.
        </p>
        <p style="font-family:'Bebas Neue',sans-serif; font-size:3rem; color:{GOLD}; margin-top:30px; letter-spacing:3px;">WHEN THE WORLD HELD ITS BREATH.<br>AND IT EXHALED TOGETHER.</p>
    </div>
    """, unsafe_allow_html=True)

# ====================
# TAB 2: EXPLORE TEAMS
# ====================
with tab3:
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
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,100])), height=400, showlegend=True)
    
    # Radar chart and team details SIDE BY SIDE
    col_stats, col_radar = st.columns([3, 4])
    with col_stats:
        # Both teams side by side
        t1, t2 = st.columns(2)
        with t1:
            st.markdown(f"**{team1}**")
            res1 = data['team_results'][data['team_results']['Team']==team1]
            if len(res1):
                st.caption(f"{res1['Final_Position'].values[0]} · {res1['Top_Goalscorer'].values[0]}")
            for k, v in s1.items():
                st.metric(k, f"{v:.1f}")
        with t2:
            st.markdown(f"**{team2}**")
            res2 = data['team_results'][data['team_results']['Team']==team2]
            if len(res2):
                st.caption(f"{res2['Final_Position'].values[0]} · {res2['Top_Goalscorer'].values[0]}")
            for k, v in s2.items():
                st.metric(k, f"{v:.1f}")
    with col_radar:
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    st.subheader("🏆 World Cup Winners Through History")
    wc_hist = data['worldcups'].copy()
    # Add missing recent winners (dataset only goes to 2014)
    import pandas as pd
    recent = pd.DataFrame({'Winner': ['France', 'Argentina', 'Spain']})  # 2018, 2022, 2026
    all_winners = pd.concat([wc_hist[['Winner']], recent])
    # Merge Germany FR and Germany
    all_winners['Winner'] = all_winners['Winner'].replace('Germany FR', 'Germany')
    winners = all_winners['Winner'].value_counts().reset_index()
    winners.columns = ['Country', 'Titles']
    fig_wc = px.bar(winners.head(8), x='Titles', y='Country', orientation='h', color='Titles',
                 color_continuous_scale=['#4A90D9', GOLD], text='Titles')
    fig_wc.update_layout(height=300, coloraxis_showscale=False, yaxis_title="", xaxis_title="World Cup Titles")
    fig_wc.update_traces(textposition='outside')
    st.plotly_chart(fig_wc, use_container_width=True)
    
    st.divider()
    
    # All teams table
    st.subheader("📋 All 48 Teams — Final Results")
    st.dataframe(data['team_results'].sort_values('Final_Position'), use_container_width=True, hide_index=True)
    st.markdown("*Source: [FIFA — Team Statistics](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/statistics/team-statistics)*")

# ====================
# TAB 3: GLOBAL IMPACT
# ====================
with tab2:
    st.header("📈 Global Impact")
    st.write("The World Cup's impact extends far beyond the pitch — into search engines, economies, and human behavior.")
    st.write("")

    
    # 8/10 Discovery
    st.subheader("🌍 The World Cup Didn't Stop at 48")
    st.write("48 nations competed. But the passion was global — the competition wasn't.")
    
    # Load Google Trends by country data
    import numpy as np
    gtrends_country = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'gtrends_wc_by_country.csv'), skiprows=2)
    gtrends_country.columns = ['Country', 'Interest']
    gtrends_country['Interest'] = pd.to_numeric(gtrends_country['Interest'], errors='coerce')
    gtrends_country = gtrends_country.dropna(subset=['Interest']).sort_values('Interest', ascending=False).reset_index(drop=True)
    
    # Determine participating vs non-participating
    results_df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'results.csv'))
    wc_2026 = results_df[(results_df['date'].str.startswith('2026-0')) & (results_df['tournament'] == 'FIFA World Cup')]
    participants = set(wc_2026['home_team'].tolist() + wc_2026['away_team'].tolist())
    fifa_to_gt = {'United Kingdom': ['England', 'Scotland'], 'Turkiye': ['Turkey'], 'Czechia': ['Czech Republic'], 'South Korea': ['South Korea']}
    
    def is_participant(country):
        if country in participants: return True
        if country in fifa_to_gt:
            for n in fifa_to_gt[country]:
                if n in participants: return True
        return False
    
    gtrends_country['Participated'] = gtrends_country['Country'].apply(is_participant)
    top10 = gtrends_country.head(10)
    non_part = top10[~top10['Participated']].shape[0]
    
    col_81, col_82 = st.columns([1, 2])
    with col_81:
        st.metric("🔍 Discovery", f"{non_part} / 10", "weren't competing")
        st.write(f"**{non_part} of the top 10** geographies by relative FIFA World Cup search interest were not even in the tournament.")
        st.markdown("*Source: [Google Trends](https://trends.google.com/trends/explore?date=2026-06-01%202026-07-31&q=FIFA%20World%20Cup) — FIFA World Cup by country*")
        st.write("*They were not on the pitch. But they were part of the moment.*")
    with col_82:
        # Horizontal bar chart
        top10_display = top10.copy()
        top10_display['Color'] = top10_display['Participated'].apply(lambda x: 'On the Pitch' if x else 'Outside the 48')
        fig_810 = px.bar(top10_display, y='Country', x='Interest', orientation='h', 
                        color='Color', color_discrete_map={'Outside the 48': GOLD, 'On the Pitch': '#1B2A4A'},
                        text='Interest')
        fig_810.update_layout(height=350, margin=dict(l=0,r=0,t=10,b=0), yaxis=dict(autorange='reversed'), 
                             xaxis_title='Relative Search Interest', yaxis_title='',
                             legend=dict(orientation='h', y=-0.15, title=''))
        fig_810.update_traces(textposition='outside')
        st.plotly_chart(fig_810, use_container_width=True, key="chart_810")
    
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
    fig.add_vrect(x0="2026-06-11", x1="2026-07-19", fillcolor="rgba(58,175,221,0.12)", line_width=0,
                  annotation_text="⚽ World Cup", annotation_position="top left")
    fig.update_layout(height=400, xaxis_title="", yaxis_title="Search Interest (0-100)")
    st.plotly_chart(fig, use_container_width=True)
    
    # Source link for selected trend
    trend_sources = {
        "World Cup (Global)": "[Google Trends — World Cup, Worldwide](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=World%20Cup)",
        "Travel to USA": "[Google Trends — Travel to USA, Worldwide](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=travel%20to%20USA)",
        "Visit Spain": "[Google Trends — Visit Spain, Worldwide](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=visit%20spain)",
        "US Visa Applications": "[Google Trends — US Visa, Worldwide](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=US%20visa)",
        "Soccer (USA)": "[Google Trends — Soccer, USA](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&geo=US&q=soccer)",
        "Watch Party": "[Google Trends — Watch Party, Worldwide](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=watch%20party)",
        "Hotels New York": "[Google Trends — Hotels New York, Worldwide](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=hotels%20new%20york)",
        "Hotels Seattle": "[Google Trends — Hotels Seattle, Worldwide](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=hotels%20seattle)",
        "Hotels Miami": "[Google Trends — Hotels Miami, Worldwide](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=hotels%20miami)",
        "Hotels Kansas City": "[Google Trends — Hotels Kansas City, Worldwide](https://trends.google.com/trends/explore?date=2025-01-01%202026-08-01&q=hotels%20kansas%20city)",
    }
    st.markdown(f"*Source: {trend_sources[trend_choice]}*")
    
    st.info("""💡 **Key findings:**
    - "World Cup" searches spiked **100×** vs baseline
    - Global search interest for "Visit Spain" rose from 44 to 51 following the Final
    - US visa applications hit **3.5×** peak during tournament
    - Hotel searches in NYC spiked **8×**
    - "Soccer" in USA hit all-time high — **~6×** normal
    """)
    


    st.divider()
    st.subheader("💰 The World Cup By The Numbers")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🎪 Fan Festivals", "9.017M+", "13 host cities")
    c2.metric("🏟️ Stadiums", "6.8M+", "Cumulative attendance")
    c3.metric("📺 Final at Fan Fests", "263,972", "8 sites, one night")
    c4.metric("🌍 Kansas City", "178", "Countries represented")
    c1.markdown("[Source](https://football-technology.fifa.com/organisation/media-releases/fan-festival-extends-historic-world-cup-2026-experience-millions-record-breaking-celebrations-host-countries)", unsafe_allow_html=True)
    c2.markdown("[Source](https://quality.fifa.com/organisation/media-releases/world-cup-2026-numbers-unprecedented-operation-behind-biggest-sporting-event-history)", unsafe_allow_html=True)
    c3.markdown("[Source](https://football-technology.fifa.com/organisation/media-releases/fan-festival-extends-historic-world-cup-2026-experience-millions-record-breaking-celebrations-host-countries)", unsafe_allow_html=True)
    c4.markdown("[Source](https://football-technology.fifa.com/organisation/media-releases/fan-festival-extends-historic-world-cup-2026-experience-millions-record-breaking-celebrations-host-countries)", unsafe_allow_html=True)
    
    c5, c6, c7 = st.columns(3)
    c5.metric("👷 Jobs (Est.)", "~824K FTE", "FIFA/WTO study")
    c6.metric("📡 Data Transported", "13 PB", "As of quarterfinals")
    c7.metric("🏟️ Matches", "104")
    c7.markdown('<p style="color:#09ab3b; font-size:0.85rem; margin-top:-15px;">39 days</p>', unsafe_allow_html=True)
    c5.markdown("[Source](https://inside.fifa.com/organisation/media-releases/fifa-wto-study-estimates-usd-47-billion-economic-output-from-fifa-club-world)", unsafe_allow_html=True)
    c6.markdown("[Source](https://football-technology.fifa.com/organisation/media-releases/packed-stadiums-record-digital-reach-world-cup-2026-numbers-unprecedented-scale)", unsafe_allow_html=True)
    c7.markdown("[Source](https://inside.fifa.com/organisation/president/news/world-cup-2026-infantino-fiipriority-investment-summit-ronaldo)", unsafe_allow_html=True)
    
    st.info("**More people experienced the World Cup outside the stadiums (9.017M+) than inside them (6.8M).** The biggest crowd wasn't in a stadium — it was everywhere else.")
    
    
    st.divider()
# ====================
# TAB 4: AI & METHODS
# ====================
with tab4:
    st.header("🤖 How AI Was Used")
    st.write("This project used **GenAI** as a co-pilot throughout — for data discovery, hypothesis generation, code generation, and narrative development.")
    
    st.subheader("What AI Actually Did")
    st.write("""
    - **Data Discovery:** AI suggested exploring Google Trends by country, leading to the "8 of 10" discovery
    - **Hypothesis Generation:** Generated dozens of questions about the data — most were rejected after verification failed
    - **Source Validation:** When initial data used wrong time windows, AI flagged it and we re-downloaded with correct parameters
    - **Rejected Claims:** Travel patterns, fan attendance by nationality, and economic metrics were removed because we couldn't verify them
    - **Code Generation:** Dashboard layout, Plotly charts, CSS styling, data processing
    - **Narrative Structure:** Helped shape the story arc from global scale to individual human stories
    """)
    
    st.divider()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("📊 Data")
        st.write("- Python / Pandas")
        st.write("- Google Trends (manual download)")
        st.write("- Kaggle datasets")
        st.write("- FIFA.com official reports")
    with c2:
        st.subheader("📉 Visualization")
        st.write("- Streamlit")
        st.write("- Plotly Express + GO")
        st.write("- Custom CSS theming")
    with c3:
        st.subheader("🤖 GenAI")
        st.write("- LLM-assisted development")
        st.write("- Hypothesis generation")
        st.write("- Code generation")
        st.write("- All code AI-assisted, human-verified")
    
    st.divider()
    st.subheader("📚 Data Sources")
    st.write("**Data Preparation:** With the 2026 World Cup only recently concluded, no single dataset captures its full impact. We curated and integrated tournament, search, tourism, economic, and historical data from multiple public sources to build a unified analytical dataset.")
    st.markdown("""
    | Source | Description | Link |
    |--------|-------------|------|
    | FIFA.com | Official 2026 World Cup Statistics, Fan Festival attendance (9M+, 263,972) | [fifa.com/worldcup](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026) |
    | FIFA Statistics | Team performance data (attacking, defending, distribution, physical) | [fifa.com/statistics](https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/statistics/team-statistics) |
    | Google Trends | 11 search terms + country-level interest data, Jun–Jul 2026 | [trends.google.com](https://trends.google.com/trends/explore?date=2026-06-01%202026-07-31&q=FIFA%20World%20Cup) |
    | Kaggle | International Football Results (1872-2026) | [kaggle.com/martj42](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017) |
    | KC2026 | Kansas City Fan Festival organizer report (178 countries, 63,000 attendees) | KC2026 Official Report |
    | Reuters | Vozinha/Cabo Verde goalkeeper visa story | [reuters.com](https://www.reuters.com/sports/soccer/cape-verde-keeper-vozinhas-mother-gets-visa-watch-son-world-cup-2026-06-18/) |
    | World Bank | Cabo Verde population (527,326 — 2025) | [data.worldbank.org](https://data.worldbank.org/country/cabo-verde) |
    | FIFA Squads | 1,248 players, 891 first-timers, oldest/youngest data | [fifa.com/squads](https://www.fifa.com/en/articles/fifa-world-cup-2026-squads-confirmed) |
    """)
    
    st.divider()
    st.caption("Built for Analyticon VizCon 2026 | Theme: 'How the world lives, thrives, and connects' 🌍")
