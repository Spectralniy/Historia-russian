





screen selectMenu():
    tag menu




    use game_menu(_("Scene Select"), scroll="viewport"):

        style_prefix "about"

        vbox:







            if renpy.seen_label("dougActOneSceneThree"):
                textbutton _("Waking Up") action Start("dougActOneSceneThree")

            if renpy.seen_label("dougActOneSceneFour"):
                textbutton _("Mæx's House") action Start("dougActOneSceneFour")

            if renpy.seen_label("dougActTwoSceneOne"):
                textbutton _("Home (not) alone") action Start("dougActTwoSceneOne")

            if renpy.seen_label("dougActTwoSceneTwo"):
                textbutton _("Enter Michelle") action Start("dougActTwoSceneTwo")

            if renpy.seen_label("dougActTwoSceneThree"):
                textbutton _("Midnight Coffee") action Start("dougActTwoSceneThree")

            if renpy.seen_label("dougActTwoSceneFour"):
                textbutton _("Reality Hits") action Start("dougActTwoSceneFour")

            if renpy.seen_label("dougActThreeSceneOne"):
                textbutton _("Truancy Woes") action Start("dougActThreeSceneOne")

            if renpy.seen_label("dougActThreeSceneTwo"):
                textbutton _("Lunchtime Dreamtime") action Start("dougActThreeSceneTwo")

            if renpy.seen_label("dougActThreeSceneThree"):
                textbutton _("Strategic Planning") action Start("dougActThreeSceneThree")

            if renpy.seen_label("dougActFourSceneOne"):
                textbutton _("Sibling Rivalry") action Start("dougActFourSceneOne")

            if renpy.seen_label("dougActFourSceneTwo"):
                textbutton _("Futile Vigilante") action Start("dougActFourSceneTwo")

            if renpy.seen_label("dougActFourSceneThree"):
                textbutton _("Flawless Explanation") action Start("dougActFourSceneThree")

            if renpy.seen_label("dougActFourSceneFour"):
                textbutton _("Reckless Arson") action Start("dougActFourSceneFour")

            if renpy.seen_label("dougActFiveSceneOne"):
                textbutton _("Breaking News") action Start("dougActFiveSceneOne")

            if renpy.seen_label("dougActFiveSceneTwo"):
                textbutton _("Apprehension") action Start("dougActFiveSceneTwo")

            if renpy.seen_label("dougActFiveSceneThree"):
                textbutton _("Final Farewell") action Start("dougActFiveSceneThree")

            if renpy.seen_label("dougActFiveSceneFour"):
                textbutton _("A Monster to Kill") action Start("dougActFiveSceneFour")

            if renpy.seen_label("dougActFiveSceneFive"):
                textbutton _("Et tu, Brute?") action Start("dougActFiveSceneFive")

            if renpy.seen_label("dougActSixSceneOne"):
                textbutton _("Damned Funeral") action Start("dougActSixSceneOne")

            if renpy.seen_label("dougActSixSceneTwo"):
                textbutton _("Epilogue") action Start("dougActSixSceneTwo")

define gui.about = ""

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
