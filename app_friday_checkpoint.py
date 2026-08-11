import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(page_title="The Night the World Held Its Breath", page_icon="&#9917;", layout="wide", initial_sidebar_state="collapsed")

# Colors
NAVY = "#1B2A4A"
GOLD = "#D4AF37"
DARK = "#0F1419"
CREAM = "#FAF3E8"

# Background images (Unsplash - free to use)
BG_HERO = "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a6?w=1920&q=80"  # crowd with hands up, lights, night atmosphere
BG_METRICS = "https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=1920&q=80"  # stadium floodlights at night
BG_STORY = "https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=1920&q=80"  # fans watching together
BG_TEAMS = "https://images.unsplash.com/photo-1551958219-acbc608c6377?w=1920&q=80"  # football pitch
BG_IMPACT = "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=1920&q=80"  # city skyline night
BG_AI = "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=1920&q=80"  # abstract tech

# Full CSS override - dark cinematic theme
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600&display=swap');
    
    /* Hide Streamlit chrome */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    .stDeployButton {{display: none;}}
    header {{visibility: hidden;}}
    
    /* Dark base */
    .stApp {{
        background-color: {DARK};
        color: #E8E8E8;
    }}
    
    /* All text white */
    .stApp p, .stApp li, .stApp span {{
        color: #E8E8E8 !important;
    }}
    .stApp h1, .stApp h2, .stApp h3 {{
        color: {GOLD} !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
    }}
    
    /* Remove default padding */
    .block-container {{
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        max-width: 100% !important;
    }}
    
    /* Section with background image */
    .cinematic-section {{
        position: relative;
        padding: 80px 60px;
        margin: 0 -60px;
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .cinematic-section::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(15, 20, 25, 0.55);
    }}
    .cinematic-section > * {{
        position: relative;
        z-index: 1;
    }}
    
    /* Hero section */
    .hero-section {{
        background-image: url('{BG_HERO}');
        background-size: cover;
        background-position: center;
        padding: 80px 40px;
        text-align: center;
        position: relative;
        margin: -1rem -1rem 0 -1rem;
    }}
    .hero-section::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(180deg, rgba(15,20,25,0.45) 0%, rgba(15,20,25,0.65) 100%);
    }}
    .hero-title {{
        font-family: 'Bebas Neue', sans-serif;
        font-size: 9rem;
        color: white;
        margin: 0;
        line-height: 0.95;
        letter-spacing: 6px;
        position: relative;
        z-index: 1;
        text-shadow: 0 4px 30px rgba(0,0,0,0.7);
    }}
    .hero-subtitle {{
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        color: {GOLD};
        margin-top: 20px;
        position: relative;
        z-index: 1;
        font-weight: 300;
    }}
    .hero-detail {{
        font-family: 'Inter', sans-serif;
        font-size: 0.85rem;
        color: rgba(255,255,255,0.5);
        margin-top: 25px;
        position: relative;
        z-index: 1;
    }}
    
    /* Metrics bar */
    .metrics-section {{
        background-image: url('{BG_METRICS}');
        background-size: cover;
        background-position: center;
        padding: 60px 40px;
        position: relative;
        margin: 0 -1rem;
    }}
    .metrics-section::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(15, 20, 25, 0.55);
    }}
    .metric-card {{
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(212,175,55,0.3);
        border-radius: 12px;
        padding: 30px 20px;
        text-align: center;
        position: relative;
        z-index: 1;
    }}
    .metric-number {{
        font-family: 'Bebas Neue', sans-serif;
        font-size: 3.5rem;
        color: {GOLD};
        line-height: 1;
    }}
    .metric-label {{
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
        color: rgba(255,255,255,0.7);
        margin-top: 8px;
    }}
    .metric-sub {{
        font-family: 'Inter', sans-serif;
        font-size: 0.75rem;
        color: rgba(212,175,55,0.6);
        margin-top: 4px;
    }}
    
    /* Story sections with backgrounds */
    .story-section {{
        background-image: url('{BG_STORY}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        padding: 80px 40px;
        position: relative;
        margin: 0 -1rem;
    }}
    .story-section::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(15, 20, 25, 0.80);
    }}
    
    .teams-section {{
        background-image: url('{BG_TEAMS}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        padding: 80px 40px;
        position: relative;
        margin: 0 -1rem;
    }}
    .teams-section::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(15, 20, 25, 0.55);
    }}
    
    .impact-section {{
        background-image: url('{BG_IMPACT}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        padding: 80px 40px;
        position: relative;
        margin: 0 -1rem;
    }}
    .impact-section::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(15, 20, 25, 0.55);
    }}
    
    .ai-section {{
        background-image: url('{BG_AI}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        padding: 80px 40px;
        position: relative;
        margin: 0 -1rem;
    }}
    .ai-section::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(15, 20, 25, 0.55);
    }}
    
    /* Pull quote */
    .pull-quote {{
        font-family: 'Inter', sans-serif;
        font-size: 1.5rem;
        color: white;
        line-height: 2.2;
        text-align: center;
        padding: 40px 60px;
        font-weight: 400;
        font-style: italic;
        text-shadow: 0 2px 10px rgba(0,0,0,0.5);
    }}
    
    /* Glass card for content blocks */
    .glass-card {{
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(212,175,55,0.4);
        border-radius: 12px;
        padding: 25px;
        margin: 15px 0;
    }}
    
    /* Section divider */
    .section-gap {{
        height: 60px;
        background: {DARK};
    }}
    
    /* Plotly charts dark bg */
    .stPlotlyChart {{
        background: transparent !important;
    }}
    
    /* Selectbox styling */
    .stSelectbox label {{
        color: {GOLD} !important;
    }}
