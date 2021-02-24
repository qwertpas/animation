from manim import *
from numpy import arctan2, diff, sign
from numpy.linalg import norm

class Run(MovingCameraScene):

    def setup(self):
        MovingCameraScene.setup(self)



    def construct(self):

        vw = MathTex(
            "\\vec{v_w}",
            "=(",
            "\\vec{r_w}",
            "\\omega",
            ").rot(-90^{\circ })"
        ).move_to(LEFT*2.5 + UP*1.5)

        vw[0].set_color(ORANGE)
        vw[2].set_color(BLUE)
        vw[3].set_color(RED)

        self.play(
            ShowCreation(vw)
        )
        self.wait(1)

        rw = MathTex(
            "\\vec{r_w}",
            "=",
            "(\\frac{\\vec{v}}{\\omega})",
            ".rot(90^{\circ })",
            "-",
            "\\vec{p}",
        ).next_to(vw, RIGHT*3)
        rw[2].set_color(RED)
        rw[5].set_color(GREEN_E)
        rw[0].set_color(BLUE)

        self.play(
            ShowCreation(rw)
        )
        self.wait(1)

        combined = MathTex(
            "\\vec{v_w}",
            "=(",
            "(",
            "(\\frac{\\vec{v}}{\\omega})",
            ".rot(90^{\circ })",
            "-",
            "\\vec{p}",
            ")",
            "*\\omega",
            ").rot(-90^{\circ })"
        ).next_to(vw, DOWN).shift(RIGHT*2)
        combined[0].set_color(ORANGE)
        combined[2].set_color(BLUE)
        combined[3].set_color(RED)
        combined[7].set_color(BLUE)
        combined[6].set_color(GREEN_E)
        combined[8].set_color(RED)

        self.play(
            Transform(rw.copy(), combined[2]),
            Transform(rw.copy(), combined[3]),
            Transform(rw.copy(), combined[4]),
            Transform(rw.copy(), combined[5]),
            Transform(rw.copy(), combined[6]),
            Transform(rw.copy(), combined[7]),
            ShowCreation(combined)
        )
        self.wait(1)

        self.play(
            Indicate(combined[2]),
            Indicate(combined[7]),
            Indicate(combined[8]),
        )
        self.wait(1)

        aftome = MathTex(
            "\\vec{v_w}",
            "=",
            "(",
            "\\vec{v}",
            ".rot(90^{\circ })",
            "-",
            "\\omega",
            "\\vec{p}",
            ")",
            ".rot(-90^{\circ })"
        ).next_to(combined, DOWN)
        aftome[0].set_color(ORANGE)
        aftome[3].set_color(RED)
        aftome[7].set_color(GREEN_E)
        aftome[6].set_color(RED)

        self.play(
            Transform(combined.copy(), aftome),
        )
        self.wait(1)

        self.play(
            Indicate(aftome[2]),
            Indicate(aftome[8]),
            Indicate(aftome[9]),
        )
        self.wait(1)

        aftrot = MathTex(
            "\\vec{v_w}",
            "=",
            "\\vec{v}",
            "-",
            "\\omega",
            "\\vec{p}",
            ".rot(-90^{\circ })"
        ).next_to(aftome, DOWN)
        aftrot[0].set_color(ORANGE)
        aftrot[2].set_color(RED)
        aftrot[5].set_color(GREEN_E)
        aftrot[4].set_color(RED)

        self.play(
            Transform(aftome.copy(), aftrot),
        )
        self.wait(1)

        self.play(
            Indicate(aftrot[3]),
            Indicate(aftrot[6]),
        )
        self.wait(1)

        aftcan = MathTex(
            "\\vec{v_w}",
            "=",
            "\\vec{v}",
            "+",
            "\\omega",
            "\\vec{p}",
            ".rot(90^{\circ })"
        ).next_to(aftrot, DOWN*1.2)
        aftcan[0].set_color(ORANGE)
        aftcan[2].set_color(RED)
        aftcan[5].set_color(GREEN_E)
        aftcan[4].set_color(RED)

        self.play(
            Transform(aftrot.copy(), aftcan),
        )

        self.wait(1)

        self.play(
            ShowCreation(SurroundingRectangle(aftcan))
        )
        self.wait(1)
