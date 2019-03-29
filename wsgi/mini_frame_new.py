def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8'), ("server", "xixihaha")])
    return 'hello wsgi 我爱你中国'
