import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = page.vertical_alignment = "center"

    def navigate_to(route):
        page.route = route
        page.update()

    boton_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.GREY_800,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.HOME, on_click=lambda _: navigate_to("/")),
                ft.IconButton(icon=ft.icons.SCHOOL, on_click=lambda _: navigate_to("/educacion")),
                ft.IconButton(icon=ft.icons.WORK, on_click=lambda _: navigate_to("/experiencia")),
            ]
        )
    )

    page.boton_appbar = boton_appbar

    def nueva_ruta(e: ft.RouteChangeEvent):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.Column(
                    [
                        ft.Image(src=f"./assets/img_hoja_vida.jpg", width=250, height=250),
                        ft.Text("NOMBRE: Jose Fernando Osorio Orozco"),
                        ft.ExpansionPanelList(
                            expand_icon_color=ft.colors.RED_800,
                            elevation=8,
                            divider_color=ft.colors.RED_800,
                            controls=[
                                ft.ExpansionPanel(
                                    header=ft.Text("CONTACTO"),
                                    content=ft.Text("EMAIL: Josefernando2002osorio@gmail.com\nTELÉFONO: 3017639871\nDOCUMENTO: 1002544675"),
                                ),
                                ft.ExpansionPanel(
                                    header=ft.Text("SOBRE MI"),
                                    content=ft.Text("Estudiante de alto rendimiento en Análisis y Desarrollo de Software en el SENA REGIONAL CALDAS. Desarrollé habilidades en lenguajes como Python, Java y C#.\nEstoy entusiasmado por buscar una pasantía en mi campo del desarrollo de Software."),
                                ),
                                ft.ExpansionPanel(
                                    header=ft.Text("HERRAMIENTAS"),                                
                                    content=ft.Text("Lenguajes de Programación: Python - C# - Java\nBases de datos: MongoDB - SQL Server Management Studio\nReact - Flet")
                                ),
                            ]
                        ),
                        ft.BottomAppBar(
                            bgcolor=ft.colors.GREY_800,
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.icons.HOME, on_click=lambda _: navigate_to("/")),
                                    ft.IconButton(icon=ft.icons.SCHOOL, on_click=lambda _: navigate_to("/educacion")),
                                    ft.IconButton(icon=ft.icons.WORK, on_click=lambda _: navigate_to("/experiencia")),
                                ]
                            )
                        )
                    ]
                )
            )
        elif page.route == "/educacion":
            page.views.append(
                ft.Column(
                    [
                        ft.Text("EDUCACIÓN"),
                        ft.ExpansionPanelList(
                            expand_icon_color=ft.colors.RED_800,
                            elevation=8,
                            divider_color=ft.colors.RED_800,
                            controls=[
                                ft.ExpansionPanel(
                                    header=ft.Text("Básica Primaria"),
                                    content=ft.Text("COLEGIO SEMINARIO REDENTORISTA\n               °5 Primaria  2013"),
                                ),
                                ft.ExpansionPanel(
                                    header=ft.Text("Secundaria"),
                                    content=ft.Text("COLEGIO SAN PEDRO CLAVER\n   Bachiller Académico  2021"),
                                ),
                                ft.ExpansionPanel(
                                    header=ft.Text("SENA - Actualidad"),
                                    content=ft.Text("Aprendiz en el campo de Análisis y desarrollo de Software.\nTecnólogo que inició el año 2022 y finalizará en el año 2025"),
                                ),
                            ]
                        ),
                        ft.BottomAppBar(
                            bgcolor=ft.colors.GREY_800,
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.icons.HOME, on_click=lambda _: navigate_to("/")),
                                    ft.IconButton(icon=ft.icons.SCHOOL, on_click=lambda _: navigate_to("/educacion")),
                                    ft.IconButton(icon=ft.icons.WORK, on_click=lambda _: navigate_to("/experiencia")),
                                ]
                            )
                        )
                    ]
                )
            )
        elif page.route == "/experiencia":
            page.views.append(
                ft.Column(
                    [
                        ft.Text("EXPERIENCIA LABORAL"),
                        ft.ExpansionPanelList(
                            expand_icon_color=ft.colors.RED_800,
                            elevation=8,
                            divider_color=ft.colors.RED_800,
                            controls=[
                                ft.ExpansionPanel(
                                    header=ft.Text("Primera Experiencia"),
                                    content=ft.Text("   Atención al Cliente:\nMesero Cafetería - 2020"),
                                ),
                                ft.ExpansionPanel(
                                    header=ft.Text("Segunda Experiencia"),
                                    content=ft.Text("     Ayudante de maestro de obra:\nInstalación de ventanales de aluminio\n   Fibras de cemento y Cielos Rasos\n                    2021-2022"),
                                ),
                                
                            ]
                        ),
                        ft.BottomAppBar(
                            bgcolor=ft.colors.GREY_800,
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(icon=ft.icons.HOME, on_click=lambda _: navigate_to("/")),
                                    ft.IconButton(icon=ft.icons.SCHOOL, on_click=lambda _: navigate_to("/educacion")),
                                    ft.IconButton(icon=ft.icons.WORK, on_click=lambda _: navigate_to("/experiencia")),
                                ]
                            )
                        )
                    ]
                )
            )
        page.update()

    page.on_route_change = nueva_ruta

    page.add(
        ft.Text("BIENVENIDO A MI\n  HOJA DE VIDA "),
        boton_appbar,
    )

ft.app(main)