import pandas as pd
from bs4 import BeautifulSoup

# Sample DataFrames
df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
df2 = pd.DataFrame({'City': ['New York', 'Los Angeles'], 'Population': [8_398_748, 3_990_456]})
df3 = pd.DataFrame({'Product': ['Laptop', 'Tablet'], 'Price': [1000, 500]})

# Convert DataFrames to HTML
html1 = df1.to_html(index=False)
html2 = df2.to_html(index=False)
html3 = df3.to_html(index=False)

# Use BeautifulSoup to build the combined HTML
soup = BeautifulSoup('<div style="display: flex; gap: 20px;"></div>', 'html.parser')
container = soup.div

# Wrap each table in a div for styling and add them to the container
for html in [html1, html2, html3]:
    table_soup = BeautifulSoup(html, 'html.parser')
    table_div = soup.new_tag('div', style="flex: 1;")
    table_div.append(table_soup)
    container.append(table_div)

# Final HTML content
final_html = str(soup)

# Print the HTML to verify
print(final_html)
