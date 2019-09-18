import pymysql
import datetime 
import time 
import testclass as tc
import testsentiment as ts

#Connect DB 

def create_db() :
    # Create New Table
    cursor.execute("DROP TABLE IF EXISTS twitterscrapernew")
    sql="""CREATE TABLE twitterscrapernew (
        ID char(20) NOT NULL,
        url  varchar(140) NOT NULL,
        datetime  varchar(22) DEFAULT NULL,
        text  varchar(280) DEFAULT NULL,
        user_id  char(20) NOT NULL,
        usernameTweet varchar(20) NOT NULL,
        sentiment FLOAT NULL,
        magnitude FLOAT NULL,
        classify_name varchar(280) DEFAULT NULL,
        classify_confidence FLOAT NULL,
        processdatetime DATETIME NOT NULL,
        processind char(1) NULL
        )  DEFAULT CHARSET=UTF8MB4 """
    cursor.execute(sql)

def save_into_db(rcd) :
    # Analyze the Classification 
    myrcd = rcd
    mycat = tc.analyzeclass(myrcd[3])
    if mycat == False :
        myclassify_name = 'NO CLASS'
        myclassify_confidence = -1.00
    else :
        myclassify_name = mycat.name
        myclassify_confidence = mycat.confidence
    #print(type(myclassify_confidence))
    # Analyze the Sentiment 
    mysen = ts.analyzesentiment(myrcd[3])
    if mysen == False :
        mysentiment_score = -100.00
        mysentiment_magnitude = -100.00
    else :
        mysentiment_score = mysen.score
        mysentiment_magnitude = mysen.magnitude

    processnow = datetime.datetime.now()
    processnow = processnow.strftime("%Y-%m-%d %H:%M:%S")
    mysql = 'insert into twitterscrapernew(ID,url,datetime,text,user_id,usernameTweet,sentiment,magnitude,classify_name,classify_confidence,processdatetime,processind) values("%s","%s","%s","%s","%s","%s","%f","%f","%s","%f","%s","%s")' \
        %(pymysql.escape_string(myrcd[0]),
        pymysql.escape_string(myrcd[1]),
        pymysql.escape_string(myrcd[2]),
        pymysql.escape_string(myrcd[3]),
        pymysql.escape_string(myrcd[4]),
        pymysql.escape_string(myrcd[5]),
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

newID ='1161767691646115840'
cursor.execute('SELECT * FROM twitterscraper WHERE ID < "'+newID+'"')
results = cursor.fetchall()
count = 0


for rcd in results :
    print('=' * 20)
    print('ID:',rcd[0])
    print('URL:',rcd[1])
    print('datetime:',rcd[2])
    print('text:',rcd[3])
    print('user_id:',rcd[4])
    print('usernameTweet:',rcd[5])
    save_into_db(rcd)
    #time.sleep(10)
    count= count + 1 
    if count % 10 == 0 :
        print('Pausing for a bit...count is',count)
        time.sleep(5)
    #if count == 3 :
    #    break 

db.close()