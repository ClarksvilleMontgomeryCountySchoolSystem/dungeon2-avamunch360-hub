good = r"""
--------------------------------------------------------------------------

@                               _                                  ,,
 \\   _   @'                    ( )_                       .      _  \\
  \\_( )_//                    / Y |                   .      /--( )_//
    | Y/--                    /\   /               .        '//  \~ \
    |_/       _ / o"         ( _\ /            .                   - \
  _ //\      | | |    .       \_\\\        .                     //  \\--,
 /_// /      | | |      .    / \ \\\ .                           \\
/ // /_______|_|_|__________/_/_\ \_______________________________\\______
-------------------------------------------- Play Cricket ----------------
Unknown
"""
bad = r"""
     OOOOOOOOOOOOOOOOOOOOOOO
   _P_                     _9_
  / @ \        _          / @ \
 //---\\      ( )        //---\\
((     ))      T        ((     ))
 \\___//       |         \\___//
  '---'        |E     dwb '---'
"""

guard_alert =  False

if not gaurd_alert:
    outcome =  "Silent you slip past the gaurd unnoticed."
    print(good)
else:
    outcome = "Doom: The guard spots you and raises the alarm."
    print(bad)
print(outcome)
