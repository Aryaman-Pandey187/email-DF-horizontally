import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
df2 = pd.DataFrame({'City': ['New York', 'Los Angeles'], 'Population': [8_398_748, 3_990_456]})
df3 = pd.DataFrame({'Product': ['Laptop', 'Tablet'], 'Price': [1000, 500]})

# Convert DataFrames to HTML
html1 = df1.to_html(index=False, border=1)
html2 = df2.to_html(index=False, border=1)
html3 = df3.to_html(index=False, border=1)

# Combine tables horizontally using a single row with inline CSS
final_html = f"""
<table style="width: 100%; border-collapse: collapse;">
  <tr>
    <td style="vertical-align: top; padding: 10px; width: 33%;">{html1}</td>
    <td style="vertical-align: top; padding: 10px; width: 33%;">{html2}</td>
    <td style="vertical-align: top; padding: 10px; width: 33%;">{html3}</td>
  </tr>
</table>
"""

# Print the HTML to verify
print(final_html)
