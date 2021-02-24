from manim import *
from numpy import arctan2, diff, sign
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
                # FadeOut(turncircle0),
                FadeOut(turncircle1),
                FadeOut(turncircle2),
                FadeOut(turncircle3),
                FadeOut(module1),
                FadeOut(module2),
                FadeOut(module3),
            )

        # wiggle_angle(2.1 * RIGHT + 0.1 * UP)
        wiggle_angle(1.6 * LEFT + 2 * UP)

        radiuslabel = MathTex("\\vec{r}", size=0.5).next_to(arrow, ORIGIN).shift(LEFT * 0.3)
        requilvalent = MathTex("=(\\frac{\\vec{v}}{\\omega}).rot(90^{\circ })", size=0.1).next_to(radiuslabel, ORIGIN).shift(DOWN*0.5 + LEFT * 0.3).scale(0.4)

        robotdot = Dot(robot.get_center())

        module0dot = Dot(robot.get_center() + pos0, color=GREEN_E)

        placement = Arrow(robot.get_center(), module0dot.get_center(), buff=0, color=GREEN_E)
        placementlabel = MathTex("\\vec{p}", size=0.5).next_to(module0dot.get_center(), RIGHT).shift(0.8*LEFT + DOWN*0.1)

        linvel = arrow.copy().rotate(-PI/2, about_point=robot.get_center()).set_color(RED)
        linvellabel = MathTex("\\vec{v}", size=0.5).next_to(linvel, ORIGIN).shift(DOWN * 0.3)
        angvel = CurvedArrow(0.2*RIGHT + 0.3 * DOWN, 0.4 * LEFT + 0.1*UP, color=RED).move_arc_center_to(arrow.get_end())
        angvellabel = Text("ω", size=0.5).next_to(angvel, RIGHT*0.5)
        rightangle = Rectangle(height=0.2, width=0.2, stroke_width=6).next_to(robotdot, ORIGIN).shift(RIGHT*0.08 + UP*0.12).rotate(linvel.get_angle())


        self.play(self.camera_frame.animate.scale(0.5).move_to(module0dot.get_center() + UP*0.8))

        self.play(
            ShowCreation(radiuslabel)
        )

        self.wait(1)

        self.play(
            ShowCreation(rightangle),
            ShowCreation(linvel),
            ShowCreation(linvellabel),
            ShowCreation(angvel),
            ShowCreation(angvellabel),
        )


        self.wait(1)

        self.play(
            Transform(robot, robotdot, run_time=2),
        )

        self.wait(0.5)
        self.play(
            ShowCreation(requilvalent, run_time=2)
        )
        self.wait(2)
        self.play(
            Transform(linvel.copy(), arrow, run_time=2)
        )
        self.wait(2)

        self.play(
            FadeOut(turncircle)
        )
        self.wait(0.5)

        self.play(
            Transform(module0, module0dot, run_time=2),
        )

        self.wait(0.5)

        self.play(
            ShowCreation(placement),
            ShowCreation(placementlabel)
        )

        self.wait(0.5)


        self.camera_frame.save_state()

        wheeltotc = Arrow(module0dot.get_center(), arrow.get_end(), buff=0, color=BLUE)
        wheeltotclabel = MathTex("\\vec{r_w}", size=0.5).next_to(wheeltotc.get_center(), RIGHT)

        self.play(
            ShowCreation(wheeltotc),
            ShowCreation(wheeltotclabel),
        )

        self.wait(1)

        self.play(
            FadeOut(linvel),
            FadeOut(linvellabel),
            FadeOut(angvel),
            FadeOut(angvellabel),
            FadeOut(rightangle)
        )

        sumeq = MathTex(
            "\\vec{r}",
            "=",
            "\\vec{p}",
            "+",
            "\\vec{r_w}",
        ).move_to(RIGHT*2 + UP*0.5)

        sumeq[2].set_color(GREEN_E)
        sumeq[4].set_color(BLUE)

        self.play(
            ShowCreation(sumeq)
        )
        self.wait(0.5)
        self.play(
            Indicate(sumeq[0]),
            ShowPassingFlash(arrow.copy().set_color(GREEN_SCREEN), time_width=0.2),
        )
        self.wait(0.5)
        self.play(
            Indicate(sumeq[2]),
            ShowPassingFlash(placement.copy().set_color(GREEN_SCREEN), time_width=0.2),
        )
        self.wait(0.5)
        self.play(
            Indicate(sumeq[4]),
            ShowPassingFlash(wheeltotc.copy().set_color(GREEN_SCREEN), time_width=0.2),
        )

        self.wait(1)

        diffeq = MathTex(
            "\\vec{r_w}",
            "=",
            "\\vec{r}",
            "-",
            "\\vec{p}",
        ).next_to(sumeq, DOWN).shift(LEFT*0.27)
        diffeq[4].set_color(GREEN_E)
        diffeq[0].set_color(BLUE)
        self.play(
            Transform(sumeq.copy()[4], diffeq[0]),
            Transform(sumeq.copy()[1], diffeq[1]),
            Transform(sumeq.copy()[0], diffeq[2]),
            Transform(sumeq.copy()[3], diffeq[3]),
            Transform(sumeq.copy()[2], diffeq[4]),
        )



        self.wait(1)

        bigeq = MathTex(
            "\\vec{r_w}",
            "=",
            "(\\frac{\\vec{v}}{\\omega}).rot(90^{\circ })",
            "-",
            "\\vec{p}",
        ).next_to(sumeq, DOWN*2.1).shift(LEFT*0.27).scale(0.5)
        bigeq[4].set_color(GREEN_E)
        bigeq[0].set_color(BLUE)

        self.play(
            ShowCreation(bigeq, run_time=2),
            Transform(requilvalent, bigeq[2])
        )
        self.wait(0.5)
        self.play(
            Indicate(diffeq[2])
        )

        self.play(
            Indicate(bigeq[2])
        )

        self.wait(1)

