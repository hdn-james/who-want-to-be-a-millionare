class Player(object):
    def __init__(self, username):
        self.username = username
        self.score = 0
        self.isPass = True
        self.isWin = True
        
    def addScore(self, score):
        self.score += score
        
    def isLose(self):
        self.isWin = False
        
    def usePass(self):
        self.isPass = False