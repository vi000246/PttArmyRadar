# 推文的結構 推/噓、推文者、推文內容、時間
class PushInfo:
    def __init__(self, tag, userid, content, time,ip=''):
        self.tag = tag
        self.userid = userid
        self.content = content
        self.time = time
        self.ip = ip
    def __eq__(self, other):
      return self.userid == other.userid and self.ip==other.ip

    def __hash__(self):
      return hash(('userid', self.userid, 'ip', self.ip))

    def __repr__(self):
      return str(self.userid) + ' ' + str(self.ip)

    def __lt__(self, other):
        return self.ip < other.ip

