label dougActOneSceneTwo:

    $ stopAllAudioTracks()


    window show
    scene bg black
    with dissolve


    scene bg street dark

    play ad_bg_1 "sounds/doug/act_1/doug_nighttime_traffic.ogg" fadein 1.5

    "The evening is starting to get a little warmer, but only marginally."

    "Even though the spring days are starting to heat up, the nights still retain winter's chill."

    "Soon the days will start getting longer and you’ll be able to go out without a jacket."

    "I’m looking forward to that."

    "I should let Mum know I’m coming home."

    doug "Ah shit."

    "I fumble around my bag, but my phone is nowhere to be seen. I must have left it at Max’s house."

    "I hope he’s still up."

    $ renpy.music.play("sounds/doug/act_1/bgm_serpent_pt1_bass.ogg", channel='ad_fg_1', loop=True, fadeout=None, synchro_start = True, fadein = 0.5, tight=None, if_changed=False)
    $ renpy.music.play("sounds/doug/act_1/bgm_serpent_pt1_cello.ogg", channel='ad_fg_2', loop=True, fadeout=None, synchro_start = True, fadein = 0.5, tight=None, if_changed=False)
    $ renpy.music.play("sounds/doug/act_1/bgm_serpent_pt1_viola.ogg", channel='ad_fg_3', loop=True, fadeout=None, synchro_start = True, fadein = 0.5, tight=None, if_changed=False)
    $ renpy.music.play("sounds/doug/act_1/bgm_serpent_pt1_violin2.ogg", channel='ad_fg_4', loop=True, fadeout=None, synchro_start = True, fadein = 0.5, tight=None, if_changed=False)
    $ renpy.music.play("sounds/doug/act_1/bgm_serpent_pt1_glockenspiel.ogg", channel='ad_fg_5', loop=True, fadeout=None, synchro_start = True, fadein = 0.5, tight=None, if_changed=False)
    $ renpy.music.play("sounds/doug/act_1/bgm_serpent_pt1_violin1.ogg", channel='ad_fg_6', loop=True, fadeout=None, synchro_start = True, fadein = 0.5, tight=None, if_changed=False)
    $ renpy.music.play("sounds/doug/act_1/bgm_serpent_pt2_master.ogg", channel='ad_fg_7', loop=True, fadeout=None, synchro_start = True, fadein = 0.5, tight=None, if_changed=False)
    $ renpy.music.play("sounds/doug/act_1/bgm_serpent_pt1_master.ogg", channel='ad_fg_8', loop=True, fadeout=None, synchro_start = True, fadein = 0.5, tight=None, if_changed=False)
    $ renpy.music.set_volume (0.75, 0, channel="ad_fg_1")
    $ renpy.music.set_volume (0, 0, channel="ad_fg_2")
    $ renpy.music.set_volume (0, 0, channel="ad_fg_3")
    $ renpy.music.set_volume (0, 0, channel="ad_fg_4")
    $ renpy.music.set_volume (0, 0, channel="ad_fg_5")
    $ renpy.music.set_volume (0, 0, channel="ad_fg_6")
    $ renpy.music.set_volume (0, 0, channel="ad_fg_7")
    $ renpy.music.set_volume (0, 0, channel="ad_fg_8")



    show bg street dark



    "As I approach Max’s house I can see lights dancing through his window."

    "He’s still watching TV."

    "I try the door,{nw}"

    play sound "sounds/doug/act_1/doug_door_open.ogg"
    stop ad_bg_1 fadeout 3

    extend " thankfully it is unlocked. I guess his parents are asleep already; there’d be hell to pay if I woke them up."


    show serpentMovieBG


    $ renpy.sound.play("sounds/doug/act_1/doug_distorted_water_pt1.ogg", channel='ad_bg_5', loop=True, fadeout=None, fadein = 0.5, tight=None)
    $ renpy.sound.play("sounds/doug/act_1/doug_distorted_water_pt2.ogg", channel='ad_bg_6', loop=True, fadeout=None, fadein = 0.5, tight=None)
    $ renpy.sound.play("sounds/doug/act_1/doug_distorted_water_pt3.ogg", channel='ad_bg_7', loop=True, fadeout=None, fadein = 0.5, tight=None)
    $ renpy.sound.set_volume (0.2, 3, channel="ad_bg_5")
    $ renpy.sound.set_volume (0, 0, channel="ad_bg_6")
    $ renpy.sound.set_volume (0, 0, channel="ad_bg_7")



    $ renpy.music.set_volume (0.75, 1, channel="ad_fg_2")

    "Inside the sound of water echoes faintly. I shouldn’t have worried about waking anyone up; they're obviously watching something."


    "Regardless, habit makes me creep up the stairs - just in case. I feel like a thief in the night."

    play sound "sounds/doug/act_1/doug_serpent_chomp_3.ogg"

    "What the hell was that?"


    $ renpy.music.set_volume (0.75, 1, channel="ad_fg_3")

    play ad_bg_2 "sounds/doug/act_1/doug_heartbeat_58_bpm.ogg" fadein 10

    $ renpy.sound.set_volume (1, 3, channel="ad_bg_2")
    $ renpy.sound.set_volume (0.4, 5, channel="ad_bg_5")
    $ renpy.sound.set_volume (0.35, 8, channel="ad_bg_6")

    "A pang of dread spears through my heart. This isn't sound from a movie; this is real."

    "Light is pouring out of Max’s parent’s room, and the same watery sound."

    "It's too loud to be a shower, and it feels like it's moving around the house."

    doug "Max…? Are you okay?"

    $ renpy.music.set_volume (1, 3, channel="ad_fg_4")

    "My heart pounds against my chest and I find it hard to swallow. My mouth is dry; my call to Max seems more like a whimper."

    "The air smells of ozone and the hair on my arms starts to stand on end."

    play sound "sounds/doug/act_1/doug_zap.ogg" noloop

    "I feel arcs of static electricity shooting from my hand to the stairway, and I yelp in shock."


    $ renpy.music.set_volume (0.6, 1, channel="ad_fg_5")

    "I reach for the banister to steady myself, but the solid wood seems to flex at my touch."

    "Like it's made of sponge."

    "The steps, too, feel like they could give way under my weight, even though I've bounded up them a hundred times or more."

    "I try to shake it off. It's late at night and my mind is playing tricks on me."

    "Even my eyes are finding it hard to focus on the world around me."

    "It's as if I'm in some new reality that my body wasn't built to handle."

    $ renpy.music.set_volume (0.6, 1  , channel="ad_fg_6")

    $ renpy.sound.set_volume (0.5, 3, channel="ad_bg_5")
    $ renpy.sound.set_volume (0.5, 2, channel="ad_bg_6")
    $ renpy.sound.set_volume (0.5, 5, channel="ad_bg_7")


    play ad_bg_3 "sounds/doug/act_1/doug_serpent_low_right.ogg" noloop

    play ad_bg_2 "sounds/doug/act_1/doug_heartbeat_120_bpm.ogg"

    "I can feel a presence getting closer and the sound of water getting louder."

    $ renpy.sound.set_volume (1, 2, channel="ad_bg_2")

    "It’s the noise of a river bursting its banks and charging down a street."

    "I creep up the last stairs and into the darkened landing, rounding the corner with caution."


    $ floatDelay = getCurrentTimeAsFloat('ad_fg_1')

    window hide
    show bg black
    with Dissolve (floatDelay)
    hide serpentMovieBG

    play ad_bg_3 "sounds/doug/act_1/doug_serpent_low_right.ogg" noloop
    play ad_bg_1 "sounds/doug/act_1/doug_serpent_low_left.ogg" noloop


    $ renpy.pause(delay=floatDelay, hard=True)




    stop ad_fg_1 fadeout 0.1
    stop ad_fg_2 fadeout 0.1
    stop ad_fg_3 fadeout 0.1
    stop ad_fg_4 fadeout 0.1
    stop ad_fg_6 fadeout 0.1

    $ renpy.music.set_volume (0.55, 0, channel="ad_fg_7")
    $ renpy.music.set_volume (0, 0, channel="ad_fg_5")

    scene cg max house serpent with dissolve

    "Before I realize it, I’m seeing something indescribable. I’m frozen in fear, my hands clutching the handrail of the stairway."

    play ad_bg_3 "sounds/doug/act_1/doug_serpent_low_left.ogg" noloop

    "A giant, glowing head arches out from Max’s parent’s bedroom."

    "At least, I think it is a head. From the front it is nothing but teeth; rows and rows of teeth disappearing into an endless blood-red maw."

    "The creature twists and shows me its body."

    "It is like a floating snake, a fluid tube about a foot across, winding its way from Max’s parent’s room."

    "Its skin is flowing liquid, glowing and brilliant. Colors dance across its surface in constant motion."

    "It’s as beautiful as it is terrifying; I can do nothing but look - not even a breath escapes from my lips."

    "The head bobs and weaves, as if it is searching for something, before ploughing into the hallway wall."

    doug "Max!"

    stop ad_bg_2 fadeout 3

    play ad_bg_3 "sounds/doug/act_1/doug_serpent_purring.ogg" noloop

    scene cg max almost dies
    with fade

    "My body engages before my brain can catch up, and I charge into Max’s room."

    "The snake is already coiling up in Max’s room and I can see him on his bed, frozen in panic."

    "The beast’s head is arched up to the ceiling, swaying like a cobra about to strike, fixated on Max."

    "I grab a pen from Max’s desk - it’s the closest thing that I can find, and try to stab the glowing, fluid body."

    "The pen and my hand pass through the snake’s body, and for a moment I feel lost in time."

    "The terrible sensation of touching the beast instantly sets my body afire, and I feel my stomach wretch as it heaves up its contents."

    play sound "sounds/doug/act_1/doug_vomit_2.ogg"

    "My projectile vomit phases through the snake’s body and all over Max’s desk."

    friendMax "D-Doug! Help me…!"

    doug "Get out of here!"

    "I try to grasp the snake’s body again, but my hands can’t find purchase. Nausea washes over my body again as I make contact with the strange, fluid body."

    friendMax "Doug!"

    scene cg max dies
    $ renpy.sound.set_volume (1, 0, channel="ad_bg_2")
    $ renpy.sound.set_volume (1, 0, channel="sound")
    play sound "sounds/doug/act_1/doug_distorted_roar.ogg"
    play ad_bg_2 "sounds/doug/act_1/doug_max_eaten.ogg"

    "In an instant, the serpent pounces. It’s endless mouth opens wide before it slams itself upon Max’s helpless body."

    "The snake’s skin glows ever brighter, more blinding than the sun, and I have to shield my eyes."

    "Instinctively, I charge into the beast, arms flailing, trying to save my friend."

    $ renpy.sound.set_volume (0.2, 0.2, channel="ad_bg_2")
    play ad_bg_2 "sounds/doug/act_1/doug_spooky_noise.ogg" noloop
    play sound "sounds/doug/act_1/doug_water_splash.ogg"
    "I feel my whole body crash into the watery form, and my brain starts to freeze."

    scene bg black
    with vpunch

    $ renpy.music.set_volume (0.6, 0.2, channel="ad_fg_5")
    $ renpy.music.set_volume (0.3, 0.2, channel="ad_fg_7")
    $ renpy.sound.set_volume (0, 0.2, channel="ad_bg_1")
    $ renpy.sound.set_volume (0, 0.2, channel="ad_bg_3")
    $ renpy.sound.set_volume (0, 0.2, channel="ad_bg_5")
    $ renpy.sound.set_volume (0.2, 0.2, channel="ad_bg_6")
    $ renpy.sound.set_volume (0.2, 0.2, channel="ad_bg_7")
    $ renpy.sound.set_volume (0, 0.2, channel="sound")

    "My eyes feel like they will bulge out of my head, and my skin bristles."

    "I can hear nothing but the darkness of the void."

    "Electricity arcs in my nose; a burning, artificial smell."

    "It's like my body is being warped and stretched in every direction at once."

    "Suddenly, I have phased through the snake’s body and reached the other side."

    scene cg max dies with vpunch

    $ renpy.music.set_volume (0, 0.2, channel="ad_fg_5")
    $ renpy.music.set_volume (0.6, 1, channel="ad_fg_7")
    $ renpy.sound.set_volume (1, 1, channel="ad_bg_1")
    $ renpy.sound.set_volume (1, 1, channel="ad_bg_2")
    $ renpy.sound.set_volume (1, 1, channel="ad_bg_3")
    $ renpy.sound.set_volume (1, 1, channel="ad_bg_4")
    $ renpy.sound.set_volume (0.55, 1, channel="ad_bg_5")
    $ renpy.sound.set_volume (0.55, 1, channel="ad_bg_6")
    $ renpy.sound.set_volume (0.55, 1, channel="ad_bg_7")
    $ renpy.sound.set_volume (1, 1, channel="sound")

    stop ad_bg_2 fadeout 0.1

    "The beast is ignoring me completely."

    "It uncoils itself as it continues downward through Max’s bed, sloshing and gurgling as it rushes past me."

    "In a moment it is gone and the room is shrouded in darkness."

    stop ad_bg_5 fadeout 3
    stop ad_bg_6 fadeout 3
    stop ad_bg_7 fadeout 3

    scene bg black
    with fade

    $ floatDelay = getCurrentTimeAsFloat('ad_fg_7')

    $ renpy.pause(delay=floatDelay, hard=True)
    $ renpy.music.set_volume (0, 2, channel="ad_fg_7")
    $ renpy.music.set_volume (0.6, 2, channel="ad_fg_5")





    "It takes a moment for my eyes to adjust."

    doug "M-Max?"

    "My voice is a hoarse whisper."

    "I creep towards Max’s bed, groping against the darkness."

    doug "Max?"

    "My voice returns slightly."

    "Part of me hopes that Max, like myself, simply passed through this phantom beast; rattled but unharmed."

    show bg_max_room_inside_dark_changed
    with dissolve

    "As the darkness starts to give way, I can finally see Max’s room."

    $ _history = True

    $ showHiddenText('',"Sleep does not come easily to me.{fast}{nw}")

    $ _history = False

    "It's perfectly empty, as if it were a showroom model that had never been lived in."

    $ _history = True

    $ showHiddenText('',"I dream of an endless red desert capped with a pitch black sky.{fast}{nw}")

    $ _history = False

    "Max is nowhere to be seen."

    $ _history = True

    $ showHiddenText('', "But then, from above, I feel a presence.{fast}{nw}")

    $ _history = False

    doug "Max?"

    $ _history = True

    $ showHiddenText ('', "A girl's face, younger than me, appears above me.{fast}{nw}")

    $ _history = False

    doug "Max?"

    $ _history = True

    $ showHiddenText(doug, "Nat, is that you?{fast}{nw}")

    "There is no answer."

    $ showHiddenText('', "But I feel an unbidden hand on my cheek.")

    scene bg_max_house_corridor_upstairs

    $ _history = False

    $ renpy.sound.set_volume (0.6, 0, channel="ad_bg_4")
    play ad_bg_4 "sounds/doug/act_1/doug_distorted_water.ogg" fadein 10

    stop music fadeout 1.0
    stop ad_bg_1 fadeout 1.0

    stop ad_fg_7 fadeout 1
    stop ad_fg_8 fadeout 1

    "I force my weakened body to Max’s parent’s room. Again, there is no-one there."

    "From downstairs the gurgling sound of water creeps back into my perception."


    $ renpy.music.set_volume (0.6, 0.2, channel="ad_fg_7")

    $ _history = True

    $ showHiddenText('',"I can hear a gurgling swirl around me, and rivers are carved into the desert.{fast}{nw}")

    scene bg_max_corridor_dark_serpent_lights_2

    $ _history = False

    "Flashing colours light up the stairwell as the beast moves around the ground floor of the house."

    $ _history = True

    $ showHiddenText('',"Flashing colours light up the sky as the world is formed before my eyes.{fast}{nw}")

    $ _history = False

    "I drag myself over the ledge of the balustrade and take a deep breath."

    $ _history = True

    $ showHiddenText('', "Rivers begin to flow around me, filling with their cooling water.{fast}{nw}")

    "The rushing water sound grows in volume and the light increases in intensity."

    $ showHiddenText('', "But the girl doesn't leave me.{fast}{nw}")



    stop music fadeout 1.0
    stop ad_bg_1 fadeout 1.0
    stop ad_fg_5 fadeout 1
    stop ad_fg_7 fadeout 1
    stop ad_fg_8 fadeout 1

    $ _history = False

    "With a guttural scream I launch myself down the stairwell and onto the back of the beast."

    play ad_bg_3 "sounds/doug/act_1/sfx_serpent_stab.ogg" noloop
    play sound "sounds/doug/act_1/doug_water_flailing.ogg"
    scene bg_max_corridor_dark_serpent_lights_3 with hpunch
    play ad_bg_2 "sounds/doug/act_1/doug_michelle_car_bump.ogg" noloop
    doug "Fuck you!{w=1.75}{nw}"


    stop ad_bg_4 fadeout 1.0
    stop ad_fg_7 fadeout 1.0
    stop ad_fg_8 fadeout 1.0
    stop ad_bg_3 fadeout 0.5

    scene bg black
    with fade

    stop sound fadeout 1.0



    $ _history = True



    $ resetTracksAudio([
        "ad_fg_1", "ad_fg_2", "ad_fg_3", "ad_fg_4", "ad_fg_5", "ad_fg_6", "ad_fg_7", "ad_fg_8",
        "music",
        "ad_bg_4", "ad_bg_5", "ad_bg_6", "ad_bg_7"
    ])


    $ renpy.movie_cutscene("videos/intro.webm")


    jump dougActOneSceneThree
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
