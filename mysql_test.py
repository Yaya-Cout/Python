def main():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="yaya.cout",
        password="password",
        database="yaya_cout"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        print(x)

    print("\n")

    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)

    mydb.commit()

    # mycursor = mydb.cursor()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


if __name__ == "__main__":
    main()
