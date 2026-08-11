# VizCon 2026 Competition Details

## Theme
**"How the world lives, thrives, and connects"** 🌍

Every day, 8 billion people wake up, eat, work, travel, celebrate, and rest — but no two corners of the world do it quite the same way. The entry that makes someone lean forward and say: "I had no idea."

## Our Angle
The 2026 FIFA World Cup as a story of **how the world connects** through sport.
- "The Night the World Held Its Breath"
- Spain 1-0 Argentina (Ferran Torres 106', extra time)
- MetLife Stadium, New Jersey
- Cabo Verde's debut + Goal of Tournament (Sidny Lopes Cabral)
- First 48-team World Cup (US/Canada/Mexico)
- Messi's 6th WC (age 39), Ronaldo's farewell

## Judging Criteria (what we optimize for)
1. **Data Storytelling & Impact (30%)** — Clear narrative arc? Memorable? Helps audience connect?
2. **Discovery & Innovation (25%)** — Surprising "I didn't know that!" moment? Novel formats?
3. **Visual Design & Aesthetics (20%)** — Beautiful? Appropriate charts? Colors/fonts in harmony? Eye drawn to key elements?
4. **Data Quality & Inclusivity (15%)** — Sources cited? Accurate? Accessible design?
5. **Technical Execution & Engagement (10%)** — Interactive? Clear guidance? Polished? Tool mastery?

## Special Awards
- 🏆 Grand Champion — Highest overall score
- 📖 Best Data Story — Most compelling narrative
- 🔍 Best Discovery — "I had no idea!" award
- 🎨 Best Visual Design — Most beautiful execution
- 🛠️ Best Use of GenAI — Must be documented
- 👥 People's Choice — Community voted

## Key Dates
- Competition begins: Mon, July 6, 2026
- Registration closes: Fri, July 24
- **Submission deadline: Fri, August 10, 2026** ← 5 DAYS LEFT
- Finalists notified: Mon, August 24
- Winners announced: Fri, September 4

## Submission Requirements
1. Visualization — publicly accessible dashboard/link
2. Data Sources — list of all datasets with links
3. Brief Description — detailed narrative on the story
4. Tools Used — which visualization tool(s)
5. GenAI Documentation (optional) — how AI tools were used

## Tools Allowed
QuickSight, Tableau, Power BI, Python, R, D3, Observable, Flourish, Streamlit, other

## Our Setup
- Tool: Streamlit (Python)
- App: ~/Desktop/Projects/vizcon/app.py
- Data: ~/Desktop/Projects/vizcon/data/ (32 CSV files)
- Theme colors: Navy (#1B2A4A) + Gold (#D4AF37)
- 4 tabs: Story, Explore Teams, Global Impact, AI & Methods

## Design Philosophy (from our prompt)
- Emotional impact before analytical impact
- Cinematic story feel (scroll experience)
- Whitespace aggressively
- Large typography
- Minimal colors
- Motion where meaningful
- Annotations instead of legends
- Every viz = artwork
- Ask "What emotion should viewer feel?" not "What chart best represents data?"

## Key "I didn't know that!" Moments to Feature
- 7% of ALL global internet traffic during the final match
- Cabo Verde (population ~600K) debut + Goal of Tournament
- Google Trends: 20x search surge for underdog teams
- $40.9B GDP impact, 800K+ jobs created
- 90 petabytes of data generated (45x more than Qatar 2022)

## CRITICAL: Story Framing (Not Just Football)

The story is NOT about football stats. It's about **human connection** — the World Cup as a lens into how the world connects.

**Core narrative:**
> "No election. No concert. No holiday. Nothing else on Earth makes 8 billion people feel the same emotion at the same second. The World Cup is not a tournament. It's a 30-day experiment in human connection. And in 2026, that heartbeat pulsed through America. The world held its breath. Then it exhaled together."

**Theme alignment:** "How the world lives, thrives, and connects" → The WC is the ultimate proof of global connection:
- How the world CONNECTS: 7% of global internet traffic in one match
- How the world THRIVES: $40.9B GDP boost, 800K jobs, city transformations
- How the world LIVES: Search behavior changes, digital curiosity surges, cultural moments

**ChatGPT-suggested angles that align with theme:**
- Did host advantage still matter in the first 48-team World Cup?
- Which countries produced the most WC players relative to population?
- How global are modern national teams? (club careers vs country they represent)
- Which "small nations" overperformed based on FIFA ranking, GDP, or population?
- How did 48-team format reshape competitive balance and global representation?

**Off-the-pitch impact data (Forbes/research):**
- Pop-up economies: 20% YoY increase in cross-border Visa transactions in host cities
- $40.9B global GDP boost (WTO projection)
- FIFA record $11B revenue
- $500M invested in counter-drone security measures
- Dallas: Cotton Belt trail + DART expansion
- Houston: EaDo repurposed into permanent entertainment hub
- 7% of ALL global internet traffic during final match
- 90 petabytes of tournament data (45x more than Qatar 2022)
- Opening-day searches for national teams doubled by the final
- Underdog teams (Belgium, Austria, Cabo Verde): 20x+ search surge

**The "I didn't know that!" moments (what wins Discovery & Innovation - 25%):**
1. Cabo Verde (population ~600K) debuting AND winning Goal of the Tournament
2. 7% of global internet = one football match
3. Google Trends showing 20x surge for underdogs
4. 90 petabytes (45x Qatar) — data explosion
5. Cross-border spending +20% in host cities

## Design System Prompt (for rebuilding)
```
You are one of the world's best interactive data visualization designers.
- DO NOT build a BI dashboard
- DO NOT create generic Plotly charts
- Audience = judges, not business stakeholders
- Goal = emotional impact BEFORE analytical impact
- Experience = scrolling through a cinematic story
- Every section should make viewers stop and think
- Every viz should be memorable a week later
- Whitespace aggressively
- Large typography
- Minimal colors (navy + gold + white)
- Motion where meaningful
- Annotations instead of legends
- Treat every visualization as artwork
- Ask "What emotion should the viewer feel?" not "What chart best represents this data?"
```
