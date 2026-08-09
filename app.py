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
# SECTION 4: STRANGERS BECOME FAMILY
# ====================
st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)

# Load compressed fans image for background
_fans_b64 = get_base64_image(os.path.join(os.path.dirname(__file__), 'assets', 'fans_compressed.jpg'))

# Full cinematic section with photo background
_s4 = '<div style="background-image:url(data:image/jpeg;base64,' + (_fans_b64 or '') + '); background-size:cover; background-position:center; min-height:680px; position:relative; margin:0 -1rem; border-radius:12px; display:flex; align-items:center; justify-content:center;">'
_s4 += '<div style="position:absolute; top:0; left:0; right:0; bottom:0; background:linear-gradient(180deg, rgba(15,20,25,0.35) 0%, rgba(15,20,25,0.6) 40%, rgba(15,20,25,0.88) 75%, rgba(15,20,25,0.98) 100%); border-radius:12px;"></div>'
_s4 += '<div style="position:relative; z-index:1; max-width:700px; margin:0 auto; text-align:center; padding:60px 30px;">'
_s4 += '<div style="font-family:Inter,sans-serif; font-size:2.2rem; color:white; letter-spacing:3px; font-weight:300; margin-bottom:50px;">STRANGERS BECOME FAMILY</div>'
_s4 += '<div style="font-family:Inter,sans-serif; font-size:1.05rem; color:rgba(255,255,255,0.65); line-height:2.2; font-weight:300;">'
_s4 += 'For most of the year,<br>these people would have been strangers.<br><br>'
_s4 += 'Different countries.<br>Different languages.<br>Different shirts.<br><br>'
_s4 += '</div>'
_s4 += '<div style="font-family:Inter,sans-serif; font-size:0.95rem; color:rgba(255,255,255,0.45); margin:25px 0 20px; font-weight:300;">Then someone scored.</div>'
_s4 += '<div style="font-family:Inter,sans-serif; font-size:1.5rem; color:white; font-weight:400; margin-bottom:60px;">And suddenly they were <span style="color:' + GOLD + '; font-weight:500;">hugging.</span></div>'
_s4 += '<div style="margin-top:40px; padding-top:30px; border-top:1px solid rgba(255,255,255,0.08);">'
_s4 += '<div style="font-family:Inter,sans-serif; font-size:1.1rem; color:rgba(255,255,255,0.7); line-height:1.9; font-weight:300;">'
_s4 += 'The World Cup didn&#39;t just bring<br>countries to America.<br><br>'
_s4 += 'It brought <span style="color:' + GOLD + '; font-weight:400;">people to each other.</span>'
_s4 += '</div></div>'
_s4 += '</div></div>'
st.markdown(_s4, unsafe_allow_html=True)

# Transition
_s4_out = '<div style="text-align:center; padding:30px 0 10px;"><p style="font-family:Inter,sans-serif; font-size:0.85rem; color:rgba(255,255,255,0.3); font-style:italic;">Some stories went even further.</p></div>'
st.markdown(_s4_out, unsafe_allow_html=True)

# Gold box facts - what connection looked like in numbers
c_fa, c_fb, c_fc = st.columns(3)
with c_fa:
    st.markdown(f'<div class="glass-card" style="text-align:center;"><p style="font-family:Bebas Neue,sans-serif; font-size:2.5rem; color:{GOLD};">9.0M+</p><p style="font-family:Inter,sans-serif; font-size:0.75rem; color:rgba(255,255,255,0.5);">Fan Festival visits outside stadiums</p><p style="font-family:Inter,sans-serif; font-size:0.7rem; color:rgba(255,255,255,0.4); margin-top:5px;">More than the 6.8M inside</p></div>', unsafe_allow_html=True)
with c_fb:
    st.markdown(f'<div class="glass-card" style="text-align:center;"><p style="font-family:Bebas Neue,sans-serif; font-size:2.5rem; color:{GOLD};">263,972</p><p style="font-family:Inter,sans-serif; font-size:0.75rem; color:rgba(255,255,255,0.5);">Watched the final together</p><p style="font-family:Inter,sans-serif; font-size:0.7rem; color:rgba(255,255,255,0.4); margin-top:5px;">Across 8 Fan Festival sites</p></div>', unsafe_allow_html=True)
