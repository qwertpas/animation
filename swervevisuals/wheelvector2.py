from manim import *
from numpy import arctan2, diff, sign
from numpy.linalg import norm
from typing_extensions import runtime

class Run(MovingCameraScene):

    def setup(self):
        MovingCameraScene.setup(self)



    def construct(self):

        robot = Square(fill_color=BLUE, fill_opacity=1, color=DARK_BLUE).move_to(DOWN * 1 + LEFT * 1)

        center = 1.6 * LEFT + 2 * UP

        turncenter = Dot(color=RED).move_to(center)
        arrow = Arrow(robot.get_center(), center, buff=0, color=WHITE)
        radiuslabel = MathTex("\\vec{r}", size=0.5).next_to(arrow, ORIGIN).shift(LEFT * 0.3)

        pos0 = np.array([0.8*RIGHT + 0.8*UP])
        vec0 = (center - robot.get_center() - pos0)[0]
        turncircle0 = Circle().move_to(center).scale(norm(vec0)).set_stroke(color=YELLOW, width=1)

        robotdot = Dot(robot.get_center())

        module0dot = Dot(robot.get_center() + pos0, color=GREEN_E)

        placement = Arrow(robot.get_center(), module0dot.get_center(), buff=0, color=GREEN_E)
        placementlabel = MathTex("\\vec{p}", size=0.5).next_to(module0dot.get_center(), RIGHT).shift(0.8*LEFT + DOWN*0.1)

        wheeltotc = Arrow(module0dot.get_center(), arrow.get_end(), buff=0, color=BLUE)
        wheeltotclabel = MathTex("\\vec{r_w}", size=0.5).next_to(wheeltotc.get_center(), RIGHT)


        self.camera_frame.scale(0.55).move_to(module0dot.get_center() + UP*1.1 + LEFT*0.8)

        self.add(turncenter, turncircle0, robotdot, module0dot, arrow, radiuslabel, placement, placementlabel, wheeltotc, wheeltotclabel)

        self.wait(0.5)

        self.play(
            FadeOut(robotdot),
            FadeOut(arrow),
            FadeOut(radiuslabel),
            FadeOut(placement),
            FadeOut(placementlabel),
        )

        self.play(
            Rotating(module0dot, radians=PI/4, about_point=center, run_time=2, rate_func=wiggle),
            Rotating(wheeltotc, radians=PI/4, about_point=center, run_time=2, rate_func=wiggle),
            Rotating(wheeltotclabel, radians=PI/4, about_point=center, run_time=2, rate_func=wiggle),
        )

        angvel = CurvedArrow(0.2*RIGHT + 0.4 * DOWN, 0.4 * LEFT + 0.6*UP, color=RED).move_arc_center_to(center)
        angvellabel = Text("ω", size=0.5).next_to(angvel, RIGHT*0.4)

        self.play(
            ShowCreation(angvel),
            ShowCreation(angvellabel)
        )

        wheelvel = wheeltotc.copy().set_color(ORANGE).rotate(-PI/2, about_point=module0dot.get_center()).scale_about_point(0.6, module0dot.get_center())
        wheelvellabel = MathTex("\\vec{v_w}", size=0.5).next_to(wheelvel, ORIGIN).shift(DOWN*0.3)
        rightangle = Rectangle(height=0.2, width=0.2, stroke_width=6).next_to(module0dot, ORIGIN).shift(RIGHT*0.04 + UP*0.14).rotate(wheelvel.get_angle())


        self.play(
            ShowCreation(wheelvel),
            ShowCreation(wheelvellabel),
            ShowCreation(rightangle),
        )


        sumeq = MathTex(
            "\\vec{v_w}",
            "=(",
            "\\vec{r_w}",
            "\\omega",
            ").rot(-90^{\circ })"
        ).move_to(RIGHT*1 + DOWN*0.8).scale(0.6)

        sumeq[0].set_color(ORANGE)
        sumeq[2].set_color(BLUE)
        sumeq[3].set_color(RED)

        self.play(
            ShowCreation(sumeq, run_time=2)
        )

        self.wait(0.5)

        self.play(
            Transform(wheeltotc.copy(), wheelvel, run_time=3)
        )

        self.wait(1)

