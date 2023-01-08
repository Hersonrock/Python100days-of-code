from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score= int(self.read_file())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            self.write_file(self.high_score)
        self.score=0
        self.update_scoreboard()

    def read_file(self):
        score_file = open("E:\Python 100 days\Day24_files_diectories_paths\Snake+Project+Code+from+Day+21\data.txt")
        raw_file_content= score_file.read()
        score_file.close()
        return raw_file_content

    def write_file(self,score):
        score_file = open("E:\Python 100 days\Day24_files_diectories_paths\Snake+Project+Code+from+Day+21\data.txt",mode="w")
        score_file.write(str(score))
        score_file.close()

        


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
