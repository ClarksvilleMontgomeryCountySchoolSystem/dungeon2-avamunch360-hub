good = r"""
MMMMm                 MMMMMMMMMMM                   mMMMMMMMMMMMm
MMMMMMM               mMMMMMMMMMm                 MMMMMMMMMMM
MMMMMMMMm              MMMMMMMMM                mMMMMMMMMMm
  MMMMMMMMM            mMMMMMMMm              MMMMMMMMM
   mMMMMMMMMm           MMMMMMM             mMMMMMMMMm
       MMMMMMMM         mMMMMMm           MMMMMMMM         0
         mMMMMMm         MMMMM           mMMMMMm         o@@@o              mmm
             MMMMM       mMMMm         MMMMM            o@@@@@@o     mmmmmMMMMM
              mMMMm       MMM         mMMMm            o@@@@@@@@@oMMMMMMMMMMMMM
@oo              MMM      mMm        MMM             o@@@@@@@@@@@@@@ooMMMMMMMMM
@@@@o              mMm     M       mMm              o@@@@@@@@@@@@@@@@@@@oooMMMM
@@@@@@@@o           MhhhHHHHHHHHhhhM              o@@@@@@@@@@@@@@@@@@@@@@@@@oo
@@@@@@@@@o       hhHHHHHHHHHHHHHHHHHhh       oo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@oo hHHHHHHHHHHHHHHHHHHHHHHHHh oo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@ooHHHHHHHHHHHHHHHHHHHHoo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@ooHHHHHHHHHHHHHHHHoo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@ooHHHHHHHHHoo@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Chad Lemon@@@@@@@@
"""
bad = r"""
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
"""

escaped = True

if escaped:
    outocme = "Legend: You step into freedom as the gates fade behind you."
    print(good)
else:
    outocme = "Doom: The dungeon claims another lost soul."
    print(bad)
print(outcome)
