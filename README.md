# PttArmyRadar
PTT網軍、業配文查詢器  

判斷網軍演算法
1. 取得推文清單
2. 移除推文名單中，相同的(帳號&IP 註:若IP為空 視為同IP)，或作者帳號
3. 取得推文者IP
4. 取出和作者同IP的推文名單 並從推文名單中刪除
5. 取得剩下的推文名單中，同IP出現次數大於1的資料做排序


requirement:
* pip install PTTLibrary
* pip install Faker