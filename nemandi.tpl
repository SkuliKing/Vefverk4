<!DOCTYPE html>
<html>
<head>
    <title>Verkefni 4</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>

    <%
    nafn=''
    braut=''
    for nemandi in bekkur['nemendur']:
        if nemandi['kt']== kt:
            nafn = nemandi['nafn']
            braut = nemandi['braut']
        end
    end %>

    <h1>Nemandi:</h1>

    <h2>Kt: {{kt}}</h2>
    <h2>Nafn: {{nafn}}</h2>
    <h2>Braut: {{braut}}</h2>
    <a href="/">Heim<a>

</body>
</html>