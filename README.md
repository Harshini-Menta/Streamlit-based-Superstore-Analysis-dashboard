# Superstore Analysis Dashboard

An interactive data analysis and visualization dashboard built using Streamlit and Plotly, designed for in-depth exploration of Superstore sales data. This dashboard allows users to upload their own Superstore dataset and provides tools to filter, analyze, and visualize data across various sales dimensions, including categories, regions, time series, and more.

## Features ✨

- **File Upload**: Supports uploading Superstore data in `.csv`, `.txt`, `.xlsx`, or `.xls` formats.
- **Dynamic Filtering**: Filter data by region, state, and city.
- **Time Series Analysis**: Visualizes sales trends over time.
- **Sales Breakdown**: Presents breakdowns by category, region, segment, and sub-categories.
- **Hierarchical Sales View**: Displays hierarchical data with a treemap view.
- **Scatter Plot Analysis**: Explores the relationship between sales and profit.
- **Downloadable Data**: Provides options to download filtered or visualized data for further analysis.

## Installation 📦

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
1. Run the Streamlit app:
   ```bash
   streamlit run dashboard.py
   ```

## Usage 🚀

1. Upload a dataset file (Superstore data in `.csv`, `.txt`, `.xlsx`, or `.xls` formats).
2. Use the sidebar filters to narrow down data by region, state, and city.
3. Explore the various interactive visualizations:
   - **Sales Breakdown by Category**: Shows category-wise sales using a bar chart.
   - **Sales Distribution by Region**: Displays regional sales distribution with a pie chart.
   - **Time Series Analysis**: Line chart for month-wise sales trends.
   - **Hierarchical View of Sales**: A treemap for sales breakdown across regions and sub-categories.
   - **Segment and Category-wise Sales**: Pie charts for sales by segment and category.
   - **Scatter Plot of Sales vs. Profit**: Scatter plot depicting the relationship between sales and profit.
   - **Data Table Views**: Expandable tables to view and download filtered datasets.

## File Structure 📁

- `dashboard.py`: The main application file containing all Streamlit and Plotly code.
- `requirements.txt`: The dependencies required to run the app.
- `Superstore.csv`: Sample dataset file to demonstrate the app's functionalities.

## Output 

https://github.com/user-attachments/assets/094f73da-2c6e-4991-97ca-6389ba9037c9


