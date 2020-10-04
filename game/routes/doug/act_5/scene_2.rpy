label dougActFiveSceneTwo:

    $ stopAllAudioTracks()


    window show
    scene bg black
    with dissolve


    scene bg school playground

    $ renpy.sound.set_volume(0.2, delay=0, channel='ad_bg_1')

    play music "sounds/doug/act_1/bgm_ambient_gyil.ogg" loop
    play ad_bg_1 "sounds/doug/act_1/doug_school_playground.ogg"

    "The school seems somewhat peaceful with Natalia's grade missing."

    "It shouldn't make this much impact, but the school isn't too large, and groups tend to stick to their 'areas' on the quadrangle."

    "There are noticeable gaps where there should be students talking and playing."

    "The silence isn't helping to dull the roaring cacophony in my mind though."

    "I should have stopped Michelle. I could have, had I tried."

    "Or tried to rescue the people that were inside."

    "But I was too busy getting out of there to do anything about it."

    "I know what she was aiming for, but now there are more deaths due to the serpent."

    "We're supposed to save people, not kill them."

    "Somewhere, out there, is someone who is going through the same pain that I did when Max was eaten."

    "That hopeless longing feeling that gnaws away at your stomach, churning it in ways that you thought were impossible."

    $ showHiddenText("" ,"The sense that you're never going to be able to feel happy again, and that the memories of{nw}")

    $ _history=False
    "The sense that you're never going to be able to feel happy again, and that the memories of{fast} that person will fade."

    "That you'll forget their face, their voice… their everything."

    "After the last person left forgets you - did you ever exist in the first place?"

    "It's a hard thought to process."

    "But until that creature is gone from this town, this will continue."

    "The means may or may not be justified by the end, but we've already come this far."

    "To give up now would make every death pointless."

    $ _history = True

    "That's why I'm here, sitting in this subdued school yard, pretending that everything is fine."

    "I need to avoid raising any suspicions until the serpent is dead or gone."

    "After that, I'll wear my punishment."

    "Of course, I'd prefer not to go to jail, but some things are more important than your own comfort."

    "Who knows how many hundreds of people the serpent has erased from history?"

    $ _history = False

    "If I can at least remember Mæx, then I can also remember the others."

    $ _history = True

    $ line = renpy.transform_text("xXëæƏmM", scrambling)
    "{alpha=0}If I can't remember[line], then the others can fucking rot in hell{/alpha}{fast}{nw}"

    $ _history = False

    "I might not know who they were, but if I can remember Max for as long as I live, then I feel that I'm remembering them all."

    "At least, in part."

    $ _history = True

    "I take a deep breath to calm my nerves."

    "There is not much that I can do here at school."

    "I decide to head to the library. Maybe I can look into the legends of the Rainbow Serpent."

    "Maybe I can find a clue there. Something that will help us fight it for real."

    stop ad_bg_1 fadeout 5.0

    scene bg library
    with dissolve

    "Michelle seems to be at least on the right path. The fire did get some kind of reaction from the beast."

    "Maybe we need to contain it somehow, trap it so that we can burn it hard."

    "I traipse up to the library, my soul heavy but with my head still in control."

    "Gotta keep it cool, and make it look like nothing is going on."

    "There's still a chance that no-one saw us at the house that burned down, and that they'll never find us."

    "After all; the people that died there didn't exist until last night."

    "There's nothing that connects Michelle and I to the crime."

    "The school's library is even more sedate than the yard. I guess not many people use physical books anymore."

    play sound "sounds/doug/act_1/doug_computer_clicking.ogg"

    "There's a kid using one of the computers in the corner, but apart from that, it's a ghost town."

    "I tried googling the serpent before but there wasn't much online."

    "For this I think I really need to hit the books."

    "The Aboriginal history section in the library is laughably small, but then again it's more detailed than the wikipedia articles."

    "I pull out a book about the Dreamtime and start flicking through the pages."

    "Dot-paintings from ancient caves stare back at me, as the dry text goes over the tales that I recall from my history classes."

    "The Rainbow Serpent was one of the Dreamtime creatures that carved rivers into the landscape of Australia."

    "Every tribe has their own Dreamtime stories, and yet the Rainbow Serpent seems to show up in all of them."

    "The story changes depending on the part of the country."

    " Around here, it decided to hide itself and became an island somewhere off shore, never to be heard of again."

    "Unfortunately, none of this is going to help me. None of the stories seem to have any information about fighting the beast."

    "Maybe I need to speak to Weeum. I consider skipping out from school, but it will have to wait."

    "I need to avoid drawing attention to myself today… {w=1.0}and tomorrow… {w=2.0}every day until I'm either arrested or until the serpent is neutralised."

    "Until then…"

    $ renpy.sound.set_volume(0.1, delay=0, channel='ad_bg_1')

    play ad_bg_1 "sounds/doug/act_1/doug_heartbeat_58_bpm.ogg"

    play sound "sounds/doug/act_1/doug_pa_chime.ogg"

    stop music fadeout 2.5

    pa "Douglass Lovett, report to the principal's office."

    $ renpy.sound.set_volume(0.5, delay=5, channel='ad_bg_1')

    "The PA message shakes me to my core. I feel my heart start to race and sweat well up in my pores."

    "I thought I was ready to accept my punishment, but I'm not."

    "My throat closes and I find myself gasping for breath."

    "I know that I need to calm down, but I can't manage to get a hold of myself."

    "Visions of being dragged away in a cop car flash before me."

    "My mother in tears, my father's disappointed face."

    "The life that I never knew."

    "My brain screams at me to run, but my body instinctively follows the instructions from the disembodied voice."

    "I stand up and walk, haltingly, towards the principal's office."


    jump dougActFiveSceneThree
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
