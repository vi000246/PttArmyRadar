# 用來比對出網軍的邏輯
from PttArmyRadar import Model
from faker import Faker
from collections import Counter
import random

class ArmyFinder:
    def __init__(self,PushList):
        self.PushList = PushList

    # 輸入List<PushInfo> 移除重覆帳號，找出重覆的IP
    def FindDuplicateIP(self,UserList):

        a = Counter(tok.ip for tok in self.PushList)
        print(a)

    # 移除推文list中的重覆帳號 回傳list [(userid,ip),...]
    def RemoveDuplicateUserId(self):
        # 移除重覆帳號
        return list(dict((x.userid, x.ip) for x in sorted(self.PushList, key=lambda v: len(v.content))).items())

    # 如果ip是空的 補上去
    def FillIpInUserList(self):
        pass



# 產生假資料
def FakeData(number):
    PushList = []
    fake = Faker('zh_TW')
    accountList = [('john','127.0.0.1'),('amy','61.65.18.65'),('lia','98.321.12.221'),('julia','140.112.1.9'),
                   ('asuka','120.36.15.60'),('roy','210.160.99.3'),('vi000246',None),('ben','123.964.123.41')]
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
    # finder.FindDuplicateIP()
    finder.FillIpInPushList()

    # for i in FakeData:
    #     print(i.tag,i.userid,i.content,i.time,i.ip)