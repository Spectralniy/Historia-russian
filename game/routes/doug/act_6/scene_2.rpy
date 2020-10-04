label dougActSixSceneTwo:

    $ stopAllAudioTracks()


    window show
    scene cg broken dam
    with dissolve



    show damBreak with Dissolve(5.0)




























    play ad_bg_1 "sounds/doug/act_1/doug_flood_ambience.ogg" fadein 5.0 loop

    areaCommander "Ok, someone give me a SITREP, now!"

    fireChief "Sir, the dam burst around mid-afternoon. We didn't start getting reports until the flooding reached Windsor."

    fireChief "They thought it was a normal flood but the river rose much faster than ever before."

    fireChief "We managed to evacuate most of them though, but here…"

    play sound "sounds/doug/act_1/doug_siren_approach.ogg" fadein 5.0

    "The Fire Chief turns to survey the flooded dam behind him."

    "Turbulent flows of water throw up a light fog around the area, making it hard to see."

    fireChief "…here they had no chance. It would have been like a tidal wave."

    areaCommander "Any idea of what we're looking at?"

    fireChief "The police sent their 'chopper up, but they couldn't see anything."

    fireChief "We've had teams up and down the river all night looking for anyone that might be left."

    fireChief "The whole valley is flooded. It will take weeks for the water to subside, let alone assess the damage."

    areaCommander "So the whole town…?"

    "The fire chief removes his helmet, averting his eyes from the Commander's gaze."

    areaCommander "How… How many?"

    fireChief "Hard to say, but early estimates are over 20,000."

    fireChief "The entire floodplain was gone in a flash."

    fireChief "We didn't even get a call…"

    fireChief "Debris and bodies are washing up all the way to the coast."

    fireChief "It's a nightmare."



    areaCommander "And the press?"

    fireChief "We're keeping them away."

    fireChief "They know, of course, but we don't want them to see."

    areaCommander "There's no point in that. Their helicopters will have seen more than our guys by now."

    areaCommander "But keep them away from here."

    areaCommander "What about the hospital?"

    "The Fire Chief simply shakes his head."

    areaCommander "Damnit."



    areaCommander "So, all we can do is wait?"

    fireChief "Until the water subsides, yes."

    fireChief "Look how fast that flow is. One step in that mess and you're gone."

    areaCommander "Right. Make sure there is an exclusion zone around the flow."

    areaCommander "And get a camera crew up here, post some pictures as soon as you can."

    areaCommander "I don't want anyone else dying trying to get an Instagram photo…"

    paraMedic "Sir!"

    paraMedic "We've found someone!"

    "The assembled teams jump as if shocked by electricity."

    "An unexpected survivor amongst the chaos."

    "Years of training snap into place, displacing the horror of the disaster before them."

    "They part to let the gurney pass through their ranks before converging behind it."

    play sound "sounds/doug/act_1/doug_car_approach_ext_short.ogg"

    "Multiple teams jump into action. An ambulance is brought up to the fore,{nw}"

    play ad_bg_2 "sounds/doug/act_1/doug_ambulance_door_open.ogg" noloop

    extend " throwing the doors wide open."

    areaCommander "Bring them here. Are they conscious?"

    paraMedic "Barely. She was stumbling around beside the flood water."

    paraMedic "She seems dazed…"

    areaCommander "It's shock. Let me see her."

    hide damBreak
    scene cg michelle rescued with dissolve



    paraMedic "Can you hear me?"

    "The small figure can only stare off into the distance, but her blinking shows that there is at least some sign of life."

    areaCommander "You're safe now."

    paraMedic "Can you tell us your name?"

    "The figure shakes gently, unable to speak."

    areaCommander "Get her in the ambulance, have a look at her."

    "The paramedic guides the small figure on the gurney towards the ambulance."

    play ad_bg_2 "sounds/doug/act_1/doug_heart_monitor_slowing.ogg" loop



    paraMedic "Let's get this off you now. It's warm in here…"

    "The paramedic removes her jacket, placing it at the end of the gurney."

    paraMedic "Looks like you've had a rough day."

    paraMedic "Do you want to talk about it?"

    michelle "I've done it…"

    paraMedic "Done it…?"

    michelle "I've saved them all…"

    paraMedic "Saved who? Are there others?"

    paraMedic "Sir! There might be others!"

    "Another jolt of electricity runs through the weary team, and rescue workers perk up at the news that there might be more survivors."

    areaCommander "Everyone, form up and start a search, there might be others!"

    michelle "I've saved them from that monster."

    paraMedic "Ok darling, lie down."

    paraMedic "You're safe now."

    michelle "We're all safe now…"

    show cg michelle rescued closeup
    with dissolve

    michelle "Because I saved us all…"

    play ad_bg_2 "sounds/doug/act_1/doug_heart_monitor_stop.ogg" loop

    paraMedic "We're losing her! Someone help me in here…"

    window hide
    scene bg black
    with fade
    play sound "sounds/doug/act_1/doug_serpent_low_left.ogg" noloop
    stop ad_bg_1 fadeout 10
    stop ad_bg_2 fadeout 10
    $ renpy.pause(delay=5, hard=True)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
