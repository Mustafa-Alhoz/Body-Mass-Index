
print('''
                                                                                                                                                         _.--,-```-.    
                                                           ,----..                         ,----..                                                      /    /      '.  
   ,---,        ,-.----.        ,---,.                    /   /   \                       /   /   \       ,---,.      ,---,.   .--.--.        ,---,.   /  ../         ; 
  '  .' \       \    /  \     ,'  .' |           ,---,   /   .     :           ,--,      /   .     :    ,'  .'  \   ,'  .' |  /  /    '.    ,'  .' |   \  ``\  .``-    '
 /  ;    '.     ;   :    \  ,---.'   |          /_ ./|  .   /   ;.  \        ,'_ /|     .   /   ;.  \ ,---.' .' | ,---.'   | |  :  /`. /  ,---.'   |    \ ___\/    \   :
:  :       \    |   | .\ :  |   |   .'    ,---, |  ' : .   ;   /  ` ;   .--. |  | :    .   ;   /  ` ; |   |  |: | |   |   .' ;  |  |--`   |   |   .'          \    :   |
:  |   /\   \   .   : |: |  :   :  |-,   /___/ \.  : | ;   |  ; \ ; | ,'_ /| :  . |    ;   |  ; \ ; | :   :  :  / :   :  |-, |  :  ;_     :   :  |-,          |    ;  . 
|  :  ' ;.   :  |   |  \ :  :   |  ;/|    .  \  \ ,' ' |   :  | ; | ' |  ' | |  . .    |   :  | ; | ' :   |    ;  :   |  ;/|  \  \    `.  :   |  ;/|         ;   ;   :  
|  |  ;/  \   \ |   : .  /  |   :   .'     \  ;  `  ,' .   |  ' ' ' : |  | ' |  | |    .   |  ' ' ' : |   :     \ |   :   .'   `----.   \ |   :   .'        /   :   :   
'  :  | \  \ ,' ;   | |  \  |   |  |-,      \  \    '  '   ;  \; /  | :  | | :  ' ;    '   ;  \; /  | |   |   . | |   |  |-,   __ \  \  | |   |  |-,        `---'.  |   
|  |  '  '--'   |   | ;\  \ '   :  ;/|       '  \   |   \   \  ',  /  |  ; ' |  | '     \   \  ',  /  '   :  '; | '   :  ;/|  /  /`--'  / '   :  ;/|         `--..`;    
|  :  :         :   ' | \.' |   |    \        \  ;  ;    ;   :    /   :  | : ;  ; |      ;   :    /   |   |  | ;  |   |    \ '--'.     /  |   |    \       .--,_        
|  | ,'         :   : :-'   |   :   .'         :  \  \    \   \ .'    '  :  `--'   \      \   \ .'    |   :   /   |   :   .'   `--'---'   |   :   .'       |    |`.     
`--''           |   |.'     |   | ,'            \  ' ;     `---`      :  ,      .-./       `---`      |   | ,'    |   | ,'                |   | ,'         `-- -`, ;    
                `---'       `----'               `--`                  `--`----'                      `----'      `----'                  `----'             '---`"     
                                                                                                                                                                        
      
''')

print("\nWelcome to the body mass index calculator")
print("\nTHIS PROGRAMME WAS MADE BY THE BEST PROGRAMMER EVER ===> @mustafa_alhoz ")
height = float(input("\nplease enter your height in meters: "))
weight = int(input("\nplease enter your weight: "))
bmi=weight/height**2
if bmi<18.5:
  print(f"\nYour BMI is {bmi}, you are underweight.\n")
elif bmi<25:
  print(f"\nYour BMI is {bmi}, you have a normal weight.\n")
elif bmi<30:
  print(f"\nYour BMI is {bmi}, you are slightly overweight.\n")
elif bmi<35:
  print(f"\nYour BMI is {bmi}, you are obese.\n")
else:
  print(f"\nYour BMI is {bmi}, you are clinically obese.\n")
  

  
  
