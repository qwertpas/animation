from manim import *
from manim.mobject.geometry import ArrowTriangleFilledTip
from numpy import sign
class Run(Scene):
    def construct(self):

        robot = Square(fill_color=BLUE, fill_opacity=1, color=DARK_BLUE).move_to(ORIGIN)
        turncenter = Dot(color=RED)
        turncircle = Circle(color=RED).scale(0)
        arrow = Arrow(ORIGIN, robot.get_center(), buff=0, color=WHITE)

        self.add(robot, turncenter, turncircle, arrow)
    
        def wiggle_angle(center):
            self.wait(0.25)

            radius = np.linalg.norm(center)
            new_turncenter = Dot(color=RED).move_to(center)
            new_turncircle = Circle(color=RED).scale(radius).move_to(center)
            new_arrow = Arrow(center, robot.get_center(), buff=0, color=WHITE)
            text = Text("(" + str(round(center[0])) + ", " + str(round(center[1])) + ")", size=0.5)
            if(radius < 5): text.move_to(center + 0.4 * DOWN)
            else: text.move_to(sign(center[1]) * 3 * UP + LEFT * 2)
            self.play(
                Transform(turncenter, new_turncenter),
                Transform(turncircle, new_turncircle),
                Transform(arrow, new_arrow),
                ShowCreation(text)
            )

            self.wait(0.25)

            angle = 1.5 * PI / radius
            if(angle > PI/2): angle = PI/2
            self.play(
                Rotating(robot, radians=angle, about_point=center, run_time=2, rate_func=wiggle),
                Rotating(arrow, radians=angle, about_point=center, run_time=2, rate_func=wiggle)
            )

            self.wait(0.5)
            self.remove(text)

        wiggle_angle(LEFT * 0.0001)

        wiggle_angle(1 * LEFT + 2 * DOWN)

        wiggle_angle(3 * LEFT)

        wiggle_angle(2 * UP + 2 * LEFT)

        wiggle_angle(3 * UP)

        wiggle_angle(5 * UP)

        wiggle_angle(50 * UP)

        wiggle_angle(1000 * UP)

        wiggle_angle(1000 * DOWN)

        wiggle_angle(50 * DOWN)

        wiggle_angle(5 * DOWN)

        wiggle_angle(3 * DOWN)

        self.remove(turncenter, turncircle, arrow)
        self.wait(0.5)




