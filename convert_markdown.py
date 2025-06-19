import markdown

with open('reconstruction_website/reconstruction_analysis_report.md', 'r', encoding='utf-8') as f:
    text = f.read()

html = markdown.markdown(text)

with open('reconstruction_website/report.html', 'w', encoding='utf-8') as f:
    f.write(html)

