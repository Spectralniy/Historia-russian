






screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("""Historia - Chapter One is © Copyright 2019. All Rights Reserved, unless released as part of the Renpy License. 

However, Non-commercial fan works using the characters and likenesses (but not the original works) are acceptable. (In other words, the copyright the characters are released under is a CC-BY-NC-SA 4.0 license)

If you'd like to make a Mod, please contact us at lucid.akumu@gmail.com

Made with {a=https://www.renpy.org/}{font=fonts/special_elite/regular.ttf}{color=#FF0000}Ren'Py{/color}{/font}{/a} [renpy.version_only].

This program contains free software under a number of licenses, including the MIT License and GNU Lesser General Public License. A complete list of software, including links to full source code, can be found {a=https://www.renpy.org/doc/html/license.html}{font=fonts/special_elite/regular.ttf}{color=#FF0000}here{/color}{/font}{/a}.

THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
""")



define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
