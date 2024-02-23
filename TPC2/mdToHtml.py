import re
import sys
import re



template = '''
<!DOCTYPE html>
<html>
<head><title>Conversao</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body><div>
'''

def clearWhiteSpaces(line):
    # Function to remove consecutive white spaces with only one ' '
    return re.sub(r'\s+',' ',line)

def subImage(line):
    return re.sub(r'!\[([^\]]*)\]\(([^\)]*)\)',lambda x: f'<br /><img class = "w3-image" src="{x[2]}" alt="{x[1]}">',line)


def subLink(line):
  
    return re.sub(r'(?<!!)\[([^\]]*)\]\(([^\)]*)\)',lambda x: f'<a href="{x[2]}">{x[1]}</a>',line)


def mardownLineToHtml(line):
    line = clearWhiteSpaces(line)
    line = subImage(line)
    line = subLink(line)
    line =subHeading(line)

    line = subBold(line)
    line = subItalic(line)
    line = subLists(line)
    return line

def markdownToHtml(file):
    html = template
    # this function turns every markdown expression into html expression
    addNewLine = False
    firstLine = True
    for line in file:
        if line == "\n":
            if not firstLine:
                if addNewLine:
                    html += "\n"
                addNewLine = True
        else:
            firstLine = False
            if not firstLine and addNewLine:
                    html += "<br />"
                    addNewLine = False
            html += (mardownLineToHtml(line))
    html = correctLists(html)
    html += "</div></body></html>"
    file = open(f"resut.html", "w", encoding="utf-8")
    file.write(html)
    file.close()


def createParagraph(md):
    #this function uses regex to create a paragraph tag for every line using regex
    return re.sub(r'(?<!<h[1-6]>)\n(?!\s*<li>)',lambda x: "<p>",md)



def addHtmlTags(line,tag):
    return f"<{tag}>{line}</{tag}>"

def subHeading(line):
    # this function turns every markdown heading expression into html heading expression
    return re.sub(r'^ {0,3}(#{1,6})\s*(.*)',lambda x: addHtmlTags(x[2],f'h{len(x[1])}') + "<br/>",line)

def subBold(line):
    # this function turns every markdown bold expression into html bold expression
    t = 'b'
    firstSub = re.sub(r'\*\*([^\*\s])\*\*|\*\*([^\*\s].*?[^\*\s])\*\*',lambda x: addHtmlTags(x[1] if x[1] else x[2],t) ,line )
    
    return re.sub(r'\b__([^_\s])__\W+|\W+__([^_\s].*?[^_\s])__\b',lambda x: addHtmlTags(x[1] if x[1] else x[2],t) ,firstSub )

def subItalic(line):
    t = 'i'
    firstSub = re.sub(r'\*([^\*\s])\*|\*([^\*\s].*?[^\*\s])\*',lambda x: addHtmlTags(x[1] if x[1] else x[2],t) ,line )
    
    return re.sub(r'\b_([^_\s])_\b|\b_([^_\s].*?[^_\s])_\b',lambda x: addHtmlTags(x[1] if x[1] else x[2],t) ,firstSub )


def subLists(md):
    # Replace unordered list items
    md = re.sub(r'^\*\s+(.*)?$', lambda x: f'<li id="unorder">{x[1]}</li>', md)
    # Replace ordered list items
    md = re.sub(r'^\d\.\s+(.*)?$', lambda x: f'<li>{x[1]}</li>', md)
    # Wrap lists in <ul> tags
    return md

def correctLists(md):
    md = re.sub(r'((<li>.*?</li>\n*)+)', lambda x : f'<ol>\n{x[1]}</ol>\n', md)
    return re.sub(r'((<li id="unorder">.*?</li>\n*)+)', lambda x : f'<ul>\n{x[1]}</ul>\n', md)


def main():
    #return re.sub(r'(\d+)\s*pl',lambda x:  str(int(x[1]) *2.54) + " cm",linha)
    leitura = sys.stdin
    if len(sys.argv) > 1:
        print("Foi passado pelo menos um argumento")
        leitura = open(sys.argv[1],"r")

    markdownToHtml(leitura)
    


if __name__ == '__main__':
    main()