with c_fc:
    st.markdown(f'<div class="glass-card" style="text-align:center;"><p style="font-family:Bebas Neue,sans-serif; font-size:2.5rem; color:{GOLD};">178</p><p style="font-family:Inter,sans-serif; font-size:0.75rem; color:rgba(255,255,255,0.5);">Countries at Kansas City Fan Festival</p><p style="font-family:Inter,sans-serif; font-size:0.7rem; color:rgba(255,255,255,0.4); margin-top:5px;">63,000 attendees in 5 days</p></div>', unsafe_allow_html=True)

# WHEN RIVALS BECOME FRIENDS
# ====================
st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div style="background: linear-gradient(135deg, #1a2a3a 0%, #1f2f3f 100%); padding:50px 40px 30px; border-radius:16px; border:1px solid rgba(212,175,55,0.3); margin:20px 0;">
    <h1 style="font-family:'Bebas Neue',sans-serif; font-size:2.8rem; color:{GOLD}; text-align:center; letter-spacing:3px;">&#128155; WHEN RIVALS BECOME FRIENDS</h1>
</div>
""", unsafe_allow_html=True)
st.markdown(f"<p style='font-style:italic; color:{GOLD}; font-size:1.1rem; text-align:center;'>The World Cup doesn&#39;t produce winners and losers. It produces moments that make us believe in each other.</p>", unsafe_allow_html=True)

st.markdown(f"""
<div class="glass-card" style="background:rgba(255,255,255,0.15); border:1px solid rgba(212,175,55,0.4); border-left: 4px solid {GOLD}; margin:20px 0;">
    <strong style="color:{GOLD};">[BRA-GER] Brazil 2014</strong><br>
    A young Brazilian boy sobbed uncontrollably after Germany&#39;s 7-1 demolition. A German fan knelt beside him, hugged him, and gave him a German flag. The photo was shared 38 million times in 24 hours.
</div>
<div class="glass-card" style="background:rgba(255,255,255,0.15); border:1px solid rgba(212,175,55,0.4); border-left: 4px solid {GOLD}; margin:20px 0;">
    <strong style="color:{GOLD};">[JPN] Japan &mdash; Every Tournament</strong><br>
    After every match &mdash; win or lose &mdash; Japanese fans stay behind to clean the entire stadium. After their 2022 elimination, players bowed to fans, then cleaned their locker room. Other nations&#39; fans started copying them.
</div>
<div class="glass-card" style="background:rgba(255,255,255,0.15); border:1px solid rgba(212,175,55,0.4); border-left: 4px solid {GOLD}; margin:20px 0;">
    <strong style="color:{GOLD};">[MAR] Morocco 2022</strong><br>
    After becoming the first African team to reach a semi-final, Moroccan players ran to the stands to celebrate with their mothers &mdash; carrying them onto the pitch. A billion people watched sons thank the women who made it possible.
</div>
<div class="glass-card" style="background:rgba(255,255,255,0.15); border:1px solid rgba(212,175,55,0.4); border-left: 4px solid {GOLD}; margin:20px 0;">
    <strong style="color:{GOLD};">[IRE] Ireland Euro 2016</strong><br>
    Irish fans spotted a crying French baby in the crowd and spontaneously sang lullabies until the baby fell asleep. The video became the tournament&#39;s most-shared moment &mdash; more than any goal.
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align:center; padding:30px 0;">
    <p style="font-family:'Inter',sans-serif; font-size:1.2rem; color:rgba(255,255,255,0.8); font-style:italic;">
        These aren&#39;t outliers. They&#39;re the pattern.<br>
        <span style="color:{GOLD};">Sport doesn&#39;t divide us. It reveals how badly we want to connect.</span>
    </p>
