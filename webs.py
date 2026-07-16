from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome</h1>
<p>This is Python.</p>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print(soup.title.text)
print(soup.h1.text)
print(soup.p.text)