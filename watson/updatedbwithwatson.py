import pymysql
import datetime 
import time 
import analyzetone as atone

#Connect DB 
#SET SQL_SAFE_UPDATES = 0;
#sudo launchctl limit maxfiles 1024 unlimited


def save_into_db(rcd) :

    # Analyze the Tones 
    myrcd = rcd
    mytone = atone.testtone(myrcd[3])
    if mytone == False :
        mytones_list = 'NO TONES'
    else :
        mytones_list = str(mytone)

    processnow = datetime.datetime.now()
    processnow = processnow.strftime("%Y-%m-%d %H:%M:%S")
    mysql = 'insert into twitterscraper_filtered_nlp_watson(ID,url,tweetdatetime,tweettext,user_id,usernameTweet,tones_list,processdatetime,processind) values("%s","%s","%s","%s","%s","%s","%s","%s","%s")' \
        %(pymysql.escape_string(myrcd[0]),
        pymysql.escape_string(myrcd[1]),
        pymysql.escape_string(myrcd[2]),
        pymysql.escape_string(myrcd[3]),
        pymysql.escape_string(myrcd[4]),
        pymysql.escape_string(myrcd[5]),
        pymysql.escape_string(mytones_list),
        processnow,
        'Y'
        )
    print(mysql)
    try:
        cursor.execute(mysql)
        db.commit()
    except:
        print("*****************************error at sql %s while save data into DB" %sql)  

db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='Max24680',
                             db='MaxDB',
                             charset='utf8')
cursor =db.cursor()
#create_db()

#newID ='1003328970069331968'
#cursor.execute('SELECT * FROM twitterscraper_filtered WHERE ID < "'+newID+'"')
cursor.execute('select * from MaxDB.twitterscraper_filtered where ID not in (select ID from MaxDB.twitterscraper_filtered_nlp_watson)')
results = cursor.fetchall()
count = 0


for rcd in results :
    print('=' * 20)
    print('ID:',rcd[0])
    print('URL:',rcd[1])
    print('datetime:',rcd[2])
    print('tweettext:',rcd[3])
    print('user_id:',rcd[4])
    print('usernameTweet:',rcd[5])
    save_into_db(rcd)
    #time.sleep(10)
    count= count + 1 
    if count % 100== 0 :
        #db.commit()
        print('Pausing for a bit...count is',count)
        time.sleep(20)
    #if count == 3 :
    #    break 

db.close()