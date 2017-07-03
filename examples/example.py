from BccardEmailParser import BccardParser

parser = BccardParser.BccardParser()

with open('email/authorization_domestic_krw.html', 'r') as f:
    html = f.read()
    parser.parse(html)
    print(parser.get_result())

with open('email/authorization_international_usd.html', 'r') as f:
    html = f.read()
    parser.parse(html)
    print(parser.get_result())


