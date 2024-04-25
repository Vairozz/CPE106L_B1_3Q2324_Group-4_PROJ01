from flet import *
from Navigation import navigation_handler
def main(page: Page):
    def route_change(route):
        page.views.clear()
        page.views.append(
            navigation_handler(page)
        )
    page.on_route_change=route_change
    page.go('/login')

app(target=main)