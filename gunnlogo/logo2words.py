from manim import *
class Run(Scene):
    def construct(self):

        logo = SVGMobject("img/gunnlogo.svg").scale(3)
        for piece in logo:
            piece.set_color("#bf1e2e")

        words = Text("GUNN", color="#bf1e2e", font="Georgia", size=5)

        self.add(logo)

        self.wait(0.5)

        self.play(
            Rotating(logo, radians=-PI/2 + 4*PI, run_time=2, rate_func=smooth),
        )

        self.play(
            Transform(logo[0], words[1], run_time=1),
            Transform(logo[1], words[0], run_time=1),
            Transform(logo[2], words[2], run_time=1),
            Transform(logo[3], words[3], run_time=1),
        )