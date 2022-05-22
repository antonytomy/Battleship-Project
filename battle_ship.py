# 2 Player Battleship

import time 

def two_player_battleship():
  # Radar initial setup - this part of the program sets up the player's screens and radars and allows them to set up their ships
 
  # make player radar matrix and ship list
  player_1_radar = [[],[],[],[],[],[],[],[],[],[]] # This is the radar that contains player 1's ships for player 1's viewing
  player_2_radar = [[],[],[],[],[],[],[],[],[],[]] # This is the radar that contains player 2's ships for player 2's viewing
  player_1_viewing_radar = [[],[],[],[],[],[],[],[],[],[]] # This is the radar that player 1 uses to see player 2's ships
  player_2_viewing_radar = [[],[],[],[],[],[],[],[],[],[]] # This is the radar that player 2 uses to see player 1's ships
  player_1_ship_list = [] # This is the list that contains the coordinates of player 1's ships
  player_2_ship_list = [] # This is the list that contains the coordinates of player 2's ships
 
  # defines a function to add null values for all cells in a radar - this will be used to fill in the player 1 and player 2 real and viewing radars
  def add_null_values_to_starting_radars(starting_radar_name):
    for i in range(10):
      for j in range(10):
        starting_radar_name[i].append("- ")

  # executes the adding null values function to fill in the four radars
  add_null_values_to_starting_radars(player_1_radar)
  add_null_values_to_starting_radars(player_2_radar)
  add_null_values_to_starting_radars(player_1_viewing_radar)
  add_null_values_to_starting_radars(player_2_viewing_radar)
 
  # defines a function that prints the player radars - this can be used in many different applications for the players to view radars
  def print_radar(radar_name):
    print("  0 1 2 3 4 5 6 7 8 9") # column headers for the coordinate system
    for i in range(10): # fills in the 10 rows with 10 corresponding values
      print(str(i) + " " + radar_name[i][0] + radar_name[i][1] + radar_name[i][2] + radar_name[i][3] + radar_name[i][4] + radar_name[i][5] + radar_name[i][6] + radar_name[i][7] + radar_name[i][8] + radar_name[i][9])

  # prints the number and type of ships people have - this is the first thing players see and it tells them how they set up ships
  print("You both get: ")
  print("1x scout (2 spaces)")
  print("2x cruisers (3 spaces)")
  print("1x submarine (3 spaces)")
  print("1x battleship (4 spaces)")
  print("1x aircraft carrier (5 spaces)")
 
  # tells to pass to player 1 and prints 40 spaces - this allows people to switch without players seeing each other's screens
  print("Pass to Player 1")
  continue_ = input("Print (yes) to continue ")
  #puts 40 lines of blank space in order to ensure that each player's ships remains confidential
  for i in range(40):
    print("")

  # defines function that assigns ships to spaces - this allows player 1 and then player 2 to choose where their ships are placed
  def ship_assignment(player_name_radar, player_ship_list_prime):
   
    # defines a function that lets a player place ships of certain length and type
    def place_ship(ship_name, ship_length, player_ship_list):
      # prints radar and lets player choose what header and orientation the ship is
      print_radar(player_name_radar)
      ship_header = input("Choose " + ship_name + " header: ")
      ship_orientation = input("Choose " + ship_name + " orientation: ")

      # adds values to personal radars and ship list by referencing the coordinate and the place within each array (row and column)
     
      # for a horizontal orientation it is the values of the x axis (first coordinate) that change
      if ship_orientation == "horizontal":
        for i in range(ship_length):
          player_ship_list.append(str(int(ship_header[0])) + str(int(ship_header[1]) + i))
          player_name_radar[int(ship_header[0])][int(ship_header[1]) + i] = "S "
     
     # for a vertical orientation it is the values of the y axis (second coordinate) that change
      elif ship_orientation == "vertical":
        for i in range(ship_length):
          player_ship_list.append(str(int(ship_header[0]) + i) + str(int(ship_header[1])))
          player_name_radar[int(ship_header[0]) + i][int(ship_header[1])] = "S "
 
    # runs the orientation/header function for all ship types
    place_ship("scout", 2, player_ship_list_prime)
    place_ship("cruiser", 3, player_ship_list_prime)
    place_ship("cruiser", 3, player_ship_list_prime)
    place_ship("submarine", 3, player_ship_list_prime)
    place_ship("battleship", 4, player_ship_list_prime)
    place_ship("aircraft carrier", 5, player_ship_list_prime)
   
    print_radar(player_name_radar)

  # defines function that clears screen and tells to pass to other player - this will allow a switching of screen without the players seeing each other's inputs
  def pass_to_other_player(player_name):
    continue_ = input("Print (yes) to continue ")
    for i in range(90):
      print("")
 
    print("Pass to " + player_name)
    continue_ = input("Print (yes) to continue ")
    for i in range(90):
      print("")

  ship_assignment(player_1_radar, player_1_ship_list) # runs ship assignment function for player 1
  pass_to_other_player("Player 2") # passes to player 2
  ship_assignment(player_2_radar, player_2_ship_list) # runs ship assignment function for player 2
  pass_to_other_player("Player 1") # passes to player 1




  # Attack - this part of the program will allow players to attack the other one - if they miss the program turns over but if they hit they get to go again until one of them wins
  def attack(player_name_viewing_radar, player_name_radar, player_opposite_name, player_opposite_ship_list, player_opposite_radar):

    # this is the legend of symbols that the radar shows
    print("- = no data")
    print("0 = miss")
    print("X = hit")
    print("S = your ship")
   
    # this prints the viewing radar for the player to see with a caption
    print_radar(player_name_viewing_radar)
    print("Map of " + player_opposite_name)
    print("")
   
    # this prints the player radar for the player to see with a caption
    print_radar(player_name_radar)
    print("Your ships")
    print("")
    print("")
   
    # takes input from player and attacks coordinate
    attack_coordinate = input("Where would you like to attack? ")
   
    # since a hit lets you play a second time, a while statement will let it go over and over until a wrong guess is inputted
    while attack_coordinate in player_opposite_ship_list:
     
      # this tells the player that they hit a ship and waits
      print("You hit a ship!")
      time.sleep(2)
     
      player_opposite_ship_list.remove(attack_coordinate) # this removes the coordinates of the hit ship from the ship list
      player_name_viewing_radar[int(attack_coordinate[0])][int(attack_coordinate[1])] = "X " # this revises the viewing radar of the first player
      player_opposite_radar[int(attack_coordinate[0])][int(attack_coordinate[1])] = "X " # this revises the player radar from the opposite player
     
      print("")
      print("")
     
      # this prints the viewing radar for the player to see with a caption
      print_radar(player_name_viewing_radar)
      print("Map of " + player_opposite_name)
      print("")

      # this prints the player radar for the player to see with a caption
      print_radar(player_name_radar)
      print("Your ships")
      print("")
      print("")
     
      attack_coordinate = input("Where would you like to attack? ")
     
    else:
      # this is what happens when you miss
      print("You missed!")
      player_name_viewing_radar[int(attack_coordinate[0])][int(attack_coordinate[1])] = "0 " # this revises the viewing radar of the first player
      player_opposite_radar[int(attack_coordinate[0])][int(attack_coordinate[1])] = "0 " # this revises the player radar from the opposite player
      pass_to_other_player("other player") # passes to the other player
 
 
  while len(player_1_ship_list) != 0 and len(player_2_ship_list) != 0:
    # this repeats the attack function rotating back and forth between players until one of the players' ship list is empty
    attack(player_1_viewing_radar, player_1_radar, "Player 2", player_2_ship_list, player_2_radar)
    attack(player_2_viewing_radar, player_2_radar, "Player 1", player_1_ship_list, player_1_radar)
  else: # this senses a win
    if len(player_1_ship_list) == 0: # if player 1's ship list is empty, player 2 wins
      # prints a win if player 2 wins
      print("Player 2 WON!")
    elif len(player_2_ship_list) == 0: # if player 2's ship list is empty, player 1 wins
      # prints a win if player 1 wins
      print("Player 1 WON!")

# runs the entire two_player_battleship function
two_player_battleship()


