class Player():
    def __init__(self, username, cookie):
        self.username = username
        self.cookie = cookie
        self.score = 0
        self.isPass = True
        self.isWin = True

    def get_username(self):
        return self.username

    def get_score(self):
        return self.score

    def get_status(self):
        return (self.isPass, self.isWin)

    def addScore(self, score):
        self.score += score

    def isLose(self):
        self.isWin = False

    def usePass(self):
        self.isPass = False
