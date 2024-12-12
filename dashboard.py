import streamlit as st 
import plotly.express as px 
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="SuperStore Analysis", page_icon=":bar_chart:", layout="wide")

st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
st.title(" :shopping_bags: SuperStore EDA")
st.markdown("An interactive dashboard for in-depth exploration of Superstore sales data.")

# File uploader widget
file = st.file_uploader(":file_folder: Upload your Superstore file", type=(["csv", "txt", "xlsx", "xls"]))

# Load data
if file is not None:
    st.write("File uploaded successfully!")
    df = pd.read_csv(file, encoding="ISO-8859-1")
elif os.path.exists("Superstore.csv"):
    df = pd.read_csv("Superstore.csv", encoding="ISO-8859-1")
    st.write("Using the default 'Superstore.csv' file.")
else:
    st.error("No file uploaded, and default file 'Superstore.csv' not found. Please upload a valid file.")
    st.stop()

# Data Preprocessing
df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce', dayfirst=True)
startDate = df["Order Date"].min()
endDate = df["Order Date"].max()

# Date filters
col1, col2 = st.columns((2))
with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("End Date", endDate))

df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()

# Sidebar Filters
st.sidebar.header("Filter Data")
region = st.sidebar.multiselect("Select your Region", df["Region"].unique())
state = st.sidebar.multiselect("Pick the State", df["State"].unique())
city = st.sidebar.multiselect("Pick the City", df["City"].unique())

# Apply filters
filtered_df = df.copy()
if region:
    filtered_df = filtered_df[filtered_df["Region"].isin(region)]
if state:
    filtered_df = filtered_df[filtered_df["State"].isin(state)]
if city:
    filtered_df = filtered_df[filtered_df["City"].isin(city)]

# Visualization 1: Sales Breakdown by Category
category_df = filtered_df.groupby(by=["Category"], as_index=False)["Sales"].sum()
st.subheader(":bar_chart: Sales Breakdown by Category")
fig = px.bar(category_df, x="Category", y="Sales", color="Category", text=['${:,.2f}'.format(x) for x in category_df["Sales"]],
             template="seaborn", color_discrete_sequence=px.colors.sequential.Viridis)
st.plotly_chart(fig, use_container_width=True)

# Visualization 2: Sales Distribution by Region
st.subheader(":earth_africa: Sales Distribution by Region")
fig = px.pie(filtered_df, values="Sales", names="Region", hole=0.5, color_discrete_sequence=px.colors.sequential.Viridis)
st.plotly_chart(fig, use_container_width=True)

# Download filtered data
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("Download Filtered Data", data=csv, file_name="Filtered_Superstore_Data.csv", mime="text/csv")