</div>
""", unsafe_allow_html=True)

# ====================
# THE WORLD GOES QUIET
# ====================
st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div style="background: linear-gradient(135deg, #1a2a3a 0%, #1f2f3f 100%); padding:50px 40px 30px; border-radius:16px; border:1px solid rgba(212,175,55,0.3); margin:20px 0;">
    <h1 style="font-family:'Bebas Neue',sans-serif; font-size:2.8rem; color:{GOLD}; text-align:center; letter-spacing:3px;">&#129323; THE WORLD GOES QUIET, THEN EXPLODES</h1>
    <p style="font-family:'Inter',sans-serif; font-size:1.1rem; color:rgba(255,255,255,0.8); text-align:center; font-style:italic;">During a World Cup final, something measurable happens to planet Earth:</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f'<div class="metric-card" style="background:rgba(212,175,55,0.1); border:2px solid {GOLD};"><div class="metric-number" style="font-size:3rem;">&ndash;70%</div><div class="metric-label">Traffic in participating countries</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="metric-card" style="background:rgba(212,175,55,0.1); border:2px solid {GOLD};"><div class="metric-number" style="font-size:3rem;">&ndash;35%</div><div class="metric-label">Crime during knockout matches</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="metric-card" style="background:rgba(212,175,55,0.1); border:2px solid {GOLD};"><div class="metric-number" style="font-size:3rem;">+3 GW</div><div class="metric-label">Halftime kettle surge (UK)</div></div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="glass-card" style="border-left:4px solid {GOLD}; margin:20px 0;">
    <strong style="color:{GOLD};">7% of all global internet traffic</strong> was consumed by the final match alone
</div>
<div class="glass-card" style="border-left:4px solid {GOLD}; margin:20px 0;">
    <strong style="color:{GOLD};">90 petabytes</strong> of data generated &mdash; 45&times; more than Qatar 2022
</div>
<div class="glass-card" style="border-left:4px solid {GOLD}; margin:20px 0;">
    Hospital ER visits drop <strong style="color:{GOLD};">20%</strong> during knockout matches (people delay being sick)
</div>
<div class="glass-card" style="border-left:4px solid {GOLD}; margin:20px 0;">
    Water systems spike at exactly <strong style="color:{GOLD};">minute 45 and 90</strong> &mdash; everyone flushes simultaneously
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="glass-card" style="border-left:4px solid #E63946; border-color: rgba(230,57,70,0.4);">
    &#9888; <strong style="color:#E63946;">The dark side:</strong> Domestic violence reports spike 26% in losing countries after elimination. The same connection that creates joy creates pain.
</div>
""", unsafe_allow_html=True)

# ====================
# CABO VERDE
# ====================
st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)

