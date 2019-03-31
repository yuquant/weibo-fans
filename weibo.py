# -*- coding: utf-8 -*-
"""
Author : Jason
Github : https://github.com/yuquant
Description : 微博批量关注,目前只能手动获取cookie
"""
import requests
import time
import re
import random
from bs4 import BeautifulSoup
import json

def main():
    num = 0
    for public_id in PUBLIC_IDS:
        print(public_id)
        for page in range(1, 6):
            url = 'https://weibo.com/p/{}/follow?relate=fans&page={}#Pl_Official_HisRelation__50'.format(public_id,
                                                                                                         page)
            headers = {'Host': 'weibo.com',
                       'Connection': 'keep-alive',
                       'Pragma': 'no-cache',
                       'Cache-Control': 'no-cache',
                       'Upgrade-Insecure-Requests': '1',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'zh-CN,zh;q=0.9',
                       'Cookie': COOKIE}
            print(page)
            try:
                content = requests.get(url, headers=headers)
                # soup = BeautifulSoup(content.text, 'html.parser')
                # target = soup.find_all('li')
                uid = re.findall(pattern='地址<\\\/em><span>(.*?)<\\\/span>.*?&uid=(\d{10})&location=', string=content.text)
                # uid = re.findall(pattern='地址<\\\/em><span>(.*?)<\\\/span>', string=content.text)
                bj_uid = [x[1] for x in uid if PLACE in x[0]]
                # uids = re.findall(pattern='&uid=(\d{10})&fnick', string=content.text)
            except Exception as e:
                print(e)
            headers = {'Host': 'weibo.com',
                       'Connection': 'keep-alive',
                       'Content-Length': '307',
                       'Origin': 'https://weibo.com',
                       'X-Requested-With': 'XMLHttpRequest',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
                       'Content-Type': 'application/x-www-form-urlencoded',
                       'Accept': '*/*',
                       'Referer': url,
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'zh-CN,zh;q=0.9',
                       'Cookie': COOKIE}
            # if not uids:
            #     print('请更新cookie')
            for uid in bj_uid:

                time.sleep(random.randint(1, 10))
                try:
                    data = 'uid={}&objectid=&f=1&extra=&refer_sort=fanslist&refer_flag=1005050008_&location=hisfans_v6&oid=1875333245&wforce=1&nogroup=1&refer_from=relate_fans&special_focus=1&template=8&isrecommend=1&is_special=0&redirect_url=%252Fp%252F1005056980219805%252Fmyfollow%253Fgid%253D4334480753977676%2523place&_t=0'.format(
                        uid)
                    r = requests.post(
                        'https://weibo.com/aj/f/followed?ajwvr=6&__rnd={}'.format(int(time.time() * 1000)),
                        headers=headers,
                        data=data)
                    if '"code":"100000"' not in r.text:
                        print(uid, '关注过多')
                        print('共关注{}个'.format(num))
                        return
                    else:
                        print('已关注', uid, r)
                        num += 1
                except Exception as e:
                    print(e)
    print('共关注{}个'.format(num))


