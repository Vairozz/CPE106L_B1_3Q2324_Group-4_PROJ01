
from flet import *
class Login(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return Container(
            width=500,
            height=750,
            bgcolor="#000000",
            border_radius=10,
            content=Column(
                width=320,
                controls=[
                    Container(
                        width=150,
                        margin=margin.only(left=350, right=10, top=10),
                        content=TextButton(
                            "Create Account",
                            style=ButtonStyle(
                                color="ffffff"
                            )
                        )

                    ),
                    Container(
                        width=300,
                        margin=margin.only(left=200, right=10, top=10),

                        content=Text(
                            "Login",
                            size=30,
                            color="#ffffff",
                            weight='w700'
                        )
                    ),
                    Container(
                        width=300,
                        margin=margin.only(left=100, right=20, top=20),
                        alignment=alignment.center,
                        content=Text(
                            "Please enter your information below in order to login your account",
                            size=14,
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
                            "Login",
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