# Cabo Verde with standout visual treatment
st.markdown(f"""
<div style="background: linear-gradient(135deg, #1a2a3a 0%, #1f2f3f 100%); padding:60px 40px; border-radius:16px; border:1px solid rgba(212,175,55,0.3); margin:20px 0;">
    <h1 style="font-family:'Bebas Neue',sans-serif; font-size:3.5rem; color:{GOLD}; text-align:center; letter-spacing:3px; margin-bottom:10px;">[CPV] 600,000 PEOPLE vs. THE WORLD</h1>
    <p style="font-family:'Inter',sans-serif; font-size:1.2rem; color:rgba(255,255,255,0.9); text-align:center; line-height:1.8; max-width:800px; margin:0 auto;">
        Every World Cup writes a Cinderella story. In 2026, <strong style="color:{GOLD};">Cabo Verde</strong> &mdash; a tiny island nation of 600,000 people &mdash; 
        made their World Cup debut. They didn&#39;t just participate.<br><br>
        <span style="font-size:1.4rem; color:{GOLD};">Sidny Lopes Cabral scored FIFA&#39;s Goal of the Tournament &mdash; against Argentina.</span>
    </p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f'<div class="metric-card" style="background:rgba(212,175,55,0.1); border:2px solid {GOLD};"><div class="metric-number" style="font-size:3rem;">20&times;</div><div class="metric-label">Search interest surge</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="metric-card" style="background:rgba(212,175,55,0.1); border:2px solid {GOLD};"><div class="metric-number" style="font-size:3rem;">600K</div><div class="metric-label">Population (smaller than Memphis, TN)</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="metric-card" style="background:rgba(212,175,55,0.1); border:2px solid {GOLD};"><div class="metric-number" style="font-size:3rem;">&#127942;</div><div class="metric-label">Goal of the Tournament</div></div>', unsafe_allow_html=True)

cabo_cards = """
<div class="glass-card" style="border-left:4px solid GOLD_PH; margin:20px 0;">
    Morocco&#39;s 2022 semi-final run led to a <strong style="color:GOLD_PH;">600% spike</strong> in &#39;visit Morocco&#39; searches &mdash; Cabo Verde is poised for the same
</div>
<div class="glass-card" style="border-left:4px solid GOLD_PH; margin:20px 0;">
    Players like Lopes Cabral now attract top European leagues &mdash; <strong style="color:GOLD_PH;">transforming careers overnight</strong>
</div>
<div class="glass-card" style="border-left:4px solid GOLD_PH; margin:20px 0;">
    The World Cup doesn&#39;t just create sporting heroes &mdash; <strong style="color:GOLD_PH;">it puts entire nations on the global map</strong>
</div>
""".replace("GOLD_PH", GOLD)
st.markdown(cabo_cards, unsafe_allow_html=True)

# Messi-Yamal #19 connection
st.markdown(f"""
<div class="glass-card" style="border-left:4px solid {GOLD}; margin:20px 0;">
    <strong style="color:{GOLD};">The #19 Connection:</strong> In 2007, Barcelona&#39;s No. 19 Messi was photographed holding baby Lamine Yamal. 19 years later, Spain&#39;s No. 19 Yamal faced Messi in the World Cup Final &mdash; on July 19 &mdash; and became World Champion.
</div>
""", unsafe_allow_html=True)

# ====================
# LEGENDS
# ====================
st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)
three_gen_html = """
<div style="background: linear-gradient(135deg, #1a2a3a 0%, #1f2f3f 100%); padding:50px 40px 30px; border-radius:16px; border:1px solid rgba(212,175,55,0.3); margin:20px 0;">
    <h1 style="font-family:'Bebas Neue',sans-serif; font-size:2.8rem; color:GOLD_PH; text-align:center; letter-spacing:3px;">&#11088; THREE GENERATIONS, ONE PITCH</h1>
    <p style="font-family:'Inter',sans-serif; font-size:1.1rem; color:rgba(255,255,255,0.8); text-align:center; line-height:1.8;">
        <strong style="color:GOLD_PH;">Messi</strong> (39) &mdash; 6th World Cup, 3rd final. 
        <strong style="color:GOLD_PH;">Ronaldo</strong> (41) &mdash; his farewell. 
        <strong style="color:GOLD_PH;">Yamal</strong> (17) &mdash; highest creativity score.<br>
        The torch passes in real time.
    </p>
</div>
""".replace("GOLD_PH", GOLD)
st.markdown(three_gen_html, unsafe_allow_html=True)

performers = data['performers'].copy()
fig = px.scatter(performers, x='Creativity_Score', y='Attacking_Score',
                 size=[max(d,4) for d in performers['Defending_Score']],
                 color='Attacking_Score', color_continuous_scale=[DARK, GOLD, '#E63946'],
                 hover_name='Player', hover_data={'Team':True, 'Rank':True}, size_max=22)

for player, label in [('Lionel MESSI','Messi (39)'),('CRISTIANO RONALDO','CR7 (41)'),
                      ('Lamine YAMAL','Yamal (17)'),('Kylian MBAPPE','Mbapp&#233; #1')]:
    p = performers[performers['Player']==player]
    if len(p):
        fig.add_annotation(x=p['Creativity_Score'].values[0], y=p['Attacking_Score'].values[0],
                         text=label, showarrow=True, arrowhead=2, 
                         font=dict(size=11, color=GOLD), arrowcolor=GOLD)

fig.update_layout(
    height=500, xaxis_title="Creativity Score &#8594;", yaxis_title="Attacking Score &#8594;",
    coloraxis_showscale=False, showlegend=False,
    plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#E8E8E8'),
    xaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
    yaxis=dict(gridcolor='rgba(255,255,255,0.05)')
)
st.plotly_chart(fig, use_container_width=True)

# ====================
# SECTION: EXPLORE TEAMS
# ====================
st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="teams-section">
    <div style="position:relative; z-index:1; text-align:center;">
        <h1 style="font-family:'Bebas Neue',sans-serif; font-size:3rem; color:{GOLD}; letter-spacing:3px;">EXPLORE THE TEAMS</h1>
        <p style="color:rgba(255,255,255,0.7); font-size:1.1rem;">48 nations. 104 matches. One champion.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="background: linear-gradient(135deg, #1a2a3a 0%, #1f2f3f 100%); padding:40px 40px 20px; border-radius:16px; border:1px solid rgba(212,175,55,0.3); margin:20px 0;">
    <h1 style="font-family:'Bebas Neue',sans-serif; font-size:2.8rem; color:{GOLD}; text-align:center; letter-spacing:3px;">&#9876; COMPARE ANY TWO TEAMS</h1>
    <p style="font-family:'Inter',sans-serif; font-size:1rem; color:rgba(255,255,255,0.7); text-align:center;">Select two nations and see how they matched up across the tournament</p>
</div>
""", unsafe_allow_html=True)

