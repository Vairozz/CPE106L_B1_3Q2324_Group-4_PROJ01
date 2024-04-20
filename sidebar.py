import flet
from flet import *
from functools import partial
import time

class MordernNavBar(UserControl):
    def __init__(self):
        super().__init__()

    #highlight selected row
    def Highlight(self, e):
        if e.data == 'true':
            e.control.bgcolor = 'white10'
            e.control.update()

            e.controls.content.controls[0].icon_color = 'white'
            e.controls.content.controls[1].color = 'white'
            e.control.update()
        else:
            e.control.bgcolor = 'None'
            e.control.update()

    #sidebar title and contents
    def UserData(self, initials:str, name:str, description:str):
        return Container(
            content=Row(
                controls=[
                    Container(
                        width = 42, 
                        height=42, 
                        bgcolor='bluegrey900',
                        alignment=alignment.center,
                        border_radius=8,
                        content=Text(
                            value=initials,
                            size=15,
                            color='white',
                        ),
                    ),
                    Column(
                        spacing=1,
                        alignment="center",
                        controls=[
                            Text(
                                value=name,
                                size=11,
                                weight='bold',
                                color='white',
                            ),
                            Text(
                                value=description,
                                size=9,
                                weight='bold',
                                color='white54',
                            ),
                        ]
                    )
                ]
            )
        )
    
    def containedIcons(self, icon_name:str, text:str):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.Highlight(e),
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color="white54",
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={"": "transparent"},
                        ),   
                    ),
                    Text(
                        value=text,
                        color="white54",
                        size=11, 
                    )
                ]
            ),
        )
    
    def build(self):
        return Container(
            width=200,
            height=580,
            padding=padding.only(top=10),
            alignment=alignment.center,
            content=Column(
                controls=[
                    #sidebar title
                    self.UserData("CPE", "Bus Scheduler App", "Software Design Lab"),
                    Divider(height=5, color="transparent"),
                    self.containedIcons(icons.SEARCH, "Search"),
                    self.containedIcons(icons.PERSON, "Profile"),
                    self.containedIcons(icons.NOTIFICATIONS, "Notifications"),
                    self.containedIcons(icons.PAYMENTS_OUTLINED, "Tickets"),
                    self.containedIcons(icons.DIRECTIONS_BUS, "Bus Units"),
                    self.containedIcons(icons.ALT_ROUTE, "Routes"),
                    Divider(height=5, color='white24'),
                    self.containedIcons(icons.LOGOUT, "Log Out"),
                ]
            ),
        )
    
def sidebar(page: Page):
    # title
    page.title = 'Bus Scheduler App'
    page.horizontal_alignment='center'
    page.vertical_alignment='center'

    page.add(
        Container(
            width=200,
            height=580,
            bgcolor='black',
            border_radius=10,
            alignment=alignment.center,
            padding=10,
            content=MordernNavBar()
        )
    )

    page.update()

if __name__ == '__main__':
    flet.app(target=sidebar)

    
