import json

with open('elements.json', 'r') as json_file:
    elements_data = json.load(json_file)
with open('electronic_configuration1.json', 'r') as json_file:
    elements_config = json.load(json_file)

try:
    ele_charac = input("Input Element : ")
    atomic_no = elements_data['elements'][ele_charac]
    int_atomic_no = int(atomic_no)
    print(f"Atomic Number : {atomic_no}")
except Exception as e:
    print("Please Input Valid Element Symbol... ")
    exit()

print(f"Electronic Configuration : ",elements_config['elements_config'][ele_charac])

if 57<=int_atomic_no<=71 or 89<=int_atomic_no<=103:
  print("Actinoides And Lanthanoids Are Not Included.")
  exit()
else:
  try:
    choice = str(input("\nEnter Subshell : "))
    if choice=='1s':
            if int_atomic_no == 1:
               sigma = ((1-1)*0.30)
            elif 2 <= int_atomic_no <= 56 or 72 <= int_atomic_no <= 88 or 104 <= int_atomic_no <= 118:
               sigma = ((2-1)*0.30)
    elif choice=='2s':
            if int_atomic_no == 3 or int_atomic_no == 4:
              sigma = (((int_atomic_no-2)-1)*0.35)+(2*0.85)
            elif 5 <= int_atomic_no <= 118:
              sigma = (((8)-1)*0.35)+(2*0.85)
    elif choice=='2p':
            if int_atomic_no == 5 :
              sigma = (((1+2)-1)*0.35)+(2*0.85)
            elif 5< int_atomic_no <= 9:
              sigma = ((((int_atomic_no)-2)-1)*0.35)+(2*0.85)
            elif 10 <= int_atomic_no <= 118:
              sigma = ((8-1)*0.35)+(2*0.85)
    elif choice=='3s': # checked
            if int_atomic_no == 11 or int_atomic_no == 12 :
              sigma = (((int_atomic_no-10)-1)*0.35)+((8)*0.85)+(2*1)
            elif 13 <= int_atomic_no <= 18:
              sigma = (((2+(int_atomic_no-12))-1)*0.35)+(8*0.85)+(2*1)
            elif 12< int_atomic_no <= 118:
              sigma = (((8)-1)*0.35)+(8*0.85)+(2*1)
    elif choice=='3p': # checked
            if 13<= int_atomic_no <= 18 :
              sigma = (((int_atomic_no-10)-1)*0.35)+((8)*0.85)+(2*1)
            elif 13 <= int_atomic_no <=  118:
              sigma = (((8)-1)*0.35)+(8*0.85)+(2*1)
    elif choice=='4s': # checked
            if int_atomic_no==19 or int_atomic_no == 20:
              sigma = (((int_atomic_no-18)-1)*0.35+(8)*0.85+(10)*1)
            elif int_atomic_no ==24 or int_atomic_no==29:
              sigma = ((1-1)*0.35+((int_atomic_no-19)+8)*0.85+(10)*1)
            elif 21<=int_atomic_no<=30:
              sigma = ((2-1)*0.35+((int_atomic_no-20)+8)*0.85+(10)*1)
            elif 31<=int_atomic_no<=36:  #
              sigma = ((int_atomic_no-30)+2-1)*0.35+((18)*0.85+(10)*1)
            elif 41 <=int_atomic_no <=118:
              sigma = ((8)-1)*0.35+((18)*0.85+(10)*1)
    elif choice=='3d': # checked
            if 21<=int_atomic_no<=23 or 25<=int_atomic_no<=28 or int_atomic_no==30:
              sigma = (((int_atomic_no-20)-1)*0.35)+((18)*1)
            elif int_atomic_no==29 or int_atomic_no==24:
              sigma = (((int_atomic_no-19)-1)*0.35)+((18)*1)
            elif 30<int_atomic_no<=118:
              sigma = (((10)-1)*0.35)+((18)*1)
    elif choice=='4p': # checked
            if 31<=int_atomic_no<=36:
              sigma = ((((int_atomic_no-30)+2)-1)*0.35+(18)*0.85+(10)*1)
            elif 37<=int_atomic_no<=118:
              sigma = ((((6)+2)-1)*0.35+(18)*0.85+(10)*1)
    elif choice=='5s':  # checked
            if int_atomic_no==37 or int_atomic_no==38:
              sigma = (((int_atomic_no-36)-1)*0.35)+((8)*0.85)+((28)*1)
            elif int_atomic_no==39 or int_atomic_no==40 or int_atomic_no==48:
              sigma = ((2-1)*0.35)+((8+(int_atomic_no-38))*0.85) + ((28)*1)
            elif int_atomic_no == 42 or int_atomic_no == 41 or int_atomic_no == 44 or int_atomic_no == 45 or int_atomic_no == 47:
              sigma = ((1-1)*0.35)+((8+(int_atomic_no-37))*0.85) + ((28)*1)
            elif int_atomic_no == 43:
              sigma = ((2-1)*0.35)+((8+5)*0.85) + ((28)*1)
            elif int_atomic_no == 46:
              print("Given Element Do Not Have Selected Subshell.")
            elif int_atomic_no == 47 or int_atomic_no == 48:
              sigma = (((int_atomic_no-46)-1)*0.35)+((18)*0.85) + ((28)*1)
            elif 49<=int_atomic_no<=54:
              sigma = (((2+(int_atomic_no-48)-1)*0.35)+((18)*0.85) + ((28)*1))
            elif 55<=int_atomic_no<=118:
              sigma = ((8-1)*0.35)+((32)*0.85) + ((28)*1)
    elif choice=='4d': # checked
            if int_atomic_no==39 or int_atomic_no==40 or int_atomic_no==48:
              sigma = (((int_atomic_no-38)-1)*0.35)+((36)*1)
            elif int_atomic_no == 42 or int_atomic_no == 41 or int_atomic_no == 44 or int_atomic_no == 45 or int_atomic_no == 47:
              sigma = (((int_atomic_no-37)-1)*0.35)+((36)*1)
            elif int_atomic_no == 43:
              sigma = ((5-1)*0.35)+((36)*1)
            elif 46 <=int_atomic_no <= 118:
              sigma = ((10-1)*0.35)+((36)*1)
    elif choice=='5p': # checked
            if 49<=int_atomic_no <= 54:
              sigma = (((2+(int_atomic_no-48))-1)*0.35)+((18)*0.85) + ((28)*1)
            elif 55<=int_atomic_no <= 118:
              sigma = (((8)-1)*0.35)+((18+14)*0.85) + ((28)*1)
    elif choice=='6s': # checked
            if int_atomic_no == 55 or int_atomic_no == 56:
              sigma = (((int_atomic_no-54)-1)*0.35)+((8)*0.85) + ((46)*1)
            elif 72 <=int_atomic_no <= 77: 
             sigma = ((2-1)*0.35)+(((int_atomic_no-70)+8)*0.85) + ((60)*1)
            elif int_atomic_no==78 or int_atomic_no==79:
             sigma = ((1-1)*0.35)+(((int_atomic_no-69)+8)*0.85) + ((60)*1)
            elif int_atomic_no==80:
             sigma = ((2-1)*0.35)+((18)*0.85) + ((60)*1)
            elif 81<=int_atomic_no<=86:
               sigma = (((2+(int_atomic_no-80))-1)*0.35)+((18)*0.85) + ((60)*1)
            elif int_atomic_no == 87 or int_atomic_no == 88:
               sigma = (((8)-1)*0.35)+((18)*0.85) + ((60)*1)
            elif 104<=int_atomic_no<=118:
               sigma = (((8)-1)*0.35)+((18+14)*0.85) + ((60)*1)
    elif choice=='6p':
            if 81<= int_atomic_no <= 86:
               sigma = ((((int_atomic_no-80)+2)-1)*0.35)+((18)*0.85) + ((60)*1)
            elif int_atomic_no==87 or int_atomic_no==88:
                sigma = (((8)-1)*0.35)+((18)*0.85) + ((60)*1)
            elif 104<=int_atomic_no<=118:
                sigma = (((8)-1)*0.35)+((18+14)*0.85) + ((60)*1)
    elif choice=='5d':
            if 72<=int_atomic_no<=78:
                 sigma = (((int_atomic_no-70)-1)*0.35) + ((6+2+14+10+6+2+10+6+2+6+2+2)*1)
            elif 79<= int_atomic_no<=88 or 104<=int_atomic_no<=118:
                  sigma = (((10)-1)*0.35) + ((6+2+14+10+6+2+10+6+2+6+2+2)*1)
    elif choice=='5f':
            if 104<=int_atomic_no<=118:
                  sigma = ((14-1)*0.35) + ((10+6+2+14+10+6+2+10+6+2+6+2+2)*1)
    elif choice=='6d':
            if 104<=int_atomic_no<=118:
                   sigma = (((int_atomic_no-102)-1)*0.35)+((2+6+14+10+6+2+14+10+6+2+10+6+2+6+2+2)*1)
    elif choice=='7s':
            if int_atomic_no==87 or int_atomic_no==88:
                    sigma = (((2)-1)*0.35)+((2+6)*0.85) + ((10+6+2+14+10+6+2+10+6+2+6+2+2)*1)
            elif 104<=int_atomic_no<=112:
                     sigma = ((2-1)*0.35)+((18)*0.85) + ((14+10+6+2+14+10+6+2+10+6+2+6+2+2)*1)
    elif choice=='7p':
            if 113<=int_atomic_no<=118:
                    sigma = ((((int_atomic_no-112)+2)-1)*0.35)+((18)*0.85) + ((14+10+6+2+14+10+6+2+10+6+2+6+2+2)*1)
    print("\nZeff ( Z* ) = Atomic_Number ( Z ) - Sheilding Constant ( \u03C3 )")
    print("Atomic_Number : ", int_atomic_no)
    print("Shielding Constant ( \u03C3 ) : ", sigma)
    print("Zeff ( Z* ) : ", atomic_no-sigma)
  except Exception:
    print("Note : Input Correct Subshell Character or Given Atomic Number Does Not Have Given Subshell\n")
                