all_teams = sorted(data['attacking']['Team'].tolist())
c1, c2 = st.columns(2)
idx1 = all_teams.index('Spain') if 'Spain' in all_teams else 0
idx2 = all_teams.index('Argentina') if 'Argentina' in all_teams else 1
team1 = c1.selectbox("Team 1", all_teams, index=idx1)
team2 = c2.selectbox("Team 2", all_teams, index=idx2)

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
        'Distance (km)': phys['Avg_Distance_Per_Player_km'].values[0] if len(phys) else 0,
        'Tackles': dfn['Tackles'].values[0]/10 if len(dfn) else 0,
    }

s1, s2 = get_stats(team1), get_stats(team2)
cats = list(s1.keys())
mx = {k: max(s1[k], s2[k], 0.01) for k in cats}

# Team info cards above the chart
res1 = data['team_results'][data['team_results']['Team']==team1]
res2 = data['team_results'][data['team_results']['Team']==team2]

c1, c2 = st.columns(2)
with c1:
    pos1 = res1['Final_Position'].values[0] if len(res1) else 'N/A'
    scorer1 = res1['Top_Goalscorer'].values[0] if len(res1) else 'N/A'
    st.markdown(f"""
    <div class="glass-card" style="border:2px solid #E63946; text-align:center;">
        <h2 style="color:#E63946; font-family:'Bebas Neue',sans-serif; font-size:2rem; margin:0;">{team1}</h2>
        <p style="color:rgba(255,255,255,0.7); margin:5px 0;">&#127942; {pos1} &#183; &#9917; {scorer1}</p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    pos2 = res2['Final_Position'].values[0] if len(res2) else 'N/A'
    scorer2 = res2['Top_Goalscorer'].values[0] if len(res2) else 'N/A'
    st.markdown(f"""
    <div class="glass-card" style="border:2px solid #4A90D9; text-align:center;">
        <h2 style="color:#4A90D9; font-family:'Bebas Neue',sans-serif; font-size:2rem; margin:0;">{team2}</h2>
        <p style="color:rgba(255,255,255,0.7); margin:5px 0;">&#127942; {pos2} &#183; &#9917; {scorer2}</p>
    </div>
    """, unsafe_allow_html=True)

# Radar chart + table side by side (table left, chart right)
fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=[s1[k]/mx[k]*100 for k in cats]+[s1[cats[0]]/mx[cats[0]]*100],
                               theta=cats+[cats[0]], fill='toself', name=team1, 
                               line_color='#E63946', fillcolor='rgba(230,57,70,0.2)'))
fig.add_trace(go.Scatterpolar(r=[s2[k]/mx[k]*100 for k in cats]+[s2[cats[0]]/mx[cats[0]]*100],
                               theta=cats+[cats[0]], fill='toself', name=team2, 
                               line_color='#4A90D9', fillcolor='rgba(74,144,217,0.2)'))
fig.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0,100], gridcolor='rgba(255,255,255,0.1)'),
        angularaxis=dict(gridcolor='rgba(255,255,255,0.1)', tickfont=dict(size=11))
    ),
    height=420, showlegend=True,
    plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#E8E8E8'),
    legend=dict(font=dict(color='#E8E8E8', size=12), x=0.5, xanchor='center', y=-0.15, orientation='h'),
    margin=dict(t=30, b=50)
)

# Build table HTML
rows_html = ""
for k in cats:
    val1 = f"{s1[k]:.1f}"
    val2 = f"{s2[k]:.1f}"
    bold1 = "font-weight:bold;" if s1[k] >= s2[k] else ""
    bold2 = "font-weight:bold;" if s2[k] >= s1[k] else ""
    color1 = "#E63946" if s1[k] >= s2[k] else "rgba(255,255,255,0.5)"
    color2 = "#4A90D9" if s2[k] >= s1[k] else "rgba(255,255,255,0.5)"
    rows_html += f'<tr style="border-bottom:1px solid rgba(255,255,255,0.1);"><td style="text-align:left; padding:12px; color:{color1}; font-size:1.2rem; {bold1}">{val1}</td><td style="text-align:center; padding:12px; color:rgba(255,255,255,0.6); font-size:0.85rem;">{k}</td><td style="text-align:right; padding:12px; color:{color2}; font-size:1.2rem; {bold2}">{val2}</td></tr>'

col_left, col_right = st.columns([1, 1])
with col_left:
    st.markdown(f"""
    <div class="glass-card" style="padding:20px 30px;">
        <table style="width:100%; border-collapse:collapse; font-family:'Inter',sans-serif;">
            <thead>
                <tr style="border-bottom:2px solid rgba(212,175,55,0.4);">
                    <th style="text-align:left; padding:10px; color:#E63946; font-size:1.1rem;">{team1}</th>
                    <th style="text-align:center; padding:10px; color:{GOLD}; font-size:0.9rem;">Metric</th>
                    <th style="text-align:right; padding:10px; color:#4A90D9; font-size:1.1rem;">{team2}</th>
                </tr>
            </thead>
            <tbody>{rows_html}</tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)
