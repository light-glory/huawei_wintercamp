import pymysql


def insert(name: str, age: int):
    try:
        insert_sql = "insert into huawei(name, age) values(%s,%s);"
        cursor.execute(insert_sql, (name, age))
    except:
        db.rollback()
    db.commit()


def select(name: str):
    select_sql = "select * from huawei where name = %s"
    cursor.execute(select_sql, (name,))
    for col in cursor.description:
        print(col[0], end='\t')
    print('\n---------')
    for row in cursor:
        print(row)
    print('\n')


def select_all():
    all_sql = "select * from huawei"
    cursor.execute(all_sql)
    for col in cursor.description:
        print(col[0], end='\t')
    print('\n------------')
    for row in cursor:
        print(row)
    print('\n')


def delete(argv):
    try:
        if type(argv) == int:
            delete_sql = 'delete from huawei where age = %s'
            cursor.execute(delete_sql, (argv,))
        elif type(argv) == str:
            delete_sql = 'delete from huawei where name = %s'
            cursor.execute(delete_sql, (argv,))
    except:
        db.rollback()
    db.commit()


def update(old, new):
    try:
        update_sql = 'update huawei SET name=%s, age=%s where name=%s and age=%s'
        cursor.execute(update_sql, (new[0], new[1], old[0], old[1]))
    except:
        db.rollback()
    db.commit()


def innerjoin():
    cursor.execute("SELECT * from huawei INNER JOIN records ON huawei.name=records.name")
    for col in cursor.description:
        print(col[0], end='\t')
    print('\n---------')
    for row in cursor:
        print(row)
    print('\n')


def leftjoin():
    cursor.execute("SELECT * from huawei LEFT JOIN records ON huawei.name=records.name")
    for col in cursor.description:
        print(col[0], end='\t')
    print('\n---------')
    for row in cursor:
        print(row)
    print('\n')


param = {
    'host': "localhost",
    'port': 3306,
    'db': 'huawei',
    'user': 'root',
    'password': '123654',
    'charset': 'utf8',
}

db = pymysql.connect(**param)
cursor = db.cursor()

# here we use those functions

db.close()
