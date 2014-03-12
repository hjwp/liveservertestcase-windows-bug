This Gist is just a minimal repro of a bug (I think) in Django's LiveServerTestCase.

Once a site has some static files (eg CSS), then clicking on a link produces an ugly uncaught exception from the LiveServer thread, like this:

```
Exception happened during processing of request from ('127.0.0.1', 1925)
Traceback (most recent call last):
  File "c:\Python33\lib\site-packages\django\test\testcases.py", line 1035, in _handle_request_noblock
    self.process_request(request, client_address)
  File "c:\Python33\lib\socketserver.py", line 332, in process_request
    self.finish_request(request, client_address)
  File "c:\Python33\lib\socketserver.py", line 345, in finish_request
    self.RequestHandlerClass(request, client_address, self)
  File "c:\Python33\lib\site-packages\django\core\servers\basehttp.py", line 126
, in __init__
    super(WSGIRequestHandler, self).__init__(*args, **kwargs)
  File "c:\Python33\lib\socketserver.py", line 666, in __init__
    self.handle()
  File "c:\Python33\lib\wsgiref\simple_server.py", line 118, in handle
    self.raw_requestline = self.rfile.readline()
  File "c:\Python33\lib\socket.py", line 297, in readinto
    return self._sock.recv_into(b)
ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
```
