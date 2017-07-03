BCCard Email Parser
=====================

Parse the BC Card authorization email.

Install
-----
.. code:: bash
    # TBA

Usage
-----
.. code:: python
    from BccardEmailParser import BccardParser

    parser = BccardParser.BccardParser()

    with open('email/authorization_domestic_krw.html', 'r') as f:
        html = f.read()
        parser.parse(html)
        print(parser.get_result())


Release
----

0.1.1 - Parsing authorization domestic/international email

