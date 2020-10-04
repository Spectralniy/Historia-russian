label dougActTwoSceneOne:

    $ stopAllAudioTracks()


    window show
    scene bg black
    with dissolve


    scene bg_doug_room_sunset_wiki_on
    with dissolve

    play music "sounds/doug/act_1/bgm_douglost4.ogg" loop

    "The sun sets as my wayward family begins to assemble in the house."

    "Natalia is first, secluding herself in her room almost as soon as she gets in."

    "I suppose that between last night and today she’s had enough of me, and doesn’t want to be dragged into another confrontation."

    "Mum is next. I hear her sleepy sighs as she settles into the dining room after a day of sleep."

    "I want to go out and say hello, but I’m afraid that I’ll slip up and she’ll go into protection mode."

    "Best to pretend that I’m studying and keep out of her way for now."

    "The worst outcome is that she starts to think that I’m on drugs. I’ll never hear the end of it."


    "Locking myself away to study isn’t that rare, so I might be able to get away with it for today."

    play sound "sounds/doug/act_1/doug_microwave_beep.ogg" fadein 2.0

    "It isn’t long before I hear the background noise of the TV flood the living room and the hum of the microwave."

    "Pasta again I suppose."

    "She works like a dog and still finds the energy to cook for us."

    "I don't know how she does it."

    "Not that boiling pasta and microwaving sauce is really gourmet cooking, but it saves me doing it."

    "Sometimes I try to cook for everyone, but it always ends up terrible. Mum subtly suggested that I leave it to her."

    mom "Dinner’s ready."

    "The emotionless cry reverberates around our little house, and Natalia and I dutifully file into the dining room."

    scene bg doug kitchen sunset
    show natalia chair upset at left
    with dissolve

    "Natalia gives me a look that tells me that she won’t say a word, but at the same time to avoid starting another row with Dad."

    "I sheepishly nod in her direction."

    "’Message Received’"

    show doug mum chair tired at right
    with dissolve

    "One look at Mum’s face tells me all I need to know. It’s been a rough day."

    "{i}Don’t ask me anything.{/i}"

    "That’s what the bags under her eyes are telling us."

    show doug mum chair tired speak
    with dissolve

    mom "How was school?"

    show natalia chair question
    with dissolve

    natalia "Uneventful."

    "I could hug my sister for jumping in before me. I still can’t trust my mouth to say what I want it to say."

    show doug mum chair tired look up
    with dissolve

    show natalia chair lookaway
    with dissolve

    mom "Hmm. And you?"

    doug "Same I guess. Just getting ready for finals."

    show doug mum chair tired speak
    with dissolve

    mom "Good… good…"

    show doug mum chair tired
    with dissolve

    "With the official family conversation ended, we start eating in silence."

    show natalia chair eating
    with dissolve

    "Spaghetti bolognese. It’s a staple of our family diet. I don’t really mind; it’s quick and it fills you up."


    "And I’m healthy enough, so it can’t be {i}that{/i} bad for you."

    "I’ve started noticing that a lot of people in this town are becoming obese, but so far we are still fit."

    $ _history = False

    show doug mum chair fixing hair
    with dissolve

    mom "Doug..."

    hide natalia
    show bg doug kitchen sunset blur
    show doug mum chair fixing hair at center
    with dissolve

    mom "I want you to know that your dad doesn’t mean everything he said last night."

    $ _history = True

    $ showHiddenText(mom, "Doug, I know you snuck out to Max's house last night.{fast}{nw}")

    "I twirl my fork in the spaghetti, sloshing the red sauce around the plate."

    $ _history = False

    mom "We just know that you only get one shot at this. You know that too, right?"

    $ _history = True

    $ showHiddenText(mom,"I'm OK with you going out, but at least let me know where you are, ok?{fast}{nw}")

    doug "I guess."

    show doug mum chair tired smile
    with dissolve

    "I don’t feel like talking to her about it."

    "I'm still not entirely sure of what happened last night."

    "Memories are overlapping in my mind, making it hard to tell reality from fiction."

    "But if I act too weird, Mum's sensors will start pinging and I'll be interrogated with vigour."

    "That's one more complication that I don't need in my life right now."

    "Mum has made her stance on drugs quite clear."

    "If the junkies were gone, so would her need to pull overtime."

    $ _history = False

    show doug mum chair tired speak
    with dissolve

    mom "He’s also got a lot of stress at the moment."

    $ _history = True

    $ showHiddenText(mom, "I'm glad that you got out of here before things got out of hand. Your dad is under a lot of stress right now.{fast}{nw}")

    show doug mum chair tired
    with dissolve

    "Stress, huh? That guy doesn’t know stress."

    "Mum has worked in an emergency ward for decades. The stories she tells us chill your blood."

    "What kind of stress could an office worker have that compares to that?"

    $ _history = False

    doug "I know."

    $ _history = True

    $ showHiddenText(doug, "Yeah right.{fast}{nw}")

    "I struggle to keep my emotions in check. If I get myself riled up now then I’ll pop when he gets home."

    show doug mum chair tired smile
    with dissolve

    mom "Well, so long as you know. He wants what’s best for you - even if you don’t see it yet."

    mom "One day you’ll thank him."

    play sound "sounds/doug/act_1/doug_drop_fork.ogg"

    "I drop the fork on my plate with a clatter."

    $ _history = False

    doug "I get it. I’m done."

    $ _history = True

    $ showHiddenText(doug, "Like hell I will!{fast}{nw}")

    show bg doug kitchen dark
    show natalia chair eating at left
    show doug mum chair tired look up at right
    with dissolve

    "I carry the half-empty plate to the sink."

    $ _history = False

    show bg doug kitchen dark plate

    "I don’t want to be petulant to my mother, but I also need time to think. Reality isn’t playing nice today, and I already know what she’s going to say."

    "She’s not wrong. I guess that is the hardest part of it all."

    $ _history = True

    "{alpha=0}fÚçķ yØù ß!ţčĥ{/alpha}{fast}{nw}"

    show doug mum chair tired
    with dissolve

    doug "I’ve got to study."

    $ renpy.music.set_volume(0.6, 4.0, channel="music")

    play music "sounds/doug/act_1/bgm_dougdowntempo_piano_strings.ogg" fadein 4.0 fadeout 4.0

    window show
    scene bg doug bedroom wiki on
    with dissolve

    "My finals are bringing a lot of stress into the family."

    "Even though I am the only one affected, Mum and Dad have both been fretting over the coming exams."

    "And that reflects back on me, so I start to get worried."

    "At the beginning of the year, I thought I had everything under control."

    "But as the day looms closer, they’ve started panicking. What if I don’t get good enough grades?"

    "It’s not like I have any other talents. I like to shoot some hoops now and again, but I’m easily the weakest player on the school team."

    "So sports aren't an option."

    "I’ve already had a couple of friends drop out of high school to start apprenticeships, but Dad wouldn’t let me do that."

    "’You need a degree to survive in this world. Almost every trade will be automated in the next 20 years.’"

    "He might be right."

    "So University has always been front of mind for me. I want to make an impact on this world, and that’s not something you can do easily as an electrician."

    "But that’s about where my ambition stops. I have a couple of subjects that I’m ok with, but nothing stellar."

    "That’s maybe the appeal of university. Get out of this tiny town and try to find out what I’m good at."

    play sound "<from 36.0>sounds/doug/act_1/doug_car_approach_ext_short.ogg"

    "Maybe that’s why I clash with Dad so much."

    "He spends too much time reading about the future of business, so he wants me studying computer science."

    "His vision of the future seems so clear, but from where I sit it’s not that simple."

    "I can hear his car pull up in the driveway now. It must already by eight o'clock."

    "Somehow I can tell by his footsteps that he hasn’t been drinking."

    "That’s a relief."

    "The door opens and he calls out to everyone."

    dad "I’m home. Doug, have you got a sec?"

    "Damnit. Here it comes."

    doug "I’m in my room."

    "I close my eyes and breathe in deeply, trying to force the confusion from my mind."

    "If Mum’s overbearing caring instincts are bad, having Dad thinking that I’m high would be much worse."

    "I don’t even want to imagine his reaction."

    play sound "sounds/doug/act_1/doug_light_door_knock.ogg"

    "He knocks on my door before opening it and leaning in."

    show doug_dad shirt looking down talking
    with dissolve

    dad "Look, Doug, I wanted to apologise for last night."

    doug "It’s ok."

    show doug_dad shirt looking up
    with dissolve

    dad "No - it’s not. I went overboard and it’s not healthy."

    dad "I just get so worried about you and your sister… I don’t want you to end up a screw-up like your uncle."

    "Ah, that old crutch. Dad wasn’t exactly on the top of the social ladder, but he was still a fair few rungs up from his kleptomaniac brother.\n"

    doug "I get it."

    show doug_dad shirt looking down talking
    with dissolve

    dad "Anyway, I want you to know that I want to support you."

    dad "But I can see you making the same mistakes I did, and I want to stop you from that."

    "A small spark of anger flares up in me. Normally I’d bite back, but I want this to be over."

    "I have other things to worry about today."

    $ showHiddenText(doug, "Well maybe you shouldn't be such a cunt about it!{fast}{nw}")

    $ _history = False

    doug "I know, I know. Thanks Dad."

    show doug_dad shirt small smile
    with dissolve

    "Dad seems to accept my thanks. He was probably expecting me to fight back as well."

    show doug_dad shirt smile
    with dissolve

    dad "Ok. I see you’re working, I’ll leave you to it."

    dad "You’re a good kid, you know that?"

    show doug_dad shirt small smile

    doug "Yeah I know."

    "He taps the door jamb and pulls the{nw}"

    play sound "sounds/doug/act_1/doug_door_close.ogg"

    "He taps the door jamb and pulls the{fast} door closed. Finally I’m left alone."

    hide doug_dad
    with dissolve

    $ _history = True

    $ showHiddenText('',"He is taken aback by my anger. I can see that he wants to fight back, but he bites his lip, punching the doorframe before storming away from my room.{fast}{nw}")

    "I tamp down the fire that is starting to grow in my belly. There’s no point in getting pissed off and starting another fight tonight."

    "Until I can trust my body again, it’s not worth making too much fuss."

    $ _history = False

    "I need to clear my head, so I grab a light jacket and my helmet and head outside."

    $ _history = True

    $ showHiddenText('',"I've gotta get away from this fuckwit before I blow my top.{fast}{nw}")

    window show
    scene bg doug livingroom
    with dissolve
    play ad_fg_1 "sounds/doug/act_1/doug_mum_headphone.ogg" fadein 1.0

    show doug mum headphones lookaway
    with dissolve

    doug "I’m going for a ride. Back in a bit."

    show doug mum headphones question
    with dissolve

    mom "Ok, have you got your helmet… oh."

    show doug mum headphones
    with dissolve

    "My mother has trained me well; no riding without a helmet. I used to think it was too nerdy, by then she showed me some photos of accidents."

    "That was enough to scare me into protecting my skull."

    stop music fadeout 3.0
    stop ad_fg_1 fadeout 3.0
    mom "Stay on the main roads. Be safe."

    doug "Sure thing Mum."
    $ renpy.music.set_volume (1, 4, channel="music")



    jump dougActTwoSceneTwo
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
