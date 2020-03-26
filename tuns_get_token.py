## 导入psycopg2包
import psycopg2
import config.postgerl_config as cfp
import sys
import dingdingRobot as ddr


## 连接到一个测试的数据库
conn = psycopg2.connect(database=cfp.sit_postgres_database, user=cfp.sit_postgres_user,password=cfp.sit_postgres_password, host=cfp.sit_postgres_url, port=cfp.sit_postgres_port)
## 建立游标，用来执行数据库操作
cursor = conn.cursor()

def select_postgrel_token(loginid):

    ## 执行SQL SELECT命令
    cursor.execute(r"SELECT token_id,user_id from cmm_token where login_id = '%s' and sys_type='1';"%loginid)

    ## 获取SELECT返回的元组
    rows = cursor.fetchall()
    for row in rows:
        print('token_id =',row[0], 'user_id =', row[1], '\n')


    ddr.dingTalk('测试环境 \n\t login_id:%s \n\t token_id:%s \n\t user_id:%s'%(loginid,row[0],row[1]))

    return rows, row[0], row[1]
    ## 关闭游标
    cursor.close()
    ## 关闭数据库连接
    conn.close()



if __name__ == '__main__':
    select_postgrel_token(sys.argv[1])

    # ddr('测试环境 login_id:%s token_id:%s user_id:%s' % (sys.argv[1],tokenid, userid))
