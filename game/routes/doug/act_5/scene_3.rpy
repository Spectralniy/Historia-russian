label dougActFiveSceneThree:

    $ stopAllAudioTracks()


    window show
    scene bg black
    with dissolve













    scene cg principal office
    with dissolve

    play ad_bg_1 "sounds/doug/act_1/doug_heartbeat_90_bpm.ogg" fadein 2 fadeout 2
    play sound "sounds/doug/act_1/doug_light_door_knock.ogg"
    $ renpy.music.play("sounds/doug/act_1/bgm_dead_sister_piano_top.ogg", channel='ad_fg_1', loop=True, fadeout=None, synchro_start = True, fadein = 0.5, tight=None, if_changed=False)
    $ renpy.music.play("sounds/doug/act_1/bgm_dead_sister_piano_bottom.ogg", channel='ad_fg_2', loop=True, fadeout=None, synchro_start = True, fadein = 0.5, tight=None, if_changed=False)
    $ renpy.music.play("sounds/doug/act_1/bgm_dead_sister_strings.ogg", channel='ad_fg_3', loop=True, fadeout=None, synchro_start = True, fadein = 0.5, tight=None, if_changed=False)
    $ renpy.music.play("sounds/doug/act_1/bgm_dead_sister_full.ogg", channel='ad_fg_4', loop=True, fadeout=None, synchro_start = True, fadein = 0.5, tight=None, if_changed=False)
    $ renpy.music.set_volume (0.75, 5, channel="ad_fg_1")
    $ renpy.music.set_volume (0, 0, channel="ad_fg_2")
    $ renpy.music.set_volume (0, 0, channel="ad_fg_3")
    $ renpy.music.set_volume (0, 0, channel="ad_fg_4")

    "I rap lightly on the door and the principal, ashen faced, beckons me into her office."

    principal "Douglas… I…"

    "I don't see any police."

    "And… there is something about her face, her expression."

    "My nerves might be getting the better of me, but something is wrong."

    "Instincts are screaming at me in a confusing chorus. I don't know if I should run or sit."

    principal "Please… sit down… I have some -{w} some bad news."

    "The penny drops. This isn't about me."

    play ad_bg_1 "sounds/doug/act_1/doug_heartbeat_120_bpm.ogg" fadein 0.2 fadeout 0.2

    $ renpy.sound.set_volume(1, delay=7, channel='ad_bg_1')

    $ renpy.music.set_volume (0.75, 4, channel="ad_fg_2")

    "But that means…"

    "I sit down."

    principal "There's been an accident…"

    principal "…at the dam."

    "Her words are drowned out by my heartbeat, now deafening in my ears."

    doug "Nat…? Is Nat okay…?"

    principal "Your parents will pick you up from here and take you to the hospital…"

    "My body is trembling, and I feel weak."

    doug "Is Nat ok? Is my sister OK?"

    "I don't realise it but I'm screaming."

    $ renpy.music.set_volume (0.75, 3, channel="ad_fg_3")

    "The Principal doesn't answer, but her face tells me the answer."

    doug "She'll be ok, right? Right?!"

    principal "I'm sorry… but your parents will be here soon."

    principal "They should be the ones to tell you…"

    stop ad_bg_1 fadeout 5
    $ renpy.sound.set_volume(1, delay=0, channel='ad_bg_1')

    scene bg hospital
    with dissolve

    show doug mum worried at right
    with dissolve

    show doug_dad shirt looking down at left
    with dissolve

    play ad_bg_2 "sounds/doug/act_1/doug_hospital_bg.ogg"

    stop ad_fg_1 fadeout 5
    stop ad_fg_2 fadeout 5
    stop ad_fg_3 fadeout 5

    $ renpy.music.set_volume (1, 15, channel="ad_fg_1")
    $ renpy.music.set_volume (1, 15, channel="ad_fg_2")
    $ renpy.music.set_volume (1, 15, channel="ad_fg_3")
    $ renpy.music.set_volume (0.45, 5, channel="ad_fg_4")

    "The scent of disinfectant."

    "The bustle of people shuffling around the waiting room."

    "That damned, incessant beeping."

    "Why isn't anyone talking to us?"

    "I'm still shaking. Dad picked me up from school in a taxi. He was as white as a ghost, and silent the whole time."

    "I don't think he could speak even if he tried."

    "Mum was already at the hospital when the accident occurred, but since she was a relative, they wouldn't let her in."

    "An orderly showed us to the waiting room, and I could tell from their face that it wasn't good news."

    "Slowly we began to piece together some of the story."

    "The year nine class had gone to the dam for their field trip."

    "It was a standard thing at our school. You learn about hydro power and the water cycle."

    "But, somehow, Natalia had gone beyond a barrier…"

    "…and fallen."

    "She was airlifted out by helicopter."

    "And we were all dragged here in a rush."

    "But it's been an hour now, and we haven't heard anything."

    "Mum is furious. Every five minutes she storms up to the nurse's station demanding answers."

    "To their credit, her colleagues don't buckle."

    "Frustrated, she gives up and returns to her plastic waiting room chair."

    "I've gnawed my nails down as far as I can. Blood leaks around their ragged edges."

    "Dad hasn't moved since he sat down. He's literally petrified of what comes next."

    "I can't believe what is happening, even though at this point we all know in our hearts what the result will be."

    "Part of me expects a surgeon in tattered scrubs to come bursting through the door at any moment, beaming at us, telling us that we can see her now."

    "And that Nat will be lying on a hospital bed, bruised and sporting a drip, but smiling faintly back at us."

    "I want that so bad."

    "But my heart is filled with doubt."

    "Every time the door swings open my head snaps around like a meercat, desperate for some news."

    "And yet, when the news comes, I didn't even hear the operating theatre's door open."

    show surgeon sad
    with dissolve

    "Oh shit."

    "He hasn't said a word, but his stance, his face, his eyes…"

    "…his eyes tell me everything I need to know."

    show doug mum wailing
    with dissolve
    show doug_dad shirt blank
    with dissolve

    "Mum collapses on the spot before he can even open his mouth."

    "Dad doesn't react. He's a statue, incapable of thought."

    surgeon "I'm… {w}I'm sorry."

    "My knees go weak. Even sitting down I can feel that my joints won't support me, so I stay put."

    "Mum begins to wail. The duty nurse rushes to her, but Mum pushes her away."

    "She stumbles away, her cries fading only barely as she dissappears from my sight."

    hide doug
    with moveoutright

    surgeon "We tried everything, but it was too late."

    "Dad stands, shakes the surgeon's hand, and walks out of the waiting room without once opening his mouth."

    hide doug_dad
    with moveoutleft

    "My mind is racing, trying to think of a way out of this."

    "It can't be real."

    "We were talking at breakfast."

    "She seemed just as happy as ever."

    doug "She's… {w=0.7}dead…?"

    "The surgeon nods grimly."

    surgeon "I'm afraid that the fall was unsurvivable."

    "I shouldn't have asked."

    "If he didn't confirm it, then maybe I didn't have to know."

    "But, like Schroedinger's cat, I've opened the box."

    "Until I asked, there was a slim chance that she was alive."

    "By asking the question I feel like I've sealed her fate."

    "My mind goes blank. I can't think. It's like my brain has stalled, permanently."

    "Then, one by one, images start to come into my mind."

    "Watching her graduate from high school."

    "Catching up at New Year's because we're going to different universities."

    "Nat at her wedding day."

    "Me looking after her kids for an afternoon."

    "My stomach turns at the waste of life, the things we won't get to do together."

    "Before I know it, my mouth is moving."

    doug "How… {w=0.3}how did it happen?"

    "The surgeon sits on the seat next to me, putting his arm around me."

    surgeon "We're not sure why, but she had crossed a barrier."

    surgeon "She fell down the face of the dam."

    "Chills race down my spine."

    "All I can imagine was how afraid she would have been as she tumbled through the air."

    "The pain of impacting with the dam wall on the way down."

    "How lonely she must have been, lying in a crumpled heap at the bottom of the concrete structure."

    "I let out an involuntary gasp as I replay the ordeal again and again in my head."

    surgeon "She… {w=0.2}would have lost consciousness straight away."

    surgeon "There would have been no pain…"

    "I know that he's trying to comfort me."

    "As an emergency surgeon he must have had to break the news to other family members in the past."

    "It could be true, or he might be lying. Either way, his words provide a small blanket of comfort."

    surgeon "Here, take this."

    "He hands me a handkerchief. I didn't realise it, but tears have been pouring down my cheeks."

    doug "Thanks."

    "I dab away the tears; my body running on auto-pilot."

    surgeon "Let me get someone to call a cab for your family."

    surgeon "It's best that you all go home and stick together."

    surgeon "The hospital's councillor will be in touch with your mother."

    surgeon "If you have any questions, you can call them."

    doug "Thanks."

    "The surgeon pats me on the back reassuringly, but I barely register the gesture."

    hide surgeon with dissolve

    "Images of Natalia tumbling like a rag doll over the edge of the dam replay constantly in my mind."

    "I shudder as I feel the impacts as if it were my own body."

    "And I can't get her face out of my mind. Her smile. Her laugh."

    $ renpy.sound.set_volume(0.2, delay=5, channel='ad_bg_2')
    $ renpy.music.set_volume (0, 7, channel="ad_fg_4")


    play music "sounds/doug/act_1/doug_reality_bubble.ogg" fadein 7

    "All gone. And for what?"

    "Just what was the purpose of her life?"

    "To be squandered like this?"

    $ _history = False

    "Max, if you're out there, I could really use a friend right now."

    $ _history = True

    "{alpha=0}Max you slimy fuck, show yourself{/alpha}{fast}{nw}"

    $ _history = False

    show maxGhost

    friendMax "You rang?"

    $ _history = True

    $ line = renpy.transform_text("You rang?", scrambling)
    $ line2 = renpy.transform_text("xXëæm", scrambling)
    "[line2]" "{alpha=0}[line]{/alpha}{fast}{nw}"

    $ line = renpy.transform_text("xXëæƏmM", scrambling)
    "{alpha=0}[line], clear as day, is sitting beside me in the waiting room.{/alpha}{fast}{nw}"

    $ _history = False

    "Max, clear as day, is sitting beside me in the waiting room."

    friendMax "You look bummed. What happened?"

    $ _history = True

    doug "Natalia… she's dead."

    hide maxGhost with dissolve
    show maxGhostSeriousBloody with dissolve

    doug "Like you."

    $ _history = False

    friendMax "Ouch. That sucks. You all right bro?"

    $ _history = True

    doug "All right? My best friend and my sister are dead! How the fuck am I supposed to be all right?"

    $ _history = False

    hide maxGhostSeriousBloody with dissolve
    show maxGhostBummedBloody with dissolve

    friendMax "Woah, ok dude. Chill. Just tying to lighten the mood."

    $ _history = True

    doug "Sorry. I'm kind of stressed right now."

    $ _history = False

    hide maxGhostBummedBloody
    with Dissolve(0.2)
    show maxGhostSmugBloody
    with dissolve

    friendMax "I can imagine."

    friendMax "How are your parents?"

    $ _history = True

    "[line2]" "{alpha=0}Think of your parents{/alpha}{fast}{nw}"

    doug "They're both broken in their own ways."

    doug "I don't think they can handle this."

    $ _history = False

    hide maxGhostSmugBloody
    with Dissolve(0.2)
    show maxGhostBummedBloody
    with Dissolve(0.5)

    friendMax "And you?"

    $ _history = True

    doug "I just can't stop thinking about how scared she must have been."

    doug "Lonely and scared."

    doug "If they brought her here, she must have been some signs of life."

    doug "And none of us were here for her."

    doug "She died without any of us being able to do anything for her."

    $ _history = False

    hide maxGhostBummedBloody
    with Dissolve(0.2)
    show maxGhostSeriousBloody
    with Dissolve(0.5)

    friendMax "Damn. That's dark. You don't seem ok at all."

    $ _history = True

    doug "{alpha=0}I'm not ok at all… {/alpha}{fast}{nw}"

    $ _history = False

    doug "I don't know what I am right now."

    hide maxGhostSeriousBloody with dissolve
    show maxGhostBummedBloody

    friendMax "Well, I know one thing."

    friendMax "And that's that you need to get out of here."

    $ _history = True

    friendMax "{alpha=0}GET OUT GET OUT GET OUT GET OUT GET OUT GET OUT GET OUT GET OUT GET OUT GET OUT GET OUT GET OUT GET OUT GET OUT GET OUT GET OUT{/alpha}{fast}{nw}"

    stop music fadeout 15

    $ _history = False

    friendMax "Hospitals give off bad vibes."

    friendMax "And your mum looks like she needs some help…"

    $ _history = True

    hide maxGhostBummedBloody
    with Dissolve(1.0)

    show doug mum wailing
    with dissolve

    "I pull myself out of my own head long enough to look at my mother, who is still sobbing on the floor."

    "Her colleagues are giving her some distance, watching with respectful and remorseful faces."

    "Somehow I manage to drag myself to my feet and walk over to her."

    doug "Mum… I'm sorry…"

    "She doesn't say anything, but clutches my legs."

    "I can feel her body shift as she tries to calm herself down with deep breaths."

    show doug mum worried
    with dissolve

    "Slowly she stands up, using my body to steady hers."

    "I can only imagine what she's thinking."

    "After working in the emergency ward for more than two decades, she must have seen her fair share of trauma."

    "But now it's personal."

    "Her only daughter has been taken away."

    doug "Let's go home."

    "She nods at me, and I wrap my arms around her waist."

    "We support each other towards the door and to the taxi waiting beyond."



    stop ad_fg_4 fadeout 3.0
    stop ad_bg_2 fadeout 3.0
    $ renpy.sound.set_volume(1, delay=3.0, channel='ad_bg_2')
    $ renpy.music.set_volume (1, 7, channel="ad_fg_4")

    jump dougActFiveSceneFour
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
