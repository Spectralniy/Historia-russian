




screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Новaя игрa") action Start()
        else:
            textbutton _("История") action ShowMenu("history")
            textbutton _("Сохрaнить") action ShowMenu("save")

        textbutton _("Зaгрузкa") action ShowMenu("load")
        textbutton _("Нaстройки") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("Остaновить воспроизведение") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Глaвное меню") action MainMenu()

        textbutton _("Инфо") action ShowMenu("about")
        textbutton _("Просмотр сцен") action ShowMenu("selectMenu")

        if renpy.variant("pc"):

            textbutton _("Помощь") action ShowMenu("help")

            textbutton _("Выйти") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
