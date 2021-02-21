from manim import *
from numpy import arctan2, sign
from numpy.linalg import norm

class Run(MovingCameraScene):

    def setup(self):
        MovingCameraScene.setup(self)



    def construct(self):

        robot = Square(fill_color=BLUE, fill_opacity=1, color=DARK_BLUE).move_to(DOWN * 1 + LEFT * 1)
        turncenter = Dot().move_to(robot.get_center())
        turncircle = Circle().scale(0).move_to(robot.get_center())
        arrow = Arrow(robot.get_center(), robot.get_center(), buff=0, color=WHITE)
        module0 = SVGMobject("img/module.svg").scale(0.2).move_to(robot.get_center() + RIGHT*0.8 + UP*0.8)
        module0[0].set_color(GREEN_E)
        module0[1].set_color(BLACK)
        module1 = module0.copy().move_to(robot.get_center() + LEFT*0.8 + UP*0.8)
        module2 = module0.copy().move_to(robot.get_center() + LEFT*0.8 + DOWN*0.8)
        module3 = module0.copy().move_to(robot.get_center() + RIGHT*0.8 + DOWN*0.8)

        self.add(robot, module0, module1, module2, module3, turncenter, turncircle, arrow)

        pos0 = np.array([0.8*RIGHT + 0.8*UP])
        pos1 = np.array([0.8*LEFT + 0.8*UP])
        pos2 = np.array([0.8*LEFT + 0.8*DOWN])
        pos3 = np.array([0.8*RIGHT + 0.8*DOWN])
    
        def wiggle_angle(center):
            radius = norm(center - robot.get_center())
            new_turncenter = Dot(color=RED).move_to(center)
            new_turncircle = Circle(color=RED).scale(radius).move_to(center)
            new_arrow = Arrow(robot.get_center(), center, buff=0, color=WHITE)

            self.play(
                Transform(turncenter, new_turncenter),
                Transform(turncircle, new_turncircle),
                Transform(arrow, new_arrow),
            )

            newmodule0 = (SVGMobject("img/module.svg").scale(0.2).move_to(robot.get_center() + pos0))
            newmodule0[0].set_color(GREEN_E)
            newmodule0[1].set_color(BLACK)
            newmodule1 = (newmodule0.copy().move_to(robot.get_center() + pos1))
            newmodule2 = (newmodule0.copy().move_to(robot.get_center() + pos2))
            newmodule3 = (newmodule0.copy().move_to(robot.get_center() + pos3))

            vec0 = (center - robot.get_center() - pos0)[0]
            vec1 = (center - robot.get_center() - pos1)[0]
            vec2 = (center - robot.get_center() - pos2)[0]
            vec3 = (center - robot.get_center() - pos3)[0]

            ang0 = np.arctan2(vec0[1], vec0[0]) + PI
            ang1 = np.arctan2(vec1[1], vec1[0]) + PI
            ang2 = np.arctan2(vec2[1], vec2[0]) + PI
            ang3 = np.arctan2(vec3[1], vec3[0]) + PI

            newmodule0.rotate(ang0)
            newmodule1.rotate(ang1)
            newmodule2.rotate(ang2)
            newmodule3.rotate(ang3)

            turncircle0 = Circle().move_to(center).scale(norm(vec0)).set_stroke(color=YELLOW, width=1)
            turncircle1 = Circle().move_to(center).scale(norm(vec1)).set_stroke(color=YELLOW, width=1)
            turncircle2 = Circle().move_to(center).scale(norm(vec2)).set_stroke(color=YELLOW, width=1)
            turncircle3 = Circle().move_to(center).scale(norm(vec3)).set_stroke(color=YELLOW, width=1)
            

            self.play(
                Transform(module0, newmodule0),
                Transform(module1, newmodule1),
                Transform(module2, newmodule2),
                Transform(module3, newmodule3),

                FadeIn(turncircle0),
                FadeIn(turncircle1),
                FadeIn(turncircle2),
                FadeIn(turncircle3),
            )

            self.wait(0.5)

            angle = 1 * PI / radius
            if(angle > PI/2): angle = PI/2
            self.play(

                Rotating(robot, radians=angle, about_point=center, run_time=3, rate_func=wiggle),
                Rotating(arrow, radians=angle, about_point=center, run_time=3, rate_func=wiggle),

                Rotating(module0, radians=angle, about_point=center, run_time=3, rate_func=wiggle),
                Rotating(module1, radians=angle, about_point=center, run_time=3, rate_func=wiggle),
                Rotating(module2, radians=angle, about_point=center, run_time=3, rate_func=wiggle),
                Rotating(module3, radians=angle, about_point=center, run_time=3, rate_func=wiggle),
            )

            self.wait(0.5)

            self.play(
                FadeOut(turncircle0),
                FadeOut(turncircle1),
                FadeOut(turncircle2),
                FadeOut(turncircle3),
            )

        # wiggle_angle(2.1 * RIGHT + 0.1 * UP)
        wiggle_angle(1.6 * LEFT + 2 * UP)


        robotdot = Dot(robot.get_center())
        robotlabel = Text("robot center", size=0.5).next_to(robotdot, LEFT)



        module3dot = Dot(robot.get_center() + pos3, color=GREEN_E)
        modulelabel = Text("module", size=0.5).next_to(module3dot, DOWN)

        placement = Arrow(robot.get_center(), (robot.get_center() + pos3)[0], buff=0, color=GREEN_E)
        placementlabel = MathTex("\\vec{p}", size=0.5).next_to(placement, LEFT).shift(DOWN * 0.2 + RIGHT * 0.5)

        linvel = Arrow(robot.get_center(), 1.6 * UP + 2 * RIGHT, buff=0, color=RED)
        linvellabel = MathTex("\\vec{v}", size=0.5).next_to(linvel, ORIGIN).shift(RIGHT * 0.2)
        angvel = CurvedArrow(0.5*RIGHT + 0.5 * DOWN, 0.5 * LEFT + 0.5*UP, color=RED).move_arc_center_to(1.2 * UP + 1.6 * RIGHT)
        angvellabel = Text("ω", size=0.5).next_to(angvel)


        self.play(self.camera_frame.animate.scale(0.7).move_to(robot.get_center() + UP))


        self.play(
            Transform(turncircle, linvel, run_time=1),
            ShowCreation(linvellabel),
            ShowCreation(angvel),
            ShowCreation(angvellabel),
        )

        self.play(
            FadeOut(module0),
            FadeOut(module1),
            FadeOut(module2),
        )

        self.play(
            Transform(robot, robotdot, run_time=2),
            ShowCreation(robotlabel),
        )
        self.play(
            Transform(module3, module3dot, run_time=2),
            ShowCreation(modulelabel),
        )
        self.play(
            ShowCreation(placement),
            ShowCreation(placementlabel)
        )





        self.wait(0.5)