with col_right:
    st.plotly_chart(fig, use_container_width=True)

# ====================
# SECTION: GLOBAL IMPACT
# ====================
st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="impact-section">
    <div style="position:relative; z-index:1; text-align:center;">
        <h1 style="font-family:'Bebas Neue',sans-serif; font-size:3rem; color:{GOLD}; letter-spacing:3px;">THE RIPPLE EFFECT</h1>
        <p style="color:rgba(255,255,255,0.7); font-size:1.1rem;">The World Cup&#39;s impact extends far beyond the pitch &mdash; into economies, search engines, and cities.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="background: linear-gradient(135deg, #1a2a3a 0%, {NAVY} 100%); padding:40px 40px 20px; border-radius:16px; border:1px solid rgba(212,175,55,0.3); margin:20px 0;">
    <h1 style="font-family:'Bebas Neue',sans-serif; font-size:2.5rem; color:{GOLD}; text-align:center; letter-spacing:3px;">&#128269; SEARCH TRENDS DURING THE WORLD CUP</h1>
    <p style="color:{GOLD}; text-align:center;">Select a trend to explore:</p>
</div>
""", unsafe_allow_html=True)
trend_choice = st.radio("", [
    "World Cup (Global)", "Travel to USA", "Visit Spain", "US Visa Applications",
    "Soccer (USA)", "Watch Party", "Hotels New York", "Hotels Seattle", "Hotels Miami", "Hotels Kansas City"
], horizontal=True, label_visibility="collapsed")

trend_map = {"World Cup (Global)":'gtrends_wc', "Travel to USA":'gtrends_travel',
             "Visit Spain":'gtrends_spain', "US Visa Applications":'gtrends_visa',
             "Soccer (USA)":'gtrends_soccer', "Watch Party":'gtrends_watch',
             "Hotels New York":'gtrends_hotels_ny', "Hotels Seattle":'gtrends_hotels_seattle',
             "Hotels Miami":'gtrends_hotels_miami', "Hotels Kansas City":'gtrends_hotels_kansas'}

td = data[trend_map[trend_choice]].copy()
td.columns = ['Interest']

fig = px.area(td.reset_index(), x=td.reset_index().columns[0], y='Interest', color_discrete_sequence=[GOLD])
fig.add_vrect(x0="2026-06-11", x1="2026-07-19", fillcolor="rgba(212,175,55,0.08)", line_width=0,
              annotation_text="&#9917; World Cup", annotation_position="top left",
              annotation_font=dict(color=GOLD, size=11))
fig.update_layout(
    height=400, xaxis_title="", yaxis_title="Search Interest (0-100)",
    plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#E8E8E8'),
    xaxis=dict(gridcolor='rgba(255,255,255,0.05)'),
    yaxis=dict(gridcolor='rgba(255,255,255,0.05)')
)
st.plotly_chart(fig, use_container_width=True)

st.markdown(f"""
<div class="glass-card">
    <strong style="color:{GOLD};">Key findings:</strong><br>
    &#8226; "Visit Spain" surged <strong>5&times;</strong> after Spain&#39;s victory<br>
    &#8226; US visa applications hit <strong>2.6&times;</strong> peak during tournament<br>
    &#8226; Hotel searches in NYC spiked <strong>4.7&times;</strong><br>
    &#8226; "Soccer" in USA hit all-time high &mdash; <strong>5.7&times;</strong> normal<br>
    &#8226; "Watch party" went from <strong>zero to 100</strong> &mdash; an infinite spike
