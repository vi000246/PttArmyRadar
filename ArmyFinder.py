# 用來比對出網軍的邏輯
from PttArmyRadar import Model
from faker import Faker
from collections import Counter
import random
from PttArmyRadar import PTT
from itertools import groupby

class ArmyFinder:
    def __init__(self,PushList):
        self.PushList = PushList # 完整推文訊息
        self.telnetServer = None # telnet的執行個體 防止重覆呼叫

    # 移除推文list中的重覆資料(只有同帳號&同IP才移除)和作者帳號 回傳list [PushInfo(...),...]
    def RemovePustListDuplicateDataAndAuthorId(self, authorid):
        self.PushList = [x for x in list(set(self.PushList)) if x.userid != authorid]

    # 如果ip是空的 補上去(先執行完RemoveDuplicateData再執行這步)
    def FillIpInPushList(self):
        for obj in self.PushList:
            if not obj.ip:
                if not self.telnetServer:
                    self.telnetServer = PTT.PTTParser()
                # 取得ip 登入次數 發文篇數
                ip,logintimes,postcount = self.telnetServer.GetUserInfo(obj.userid)
                obj.ip = ip

    # 找出PushList中 跟作者ip一樣的帳號 自PushList中刪除 並回傳符合的list
    def GetUserIdSameAsAuthorIP(self,authorip):
        authoripList = []
        for obj in self.PushList.copy():
            if obj.ip == authorip:
                i = self.PushList.index(obj)
                authoripList.append(self.PushList.pop(i))

        return authoripList


    # 輸入[PushInfo(),...] 找出重覆的IP  (需要在GetUserIdSameAsAuthorIP之後呼叫)
    # 回傳格式[[(IP,出現次數),[PushInfo()...]],[....],...]
    def GetDuplicateIP(self):
        grouplist = []
        for g, items in groupby(sorted(self.PushList), key=lambda a: a.ip):
            listitems = list(items)
            if len(listitems) > 1:
                grouplist.append([(g,len(listitems)),listitems])

        return grouplist





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
    finder.RemovePustListDuplicateDataAndAuthorId('john')
    finder.FillIpInPushList()
    print("和作者相同ip的帳號",finder.GetUserIdSameAsAuthorIP('140.112.1.9'))
    print(finder.GetDuplicateIP())

    # print(finder.tupleList)

    # for i in FakeData:
    #     print(i.tag,i.userid,i.content,i.time,i.ip)