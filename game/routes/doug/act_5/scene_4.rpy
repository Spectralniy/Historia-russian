label dougActFiveSceneFour:

    $ stopAllAudioTracks()


    window show
    scene bg black
    with dissolve


    scene bg doug bedroom
    with dissolve

    play music "sounds/doug/act_1/bgm_lazy_afternoon_corrupt.ogg"

    $ line2 = renpy.transform_text("xXëæm", scrambling)
    $ _history = False

    show maxGhostBummedBloody
    with dissolve

    friendMax "How many times do I have to tell you, it's not your fault?"

    $ _history = True

    "[line2]" "{alpha=0}It's all your fault!{/alpha}{fast}{nw}"

    $ _history = False
    friendMax "Not for me, not for Natalia."

    $ _history = True

    "[line2]" "{alpha=0}You killed Nat! You Let me die!{/alpha}{fast}{nw}"

    $ _history = False

    friendMax "There was nothing you could do…"

    $ _history = True

    "[line2]" "{alpha=0}You should have done something!{/alpha}{fast}{nw}"

    "I know he's trying to make me feel better, but I'm simply not in the mood."

    "I only want to lie on my bed until sleep finally comes to me."

    "Dad vanished almost as soon as we got home. I have no idea where he went."

    "Mum opened herself a bottle of wine, drinking it alone on the kitchen table with her tears."

    "I can't bear to talk to either of them. I don't even know what I'd say."

    "I know I should say something, but the words are knotted in my throat. I don't think that I could speak without breaking into tears."

    "None of us have had the courage to go into Natalia's room yet."

    "It… simply doesn't feel real."

    "Every scuffle from the kitchen makes me think that she's come home, and this is just a bad dream."

    $ _history = False

    hide max
    with dissolve
    show maxGhostSeriousBloody
    with dissolve

    friendMax "But it's not a dream, is it?"

    $ _history = True
    $ line2 = renpy.transform_text("XëæMa", scrambling)

    "[line2]" "{alpha=0}That's right - it's only a dream.{/alpha}{fast}{nw}"

    $ _history = False

    friendMax "This is as real as it gets, my friend."

    $ _history = True

    "[line2]" "{alpha=0}A bitter dream that will fade with time...{/alpha}{fast}{nw}"

    doug "I know… I know… but it shouldn't be like this."

    $ _history = False

    hide maxGhostSeriousBloody
    with dissolve
    show maxGhostBummedBloody
    with dissolve

    friendMax "Then what should it be like?"

    $ _history = True

    "[line2]" "{alpha=0}That's because it's not. You're just waking up.{/alpha}{fast}{nw}"

    $ _history = False

    doug "I don't know. {w} You.{w} Natalia…{w} You should both be here."

    $ _history = True

    "[line2]" "{alpha=0}Once you're awake, we will fade away. We were never here.{/alpha}{fast}{nw}"

    $ _history = False

    doug "Just… everything the way it was."

    doug "Maybe you flirting with her or something."

    hide maxGhostBummedBloody
    with dissolve
    show maxGhostSmugBloody
    with dissolve

    $ _history = True
    $ line2 = renpy.transform_text("DOUGmax", scrambling)

    "[line2]" "{alpha=0}Just… everything the way it was.{/alpha}{fast}{nw}"

    $ _history = False
    "Max leans back on my desk chair, his hands clasped around the back of his head."

    $ _history = True

    "{alpha=0}I lean back on my chair and clasp my hands behind my head{/alpha}{fast}{nw}"

    $ _history = False

    "It pisses me off that he can be so relaxed about this."

    $ _history = True

    "{alpha=0}How could anyone ever hope to relax after something like this?{/alpha}{fast}{nw}"

    $ _history = False

    friendMax "Of course I'm relaxed. There is literally nothing that can hurt me now."

    friendMax "Unless you get a lobotomy."

    hide maxGhostSmugBloody
    with dissolve
    show maxGhostSeriousBloody
    with dissolve

    friendMax "Please don't get a lobotomy."

    $ _history = True

    "[line2]" "{alpha=0}You need a lobotomy.{/alpha}{fast}{nw}"

    $ _history = False

    hide maxGhostSeriousBloody
    with dissolve
    show maxGhostSmugBloody
    with dissolve

    "I twist away from the figure, trying to hide Max's visage from my sight, but he is there, next to me in my bed."

    $ _history = True

    "{alpha=0}I twist and turn in my bed, pulling my sheets into a knot, but sleep does not come easily.{/alpha}{fast}{nw}"

    $ _history = False

    friendMax "Dude, you can't get rid of me. I'm here now. Talk to me, ok?"

    $ _history = True

    doug "Fine. What do you want?"

    $ _history = False
    friendMax "I want you to know that it's not your fault."

    $ _history = True

    "[line2]" "{alpha=0}I want you to know that you don't carry the blame for anything.{/alpha}{fast}{nw}"

    $ _history = False
    friendMax "That there's nothing that you could have done."

    $ _history = True

    "[line2]" "{alpha=0}We are simple figments of your imagination.{/alpha}{fast}{nw}"

    $ _history = False

    friendMax "And there's nothing that you can do."

    $ _history = True
    $ line2 = renpy.transform_text("DougëæMm", scrambling)

    "[line2]" "{alpha=0}We will slowly fade away.{/alpha}{fast}{nw}"

    $ _history = False

    friendMax "The pain will subside - when you learn to let go."

    $ _history = True

    "[line2]" "{alpha=0}The pain will be gone when you let us go.{/alpha}{fast}{nw}"

    $ _history = False

    "I close my eyes and try to ignore the phantom."

    "I don't want the pain to subside."

    $ _history = True
    "{alpha=0}I want the pain to subside.{/alpha}{fast}{nw}"

    $ _history = False

    "I don't want to forget."

    $ _history = True


    "{alpha=0}I want to forget.{/alpha}{fast}"

    $ _history = False

    "I don't want to give up."

    stop music fadeout 5

    $ _history = True

    "{alpha=0}I want to give up.{nw}{/alpha}"



    hide maxGhostSmugBloody
    with dissolve



    play sound "sounds/doug/act_1/doug_tap_glass.ogg"

    $ _history = False

    "I jump up with a start. That was a real noise, not a clinking of Mum's glass, or a phantasm in my bed."

    $ _history = True

    "{alpha=0.3}I jump up with a start. That was a real noise, not a clinking of Mum's glass, or a noise in my head.{/alpha}{fast}{nw}"

    "My eyes snap open and focus on my room's tiny windows."

    $ renpy.music.set_volume (0.7, 0, channel="music")

    play music "<to 12.750>sounds/doug/act_1/bgm_michelle_dougroom_intro_12.750.ogg" fadein 0.5
    queue music "sounds/doug/act_1/bgm_michelle_dougroom_loop.ogg" loop

    show michelle window doug room
    with dissolve

    michelle "Let me in!"

    "I don't want to see anyone now; least of all Michelle."

    "I contemplate locking the windows and ignoring her, but maybe the company would do me good."

    $ _history = False

    "I look around the room. Max is nowhere to be seen."

    $ _history = True

    "Reluctantly I throw the catch on the window, and Michelle lets herself in."

    show michelle jacket side grin
    with dissolve

    michelle "Thanks. It's cold out there."

    doug "Sure."

    "My voice is barely above a whisper."

    show michelle jacket side blank
    with dissolve

    "Michelle takes a moment to start the conversation and I wonder if she maybe came here looking for consolation as well."

    "She always spoke highly of Nat. She obviously knows at least about the accident."

    michelle "So... What's our plan for tonight? I figured we better discuss beforehand."

    "But, no.{w} Michelle only has eyes for the Serpent.{w} I should have known that much."

    "She really is mad, isn't she?"

    doug "I'm not in the mood."

    show michelle jacket front upset
    with dissolve

    michelle "Mood? Mood?! Mood has nothing to do with this."

    michelle "We have a monster to kill."

    michelle "You and I… We're supposed to be a team. Inseparable."

    michelle "We're supposed to kill that thing together, right?"

    doug "I…{w} I just can't tonight."

    doug "I can't stop thinking about everything that's happened."

    show michelle jacket front speaking
    with dissolve

    michelle "And who's fault is that?"

    doug "Mine…?"

    show michelle jacket front surprised
    with dissolve

    michelle "No! It's the Serpent!"

    michelle "The Serpent did all of this!"

    show michelle jacket front upset
    with dissolve

    michelle "We need to kill that motherfucker right now!"

    michelle "But I need your help to do that."

    show michelle jacket front
    with dissolve

    doug "You can't kill it."

    doug "We can't kill it."

    doug "It's pointless. We should just let it eat us and be done with it."

    show michelle jacket front furious closer
    with dissolve

    with hpunch

    play sound "sounds/doug/act_1/doug_slap.ogg"

    "Michelle's backhand burns across my cheek."

    michelle "Can you even hear yourself?"

    michelle "You're not that kind of person, Doug. You don't give up! I know it!"

    doug "What the fuck do you know about me?"

    show michelle jacket speaking closer
    with dissolve

    michelle "I know that you want to see this fucker dead."

    michelle "You don't think I know about loss? I never let that stop me."

    michelle "Sure, it sucks about Nat, but now it's just you and me against this thing. That hasn't changed."

    michelle "We need to make it pay for what it's done."

    michelle "You and I. {w}Together."

    show michelle jacket uncertain closer
    with dissolve

    "She changes her tone and looks at me sheepishly."

    "This is not about the Serpent anymore."

    show michelle jacket uncertain speaking closer
    with dissolve

    michelle "Don't you want that?"

    doug "W-what did you say?"

    play sound "sounds/doug/act_1/dou_sit_on_bed.ogg"

    show michelle jacket front uncertain closeup
    with dissolve

    "Michelle sits down on the bed, leaning backwards, and drawing me towards her."

    "Confused, I feel myself following her out of instinct."

    "Part of me yearns to be held right now, for some human contact to remind me that I'm still alive."

    michelle "Just you… {w}and me…{w} together…"

    show michelle jacket front lusty closeup
    with dissolve

    "Before I know it she is kissing me, and my body relinquishes. I kiss her back and the feeling of touch jerks me back to reality."

    "My consciousness starts to rearrange itself as cold realisation courses across my skin."

    "I don't want to think about Natalia any more."

    "I mean, I want to remember her, but I need a distraction. I can't shake the image of her tumbling down that dam, no matter how hard I try."

    "I don't feel like drinking. But a certain rage begins to boil in my belly."

    $ _history = False

    "That lizard took Max from me, and probably Natalia as well."

    $ _history = True

    "{alpha=0}That lizard took Nat from me, and probably Michelle as well.{/alpha}{fast}{nw}"

    "I need to make it pay."

    "Michelle lets go of me, her face flushed and gaze slightly muddled."

    show michelle jacket front speaking closer
    with dissolve

    michelle "We need to kill this thing. The sooner the better."

    $ _history = False

    show michelle jacket front closer
    with dissolve

    show maxGhostWideRight

    friendMax "She's right, you know."

    "Max reappears at the corner of my vision. I try to focus on him, but I can't."

    friendMax "You can't change the past."

    friendMax "It's set in stone. Once something has happened, it's happened."

    friendMax "But you can get revenge. Kill that serpent. Avenge me!"

    $ _history = True

    hide maxGhostWideRight
    with dissolve

    "I sigh in resignation."

    "I'm trapped. There is no way backwards, no path to the side."

    "I'm locked on this course of action."

    "If I give up now, all of those who have died will be in vain."

    "Killing the Serpent won't bring Nat back."

    $ _history = False

    "Or Max."

    $ _history = True

    "{alpha=0}Or those people that died in Michelle's house fire.{/alpha}{fast}{nw}"

    "I know that, but it will at least prevent anyone else from having this same torment."

    "But for now I need an ally - even if she is an arsonist."

    "My mind is made up. There will be time for grief later. For now, it's time for action."

    doug "Let's kill this motherfucker tonight."

    stop music fadeout 4

    show michelle jacket front determined closer
    with dissolve

    "Michelle smiles triumphantly and pulls me closer again..."

    scene bg black with dissolve
    $ renpy.pause(delay=2, hard=True)


    jump dougActFiveSceneFive
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
