import pymysql
import datetime 
import time 
import testclass as tc
import testsentiment as ts

#Connect DB 
#SET SQL_SAFE_UPDATES = 0;
#sudo launchctl limit maxfiles 1024 unlimited


def save_into_db(rcd) :
    # Analyze the Classification 
    myrcd = rcd
    mycat = tc.analyzeclass(myrcd[2])
    if mycat == False :
        myclassify_name = 'NO CLASS'
        myclassify_confidence = -1.00
    else :
        myclassify_name = mycat.name
        myclassify_confidence = mycat.confidence
    #print(type(myclassify_confidence))
    # Analyze the Sentiment 
    mysen = ts.analyzesentiment(myrcd[2])
    if mysen == False :
        mysentiment_score = -100.00
        mysentiment_magnitude = -100.00
    else :
        mysentiment_score = mysen.score
        mysentiment_magnitude = mysen.magnitude

    processnow = datetime.datetime.now()
    processnow = processnow.strftime("%Y-%m-%d %H:%M:%S")
    mysql = 'insert into twitterscraper_merged_new1_nlp1(myindex,mydatetime,mytext,sentiment,magnitude,classify_name,classify_confidence,processdatetime,processind) values("%s","%s","%s","%s","%s","%s","%s","%s","%s")' \
        %(myrcd[0],
        pymysql.escape_string(myrcd[1]),
        pymysql.escape_string(myrcd[2]),
        mysentiment_score,
        mysentiment_magnitude,
        pymysql.escape_string(myclassify_name),
        myclassify_confidence,
        processnow,
        'Y'
        )
    print(mysql)
    try:
        cursor.execute(mysql)
        #db.commit()
    except:
        print("*****************************error at sql %s while save data into DB" %sql)  

db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='Max24680',
                             db='MaxDB2',
                             charset='utf8')
cursor =db.cursor()
#create_db()

#newID ='1003328970069331968'
#cursor.execute('SELECT * FROM twitterscraper_filtered WHERE ID < "'+newID+'"')
cursor.execute('select * from twitterscraper_merged_new1 where myindex not in (select myindex from twitterscraper_merged_new1_nlp1)')
results = cursor.fetchall()
count = 0


for rcd in results :
    print('=' * 20)
    print('Index:',rcd[0])
    print('datetime:',rcd[1])
    print('text:',rcd[2])
    save_into_db(rcd)
    #time.sleep(10)
    count= count + 1 
    if count % 100 == 0 :
        db.commit()
        print('Pausing for a bit...count is',count)
        time.sleep(20)
    #if count == 3 :
    #    break 

db.close()