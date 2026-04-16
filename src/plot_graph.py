import numpy as np
import pandas as pd
import plotly.express as px # Recommended over base plotly for quick graphs

def create_trend_graph(transactions):
    """
    Analyzes transaction data and generates an interactive line graph
    showing the number of books issued over time.
    """
    print("\n--- Generating Borrowing Trends ---")

    # 1. Check if there is data to plot
    if not transactions:
        print("Error: No transactions available to analyze.")
        return

    # 2. Convert the nested dictionary into a Pandas DataFrame
    # orient='index' tells Pandas that your dictionary keys (T001, T002) are the rows
    df = pd.DataFrame.from_dict(transactions, orient='index')

    # 3. Filter for only "Issued" books (assuming type '1' is issued based on previous code)
    df_issues = df[df['type'] == '1'].copy()

    if df_issues.empty:
        print("Notice: No books have been issued yet. Not enough data for a trend line.")
        return

    # 4. Convert the string dates into proper Datetime objects
    # This ensures the graph plots chronological time correctly, not alphabetical order
    try:
        df_issues['date'] = pd.to_datetime(df_issues['date'], format='%d/%m/%Y')
    except ValueError as e:
        print(f"Error processing dates: {e}")
        return

    # 5. Group the data by date and count the number of issues per day
    # This creates a new dataframe with two columns: 'date' and 'books_issued'
    trend_data = df_issues.groupby('date').size().reset_index(name='books_issued')

    # 6. Sort chronologically just in case
    trend_data = trend_data.sort_values('date')

    # 7. Generate the Plotly Line Graph
    fig = px.line(
        trend_data,
        x='date',
        y='books_issued',
        title='Library Borrowing Trends Over Time',
        labels={'date': 'Date', 'books_issued': 'Number of Books Issued'},
        markers=True # Adds dots at each data point for better readability
    )

    # 8. Open the interactive graph in the default web browser
    fig.show()