</style>
""", unsafe_allow_html=True)

# ====================
# DATA
# ====================
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

# Load local images as base64 for reliable rendering
import base64
def get_base64_image(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

fans_b64 = get_base64_image(os.path.join(os.path.dirname(__file__), 'assets', 'fans_celebrating.png'))
stadium_b64 = get_base64_image(os.path.join(os.path.dirname(__file__), 'assets', 'football_stadium_night.jpg'))

# ====================
# SECTION 1: HERO
# ====================
st.markdown(f"""
<div class="hero-section">
    <h1 style="font-family:'Bebas Neue',sans-serif !important; font-size:clamp(4rem, 12vw, 10rem) !important; color:white !important; margin:0 !important; line-height:0.95 !important; letter-spacing:6px; text-shadow:0 4px 30px rgba(0,0,0,0.7); position:relative; z-index:1;">THE NIGHT THE WORLD<br>HELD ITS BREATH</h1>
    <p class="hero-subtitle">How the 2026 FIFA World Cup proved that billions of strangers share one heartbeat</p>
    <p class="hero-detail">Spain 1&ndash;0 Argentina &#183; MetLife Stadium, NJ &#183; July 19, 2026 &#183; 106th minute</p>
</div>
""", unsafe_allow_html=True)

# ====================
# SECTION 2: KEY METRICS
# ====================
st.markdown(f"""
<div style="background-image:url('data:image/jpeg;base64,{stadium_b64}'); background-size:cover; background-position:center; padding:60px 40px; position:relative; margin:0 -1rem;">
    <div style="position:absolute; top:0; left:0; right:0; bottom:0; background:rgba(15,20,25,0.70);"></div>
    <div style="position:relative; z-index:1; text-align:center; max-width:800px; margin:0 auto; padding:20px 0;">
        <div style="display:flex; justify-content:space-around; align-items:flex-start;">
            <div style="flex:1; padding:0 15px;">
                <div style="font-family:'Bebas Neue',sans-serif; font-size:5.5rem; color:{GOLD}; line-height:1;">48</div>
                <div style="font-family:'Inter',sans-serif; font-size:1rem; color:rgba(255,255,255,0.85); font-weight:300; margin-top:8px;">Nations entered.</div>
            </div>
            <div style="flex:1; padding:0 15px;">
                <div style="font-family:'Bebas Neue',sans-serif; font-size:5.5rem; color:{GOLD}; line-height:1;">16</div>
                <div style="font-family:'Inter',sans-serif; font-size:1rem; color:rgba(255,255,255,0.85); font-weight:300; margin-top:8px;">Cities hosted.</div>
            </div>
            <div style="flex:1; padding:0 15px;">
                <div style="font-family:'Bebas Neue',sans-serif; font-size:5.5rem; color:{GOLD}; line-height:1;">3</div>
                <div style="font-family:'Inter',sans-serif; font-size:1rem; color:rgba(255,255,255,0.85); font-weight:300; margin-top:8px;">Countries welcomed<br>the world.</div>
            </div>
            <div style="flex:1; padding:0 15px;">
                <div style="font-family:'Bebas Neue',sans-serif; font-size:6.5rem; color:{GOLD}; line-height:1;">1</div>
                <div style="font-family:'Inter',sans-serif; font-size:1.1rem; color:{GOLD}; font-weight:500; margin-top:8px;">Planet watched<br>together.</div>
            </div>
        </div>
        <div style="margin-top:40px;">
            <p style="font-family:'Bebas Neue',sans-serif; font-size:2rem; color:{GOLD}; letter-spacing:4px; margin:0;">ONE PLANET. ONE MOMENT.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ====================
# SECTION 3: THE STORY
# ====================
st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="story-section">
    <div style="position:relative; z-index:1; max-width:900px; margin:0 auto;">
        <h1 style="font-family:'Bebas Neue',sans-serif; font-size:3rem; color:{GOLD}; text-align:center; letter-spacing:3px;">THE WORLD SHOWS UP</h1>
        <p class="pull-quote">
            On July 19, 2026, 1.5 billion people watched the final.<br>
            Most had no connection to either team.<br><br>
            In Bangalore, a software engineer in a Messi jersey consoled a stranger.<br>
            In Lagos, a taxi driver pulled over.<br>
            In Tokyo, an office erupted at 4 AM.<br><br>
            <span style="color:{GOLD};">The World Cup isn&#39;t just sport.<br>
            It&#39;s one of the rare moments when billions experience the same story at the same time.</span>
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ====================
# SECTION 3: THE DISCOVERY
# ====================
st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)

