init python:
    import random
    import time


    def scrambling(string):
        return '{fast}' + scramblePhrase(string) + '{nw}'


    def scramblePhrase(phrase):
        chars = list(phrase)
        
        random.shuffle(chars)
        
        return ''.join(chars)


    def scrambledPhrase(character, start, end, seed = '', iterations = 5):
        string = start + end if seed == '' else seed
        
        renpy.say(character, start + '{fast}{nw}')
        
        time.sleep(0.2)
        
        for i in range(iterations):
            renpy.say(character, scramblePhrase(string) + '{fast}{nw}')
        
        renpy.say(character, end)


    def showRapidPhrases(character, phrases):
        for phrase in phrases:
            renpy.say(character, phrase + '{nw}')






    def showHiddenText(character, string):
        renpy.say(
            character,
            '{outlinecolor=#00000000}{alpha=0.0}' +
                string +
            '{/alpha}{/outlinecolor}{fast}{nw}'
        )





    def scrambleWordInPhrase(character, phrase, iterations = 5):
        words = phrase.split(' ');
        
        for iteration in range(iterations):
            newWords = []
            
            for word in words:
                questionMark = False
                
                if '?' in word:
                    questionMark = True
                    word.replace('?', '')
                
                if '__' in word:
                    scrambledWord = scramblePhrase(word.replace('__', ''))
                    word = scrambledWord if (questionMark is False) else scrambledWord + '?'
                
                newWords.append(word)
            
            renpy.say(character, ' '.join(newWords) + '{fast}{nw}')




    def getCurrentTime(music_channel):
        currTime = renpy.music.get_pos(channel=music_channel)
        signatures = [6, 14, 22, 30, 36, 42, 48, 56, 62]
        
        if not renpy.music.is_playing(channel=music_channel):
            return 0
        
        for signature in signatures:
            if currTime is None:
                return 0
            
            if signature is None:
                return 0
            
            if currTime < signature:
                return signature - currTime
        
        return 0


    def getCurrentTimeAsFloat(music_channel):
        return float(
            getCurrentTime(music_channel)
        )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
