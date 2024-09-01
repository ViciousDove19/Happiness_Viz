import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Shareable Chart Example", layout="wide")

happiness = [5,5,5,5,5,5,5,5,5,5,5]

happiness[0] = st.select_slider(
    "How was your 2014?",
    options=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ],
)

happiness[1] = st.select_slider(
    "How was your 2015?",
    options=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ],
)

happiness[2] = st.select_slider(
    "How was your 2016?",
    options=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ],
)

happiness[3] = st.select_slider(
    "How was your 2017?",
    options=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ],
)

happiness[4] = st.select_slider(
    "How was your 2018?",
    options=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ],
)

happiness[5] = st.select_slider(
    "How was your 2019?",
    options=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ],
)

happiness[6] = st.select_slider(
    "How was your 2020?",
    options=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ],
)

happiness[7] = st.select_slider(
    "How was your 2021?",
    options=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ],
)

happiness[8] = st.select_slider(
    "How was your 2022?",
    options=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ],
)

happiness[9] = st.select_slider(
    "How was your 2023?",
    options=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ],
)

happiness[10] = st.select_slider(
    "How was your 2024?",
    options=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ],
)



# Create some sample data
data = pd.DataFrame({
    'x': [2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024],
    'y': happiness
})

# Create a chart
fig = px.line(data, x='x', y='y', title='Sample Line Chart')

# Display the chart
st.plotly_chart(fig, use_container_width=True)

# Add a sharing button
if st.button('Share this chart'):
    # Get the chart as HTML
    chart_html = fig.to_html(include_plotlyjs='cdn')
    
    # Create a download link
    st.download_button(
        label="Download HTML",
        data=chart_html,
        file_name="chart.html",
        mime="text/html"
    )

    # Display the embed code
    st.code(f'<iframe src="{st.get_option("server.headless") and "https://share.streamlit.io" or "http://localhost:8501"}?embed=true" height="600" width="100%"></iframe>')

    st.success("You can now download the chart as an HTML file or use the embed code to share it on a website!")