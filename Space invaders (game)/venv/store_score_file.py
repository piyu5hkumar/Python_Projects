import sqlite3


class MyDataBase:
    def __init__(self):
        self.conn = sqlite3.connect('stored_data.db')
        self.curr = self.conn.cursor()

    def checkUser(self, user):
        data = list(self.curr.execute(r"SELECT * FROM all_score WHERE user = '{}'".format(user)))
        if len(data) > 0:
            return True
        else:
            return False

    def insertDB(self, user, score, date):
        if self.checkUser(user) == True:
            previousScore = list(self.curr.execute(r"SELECT score FROM all_score WHERE user = '{}'".format(user)))
            if previousScore[0][0] < score:
                self.curr.execute(r"UPDATE all_score SET score = {} WHERE user = '{}'".format(score, user))
        else:
            self.curr.execute("INSERT INTO all_score VALUES (?,?,?)", (user, score, date))
        self.conn.commit()

    def highScore(self):  # SELECT * FROM all_score WHERE score =
        maxScore = list(self.curr.execute('SELECT max(score) FROM all_score'))[0][0]
        maxScoreData = list(self.curr.execute(r'SELECT * FROM all_score WHERE score ={}'.format(maxScore)))
        return maxScoreData[0]

    def clearRecords(self):
        self.curr.execute('DELETE FROM all_score')
        conn.commit()

    def allRecords(self):
        for row in self.curr.execute('SELECT * FROM all_score'):
            print(row)


DATABASE = MyDataBase()
