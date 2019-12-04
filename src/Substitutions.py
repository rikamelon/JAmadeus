import re


def stands():

    return [
        lambda x: re.sub("Star Platinum", "「S t a r   P l a t i n u m」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Magician's Red", "「M a g i c i a n ' s   R e d」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Hermit Purple", "「H e r m i t   P u r p l e」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Hierophant Green", "「H i e r o p h a n t   G r e e n」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Silver Chariot", "「S i l v e r   C h a r i o t」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("The Fool", "「T h e   F o o l」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("The World", "「T h e   W o r l d」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Tower of Gray", "「T o w e r   o f   G r a y」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Dark Blue Moon", "「D a r k   B l u e   M o o n」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Strength", "「S t r e n g t h」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Ebony Devil", "「E b o n y   D e v i l」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Yellow Temperance", "「Y e l l o w   T e m p e r a n c e」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Hanged Man", "「H a n g e d   M a n」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Emperor", "「E m p e r o r」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Empress", "「E m p r e s s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Wheel of Fortune", "「W h e e l   o f   F o r t u n e」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Justice", "「J u s t i c e」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Lovers", "「L o v e r s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Sun", "「S u n」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Death Thirteen", "「D e a t h   T h i r t e e n」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Judgment", "「J u d g m e n t」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("High Priestess", "「H i g h   P r i e s t e s s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Geb", "「G e b」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Khnum", "「K h n u m」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Tohth", "「T o h t h」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Anubis", "「A n u b i s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Bastet", "「B a s t e t」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Sethan", "「S e t h a n」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Soiris", "「S o i r i s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Horus", "「H o r u s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Atum", "「A t u m」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Tenore Sax", "「T e n o r e   S a x」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Cream", "「C r e a m」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Crazy Diamond", "「C r a z y   D i a m o n d」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("The Hand", "「T h e   H a n d」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Echoes", "「E c h o e s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Heaven's Door", "「H e a v e n ' s   D o o r」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Killer Queen", "「K i l l e r   Q u e e n」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Aqua Necklace", "「A q u a   N e c k l a c e」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Bad Company", "「B a d   C o m p a n y」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Red Hot Chili Pepper", "「R e d   H o t   C h i l i   P e p p e r」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("The Lock", "「T h e   L o c k」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Surpace", "「S u r p a c e」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Love Deluxe", "「L o v e   D e l u x e」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Pearl Jam", "「P e a r l   J a m」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Achtung Baby", "「A c h t u n g   B a b y」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Ratt", "「R a t t」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Harvest", "「H a r v e s t」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Cinderella", "「C i n d e r e l l a」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Atom Heart Father", "「A t o m   H e a r t   F a t h e r」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Boy II Man", "「B o y   I I   M a n」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Earth Wind and Fire", "「E a r t h   W i n d   a n d   F i r e」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Highway Star", "「H i g h w a y   S t a r」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Stray Cat", "「S t r a y   C a t」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Super Fly", "「S u p e r   F l y」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Enigma", "「E n i g m a」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Cheap Trick", "「C h e a p   T r i c k」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Gold Experience", "「G o l d   E x p e r i e n c e」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Sticky Fingers", "「S t i c k y   F i n g e r s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Moody Blues", "「M o o d y   B l u e s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Sex Pistols", "「S e x   P i s t o l s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Aerosmith", "「A e r o s m i t h」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Purple Haze", "「P u r p l e   H a z e」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Spice Girl", "「S p i c e   G i r l」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("King Crimson", "「K i n g   C r i m s o n」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Black Sabbath", "「B l a c k   S a b b a t h」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Soft Machine", "「S o f t   M a c h i n e」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Kraft Work", "「K r a f t   W o r k」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Little Feet", "「L i t t l e   F e e t」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Man in the Mirror", "「M a n   i n   t h e   M i r r o r」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Mr.President", "「M r . P r e s i d e n t」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Beach Boy", "「B e a c h   B o y」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("The Grateful Dead", "「T h e   G r a t e f u l   D e a d」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Baby Face", "「B a b y   F a c e」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("White Album", "「W h i t e   A l b u m」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Clash", "「C l a s h」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Talking Head", "「T a l k i n g   H e a d」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Notorious B.I.G", "「N o t o r i o u s   B . I . G」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Metallica", "「M e t a l l i c a」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Green Day", "「G r e e n   D a y」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Oasis", "「O a s i s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Rolling Stones", "「R o l l i n g   S t o n e s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Stone Free", "「S t o n e   F r e e」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Kiss", "「K i s s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Burning Down the House", "「B u r n i n g   D o w n   t h e   H o u s e」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Foo Fighters", "「F o o   F i g h t e r s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Weather Report", "「W e a t h e r   R e p o r t」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Diver Down", "「D i v e r   D o w n」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Whitesnake", "「W h i t e s n a k e」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("C-Moon", "「C - M o o n」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Made in Heaven", "「M a d e   i n   H e a v e n」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Goo Goo Dolls", "「G o o   G o o   D o l l s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Manhattan Transfer", "「M a n h a t t a n   T r a n s f e r」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Highway to Hell", "「H i g h w a y   t o   H e l l」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Marilyn Manson", "「M a r i l y n   M a n s o n」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Jumpin' Jack Flash", "「J u m p i n '   J a c k   F l a s h」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Limp Bizkit", "「L i m p   B i z k i t」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Survivor", "「S u r v i v o r」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Planet Waves", "「P l a n e t   W a v e s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Dragon's Dream", "「D r a g o n ' s   D r e a m」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Yo-Yo Ma", "「Y o - Y o   M a」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Green, Green Grass of Home", "「G r e e n ,   G r e e n   G r a s s   o f   H o m e」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Jail House Lock", "「J a i l   H o u s e   L o c k」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Bohemian Rhapsody", "「B o h e m i a n   R h a p s o d y」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Sky High", "「S k y   H i g h」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Under World", "「U n d e r   W o r l d」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Tusk", "「T u s k」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Ball Breaker", "「B a l l   B r e a k e r」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Oh! Lonesome Me", "「O h !   L o n e s o m e   M e」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Scary Monsters", "「S c a r y   M o n s t e r s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Cream Starter", "「C r e a m   S t a r t e r」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Ticket to Ride", "「T i c k e t   t o   R i d e」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Dirty Deeds Done Dirt Cheap", "「D i r t y   D e e d s   D o n e   D i r t   C h e a p」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("In a Silent Way", "「I n   a   S i l e n t   W a y」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Hey Ya!", "「H e y   Y a !」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Tomb of the Boom", "「T o m b   o f   t h e   B o o m」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Boku no Rhythm wo Kiitekure", "「B o k u   n o   R h y t h m   w o   K i i t e k u r e」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Wired", "「W i r e d」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Mandom", "「M a n d o m」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Catch the Rainbow", "「C a t c h   t h e   R a i n b o w」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Sugar Mountain's Spring", "「S u g a r   M o u n t a i n ' s   S p r i n g」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Tatoo You!", "「T a t o o   Y o u !」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Tubular Bells", "「T u b u l a r   B e l l s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("20th Century Boy", "「2 0 t h   C e n t u r y   B o y」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Civil War", "「C i v i l   W a r」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Chocolate Disco", "「C h o c o l a t e   D i s c o」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Soft & Wet", "「S o f t   &   W e t」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Paisely Park", "「P a i s e l y   P a r k」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Nut King Call", "「N u t   K i n g   C a l l」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Paper Moon King", "「P a p e r   M o o n   K i n g」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("King Nothing", "「K i n g   N o t h i n g」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Speed King", "「S p e e d   K i n g」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Fun Fun Fun", "「F u n   F u n   F u n」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("California King Bed", "「C a l i f o r n i a   K i n g   B e d」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Born This Way", "「B o r n   T h i s   W a y」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Les Feuilles", "「L e s   F e u i l l e s」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("I Am a Rock", "「I   A m   a   R o c k」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Doobie Wah!", "「D o o b i e   W a h !」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Love Love Deluxe", "「L o v e   L o v e   D e l u x e」", x,
                         flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Schott Key No.1", "「S c h o t t   K e y   N o . 1」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Schott Key No.2", "「S c h o t t   K e y   N o . 2」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Vitamin C", "「V i t a m i n   C」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Walking Heart", "「W a l k i n g   H e a r t」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Milagro Man", "「M i l a g r o   M a n」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Blue Hawaii", "「B l u e   H a w a i i」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Doggy Style", "「D o g g y   S t y l e」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Brain Storm", "「B r a i n   S t o r m」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Ozon Baby", "「O z o n   B a b y」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Doctor Wu", "「D o c t o r   W u」", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub("Awaking III Leave", "「A w a k i n g   I I I   L e a v e」", x,
                         flags=re.IGNORECASE | re.MULTILINE),

    ]


def beginning_b():
    return [
        lambda x: re.sub("^b", "🅱", x, flags=re.IGNORECASE | re.MULTILINE),
        lambda x: re.sub(" b", " 🅱", x, flags=re.IGNORECASE | re.MULTILINE)
    ]


def im_x():
    return [lambda x: re.sub("^.*( |^)i['‘ʼ’]?m (.+)", r"Hi \2, I'm dad!", x, flags=re.I | re.MULTILINE)]


def shoot_me():
    return [lambda x: re.sub("^.*shoot me.*", ":gun:", x, flags=re.I | re.M)]


def kill_me():
    return [lambda x: re.sub("^.*kill me.*", ":gun:", x, flags=re.I | re.M)]


def stab_me():
    return [lambda x: re.sub("^.*stab me.*", ":dagger:", x, flags=re.I | re.M)]


def nicu():
    return [lambda x: re.sub("^.*nicu.*", "nicu nicu\nvery nicu shiza-chan", x, flags=re.I | re.M)]


def stand():
    return [lambda x: re.sub("^.*stand.*", "What, a stand?", x, flags=re.I | re.M)]


def nullpo():
    return [lambda x: re.sub("^.*nullpo.*", "Gah!", x, flags=re.I | re.M)]


def cyanide():
    return [lambda x: re.sub("^.*(cyanide|cyan|cya|see (you|ya)).*", "cyanide :wave:", x, flags=re.I | re.M)]


def thanks_bot():
    return [lambda x: re.sub("^.*thanks bot.*", "<:thumb:595365230666711056>", x, flags=re.I | re.M)]
