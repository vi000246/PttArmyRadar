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


    def GetUserIP(self,userid):
        ErrorCode, UserInfo = self.PTTBot.getUserInfo(userid)
        ip = None

        if ErrorCode == self.PTTBot.NoUser:
            self.PTTBot.Log('No such user')

        if ErrorCode != self.PTTBot.Success:
            self.PTTBot.Log('getUserInfo fail error code: ' + str(ErrorCode))
        else:
            ip = UserInfo.getLastIP()

        return ip


if __name__ == '__main__':
    a = PTTParser()
    print(a.GetUserIP('vi000246'))
    print(a.GetUserIP('digforapples'))
    print(a.GetUserIP('F7'))
    print(a.GetUserIP('you cant find this account'))
    a.PTTBot.logout()