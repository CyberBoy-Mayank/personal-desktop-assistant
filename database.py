# Modules
from sqlite3 import connect


def createConnection():
    """For connect to the database."""
    connection = connect("DataBase\\memory.db")
    return connection


def getQuestionsAndAnswers():
    """Retrieve questions and answers from the database."""
    con = createConnection()
    cur = con.cursor()
    cur.execute("SELECT * FROM questionsAndAnswers")
    return cur.fetchall()


def insertQuestionAndAnswer(question, answer):
    """Insert questions and its answers."""
    con = createConnection()
    cur = con.cursor()
    # insert into table-name values('question','answer')
    query = "INSERT INTO questionsAndAnswers values('" + question + "', '" + answer + "')"
    cur.execute(query)
    con.commit()


def getAnswerFromMemory(question: str):
    """Retrieve question's answers from the database."""
    rows = getQuestionsAndAnswers()
    answer = str("")
    for row in rows:
        if row[0] in question:
            answer = row[1]
            break
    return answer


def getValue(table: str, field: str):
    """Retrieve values."""
    con = createConnection()
    cur = con.cursor()
    query = f"select value from {table} where name = '{field}'"
    cur.execute(query)
    return cur.fetchall()[0][0]


def updateValue(table: str, field: str, newValue: str):
    """Update values."""
    con = createConnection()
    cur = con.cursor()
    query = f"update {table} set value = '{newValue}' where name = '{field}'"
    cur.execute(query)
    con.commit()
