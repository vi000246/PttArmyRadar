import re
import requests
from lxml import etree
from PttArmyRadar import Model

# 取得網頁版PTT的推文名單與作者名單
class WebPttParser:
    def __init__(self, url):
        url = url.replace(" ", "")
        if not re.match("^https:\/\/www\.ptt\.cc\/bbs\/[A-Za-z_-]+\/M\.[\d]+\.A\.[\w]+\.html$",url):
            raise Exception('請輸入web版PTT的文章網址 範例:https://www.ptt.cc/bbs/(看板名)/M.1234567890.A.D9B.html')
        self.url = url
        self.content = None # 儲放html
        self.etree = None # xpath的物件 用來儲放html dom樹

    # 取得文章的html
    def GetContent(self):
        cookie = {'over18': '1'}

        r = requests.get(self.url, cookies=cookie)
        self.content = r.text
        self.etree = etree.HTML(r.text)


    # 取得推文名單 回傳List<Model.PushInfo>
    def GetPushList(self):
        PushList = []

        if not self.content:
            raise Exception('無法取得文章html')
        # print(self.content)
        pushDiv = self.etree.xpath('//div[contains(@class, "push")]')

        for pushline in pushDiv:
            tag = pushline.xpath('./span[contains(@class, "push-tag")]/text()')[0]
            userid = pushline.xpath('./span[contains(@class, "push-userid")]/text()')[0]
            content = pushline.xpath('./span[contains(@class, "push-content")]/text()')[0]
            # 取出ip(如果有的話)跟推文時間
            timeAndIP = re.search('(?P<ip>\d+\.\d+\.\d+\.\d+)?.*(?P<time>\d{2}\/\d{2}\s\d{2}:\d{2})',
                                  pushline.xpath('./span[contains(@class, "push-ipdatetime")]/text()')[0])

            PushList.append(Model.PushInfo(tag, userid, content, timeAndIP.group("time"), timeAndIP.group("ip")))

        for i in PushList:
            print(i.tag,i.userid,i.content,i.time,i.ip)

        return PushList

    # 取得文章作者資訊 回傳使用者帳號、IP
    def GetAuthorInfo(self):
        authorId = re.search('^(\w+)(?=\s\(.*\))',self.etree.xpath('//span[@class="article-meta-value"]/text()')[0])
        userFrom = re.search('批踢踢實業坊\(ptt\.cc\), 來自: (\d+\.\d+\.\d+\.\d+)', self.content)
        print("作者:"+authorId.group(1))
        print("ip:"+userFrom.group(1))
        return authorId.group(1), userFrom.group(1)







if __name__ == '__main__':
    # a = WebPttParser("https://www.ptt.cc/bbs/Gossiping/M.1518492647.A.08F.html")
    a = WebPttParser("https://www.ptt.cc/bbs/OverWatch/M.1518495124.A.319.html  ")
    a.GetContent()
    a.GetAuthorInfo()
    a.GetPushList()
