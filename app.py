import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_csv("cafe_sales.csv")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

st.title("Qahwa Corner - Sales Dashboard")

# محدد الفروع (Branch Selector)
branches = ["All"] + list(df["branch"].unique())
selected_branch = st.sidebar.selectbox("Select Branch", branches)
filtered_df = df if selected_branch == "All" else df[df["branch"] == selected_branch]

# مؤشر إجمالي الإيرادات (Total-Revenue Metric)
st.metric("Total Revenue (SAR)", f"{filtered_df['total_sar'].sum():,.2f} SAR")

# مخطط شريطي للإيرادات حسب المنتج (Bar Chart of Revenue by Product)
st.subheader("Revenue by Product")
prod_rev = filtered_df.groupby("product")["total_sar"].sum().sort_values(ascending=True)
fig, ax = plt.subplots(figsize=(8, 4.5))
prod_rev.plot(kind="barh", ax=ax, color="#2ca02c")
ax.set_xlabel("Total Revenue (SAR)")
ax.set_ylabel("Product")
st.pyplot(fig)
