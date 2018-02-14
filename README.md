# PttArmyRadar
PTT網軍、業配文查詢器  

判斷網軍演算法
1. 取得推文清單
2. 取得推文者IP
3. 移除推文名單中 重覆相同帳號及IP，以及作者帳號
4. 取出和作者同IP的推文名單 並從推文名單中刪除
5. 計算出剩下的推文名單同IP出現的次數做排序


requirement:
* pip install PTTLibrary
* pip install Faker