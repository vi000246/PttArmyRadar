# 處理和Telnet有關的所有logic
from PTTLibrary import PTT
import yaml

class PTTParser:
    def __init__(self):
        f = open('config.yaml', encoding = 'utf8')
        config = yaml.load(f)
        self.PTTBot = PTT.Library(config['account'], config['password'], kickOtherLogin=False)
        if not self.PTTBot.isLoginSuccess():
            self.PTTBot.Log('登入失敗')

    # 回傳使用者的(IP,登入次數,文章數)
    def GetUserInfo(self,userid):
        ErrorCode, UserInfo = self.PTTBot.getUserInfo(userid)
        if ErrorCode == self.PTTBot.NoUser:
            self.PTTBot.Log('No such user')

        if ErrorCode != self.PTTBot.Success:
            self.PTTBot.Log('getUserInfo fail error code: ' + str(ErrorCode))
            return None,None,None
        else:
            return UserInfo.getLastIP(),str(UserInfo.getLoginTime()),str(UserInfo.getPost())



if __name__ == '__main__':
    a = PTTParser()
    print(a.GetUserInfo('vi000246'))
    print(a.GetUserInfo('digforapples'))
    print(a.GetUserInfo('F7'))
    print(a.GetUserInfo('you cant find this account'))
    a.PTTBot.logout()