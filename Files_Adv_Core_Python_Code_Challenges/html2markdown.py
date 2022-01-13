import re

def urls(func):
    '''This is the urls function decorator'''
    def wrapper(*args):
        '''This is the wrapper function'''
        url = re.compile(r'<a href="(.*?)">(.*?)</a>')
        f_r = func(*args)
        result = url.sub(r'[\2](\1)', f_r)
        return result
    return wrapper

def paragraphs(func):
    '''This is the paragraphs function decorator'''    
    def wrapper(*args):
        '''This is the wrapper function'''
        paragraph = re.compile(r'(?m)(<p>)(.+?)(</p>)')
        f_r = func(*args)
        if re.findall(r'(</p><p>)', f_r):
            r3sult = re.sub(r'(</p><p>)', r'\n\n', f_r)
            resu1t = re.sub(r'(<p>)', r'', r3sult)
            result = re.sub(r'(</p>)', r'', resu1t)
        else:
            result = paragraph.sub(r'\2', f_r)
        return result
    return wrapper

def space(func):
    '''This is the function decorator space'''
    def wrapper(*args):
        '''This is the wrapper function'''
        space = re.compile(r'(?m)(\s+)')
        f_r = func(*args)
        result = space.sub(r' ', f_r)
        return result
    return wrapper

def italic(func):
    '''This is the function decorator italic'''
    def wrapper(*args):
        '''This is the wrapper function'''
        italic = re.compile(r'(<em>)(.+?)(</em>)')
        f_r = func(*args)
        result = italic.sub(r'*\2*', f_r)
        return result
    return wrapper

@urls
@paragraphs
@space
@italic
def html2markdown(html):
    '''Take in html text as input and return markdown'''
    markdown = html
    return markdown