# Load and process data
import numpy as np
gtrends_raw = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'gtrends_wc_by_country.csv'), skiprows=2)
gtrends_raw.columns = ['Country', 'Interest']
gtrends_raw['Interest'] = pd.to_numeric(gtrends_raw['Interest'], errors='coerce')
gtrends_data = gtrends_raw.dropna(subset=['Interest']).sort_values('Interest', ascending=False).reset_index(drop=True)

matches_df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', 'results.csv'))
wc_2026 = matches_df[(matches_df['date'].str.startswith('2026-0')) & (matches_df['tournament'] == 'FIFA World Cup')]
participants = set(wc_2026['home_team'].tolist() + wc_2026['away_team'].tolist())

gtrends_to_fifa = {'United Kingdom': ['England', 'Scotland'], 'Turkiye': ['Turkey'], 'Czechia': ['Czech Republic'], 'South Korea': ['South Korea']}

def is_participant(country):
    if country in participants:
        return True
    if country in gtrends_to_fifa:
        for fifa_name in gtrends_to_fifa[country]:
            if fifa_name in participants:
                return True
    return False

gtrends_data['Participated'] = gtrends_data['Country'].apply(is_participant)
top10 = gtrends_data.head(10)
non_participant_count = top10[~top10['Participated']].shape[0]
discovery_num = str(non_participant_count)

# Build ranking rows HTML
ranking_rows = ''
for idx, row in top10.iterrows():
    rank = idx + 1
    country = row['Country'].upper()
    score = int(row['Interest'])
    participated = row['Participated']
    bar_width = score
    if participated:
        rank_color = 'rgba(255,255,255,0.4)'
        name_color = 'rgba(255,255,255,0.5)'
        bar_bg = f'linear-gradient(90deg, rgba(80,80,90,0.6) 0%, rgba(60,60,70,0.3) {bar_width}%, transparent {bar_width}%)'
        label = 'ON THE PITCH'
        label_color = 'rgba(255,255,255,0.35)'
        score_color = 'rgba(255,255,255,0.5)'
    else:
        rank_color = GOLD
        name_color = 'white'
        bar_bg = f'linear-gradient(90deg, rgba(212,175,55,0.5) 0%, rgba(180,140,30,0.2) {bar_width}%, transparent {bar_width}%)'
        label = 'OUTSIDE THE 48'
        label_color = GOLD
        score_color = GOLD
    ranking_rows += f'<div style="background:{bar_bg}; padding:10px 15px; margin:3px 0; border-radius:3px; display:flex; align-items:center; justify-content:space-between;"><div style="display:flex; align-items:center; gap:18px;"><span style="font-family:Inter,sans-serif; font-size:0.85rem; color:{rank_color}; font-weight:600; width:28px;">{rank:02d}</span><span style="font-family:Inter,sans-serif; font-size:0.95rem; color:{name_color}; font-weight:500; letter-spacing:0.5px;">{country}</span></div><div style="display:flex; align-items:center; gap:20px;"><span style="font-family:Inter,sans-serif; font-size:0.7rem; color:{label_color}; letter-spacing:1.5px;">{label}</span><span style="font-family:Inter,sans-serif; font-size:1.1rem; color:{score_color}; font-weight:600; width:40px; text-align:right;">{score}</span></div></div>'

