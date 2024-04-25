from flet import *
from Login import Login
from Register import Register

def navigation_handler(page):
    return{
        '/login' : View(
            route='/login',
            controls=[
                Login(page)
            ]
        ),
        '/register': View(
            route='/register',
            controls=[
                Register(page)
            ]
        )
    }