if __name__ == "__main__":
    # 想要复制的微博号id
    PUBLIC_IDS = [
        '1002062964296501',  # 重庆大学计算机学院虎溪校区
        '1002063786221941',  # 重庆大学建管学院研究生
        '1002066034587500',  # 重庆大学新闻学院团委学生会
        '1002062631837083',  # 重庆大学动力工程学院团委
        '1002061997555577',  # 重庆大学物理学院
        '1005052026508553',  # 重庆大学微软学生俱乐部
        '1002062377515894',  # 重大虎溪学生事务
        '1002063089852951',  # 重庆大学电气团委
        '1005052941819733',  # 重庆大学经管学院研究生
        '1002061838006721',  # 重庆大学学生艺术团缙云话剧队
        '1002063357770294',  # 重庆大学摄影俱乐部
        '1002061982186011',  # 重庆大学党委组织部
        '1002061987652387',  # 重庆大学弘深学院
        '1002061984156575',  # 重庆大学通信工程学院
        '1002062419403604',  # 重庆大学计算机协会
        '1002062525439312',  # 重庆大学机械工程学院研究生
        '1002062408618127',  # 重庆大学艺术学院团委学生会
        '1006062779187793',  # 重庆大学吧
        '1005052409494832',  # 重庆大学大数据与软件学院
        '1002061957204342',  # 重庆大学光电学院
        '1002062338781785',  # 重庆大学学生记者团
        '1002061997474471',  # 重庆大学动力工程学院
        '1002062231079062',  # 重庆大学图管会
        '1002062454787062',  # 重庆大学学生艺术团
        '1002061885066331',  # 重庆大学经管学院EDP
        '1002062410180630',  # 重庆大学北京校友会
        '1002062347312477',  # 重庆大学外国语学院flc
        '1002062009093341',  # 重庆大学材料学院
        '1002062185733865',  # 重庆大学电气学生会
        '1002062405118721',  # 重庆大学城环学院
        '1002061237021274',  # 重庆大学新重大之声
        '1002062244790925',  # 重庆大学MBA
        '1002062959394845',  # 重庆大学实习与就业协会
        '1002062424667071',  # 重庆大学学生职业发展协会
        '1002062414502951',  # 重庆大学土木工程学院
        '1002063165471573',  # 重庆大学研究生工作部
        '1002062385015707',  # 重庆大学机械学院
        '1002061982414165',  # 重庆大学法学院
        '1006061739225615',  # 重庆大学爱心社
        '1002062682895125',  # 重庆大学方程式赛车队
        '1002061916940737',  # 重庆大学EMBA
        '1002061947736931',  # 重庆大学建管学院
        '1005052150179835',  # 重庆大学微校园
        '1002061684427313',  # 重庆大学青年志愿者协会
        '1002061906025024',  # 重庆大学新闻学院
        '1002062492805904',  # 重庆大学校友总会
        '1002061984137601',  # 重庆大学公管学院
        '1002062013699140',  # 重庆大学招生办公室
        '1002061919262405',  # 重庆大学虎溪之声
        '1002062259570754',  # 重庆大学电气工程学院
        '1002061833756303',  # 重庆大学学生社团联合会
        '1002061831745354'  # 新重庆大学_上海校友会 
        '1002062423262642',  # 重庆大学勤工助学服务总队
        '1002062127966770',  # 重庆大学环保者协会
        '1002061982202007',  # 重庆大学美视电影学院
        '1002061981005335',  # 重庆大学研究生院
        '1003061651171442',  # 虎溪虎-肖铁岩
        '1005051661057683',  # 重庆大学金镝
        '1002062054538287',  # 重庆大学研究生团委
        '1005052283449054',  # 重庆大学校友录
        '1002061677759264',  # 重庆大学学生工作
        '1002062093458014',  # 重庆大学学生会
        '1002061875333245',  # 重庆大学
        '1002061982692745',  # 重庆大学建筑城规学院
        '1005051650091985',  # 重庆大学出版社
        '1002061987613253',  # 重庆大学虎溪校区
        '1001062319580574',  # 重庆大学微博协会
        '1002062013275930',  # 重庆大学研究生会
        '1002062505724424',  # 重庆大学校园直播间
        '1001061660125537',  # 重庆大学图书馆
        '1002061709728983',  # 重庆大学民主湖论坛
        '1001061709467465',  # 共青团重庆大学委员会

                  ]
    # 每次需要手动关注通过F12获取更新,见[guide.png]
    PLACE = '北京'
    COOKIE = 'SINAGLOBAL=6607525835279.375.1492593520448; __guid=15428400.3316352832784033300.1551532805436.9214; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFA16FqlvpLiPPZ6ZhdYlWl5JpX5KMhUgL.Foq41h5EeK.Reh-2dJLoIc7LxK.L1hML12BLxK-LB.2L1hqLxK-LBKBLBKMLxK-LB-BLBKqLxK-L12eL1KMLxKBLB.2LB-eLxKqL1K-LBo5LxK-LB-BL1KMLxKMLB.zL12qLxKqLBo-L12-LxK-L1hnL1hqLxKBLB.eL1-2t; UOR=login.sina.com.cn,vdisk.weibo.com,login.sina.com.cn; Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; ALF=1585567280; SSOLoginState=1554031283; SCF=ApvnSjuEWEfo3HfrDGBfgEB0qiH4UzEpnNK_XJSTQpjKvow-BOBOCmlnYle88Tuf-iLj1NpkCkuSogylE9hXNrs.; SUB=_2A25xpNLkDeRhGeBH41IT8SfEyzmIHXVS0EMsrDV8PUNbmtBeLU7ZkW9NQbkDQnU1KMlzchcXytbwXrQ408xobue9; SUHB=0C1yw_mLUl15g3; wvr=6; YF-V5-G0=b4445e3d303e043620cf1d40fc14e97a; wb_view_log_6980219805=1920*10801.5; _s_tentry=-; Apache=5238487155394.633.1554031295644; ULV=1554031295660:42:10:1:5238487155394.633.1554031295644:1553304183719; monitor_count=2; YF-Page-G0=4b5a51adf43e782f0f0fb9c1ea76df93|1554031350|1554031296; webim_unReadCount=%7B%22time%22%3A1554031351911%2C%22dm_pub_total%22%3A2%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A3%2C%22msgbox%22%3A0%7D'

    main()
