import taipy as tp
from taipy.gui import Gui

from pages import *


pages = {
    "/": root_page,
    "login": login,
	"signup": signup
}


if __name__ == "__main__":

    gui = Gui(pages=pages)
    tp.run(gui,title="Catch up")
