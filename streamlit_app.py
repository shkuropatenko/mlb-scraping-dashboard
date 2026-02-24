import pandas as pd

DATA_URL = "https://www.espn.com/mlb/worldseries/history/winners"

def load_raw_table() -> pd.DataFrame:
    tables = pd.read_html(DATA_URL, header=None)
    return tables[0].copy()

df_raw = load_raw_table()

st.subheader("Raw scraped table (preview)")
st.dataframe(df_raw.head(20), use_container_width=True)

def load_data() -> pd.DataFrame:
  tables = pd.read_html(DATA_URL, header=None)
  df = tables[0].copy()

  df.columns = ["Season", "Winner", "Loser", "Series"]

  df["Season"] = pd.to_numeric(df["Season"], errors="coerce")
  df = df.dropna(subset=["Season"])
  df["Season"] = df["Season"].astype(int)

  for c in ["Winner", "Loser", "Series"]:
    df[c] = df[c].astype(str).str.strip()

  return df

df = load_data()

st.subheader("Cleaned dataset (preview)")
st.dataframe(df.head(20), use_container_width=True)

min_year, max_year = int(df["Season"].min()), int(df["Season"].max())

st.sidebar.header("Filters")
year_range = st.sidebar.slider("Season range", min_year, max_year, (max_year - 30, max_year))

filtered = df[(df["Season"] >= year_range[0]) & (df["Season"] <= year_range[1])].copy()

st.subheader("Filtered results")
st.write(f"Seasons: {year_range[0]}–{year_range[1]} | Rows: {len(filtered)}")
st.dataframe(filtered, use_container_width=True)