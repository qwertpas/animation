from manim import *
from numpy import sign
class Run(Scene):
    def construct(self):

        v = 2.0
        angvel = PI/4

        robot = Square(fill_color=BLUE, fill_opacity=1, color=DARK_BLUE).move_to(LEFT * 4)
        turncenter = Dot(color=RED)
        turncircle = Circle(color=RED).scale(0)
        arrow = Arrow(ORIGIN, robot.get_center(), buff=0, color=WHITE)

        line = Line(LEFT * 4, RIGHT * 4, color=GRAY)

        self.add(robot, line, turncenter, turncircle, arrow)

        

        tc = np.array([0, v / angvel, 0])
        # self.add(Arrow(ORIGIN, tc, buff=0))

        def update_arrow(arrow):
            arrow.become(Arrow(robot.get_center(), robot.get_center() + tc, buff=0))

        def update_dot(turncenter):
            turncenter.become(Dot(robot.get_center() + tc))

        def update_circle(turncircle):
            radius = np.linalg.norm(tc)
            turncircle.become(Circle().scale(radius).move_to(robot.get_center() + tc))

        arrow.add_updater(update_arrow)
        turncenter.add_updater(update_dot)
        turncircle.add_updater(update_circle)

        self.play(
            Rotating(robot, radians = angvel * (8/v), run_time=8/v, rate_func=linear),
            MoveAlongPath(robot, line, run_time=8/v, rate_func=linear),

        )


        self.wait(0.5)

