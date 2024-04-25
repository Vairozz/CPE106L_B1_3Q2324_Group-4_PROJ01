
from flet import *
class Register(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page =page

    def build(self):
        page.title = "Login and Register"

        return Container(
            width=500,
            height=750,
            bgcolor="#000000",
            border_radius=10,
            content=Column(
                width=320,
                controls=[
                    Container(
                        width=300,
                        margin=margin.only(left=200, right=10, top=10),

                        content=Text(
                            "Register",
                            size=30,
                            color="#ffffff",
                            weight='w700'
                        )
                    ),
                    Container(
                        width=400,
                        margin=margin.only(left=50, right=20, top=20),
                        alignment=alignment.center,
                        content=Text(
                            "Please enter your information below in order to create your account",
                            size=20,
                            text_align="center"

                        )
                    ),
                    Container(
                        width=450,
                        margin=margin.only(left=30, right=30, top=35),
                        content=Column(
                            controls=[
                                Text(
                                    "Username",
                                    size=14,
                                    color="ffffff"
                                ),
                                TextField(
                                    text_style=TextStyle(
                                        color="ffffff"
                                    ),
                                    border_radius=15,
                                    border_color=colors.WHITE,
                                    focused_border_color=colors.RED_700,

                                )
                            ]
                        )
                    ),
                    Container(
                        width=450,
                        margin=margin.only(left=30, right=30, top=35),
                        content=Column(
                            controls=[
                                Text(
                                    "Email",
                                    size=14,
                                    color="ffffff"
                                ),
                                TextField(
                                    text_style=TextStyle(
                                        color="ffffff"
                                    ),
                                    border_radius=15,
                                    border_color=colors.WHITE,
                                    focused_border_color=colors.RED_700,

                                )
                            ]
                        )
                    ),
                    Container(
                        width=450,
                        margin=margin.only(left=30, right=30, top=35),
                        content=Column(
                            controls=[
                                Text(
                                    "Password",
                                    size=14,
                                    color="ffffff"
                                ),
                                TextField(
                                    text_style=TextStyle(
                                        color="ffffff"
                                    ),
                                    password=True,
                                    can_reveal_password=True,
                                    border_radius=15,
                                    border_color=colors.WHITE,
                                    focused_border_color=colors.RED_700,

                                )
                            ]
                        )
                    ),
                    Container(
                        width=300,
                        margin=margin.only(left=100, right=20, top=50),
                        content=ElevatedButton(
                            "Create Account",
                            height=55,
                            width=300,
                            style=ButtonStyle(
                                color="#ffffff",
                                bgcolor=colors.ORANGE_700,
                                shape={
                                    MaterialState.HOVERED: buttons.RoundedRectangleBorder(radius=10),
                                    MaterialState.DEFAULT: buttons.RoundedRectangleBorder(radius=10),
                                }

                            ),
                        )
                    )

                ]
            ),
        )



