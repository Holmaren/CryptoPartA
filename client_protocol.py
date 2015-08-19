import json

class ClientProtocol:
    def __init__(self, student_id):
        self.student_id = student_id
        self.counter = 1

    # Messages a client can send to a server
    def hello(self):
        msg = { "type": "CLIENT_HELLO", "id": self.student_id, "n": self.counter, "part": "one"}
        return json.dumps(msg).encode('utf-8')

    def dhex_start(self):
        msg = {"type": "CLIENT_DHEX_START", "n": self.counter }
        return json.dumps(msg).encode('utf-8')

    def dhex(self, Yc):
        msg = { "type": "CLIENT_DHEX", "dh_Yc": Yc, "n": self.counter }
        return json.dumps(msg).encode('utf-8')

    def dhex_done(self):
        msg = { "type": "CLIENT_DHEX_DONE", "n": self.counter }
        return json.dumps(msg).encode('utf-8')

    def parse(self, msg):
        m = json.loads(msg)
        return m
