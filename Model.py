# 推文的結構 推/噓、推文者、推文內容、時間
class PushInfo:
    def __init__(self, tag, userid, content, time,ip=''):
        self.tag = tag
        self.userid = userid
        self.content = content
        self.time = time
        self.ip = ip

