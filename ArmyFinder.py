# 用來比對出網軍的邏輯
from PttArmyRadar import Model
from faker import Faker
from collections import Counter

class ArmyFinder:

    # 輸入List<PushInfo> 移除重覆帳號，找出重覆的IP
    def FindDuplicateIP(self,PushList):
        # 移除重覆帳號


        a = Counter(tok.ip for tok in PushList)
        print(a)

    # 將推文list中 移除重覆帳號 ip為空的帳號補上IP
    def FillIpInPushList(self,PushList):
        # 移除重覆帳號
        accounts = set([info.userid for info in PushList])
        print(accounts)


# 產生假資料
def FakeData(number):
    PushList = []
    fake = Faker('zh_TW')
    iplist = ['127.0.0.1','61.65.18.65','98.321.12.221','140.112.1.9','120.36.15.60','210.160.99.3','118.336.12.1',
              '123.964.123.41','140.116.12.1','140.118.123.2','140.119.68.1','140.117.3.1','212.123.12.10','210.127.51.1',
              '135.651.123.13','128.98.36.1','123.68.54.1','21.56.1.5','216.369.25.1','212.254.52.1','215.59.11.1','220.598.14.1'
              ]
    accountList = ['john','amy','lia','julia','asuka','roy','joe','ben']
    for i in range(0,number):
        PushList.append(Model.PushInfo(fake.word(ext_word_list=['推','噓','→']),
                                       # fake.user_name(),
                                       fake.word(ext_word_list=accountList),
                                       fake.text(max_nb_chars=20, ext_word_list=None),
                                       fake.date(pattern="%Y-%m-%d", end_datetime=None),
                                       # fake.ipv4(network=False)
                                       fake.word(ext_word_list=iplist)
                                       ))
    
    return PushList

if __name__ == '__main__':
    FakeData = FakeData(300)
    finder = ArmyFinder()
    # finder.FindDuplicateIP(FakeData)
    finder.FillIpInPushList(FakeData)

    # for i in FakeData:
    #     print(i.tag,i.userid,i.content,i.time,i.ip)