# Full section HTML
section_html = f'''
<div style="background-image:url('data:image/jpeg;base64,{stadium_b64}'); background-size:cover; background-position:top center; position:relative; padding:50px 40px 40px; margin:0 -1rem; border-radius:8px;">
    <div style="position:absolute; top:0; left:0; right:0; bottom:0; background:linear-gradient(180deg, rgba(15,20,25,0.5) 0%, rgba(15,20,25,0.92) 30%, rgba(15,20,25,0.97) 100%); border-radius:8px;"></div>
    <div style="position:relative; z-index:1; max-width:850px; margin:0 auto;">
        <div style="text-align:center; margin-bottom:8px;">
            <p style="font-family:Inter,sans-serif; font-size:0.85rem; color:rgba(255,255,255,0.4); letter-spacing:4px; font-weight:300; margin:0;"><span style="color:{GOLD};">48</span> NATIONS COMPETED.</p>
        </div>
        <div style="text-align:center; margin-bottom:15px;">
            <p style="font-family:Inter,sans-serif; font-size:clamp(1.6rem, 3.2vw, 2.4rem); color:white; letter-spacing:1px; line-height:1.3; font-weight:300; margin:0;">But the World Cup<br>didn&#39;t stop at <span style="color:{GOLD}; font-weight:600;">48.</span></p>
        </div>
        <div style="text-align:center; margin-bottom:10px;">
            <p style="font-family:Bebas Neue,sans-serif; font-size:clamp(3.5rem, 8vw, 6rem); line-height:0.9; margin:0; letter-spacing:-1px;"><span style="color:{GOLD};">{discovery_num}</span><span style="color:rgba(255,255,255,0.45);"> / 10</span></p>
        </div>
        <div style="text-align:center; margin-bottom:25px;">
            <p style="font-family:Inter,sans-serif; font-size:1.05rem; color:rgba(255,255,255,0.7); line-height:1.9; margin:0; font-weight:300;">of the top 10 reported geographies<br>by relative FIFA World Cup search interest<br><span style="color:{GOLD}; font-weight:500;">weren&#39;t competing.</span></p>
        </div>
        <div style="margin-bottom:35px;">{ranking_rows}</div>
        <div style="text-align:center; padding:25px 0;">
            <p style="font-family:Inter,sans-serif; font-size:clamp(1.1rem, 2vw, 1.4rem); color:rgba(255,255,255,0.8); letter-spacing:0.5px; line-height:2; font-weight:300; font-style:italic; margin:0;">They weren&#39;t on the pitch.<br>But they were <span style="color:{GOLD}; font-weight:500;">part of the moment.</span></p>
        </div>
        <div style="border-top:1px solid rgba(255,255,255,0.1); padding-top:15px; margin-top:10px;">
            <p style="font-family:Inter,sans-serif; font-size:0.65rem; color:rgba(255,255,255,0.3); text-align:center; margin:0;">Google Trends &middot; FIFA World Cup &middot; Worldwide &middot; Jun 1&ndash;Jul 31, 2026<br>Google Trends values represent normalized relative search interest within each geography, not absolute search volume. Some geographies may have insufficient/unreported Trends data.</p>
        </div>
    </div>
</div>
'''
st.markdown(section_html, unsafe_allow_html=True)

# Expandable methodology
st.markdown("""
<details style="color:rgba(255,255,255,0.3); font-size:0.7rem; text-align:center; margin:10px auto; max-width:600px;">
    <summary style="cursor:pointer; color:rgba(255,255,255,0.4);">HOW THIS WAS CALCULATED</summary>
    <p style="line-height:1.8; margin-top:10px; text-align:left; padding:0 20px;">
        Query: &quot;FIFA World Cup&quot;<br>
        Geography: Worldwide<br>
        Period: June 1 &ndash; July 31, 2026<br>
        Source: Google Trends &quot;Interest by Region&quot; (country-level)<br><br>
        Joined with the official FIFA 2026 World Cup participant list (48 nations) derived from match records.<br><br>
        Country name normalization: United Kingdom mapped to England/Scotland (both participated).
        T&uuml;rkiye mapped to Turkey. Czechia mapped to Czech Republic.<br><br>
        Result: 8 of the top 10 reported geographies by normalized relative search interest were classified as non-participants in the 2026 FIFA World Cup.<br><br>
        The normalized index is NOT search volume. A value of 100 means the highest relative concentration of searches for this term within that geography during the specified period.
    </p>
</details>
""", unsafe_allow_html=True)

# ====================
# ====================
# ════════════════════════════════════════════════════════════
# CHAPTER 3: THE WORLD CAME WITHOUT A TICKET
# ════════════════════════════════════════════════════════════
st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)

# --- Hero: 9M vs 6.8M side by side with glass panels ---
ch3_hero = '<div style="text-align:center; padding:30px 20px 15px;"><p style="font-family:Inter,sans-serif; font-size:0.75rem; color:rgba(255,255,255,0.4); letter-spacing:3px;">CHAPTER 3</p><p style="font-family:Bebas Neue,sans-serif; font-size:clamp(2.5rem, 5vw, 4rem); color:white; letter-spacing:3px; margin-top:5px;">THE WORLD CAME WITHOUT A TICKET</p></div>'
st.markdown(ch3_hero, unsafe_allow_html=True)

# Side-by-side glass panels
col3a, col3b, col3c = st.columns([2, 1, 2])
with col3a:
    st.markdown('<div style="padding:25px; border:1px solid rgba(212,175,55,0.4); border-radius:12px; background:rgba(212,175,55,0.05); text-align:center;"><p style="font-family:Bebas Neue,sans-serif; font-size:3.5rem; color:' + GOLD + '; margin:0;">9.0M+</p><p style="font-family:Inter,sans-serif; font-size:0.75rem; color:rgba(212,175,55,0.7); letter-spacing:1.5px; margin-top:5px;">FAN FESTIVALS</p><p style="font-family:Inter,sans-serif; font-size:0.8rem; color:rgba(255,255,255,0.5); margin-top:8px;">outside the stadiums</p></div>', unsafe_allow_html=True)
