import numpy as np
import pandas as pd
import plotly.express as px
def create_trend_graph(transactions):
    """
    Create a trend graph
    :param transactions:
    :return:
    """
    print("\n--- Generating Borrowing Trends ---")

    # Check if there is data to plot
    if not transactions:
        print("Error: No transactions available to analyze.")
        return

    # Put dictionary into data frame
    df = pd.DataFrame.from_dict(transactions, orient='index')

    # Filters out returned books
    df_issues = df[df['type'] == '1'].copy()

    if df_issues.empty:
        print("Notice: No books have been issued yet. Not enough data for a trend line.")
        return

    # Convert date strings into datetime objects
    try:
        df_issues['date'] = pd.to_datetime(df_issues['date'], format='%d/%m/%Y')
    except ValueError as e:
        print(f"Error processing dates: {e}")
        return

    trend_data = df_issues.groupby('date').size().reset_index(name='books_issued')

    trend_data = trend_data.sort_values('date')

    # Generate plot
    fig = px.line(
        trend_data,
        x='date',
        y='books_issued',
        title='Library Borrowing Trends Over Time',
        labels={'date': 'Date', 'books_issued': 'Number of Books Issued'},
        markers=True # Add dots for each points
    )

    # Show plot
    fig.show()