from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("root", "root", ".", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()
print(f'User: root Password: root')