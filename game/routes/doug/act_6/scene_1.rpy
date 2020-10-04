label dougActSixSceneOne:

    $ stopAllAudioTracks()


    window hide
    scene bg black
    with dissolve


    scene cg natalias funeral
    with Dissolve(4)
    window show
    with dissolve






    play ad_bg_1 "sounds/doug/act_1/doug_funeral_amb.ogg" loop
    $ renpy.music.set_volume (0.6,0, channel="music")
    play music "sounds/doug/act_1/bgm_dead_sister_full.ogg"

    "I wish it were raining."

    "Until today, I always imagined that funerals only took place in the rain."

    "But instead the sun is shining bright, and the cool spring breeze comfortably wafts between the assembled onlookers."

    "A sea of sad faces in their best clothes."

    "Soft sobs from children who aren't yet capable of understanding what has happened."

    "Mournful adults shaking their heads and repeating platitudes about how it was a life taken too early."

    "And here I am, waiting silently for the hearse to arrive."

    "Dad stands next to me, dutifully shaking hands with everyone that comes to offer condolences."

    "He thanks them, but I know what he's thinking. He would give all he had to be anywhere else in the world."

    "Mum is trying to contain herself but her constant sniffling tells the truth of the matter."

    "People from my class in school stand around nervously, not knowing what to say to me."

    "They roll out the tropes they've seen on TV."

    "'I'm sorry for your loss.'"

    "'She was taken before her time.'"

    "'If there's anything I can do…'"

    "Sweet nothings said in a time of crisis."

    "And me? I'm furious."

    "Furious that Michelle put me here."

    "Furious that I was powerless to stop her, and that she's now on the loose, probably making someone else's life hell."

    play sound "sounds/doug/act_1/doug_car_approach_EXT.mp3"

    "Furious at the Serpent for throwing me into this situation."

    "If only I didn't leave my phone at Max's house that night and let the Serpent go about its business."

    "I would have been as clueless as the rest of the people gathered here today."

    "But I'm not."

    "Everyone else here thinks about today as the end of a tragic accident."

    "But I know the truth. And I can't tell anyone."

    "Natalia was murdered in cold blood."

    "Murdered so that a psychopath could chase ghosts."

    $ renpy.sound.set_volume (0.5, 1, channel="ad_bg_1")

    "There is suddenly a shift in the crowd, and I look towards the cemetery gates."

    "The unmistakable shape of the hearse is winding its way towards the chapel."

    "My heart stops. I thought I was ready for this but I'm not."

    "I want to run. Run into the rolling field of green dotted with grey headstones."

    "But I stand fast."

    "This isn't my day."

    "It's Nat's."

    "One more goodbye before the dark night."

    "I take a deep breath and try to remember what the funeral director told us."

    "The hearse will arrive here, and they'll move the casket onto a trolley."

    "The crowd will have a chance to write their last farewells on the outside, then we will carry her into the chapel."

    "Mum opted for cremation. She couldn't bear the thought of her only daughter rotting away in the ground."

    "We'll all say a few words, and then that will be it."

    "I subconsciously feel for the folded paper in my jacket pocket."

    "I tried to write some words down last night, but I couldn't think of anything that seemed worthy of the occasion."

    "It was too much pressure."

    "How are you supposed to say goodbye to someone that you've always known?"

    "I secretly hope that the hearse never arrives and that I don't have to speak."

    "But my wishes can't stop time. The hearse is soon upon us, slowing as the crowd parts to let it through."

    "The rumbling engine stops, and for a moment there is no sound in the cemetery."

    stop sound fadeout 3

    "A few sniffles break the tension, and the undertakers alight from the vehicle, solemnly opening the back door to reveal the tiny white coffin."

    "It's smaller than I imagined. I can't picture Nat crammed inside."

    "But thankfully I don't have to see that."

    "The undertakers skillfully remove the casket and place it onto a wheeled trolley and position Nat at the door of the chapel."

    funeralDirector "Ladies and Gentlemen. Before the service the family would like to invite you to write a farewell message on the coffin."

    funeralDirector "There are markers available here. We will begin in fifteen minutes."

    "Hearing such a loud voice after the whispers of the crowd is a bit of a shock to me."

    "The funeral director then passes a marker to my father, who pauses for a moment before scribbling on the white veneer of the coffin."

    "His writing is barely legible."

    "He passes the marker to my mother, but he places a hand on the coffin, his chest heaving as he tries to maintain his composure."

    "Mum scrawls 'Wait for me' on the side of the coffin and passes the marker to me."

    "I can't think of what to write. My emotions are too turbulent to be coherent."

    "I quickly scribble 'Love you always little sister' and hand the pen to the next person waiting."

    "As we step back the crowd descends on the coffin, and soon the white surface is a colourful montage of farewells, in-jokes and doodles."

    "Some of her friends laugh through tears as they write secret messages that only they would understand."

    "I want to yell at them, to stop them desecrating my sister, but Mum holds me back."

    mom "Everyone grieves in their own way."

    mom "You don't have a monopoly on your sister."

    "I let my shoulders sag and scan the crowd."

    "Almost everyone from Nat's class is here."

    "Save one obvious exception."

    "I'm not sure how I would react if Michelle showed her face here."

    "But I'm pretty sure that I wouldn't let her leave alive."

    "I take a nervous breath and decide to focus on the task at hand."

    "Some of the older relatives have already started to file inside the small chapel and take their seats."

    "There clearly aren't enough seats for everyone."

    "I guess that is an advantage of dying young; you still have enough friends to pack out a funeral."

    "I remember when my grandmother died, and apart from us, the only other guests were residents of her nursing home."

    "They were bussed in."

    "A service provided by the home so that no-one was alone at their final goodbye."

    "In the end, death comes for us all."

    stop ad_bg_1 fadeout 15
    $ renpy.sound.set_volume (1, 15, channel="ad_bg_1")

    "The crowd outside begins to thin, and the pall bearers take up their position."

    "I stand opposite Dad, his face contorted by pain and grief."

    "Clearly, he doesn't want to do this."

    funeralDirector "Ok, we're going to lift on three. One, two… three…"

    show cg natalias funeral coffin
    with dissolve

    "We clumsily lift the heavy coffin up onto our shoulders and the undertakers remove the trolley."

    "With the coffin against my face I can read more of the messages."

    "I avert my eyes; I don't want to feel anything anymore."

    "But the messages seep into my brain, and I realise how little I knew about my sister."

    "Her friends."

    "Her dreams."

    "I'm overcome with the desire to simply sit with her for hours to ask about her world."

    "But now, I'll never get the chance."

    funeralDirector "Gentlemen, let's proceed."

    "We start to shuffle together, letting the weight of the coffin settle into our shoulders."

    "The ground shakes as we take our first steps."

    "I'm not sure if I imagined that or not."

    "We quickly settle into a rhythm as we move into the chapel."

    "The crowd stands and turns to face us."

    play sound "sounds/doug/act_1/doug_dam_boom.ogg"
    play ad_bg_4 "sounds/doug/act_1/doug_thunder_final.ogg"

    "A thunderclap rolls harmlessly over the cloudless sky."

    "I try to ignore the weight I'm lifting and the leering faces."

    "The rising bile in my stomach."

    "It feels like the earth is shifting under my feet."

    "The sounds around me filter through my head, bypassing my mind."

    "The whimpering and sniffles of the crowd."

    "The dirge playing over the chapel's sound system."

    $ renpy.music.set_volume (1, 10, channel="ad_bg_1")

    "And a distant swell of water."

    play ad_bg_2 "sounds/doug/act_1/doug_air_raid.ogg"

    "Suddenly, a klaxon cuts through the solemnity of the service."

    "I look to the funeral director leading the procession."

    show cg natalias funeral wave
    with Dissolve(3.0)

    "He turns to look back towards us."

    "Thunder and sloshing rises in crescendo, and the funeral director's jaw drops in shock."

    "Sound crashes down around me as…{nw}"
    $ _history = False

    stop ad_bg_1

    stop ad_bg_2

    stop ad_bg_4

    stop sound

    stop music
    scene bg black
    $ renpy.sound.set_volume (0.65,0,channel="sound")
    play sound "sounds/doug/act_1/doug_ebs_tone.ogg" loop

    play ad_bg_1 "sounds/doug/act_1/doug_geiger_counter.ogg" noloop
    ".{w=1.5}{nw}"
    play music "sounds/doug/act_1/bgm_best_friends.ogg" loop
    ".{fast} .{w=1.5} .{w=1.0}{nw}"
    window hide
    $ renpy.pause(delay=4, hard=True)



    show text "{b}Historia{/b}{vspace=30}Chapter 1{vspace=30}{i}by Lucid A96{/i}{nw}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve

    show text "{b}Character Art{/b}{vspace=30}NotImportant{nw}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve


    show text "{b}Background Art{/b}{vspace=30}NotImportant{vspace=20}Camille{nw}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve

    show text "{b}Music{/b}{vspace=30}ML Beck{nw}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve

    show text "{b}Scenario{/b}{vspace=30}NotImportant{vspace=20}Cpl Crud{nw}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve

    show text "{b}Technical Direction{/b}{vspace=30}Rob{vspace=20}Magic{nw}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve

    show text "{b}Video and Animation{/b}{vspace=30}Magic{vspace=20}Cpl Crud{nw}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve

    show text "{b}Sound Design{/b}{vspace=30}ML Beck{vspace=20}Cpl Crud{nw}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve

    show text "{b}Proof Reading{/b}{vspace=30}SilentCook{vspace=20}Zane \"Zaniel\" Critch{vspace=20}ReddlyB{vspace=20}DuaneMoody{vspace=20}MattyD{nw}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve

    show text "{b}Japan Support{/b}{vspace=30}Hir{nw}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve

    show text "{b}Producer{/b}{vspace=30}Cpl Crud{nw}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve


    $ _history = True
    stop sound
    $ renpy.sound.set_volume (1,0,channel="sound")
    stop ad_bg_1
    stop music
    play sound "<from 5 to 8.5>sounds/doug/act_1/doug_computer_telemetry.ogg" noloop
    queue sound "sounds/doug/act_1/doug_radio_chatter.ogg" noloop
    $ renpy.pause(delay=6, hard=True)


    jump dougActSixSceneTwo
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
