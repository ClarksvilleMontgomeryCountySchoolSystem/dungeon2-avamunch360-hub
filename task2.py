good = r"""
                 __
                  /o \_____
                  \__/-="="`
                __
               / o\
               \_ /
                <|
                <|
                <|
jgs              `
"""
bad = r"""
                 ,-. 
                 (  \()Oo
                  `-,---.
          .-.       \   |
     oO()/   )       \  \
     ,--- ,-'         |_/
     |   /           ,-.
    /  _/            |_/
    \_/
    ,-.
    \_/    
s-v
"""
has_key = True

if has_key:
    Outcome = "Click: The lock turns smoothly and the door creaks open."
    print(good)
else:
    Outcome = "Doom: The door stays sealed as footsteps echo behind you. "
    print(bad)
print(Outcome)
