def print_text(text):
    with open('main.txt', 'w', encoding="utf-8") as f:
        f.write(text)
        f.write('/n')



def print_html(text,title,file='index.html'):
    
    code =f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body><h1>{title}'''+'</h1>'+text+'''
    
</body>
</html>'''
    
    with open(file,'w',encoding="utf-8") as f:
        f.write(code)
        
       