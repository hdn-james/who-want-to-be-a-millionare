class Player():
    def __init__(self, username, port):
        self.username = username
        self.port = port
        self.score = 0
        self.isPass = True
        self.isWin = True

    def get_username(self):
        return self.username

    def get_port(self):
        return self.port

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
