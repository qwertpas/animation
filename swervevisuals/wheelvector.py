from manim import *
from numpy import arctan2, sign

class Run(Scene):
    module0, module1, module2, module3 = 0,0,0,0
    def construct(self):

        robot = Square(fill_color=BLUE, fill_opacity=1, color=DARK_BLUE).move_to(DOWN * 1 + LEFT * 1)
        turncenter = Dot(color=RED).move_to(robot.get_center())
        turncircle = Circle(color=RED).scale(0).move_to(robot.get_center())
        arrow = Arrow(robot.get_center(), robot.get_center(), buff=0, color=WHITE)
        module0 = SVGMobject("img/module.svg").scale(0.2).move_to(robot.get_center() + RIGHT*0.8 + UP*0.8)
        module0[0].set_color(GREEN)
        module0[1].set_color(BLACK)
        module1 = module0.copy().move_to(robot.get_center() + LEFT*0.8 + UP*0.8)
        module2 = module0.copy().move_to(robot.get_center() + LEFT*0.8 + DOWN*0.8)
        module3 = module0.copy().move_to(robot.get_center() + RIGHT*0.8 + DOWN*0.8)

        self.add(robot, module0, module1, module2, module3, turncenter, turncircle, arrow)
    
        def wiggle_angle(center):
            radius = np.linalg.norm(center - robot.get_center())
            new_turncenter = Dot(color=RED).move_to(center)
            new_turncircle = Circle(color=RED).scale(radius).move_to(center)
            new_arrow = Arrow(robot.get_center(), center, buff=0, color=WHITE)

            self.play(
                Transform(turncenter, new_turncenter),
                Transform(turncircle, new_turncircle),
                Transform(arrow, new_arrow),
            )

            pos0 = np.array([0.8*RIGHT + 0.8*UP])
            pos1 = np.array([0.8*LEFT + 0.8*UP])
            pos2 = np.array([0.8*LEFT + 0.8*DOWN])
            pos3 = np.array([0.8*RIGHT + 0.8*DOWN])

            newmodule0 = (SVGMobject("img/module.svg").scale(0.2).move_to(robot.get_center() + pos0))
            newmodule0[0].set_color(GREEN)
            newmodule0[1].set_color(BLACK)
            newmodule1 = (newmodule0.copy().move_to(robot.get_center() + pos1))
            newmodule2 = (newmodule0.copy().move_to(robot.get_center() + pos2))
            newmodule3 = (newmodule0.copy().move_to(robot.get_center() + pos3))

            vec0 = (center - robot.get_center() - pos0)[0]
            vec1 = (center - robot.get_center() - pos1)[0]
            vec2 = (center - robot.get_center() - pos2)[0]
            vec3 = (center - robot.get_center() - pos3)[0]

            ang0 = np.arctan2(vec0[1], vec0[0])
            ang1 = np.arctan2(vec1[1], vec1[0])
            ang2 = np.arctan2(vec2[1], vec2[0])
            ang3 = np.arctan2(vec3[1], vec3[0])

            newmodule0.rotate(ang0)
            newmodule1.rotate(ang1)
            newmodule2.rotate(ang2)
            newmodule3.rotate(ang3)
            

            self.play(
                Transform(module0, newmodule0),
                Transform(module1, newmodule1),
                Transform(module2, newmodule2),
                Transform(module3, newmodule3),

                FadeIn(Circle().move_to(center).scale(np.linalg.norm(vec0)))
            )

            self.wait(0.25)

            angle = 1.5 * PI / radius
            if(angle > PI/2): angle = PI/2
            self.play(
                Rotating(robot, radians=angle, about_point=center, run_time=2, rate_func=wiggle),
                Rotating(arrow, radians=angle, about_point=center, run_time=2, rate_func=wiggle),

                Rotating(module0, radians=angle, about_point=center, run_time=2, rate_func=wiggle),
                Rotating(module1, radians=angle, about_point=center, run_time=2, rate_func=wiggle),
                Rotating(module2, radians=angle, about_point=center, run_time=2, rate_func=wiggle),
                Rotating(module3, radians=angle, about_point=center, run_time=2, rate_func=wiggle),
            )

            self.wait(0.5)


        wiggle_angle(2 * RIGHT + 2 * UP)
        wiggle_angle(2 * LEFT + 2 * UP)
        


        self.wait(0.5)