with col3b:
    st.markdown('<div style="text-align:center; padding-top:40px;"><p style="font-family:Inter,sans-serif; font-size:1.2rem; color:rgba(255,255,255,0.25);">vs.</p></div>', unsafe_allow_html=True)
with col3c:
    st.markdown('<div style="padding:25px; border:1px solid rgba(255,255,255,0.15); border-radius:12px; background:rgba(255,255,255,0.02); text-align:center;"><p style="font-family:Bebas Neue,sans-serif; font-size:3.5rem; color:rgba(255,255,255,0.5); margin:0;">6.8M</p><p style="font-family:Inter,sans-serif; font-size:0.75rem; color:rgba(255,255,255,0.35); letter-spacing:1.5px; margin-top:5px;">STADIUMS</p><p style="font-family:Inter,sans-serif; font-size:0.8rem; color:rgba(255,255,255,0.4); margin-top:8px;">inside the gates</p></div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:center; padding:15px 0;"><p style="font-family:Inter,sans-serif; font-size:1rem; color:rgba(255,255,255,0.7); font-weight:300;">More people experienced the World Cup outside the stadiums than inside them.</p></div>', unsafe_allow_html=True)

# --- 263,972 + Fan Festival map side by side ---
col3d, col3e = st.columns([3, 2])
with col3d:
    # Map
    festival_sites = {'Mexico City': (19.43, -99.13), 'Guadalajara': (20.67, -103.35), 'Toronto': (43.65, -79.38), 'Houston': (29.76, -95.37), 'Miami': (25.76, -80.19), 'Philadelphia': (39.95, -75.17), 'Los Angeles': (34.05, -118.24), 'Dallas': (32.78, -96.80)}
    fig_map = go.Figure()
    fig_map.add_trace(go.Scattergeo(lon=[c[1] for c in festival_sites.values()], lat=[c[0] for c in festival_sites.values()], mode='markers+text', marker=dict(size=10, color=GOLD, opacity=0.9, line=dict(width=1, color='white')), text=list(festival_sites.keys()), textposition='top center', textfont=dict(size=7, color='rgba(255,255,255,0.6)'), showlegend=False, hoverinfo='text', hovertext=list(festival_sites.keys())))
    fig_map.add_trace(go.Scattergeo(lon=[c[1] for c in festival_sites.values()], lat=[c[0] for c in festival_sites.values()], mode='markers', marker=dict(size=22, color=GOLD, opacity=0.08), showlegend=False, hoverinfo='skip'))
    fig_map.update_geos(showframe=False, showcoastlines=True, coastlinecolor='rgba(255,255,255,0.08)', showland=True, landcolor='rgba(20,25,30,1)', showocean=True, oceancolor='rgba(12,16,20,1)', showlakes=False, showcountries=True, countrycolor='rgba(255,255,255,0.04)', projection_type='natural earth', bgcolor='rgba(0,0,0,0)', lataxis=dict(range=[12, 52]), lonaxis=dict(range=[-125, -65]))
    fig_map.update_layout(height=220, margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', showlegend=False)
    st.plotly_chart(fig_map, use_container_width=True, config={'displayModeBar': False})
with col3e:
    st.markdown('<div style="padding:20px; border:1px solid rgba(212,175,55,0.3); border-radius:12px; background:rgba(212,175,55,0.03); text-align:center;"><p style="font-family:Inter,sans-serif; font-size:0.7rem; color:rgba(255,255,255,0.35); letter-spacing:2px;">FAN FESTIVALS. EVERYWHERE.</p><p style="font-family:Bebas Neue,sans-serif; font-size:2.8rem; color:' + GOLD + '; margin:10px 0 5px;">263,972</p><p style="font-family:Inter,sans-serif; font-size:0.75rem; color:rgba(255,255,255,0.5);">watched the final across eight sites</p><p style="font-family:Inter,sans-serif; font-size:0.85rem; color:rgba(255,255,255,0.4); margin-top:12px; line-height:1.6; font-weight:300;">They didn&#39;t have a ticket.<br><span style="color:white; font-weight:400;">They had <span style="color:' + GOLD + ';">each other.</span></span></p></div>', unsafe_allow_html=True)

# --- Kansas City bar ---
st.markdown('<div style="text-align:center; padding:15px 20px; margin:15px 0; border-radius:8px; background:linear-gradient(90deg, rgba(212,175,55,0.1) 0%, rgba(212,175,55,0.03) 100%); border:1px solid rgba(212,175,55,0.2);"><p style="font-family:Inter,sans-serif; font-size:1.1rem; color:white; margin:0;"><span style="color:' + GOLD + '; font-weight:500;">178 COUNTRIES</span> <span style="color:rgba(255,255,255,0.3);">&rarr;</span> <span style="font-weight:400;">KANSAS CITY</span> <span style="color:rgba(255,255,255,0.3);">&middot;</span> <span style="color:rgba(255,255,255,0.5); font-size:0.85rem;">63,000 attendees &middot; first five festival days</span></p></div>', unsafe_allow_html=True)

# --- Strangers Become Family: TEXT LEFT + PHOTO RIGHT ---
col3f, col3g = st.columns([2, 3])
with col3f:
    st.markdown('<div style="padding:20px 10px;"><p style="font-family:Bebas Neue,sans-serif; font-size:2.2rem; color:white; letter-spacing:2px; line-height:1.2;">STRANGERS<br>BECOME FAMILY</p><p style="font-family:Inter,sans-serif; font-size:0.9rem; color:rgba(255,255,255,0.5); line-height:1.8; margin-top:15px; font-weight:300;">For most of the year,<br>these people would have been strangers.<br><br>Different countries.<br>Different languages.<br>Different shirts.</p><p style="font-family:Inter,sans-serif; font-size:0.85rem; color:' + GOLD + '; margin-top:15px; font-style:italic;">Then someone scored.</p><p style="font-family:Bebas Neue,sans-serif; font-size:1.8rem; color:white; margin-top:10px;">AND SUDDENLY<br>THEY WERE <span style="color:' + GOLD + ';">HUGGING.</span></p></div>', unsafe_allow_html=True)
with col3g:
    _fans_img = get_base64_image(os.path.join(os.path.dirname(__file__), 'assets', 'fans_compressed.jpg'))
    if _fans_img:
        st.markdown('<div style="background-image:url(data:image/jpeg;base64,' + _fans_img + '); background-size:cover; background-position:center; height:320px; border-radius:12px; border:1px solid rgba(212,175,55,0.2);"></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="height:320px; border-radius:12px; background:linear-gradient(135deg, rgba(30,40,55,1), rgba(20,25,35,1)); border:1px solid rgba(212,175,55,0.2);"></div>', unsafe_allow_html=True)

# Transition
st.markdown('<div style="text-align:center; padding:25px 20px 10px;"><p style="font-family:Inter,sans-serif; font-size:0.9rem; color:rgba(255,255,255,0.4); font-style:italic;">9 million came to watch. 1,248 came to play. For most, it was the first time.</p></div>', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════
# CHAPTER 4: FOR SOME, THE FIRST. FOR SOME, THE LAST.
# ════════════════════════════════════════════════════════════
st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)

ch4_head = '<div style="padding:20px 20px 10px;"><p style="font-family:Inter,sans-serif; font-size:0.75rem; color:rgba(255,255,255,0.4); letter-spacing:3px;">CHAPTER 4</p><p style="font-family:Bebas Neue,sans-serif; font-size:clamp(2rem, 4vw, 3.2rem); color:white; letter-spacing:2px; margin-top:5px; line-height:1.2;">FOR SOME, THE FIRST.<br>FOR SOME, THE LAST.<br>FOR SOME, <span style="color:' + GOLD + ';">EVERYTHING.</span></p></div>'
st.markdown(ch4_head, unsafe_allow_html=True)

# --- 891 / 71% / 357 data strip ---
st.markdown('<div style="display:flex; align-items:center; justify-content:center; gap:15px; padding:15px 20px; margin:10px 0; flex-wrap:wrap;"><div style="text-align:center;"><span style="font-family:Bebas Neue,sans-serif; font-size:2rem; color:' + GOLD + ';">891</span><span style="font-family:Inter,sans-serif; font-size:0.7rem; color:rgba(255,255,255,0.4); margin-left:5px;">FIRST-TIMERS</span></div><div style="padding:8px 15px; border:1px solid rgba(212,175,55,0.3); border-radius:8px; background:rgba(212,175,55,0.05);"><span style="font-family:Bebas Neue,sans-serif; font-size:2rem; color:' + GOLD + ';">71%</span><span style="font-family:Inter,sans-serif; font-size:0.7rem; color:rgba(255,255,255,0.5); margin-left:5px;">experiencing a World Cup for the first time</span></div><div style="text-align:center;"><span style="font-family:Bebas Neue,sans-serif; font-size:2rem; color:rgba(255,255,255,0.4);">357</span><span style="font-family:Inter,sans-serif; font-size:0.7rem; color:rgba(255,255,255,0.3); margin-left:5px;">RETURNING</span></div></div>', unsafe_allow_html=True)

# --- Player timeline with circular placeholders ---
# Age markers as a visual row
players_html = '<div style="display:flex; justify-content:space-between; align-items:flex-end; padding:20px 10px; margin:10px 0; border-bottom:2px solid rgba(212,175,55,0.2); position:relative;">'

player_data = [
    ('GM', 'MORA', '17', 'Youngest player', 'rgba(255,255,255,0.3)', 'rgba(255,255,255,0.5)'),
    ('LY', 'YAMAL', '18', 'WORLD CHAMPION', GOLD, 'white'),
    ('LM', 'MESSI', '39', 'SIX WORLD CUPS\nTHREE FINALS', GOLD, 'white'),
    ('VZ', 'VOZINHA', '40', "CABO VERDE'S\nFIRST WORLD CUP", GOLD, 'white'),
    ('CR', 'RONALDO', '41', 'SIX WORLD CUPS', GOLD, 'white'),
    ('CG', 'GORDON', '43', 'Oldest player', 'rgba(255,255,255,0.3)', 'rgba(255,255,255,0.5)'),
]

for initials, name, age, desc, border_color, text_color in player_data:
    desc_lines = desc.replace('\n', '<br>')
    players_html += f'<div style="text-align:center; flex:1;"><div style="width:50px; height:50px; border-radius:50%; border:2px solid {border_color}; display:flex; align-items:center; justify-content:center; margin:0 auto 8px; background:rgba(15,20,25,0.8);"><span style="font-family:Inter,sans-serif; font-size:0.75rem; color:{border_color}; font-weight:600;">{initials}</span></div><p style="font-family:Bebas Neue,sans-serif; font-size:1.3rem; color:{text_color}; margin:0;">{age}</p><p style="font-family:Inter,sans-serif; font-size:0.7rem; color:{border_color}; margin:2px 0; font-weight:500;">{name}</p><p style="font-family:Inter,sans-serif; font-size:0.6rem; color:rgba(255,255,255,0.4); line-height:1.4;">{desc_lines}</p></div>'

players_html += '</div>'
st.markdown(players_html, unsafe_allow_html=True)

# --- Cabo Verde feature panel ---
col4a, col4b = st.columns([3, 2])
with col4a:
    st.markdown('<div style="padding:20px; border:1px solid rgba(212,175,55,0.3); border-radius:12px; background:rgba(212,175,55,0.03);"><p style="font-family:Inter,sans-serif; font-size:0.7rem; color:rgba(255,255,255,0.4); letter-spacing:2px;">CABO VERDE</p><p style="font-family:Bebas Neue,sans-serif; font-size:2.8rem; color:' + GOLD + '; margin:5px 0;">527K</p><p style="font-family:Inter,sans-serif; font-size:0.8rem; color:rgba(255,255,255,0.5); letter-spacing:1px;">PEOPLE. ONE FIRST WORLD CUP.</p><p style="font-family:Inter,sans-serif; font-size:0.85rem; color:rgba(255,255,255,0.55); margin-top:12px; font-weight:300; line-height:1.7;">One of the tournament&#39;s smallest nations had finally reached its biggest stage.</p></div>', unsafe_allow_html=True)
with col4b:
    st.markdown('<div style="padding:20px; border:1px solid rgba(255,255,255,0.1); border-radius:12px; background:rgba(255,255,255,0.02);"><p style="font-family:Inter,sans-serif; font-size:0.85rem; color:rgba(255,255,255,0.5); line-height:2.4; font-weight:300;">Spain &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color:' + GOLD + '; font-weight:500;">0&#8211;0</span><br>Uruguay &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color:' + GOLD + '; font-weight:500;">2&#8211;2</span><br>Argentina &nbsp;&nbsp;&nbsp;&nbsp; <span style="color:rgba(255,255,255,0.4);">2&#8211;3</span></p><p style="font-family:Inter,sans-serif; font-size:0.7rem; color:rgba(255,255,255,0.3); margin-top:5px;">&darr;</p><p style="font-family:Inter,sans-serif; font-size:0.8rem; color:' + GOLD + '; letter-spacing:1px; font-weight:400;">ROUND OF 32</p></div>', unsafe_allow_html=True)

# Closing
st.markdown('<div style="text-align:center; padding:20px;"><p style="font-family:Inter,sans-serif; font-size:1rem; color:rgba(255,255,255,0.6); font-weight:300;">17 years. 43 years. 527,000 people.</p><p style="font-family:Inter,sans-serif; font-size:1.05rem; color:white; margin-top:5px;">Different journeys. <span style="color:' + GOLD + ';">Same dream.</span></p></div>', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════
# CHAPTER 5: STORIES DATA ALONE CAN'T TELL
# ════════════════════════════════════════════════════════════
st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)

ch5_head = '<div style="padding:20px 20px 10px;"><p style="font-family:Inter,sans-serif; font-size:0.75rem; color:rgba(255,255,255,0.4); letter-spacing:3px;">CHAPTER 5</p><p style="font-family:Bebas Neue,sans-serif; font-size:clamp(2rem, 4vw, 3rem); color:white; letter-spacing:2px; margin-top:5px;">STORIES DATA ALONE<br>CAN&#39;T TELL</p></div>'
st.markdown(ch5_head, unsafe_allow_html=True)

# --- 27 shots visual + story side by side ---
col5a, col5b = st.columns([2, 3])
with col5a:
    # 27 shot dots
    shots_html = '<div style="padding:20px; border:1px solid rgba(212,175,55,0.2); border-radius:12px; background:rgba(15,20,25,0.8); text-align:center;"><p style="font-family:Inter,sans-serif; font-size:0.7rem; color:rgba(255,255,255,0.35); letter-spacing:2px; margin-bottom:12px;">VS SPAIN: 27 SHOTS</p><div style="display:flex; flex-wrap:wrap; gap:5px; justify-content:center; max-width:200px; margin:0 auto;">'
    save_positions = [2, 5, 9, 12, 17, 21, 26]
    for i in range(27):
        if i in save_positions:
            shots_html += '<div style="width:16px; height:16px; border-radius:50%; background:' + GOLD + ';"></div>'
        else:
            shots_html += '<div style="width:16px; height:16px; border-radius:50%; background:rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.08);"></div>'
    shots_html += '</div><p style="font-family:Inter,sans-serif; font-size:0.65rem; color:rgba(255,255,255,0.3); margin-top:10px;"><span style="color:' + GOLD + ';">&#9679;</span> SAVED (7) &nbsp; &#9679; ON TARGET</p><p style="font-family:Bebas Neue,sans-serif; font-size:3rem; color:white; margin-top:15px;">0 &#8211; 0</p><p style="font-family:Inter,sans-serif; font-size:0.8rem; color:' + GOLD + ';">SHE WAS RIGHT.</p></div>'
    st.markdown(shots_html, unsafe_allow_html=True)

with col5b:
    st.markdown('<div style="padding:25px; border:1px solid rgba(212,175,55,0.15); border-radius:12px; background:linear-gradient(135deg, rgba(25,30,40,1), rgba(15,20,25,1));"><p style="font-family:Bebas Neue,sans-serif; font-size:1.5rem; color:white; margin-bottom:15px;">SHE SAID NO ONE WOULD SCORE.</p><p style="font-family:Inter,sans-serif; font-size:0.9rem; color:rgba(255,255,255,0.6); line-height:1.9; font-weight:300;">At 40, Vozinha made seven saves to secure a historic 0&#8211;0 draw against Spain. Cabo Verde&#39;s first-ever World Cup match.<br><br>His mother couldn&#39;t attend that game. After his emotional words touched millions, the U.S. Embassy in Praia helped facilitate her visa.<br><br><span style="color:' + GOLD + ';">She made it in time to see her son play.</span></p><p style="font-family:Inter,sans-serif; font-size:0.65rem; color:rgba(255,255,255,0.3); margin-top:15px;">Source: Reuters, June 18, 2026</p></div>', unsafe_allow_html=True)

# --- Final synthesis ---
st.markdown('<div style="max-width:700px; margin:25px auto; padding:30px; border:1px solid rgba(212,175,55,0.3); border-radius:12px; background:rgba(212,175,55,0.03); text-align:center;"><p style="font-family:Inter,sans-serif; font-size:1.1rem; color:white; font-weight:300; line-height:2.2;">The world held its breath.<br><br><span style="color:rgba(255,255,255,0.6);">9 million gathered without a ticket.<br>178 countries shared one city.<br>891 players lived their first dream.<br>One mother saw her son keep his promise.</span><br><br><span style="color:' + GOLD + '; font-weight:400; font-size:1.2rem;">Then it exhaled together.</span></p></div>', unsafe_allow_html=True)

# --- Sources + AI ---
st.markdown('<div style="text-align:center; padding:20px; max-width:600px; margin:0 auto;"><p style="font-family:Inter,sans-serif; font-size:0.6rem; color:rgba(255,255,255,0.25); line-height:1.8;">Sources: FIFA.com &middot; Google Trends &middot; KC2026 &middot; Reuters &middot; World Bank &middot; Kaggle</p></div>', unsafe_allow_html=True)

st.markdown("""<details style="color:rgba(255,255,255,0.3); font-size:0.7rem; text-align:center; margin:5px auto; max-width:600px;"><summary style="cursor:pointer; color:rgba(255,255,255,0.4);">HOW AI WAS USED</summary><p style="line-height:1.8; margin-top:10px; text-align:left; padding:0 20px;">Structured data &rarr; AI-generated hypotheses &rarr; public-web research &rarr; source validation &rarr; rejected unsupported claims &rarr; cross-dataset analysis &rarr; human editorial selection.<br><br>Example: AI surfaced a country-interest pattern in Google Trends. We challenged the first dataset, recreated the export manually, corrected the time window, joined it to FIFA&#39;s participant list, and only then accepted the finding.<br><br>Tools: Streamlit, Plotly, Python, Kiro (Amazon AI agent)</p></details>""", unsafe_allow_html=True)

# Footer
st.markdown('<div style="text-align:center; padding:25px 20px 40px;"><p style="font-family:Inter,sans-serif; font-size:0.65rem; color:rgba(255,255,255,0.2);">Built for Analyticon VizCon 2026 &middot; &quot;How the world lives, thrives, and connects&quot;<br>By Greeshma Joseph &middot; Streamlit + Plotly + Python + Kiro</p></div>', unsafe_allow_html=True)
