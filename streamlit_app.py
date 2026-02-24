import pandas as pd

DATA_URL = "https://www.espn.com/mlb/worldseries/history/winners"

def load_raw_table() -> pd.DataFrame:
    tables = pd.read_html(DATA_URL, header=None)
    return tables[0].copy()

df_raw = load_raw_table()

st.subheader("Raw scraped table (preview)")
st.dataframe(df_raw.head(20), use_container_width=True)