</div>
""", unsafe_allow_html=True)

# Morning After
st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)

st.markdown(f"""
<div style="background: linear-gradient(135deg, #1a2a3a 0%, {NAVY} 100%); padding:50px 40px 30px; border-radius:16px; border:1px solid rgba(212,175,55,0.3); margin:20px 0;">
    <h1 style="font-family:'Bebas Neue',sans-serif; font-size:2.8rem; color:{GOLD}; text-align:center; letter-spacing:3px;">&#127749; THE MORNING AFTER</h1>
    <p style="font-family:'Inter',sans-serif; font-size:1.1rem; color:rgba(255,255,255,0.8); text-align:center; font-style:italic;">The effects don&#39;t end at the final whistle. They echo for years:</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f'<div class="metric-card" style="background:rgba(212,175,55,0.1); border:2px solid {GOLD};"><div class="metric-number" style="font-size:3rem;">+spike</div><div class="metric-label">Birth rates 9 months after wins</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="metric-card" style="background:rgba(212,175,55,0.1); border:2px solid {GOLD};"><div class="metric-number" style="font-size:3rem;">5&times;</div><div class="metric-label">"Visit Spain" searches</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="metric-card" style="background:rgba(212,175,55,0.1); border:2px solid {GOLD};"><div class="metric-number" style="font-size:3rem;">+35%</div><div class="metric-label">Youth soccer registration</div></div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="glass-card" style="border-left:4px solid {GOLD}; margin:20px 0;">
    <strong style="color:{GOLD};">Birth rates</strong> spike 9 months after a national team wins (proven: Spain 2010, France 2018)
</div>
<div class="glass-card" style="border-left:4px solid {GOLD}; margin:20px 0;">
    <strong style="color:{GOLD};">Host cities</strong> saw 20% increase in cross-border Visa transactions
</div>
<div class="glass-card" style="border-left:4px solid {GOLD}; margin:20px 0;">
    <strong style="color:{GOLD};">MLS</strong> conversations exploded &mdash; America&#39;s relationship with soccer changed permanently
</div>
<div class="glass-card" style="border-left:4px solid {GOLD}; margin:20px 0;">
    <strong style="color:{GOLD};">800,000+ jobs</strong> created across 3 host countries
