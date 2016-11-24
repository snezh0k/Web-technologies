import urlparse

def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    params = urlparse.parse_qsl(environ["QUERY_STRING"], keep_blank_values=True)
    
    body = ""
    for k in params:
        body += str(k[0])
        body += "="
        body += str(k[1])
        body += "\n"
    
    start_response(status, headers)
    return [ body ]
