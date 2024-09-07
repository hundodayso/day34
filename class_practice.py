from uuid import uuid4


class Cable:
    def __init__(self, cable_name):
        self.cable_name = cable_name
        self.uid = uuid4().hex
        self.length = 10
        self.type = "4E4"
        self.impedance = complex(0.35 + 0.015)
        self.upstream_connection = None

    def connect_upstream(self):
        pass
