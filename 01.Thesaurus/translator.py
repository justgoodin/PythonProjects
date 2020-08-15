from difflib import get_close_matches
import mysql.connector
import keyword

connector = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = connector.cursor()

def translate(word):
    cursor.execute(f"SELECT * FROM Dictionary WHERE Expression ='{word}'")
    results = cursor.fetchall()
    if results:
        output = [False,results]
    else:
        cursor.execute(f"SELECT * FROM Dictionary")
        results = cursor.fetchall()
        match = get_close_matches(word,keyword.kwlist)
        #print(results[0])
        output = [True,match[0]]
    
    return output

#translate("rainn")