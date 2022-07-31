starturl = input('Enter web url or enter: ')
if ( len(starturl) < 1 ) : starturl = 'http://www.dr-chuck.com/'
if ( starturl.endswith('/') ) :
    starturl = starturl[:-1]
    print(starturl)
    web = starturl
if ( starturl.endswith('.htm') or starturl.endswith('.html') ) :
    pos = starturl.rfind('/')
    print(pos)
    web = starturl[:pos]
    print(web)
