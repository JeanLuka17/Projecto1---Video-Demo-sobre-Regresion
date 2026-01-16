
from manim import *
import numpy as np


class RegressionGroup3FinalV3(Scene):
    def construct(self):

        self.camera.background_color = "#1e1e1e"

        # =========================================================
        # 1. PORTADA
        # =========================================================
        title = Text("Regresión Lineal vs No Lineal", font_size=42)
        title.set_color_by_gradient(BLUE, TEAL)
        title.to_edge(UP, buff=1.5)

        subtitle = Text("Visualización de Ajuste de Datos", font_size=24, color=GRAY_B)
        subtitle.next_to(title, DOWN)

        box = RoundedRectangle(corner_radius=0.2, stroke_color=WHITE, stroke_opacity=0.5, height=3.2, width=8)

        group_title = Text("Grupo 3", font_size=32, color=YELLOW).move_to(box.get_top() + DOWN * 0.5)
        names = VGroup(
            Text("Angel Oriundo, Carlos Enrique", font_size=24, color=WHITE),
            Text("Terrazo Santiago, Jean Luka", font_size=24, color=WHITE),
            Text("Villanueva Lara, Carlos Armando", font_size=24, color=WHITE)
        ).arrange(DOWN, buff=0.35).next_to(group_title, DOWN, buff=0.4)

        intro_group = VGroup(box, group_title, names).next_to(subtitle, DOWN, buff=0.5)

        self.play(Write(title, run_time=2), FadeIn(subtitle, run_time=2))
        self.play(Create(box), FadeIn(group_title), Write(names), run_time=4)
        self.wait(4)

        self.play(
            FadeOut(subtitle), FadeOut(intro_group), FadeOut(title)
        )

        # =========================================================
        # 2. ESCENARIO GRÁFICO
        # =========================================================
        plane = NumberPlane(
            x_range=[-1, 10], y_range=[-2, 12],
            x_length=8, y_length=5,
            background_line_style={
                "stroke_color": TEAL, "stroke_width": 1, "stroke_opacity": 0.2
            },
            axis_config={"include_numbers": True, "font_size": 18}
        ).shift(DOWN * 0.5)

        labels = plane.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(plane, run_time=3), FadeIn(labels))
        self.wait(1)

        # =========================================================
        # 3. REGRESIÓN LINEAL
        # =========================================================
        section_1 = Text("1. Regresión Lineal", font_size=32, color=YELLOW).to_edge(UP, buff=0.5)
        self.play(Write(section_1))

        np.random.seed(42)
        x_vals = np.linspace(1, 9, 10)
        y_vals = 0.8 * x_vals + 1 + np.random.normal(0, 0.8, size=10)

        dots = VGroup(*[
            Dot(plane.c2p(x, y), color=TEAL, radius=0.12).set_stroke(WHITE, 1)
            for x, y in zip(x_vals, y_vals)
        ])

        self.play(LaggedStart(*[DrawBorderThenFill(d) for d in dots], lag_ratio=0.3), run_time=5)
        self.wait(1)

        # Línea
        line = plane.plot(lambda x: 0.8 * x + 1, color=RED, stroke_width=4)
        # CORRECCIÓN 1: Fórmula y = mx + b
        eq_text = Text("y = mx + b", font_size=24, color=RED).next_to(line, UP, buff=0.2)

        self.play(Create(line, run_time=3))
        self.play(Write(eq_text))

        residuals = VGroup()
        for x, y, dot in zip(x_vals, y_vals, dots):
            line_point = plane.c2p(x, 0.8 * x + 1)
            dashed = DashedLine(dot.get_center(), line_point, color=ORANGE, dash_length=0.1)
            residuals.add(dashed)

        self.play(Create(residuals), run_time=3)
        self.play(Indicate(residuals, color=YELLOW))
        self.wait(3)

        self.play(
            FadeOut(dots), FadeOut(line), FadeOut(eq_text),
            FadeOut(residuals), FadeOut(section_1)
        )

        # =========================================================
        # 4. REGRESIÓN NO LINEAL
        # =========================================================
        section_2 = Text("2. Regresión No Lineal", font_size=32, color=GREEN).to_edge(UP, buff=0.5)
        self.play(Write(section_2))

        y_quad = 0.25 * (x_vals - 4) ** 2 + 1 + np.random.normal(0, 0.4, size=10)
        dots_quad = VGroup(*[
            Dot(plane.c2p(x, y), color=PURPLE, radius=0.12).set_stroke(WHITE, 1)
            for x, y in zip(x_vals, y_quad)
        ])

        self.play(FadeIn(dots_quad, shift=UP), run_time=2)
        self.wait(1)


        bad_line = plane.plot(lambda x: 0.1 * x + 3, color=GRAY, stroke_width=3)


        bad_txt = Text("Subajuste", color=RED, font_size=24)

        bad_txt.next_to(bad_line, UP, buff=0.2)

        self.play(Create(bad_line, run_time=2))
        self.play(FadeIn(bad_txt))
        self.wait(2)

        cross = Cross(bad_txt, stroke_color=RED, stroke_width=3)
        self.play(Create(cross))
        self.wait(1.5)

        self.play(FadeOut(bad_line), FadeOut(bad_txt), FadeOut(cross))

        # Curva CORRECTA
        curve = plane.plot(lambda x: 0.25 * (x - 4) ** 2 + 1, color=GOLD, stroke_width=5)
        eq_quad = Text("y = ax^2 + bx + c", font_size=24, color=GOLD).to_corner(UR).shift(DOWN * 2, LEFT * 1)

        self.play(Create(curve, run_time=4))
        self.play(Write(eq_quad))

        self.play(Indicate(curve, scale_factor=1.05))
        self.wait(4)

        # =========================================================
        # 5. FINAL
        # =========================================================
        self.play(FadeOut(Group(*self.mobjects)))

        final_text = Text("¡Gracias por ver!", font_size=48, gradient=(BLUE, PURPLE))
        self.play(GrowFromCenter(final_text, run_time=2))
        self.wait(4)

if __name__ == "__main__":
    import os
    # AQUÍ ESTABA EL ERROR: Cambiamos main.py por codigo_manin.py
    os.system("manim -pqh codigo_manin.py RegressionGroup3FinalV3")