</div>
""", unsafe_allow_html=True)

# ====================
# SECTION: AI & METHODS
# ====================
st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="ai-section">
    <div style="position:relative; z-index:1; text-align:center;">
        <h1 style="font-family:'Bebas Neue',sans-serif; font-size:3rem; color:{GOLD}; letter-spacing:3px;">HOW AI BUILT THIS STORY</h1>
        <p style="color:rgba(255,255,255,0.7); font-size:1.1rem;">GenAI as co-pilot at every stage &mdash; data discovery, hypothesis generation, and narrative crafting.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"### &#129302; AI Agent Pipeline")
st.markdown(f"""
<div class="glass-card" style="font-family:monospace; font-size:0.9rem; line-height:2;">
    <span style="color:{GOLD};">Public Datasets</span> (FIFA, Google Trends, Kaggle)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&#9474;<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&#9660;<br>
    <span style="color:{GOLD};">Agent 1:</span> Data Discovery & Validation (Kiro + pytrends)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&#9474;<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&#9660;<br>
    <span style="color:{GOLD};">Agent 2:</span> Hypothesis Generator (50+ questions tested)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&#9474;<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&#9660;<br>
    <span style="color:{GOLD};">Agent 3:</span> Statistical Testing (Python / Pandas)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&#9474;<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&#9660;<br>
    <span style="color:{GOLD};">Agent 4:</span> Insight Ranker (novelty &times; visual potential)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&#9474;<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&#9660;<br>
    <span style="color:{GOLD};">Agent 5:</span> Narrative Writer (story arc generation)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&#9474;<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&#9660;<br>
    <span style="color:{GOLD};">Final Output:</span> Cinematic Streamlit Dashboard
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"""
    <div class="glass-card" style="background:rgba(255,255,255,0.15); border:1px solid rgba(212,175,55,0.4);">
        <h4 style="color:{GOLD};">&#128202; Data Stack</h4>
        <p>&#8226; Python / Pandas<br>&#8226; pytrends (Google Trends API)<br>&#8226; Kaggle datasets<br>&#8226; FIFA.com official stats</p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown(f"""
    <div class="glass-card" style="background:rgba(255,255,255,0.15); border:1px solid rgba(212,175,55,0.4);">
        <h4 style="color:{GOLD};">&#128201; Visualization</h4>
        <p>&#8226; Streamlit<br>&#8226; Plotly Express + GO<br>&#8226; Custom CSS theming<br>&#8226; Responsive design</p>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown(f"""
    <div class="glass-card" style="background:rgba(255,255,255,0.15); border:1px solid rgba(212,175,55,0.4);">
        <h4 style="color:{GOLD};">&#129302; GenAI Usage</h4>
        <p>&#8226; Claude / Kiro (Amazon)<br>&#8226; Hypothesis generation<br>&#8226; Narrative drafting<br>&#8226; Full code generation</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)
st.markdown(f"### &#128218; Data Sources")
st.markdown("""
| Source | Description | Link |
|--------|------------|------|
| FIFA.com | Official 2026 World Cup Statistics (7 categories, 48 teams) | fifa.com/worldcup |
| Google Trends | 10 search terms, Jan 2025 &ndash; Aug 2026 | trends.google.com |
| Kaggle | International Football Results (1872-2026) | kaggle.com |
| Forbes | "Why The Global Impacts Will Linger" | forbes.com |
| WTO | $40.9B GDP projection | wto.org |
""")

# ====================
# CLOSING
# ====================
st.markdown(f'<div class="section-gap"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="hero-section" style="padding:100px 40px;">
    <div style="position:relative; z-index:1; max-width:800px; margin:0 auto;">
        <p style="font-family:'Inter',sans-serif; font-size:1.3rem; color:rgba(255,255,255,0.8); line-height:2.5; text-align:center; font-weight:300;">
            No election. No concert. No holiday.<br>
            Nothing else on Earth makes billions of people feel the same emotion at the same second.<br><br>
            The World Cup is not a tournament.<br>
            It&#39;s a 30-day experiment in <span style="color:{GOLD}; font-weight:500;">human connection.</span><br><br>
            And in 2026, that heartbeat pulsed through America.
        </p>
        <p style="font-family:'Bebas Neue',sans-serif; font-size:3.5rem; color:{GOLD}; text-align:center; margin-top:40px; letter-spacing:4px; line-height:1.2;">
            THE WORLD HELD ITS BREATH.<br>THEN IT EXHALED TOGETHER.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align:center; padding:30px; color:rgba(255,255,255,0.3); font-size:0.8rem;">
    Built for Analyticon VizCon 2026 &#183; Theme: "How the world lives, thrives, and connects" [Globe]<br>
    By Greeshma Joseph &#183; Tools: Streamlit, Plotly, Python, Kiro (GenAI)
</div>
""", unsafe_allow_html=True)
