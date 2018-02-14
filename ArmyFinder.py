# 用來比對出網軍的邏輯
from PttArmyRadar import Model
from faker import Faker
from collections import Counter
import random
from PttArmyRadar import PTT

class ArmyFinder:
    def __init__(self,PushList):
        self.PushList = PushList # 完整推文訊息
        self.tupleList = [] # (userid,ip)的list
        self.telnetServer = None # telnet的執行個體 防止重覆呼叫

    # 移除推文list中的重覆資料(只有同帳號&同IP才移除)和作者帳號 回傳list [(userid,ip),...]
    def RemovePustListDuplicateDataAndAuthorId(self, authorid):
        self.tupleList =  list(set([(x.userid, x.ip) for x in self.PushList if x.userid != authorid]))

    # 如果ip是空的 補上去(先執行完RemoveDuplicateData再執行這步)
    def FillIpInPushList(self):
        for obj in self.tupleList:
            if not obj[1]:
                if not self.telnetServer:
                    self.telnetServer = PTT.PTTParser()

                ip = self.telnetServer.GetUserIP(obj[0])
                self.update_in_tuplelist(obj[0],ip)

    # 依據userid 更新tupleList的ip
    def update_in_tuplelist(self,userid, ip):
        self.tupleList =  [(k, v) if (k != userid) else (userid, ip) for (k, v) in self.tupleList]

    # 找出tuplelist中 跟作者ip一樣的帳號 自tuplelist中刪除 並回傳符合的list
    def GetUserIdSameAsAuthorIP(self,authorip):
        authoripList = []
        for obj in self.tupleList.copy():
            if obj[1] ==authorip:
                i = self.tupleList.index(obj)
                authoripList.append(self.tupleList.pop(i))

        return authoripList


    # 輸入[(userid,ip),...] 找出重覆的IP  (需要在GetUserIdSameAsAuthorIP之後呼叫)
    def FindDuplicateIP(self):
        countlist = Counter(tok[1] for tok in self.tupleList)
        print(countlist)
        a = [(k,v) for k, v in countlist.most_common() if v > 1 ]
        print("重覆的ip",a)



# 產生假資料
def FakeData(number):
    PushList = []
    fake = Faker('zh_TW')
    accountList = [('john','127.0.0.1'),('john','127.0.0.1'),('amy','127.0.0.1'),
                   ('lia','140.112.1.9'),('julia','140.112.1.9'),
                   ('asuka','140.112.1.9'),('roy','140.112.1.9'),('vi000246','140.112.1.9'),('ben','123.964.123.41'),
                   ('yich','127.0.0.1'),('beef','127.0.0.1'),('aloha','235.151.123.1'),('yamaha','235.151.123.1')]
    for i in range(0,number):
        user = random.choice(accountList)
        PushList.append(Model.PushInfo(fake.word(ext_word_list=['推','噓','→']),
                                       # fake.user_name(),
                                       user[0],
                                       fake.text(max_nb_chars=20, ext_word_list=None),
                                       fake.date(pattern="%Y-%m-%d", end_datetime=None),
                                       # fake.ipv4(network=False)
                                       user[1]
                                       ))
    
    return PushList

if __name__ == '__main__':
    FakeData = FakeData(300)
    finder = ArmyFinder(FakeData)
    finder.RemovePustListDuplicateDataAndAuthorId('vi0002467')
    finder.FillIpInPushList()
    print("和作者相同的帳號",finder.GetUserIdSameAsAuthorIP(''))
    finder.FindDuplicateIP()

    # print(finder.tupleList)

    # for i in FakeData:
    #     print(i.tag,i.userid,i.content,i.time,i.ip)