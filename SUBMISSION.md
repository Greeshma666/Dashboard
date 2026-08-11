# VizCon 2026 Submission

## Title
**When the World Held Its Breath**
How the 2026 FIFA World Cup proved that billions of strangers can share one heartbeat.

## Brief Description

The 2026 FIFA World Cup wasn't just 104 matches across 48 nations — it was a 39-day experiment in human connection. This visualization explores what happens when the entire planet chooses to feel the same thing at the same time.

Using verified data from FIFA, Google Trends, and local organizer reports, we uncovered a surprising discovery: **8 of the top 10 geographies by relative FIFA World Cup search interest weren't even competing in the tournament.** Nepal, Bangladesh, Jamaica, and Trinidad & Tobago showed higher relative search intensity than traditional football powers like Germany, Spain, or Brazil.

The story zooms from global scale to human intimacy: 9 million people gathered at Fan Festivals outside stadiums (more than the 6.8 million inside). 178 countries were represented at a single Fan Festival in Kansas City. And Cabo Verde — a nation of 527,000 people — went from near-zero global search interest to peak 100 during their first-ever World Cup, with spikes perfectly aligning to each match day.

This isn't a football dashboard. It's a story about how the world lives, thrives, and connects — told through the one event that makes billions of strangers feel like family.

## Data Sources

| Source | Description | Link |
|--------|-------------|------|
| FIFA.com | Official 2026 World Cup statistics, squad data, Fan Festival attendance (9M+, 263,972 final viewers) | fifa.com/worldcup |
| Google Trends | 11 search terms including "FIFA World Cup" by country, "Cabo Verde", "Watch Party", "Soccer" (USA), hotel searches, visa demand | trends.google.com |
| KC2026 | Kansas City Fan Festival report (178 countries, 63,000 attendees) | KC2026 organizer |
| Reuters | Vozinha/Cabo Verde goalkeeper story verification | reuters.com |
| World Bank | Cabo Verde population (527,326) | data.worldbank.org |
| Kaggle | International football results (1872-2026), historical World Cup data | kaggle.com |

## Tools Used
- **Streamlit** — Interactive web dashboard framework
- **Plotly** — Data visualization (area charts, radar charts, scatter plots, geo maps)
- **Python / Pandas** — Data processing and analysis
- **Kiro (Amazon AI agent)** — GenAI co-pilot for data discovery, hypothesis generation, code generation, and narrative development

## GenAI Documentation

GenAI (Kiro/Claude) was used as an active co-pilot throughout the project:

1. **Data Discovery** — AI suggested searching Google Trends for country-level World Cup interest, leading to the "8/10" discovery
2. **Hypothesis Testing** — AI generated 50+ questions about the data; we systematically validated each claim against primary sources
3. **Source Validation** — When the initial Google Trends dataset used a 1-year window, we challenged it, re-downloaded with the correct 2-month window (Jun-Jul 2026), and only then accepted the finding
4. **Rejected Claims** — AI initially surfaced claims about travel patterns, fan behavior, and economic metrics that we couldn't verify. These were removed rather than included with fabricated data
5. **Narrative Development** — AI helped structure the 5-chapter zoom: Planet → Countries → Cities → Players → One family
6. **Code Generation** — Dashboard code, Plotly charts, CSS styling, and data processing pipelines

The key principle: **AI surfaced patterns, humans verified facts.** Every number in the final dashboard traces to a cited source.

## Visualization Link
https://greeshma666-dashboard.streamlit.app
