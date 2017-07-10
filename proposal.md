# PDX Trail: Education Game Project by Jenna M. Tucker


#### Overview:
PDX Trail is an educational game designed as a parody of the beloved educational game The Oregon Trail.  The game mimics the quintessential elements of the game play and lingo to satisfy nostalgia for The Oregon Trail.  While The Oregon Trail simulates the shared historical experience of folks taking the Oregon Trail, PDX Trail simulates a shared future where ecological hardship sparks migration to the Cascades and the sprawling Portland area. Players will choose a level of difficulty for their game play, name their team members, and choose an initial inventory including food, clothes, means of carrying their inventory, basic tech, and social use items like music and books before they set out.  Success along the trail will depend on player choices and luck both. Foraging / scavenging will replace hunting as a way to subsidize inventory.


#### Specific Functionality:
Intro Screen:
  - Title
  - Maker and date
  - First menu: Play, Learn, Wall of Names, Exit
  - Enter choice __

 Gameplay Screen:
  - You can go as:
  - Character / difficulty level choices
  - Enter choice __
  - User choice determines the maximum size of inventory

Names Screen:
  - You will lead a team of four others.
  - Enter name 2-5 __
  - Are these names correct? __ y/n

Inventory Explained Page
  - explains inventory (no user inputs)

Inventory Overview Page
  - summary of inventory items and empty spaces by category
  - user blocked from departure if overpacked
  - user can choose to unpack items

Pack Screen
  - list of available items by category
  - users can choose to pack items
  - user returns to Inventory Overview Page

Play Screen
  - summary of health of team members
  - Play menu:  Walk on, Take some rest, Scavenge/forage, search through packs, Look at the map

Traveling Screen
  - **if one graphic, place here**
  - automatic traveling: health, day count, mile count, miles to a landmark
  - press enter to return to play screen
  - randomized happenings: good luck and bad luck

Landmark Story Screen
  - each landmark will have a unique section of story

Landmark Unique Game Play Screen
  - user choices that will affect health and inventory

Map of Trail with Landmarks

Final Win Screen
  - Last landmark.
  - Last menu:  See wall of names. Enter on wall of names.

Wall of Names Entry Screen
  - add user name, names of those lost, and a character-limited user message
  - show user entered wall of names

Wall of Names
  - displays user entered names and messages


#### *Data Model:*


#### Technical Components:

Python backend / control flow:
    Character class:
        Creates characters with unique names and health scores.
    Item class:
        Creates inventory items with type attribute "item" and unique names and descriptions.
    Food class:
        Child of Item class that includes standard name and description.
    Inventory class:
        Houses all five characters during game play.
        Creates the player's inventory with a specific limit.
        Holds pack and unpack functions to take and remove items.
    Place class:
        Creates a list places with names and corresponding inventories to discovery while scavenging/foraging.
    Occurrence class:
        Creates a loss to either a single character, every character, or the player's inventory.

Gameplay:
  - characters and player inventory
  - calls random experiences
  - controls game play
  - removes characters from inventory and prompts user when they die


Javascript web interface:
  - allows user to enter: character names, choices, navigate play screens, enter name & message on wall
  - possibly helps animate graphics

Django:
  - Possibly sends info back and forth to Python scripts and JS scripts?
  - Possibly allows the walls names and messages to be saved?

HTML / CSS:
  - Modifies what the player sees from plain text into organized gameplay menus and screens with graphics.
  - Animates simple graphics.

Unanswered:
  - What determines when the screens switch / what fills a single screen?  HMTL/CSS?


#### Schedule:

**First Layer:**  (Week 4, 2.5 days)       *Finished
    Python backend:
        Basic:
  - Character class
  - Item class
  - Food (Item) class
  - Inventory class
  - Place class
  - Occurrence class

Prompt choice for game play character/difficulty
        Prompt for four character names
        Instantiate characters and limited inventory
        Explain inventory.
        Display initial inventory of items that can be packed.
        Display player's inventory.
        Prompt for what items the play wants to pack or unpack.
        Block player when pack is full.
        Present game play menu.
        Add miles, reduce health, remove food for days walked.
        Generate random occurrences with loses to single characters, each character, and inventory.
        Add days and health for days rested.
        Present random finds for foraging / scavenging.
        Allow player to pack random finds and/or unpack items.


**Keep a running milestone story / game play idea sheet:           Weeks 8-10**

**Second Layer:** (approx. 2 days)
    Python backend:
        End game:
            End game when player named "you" dies.
        Landmarks:
            Set specific mile counts to trigger landmarks.
            Decide if landmarks/milestones will be a class.
            Create 3 unique landmark stories / game play menus.
            Allow interactions with inventories. Use unpack item function.
            Player choices should determine outcomes.

**Third Layer:** (approx 2 days)
    User Interface:
        Separate screens as they will be presented to user.
        Set up both automatic and user-driven movement among screens.
        Connect Python and JS interface.  Django?

**Fourth Layer:** (approx 4 days)
    Design basic layout and aesthetic of screens.
    Find a map and mark 12 milestones.


**Fifth Layer:** (approx 5 days)
Build out game:
  Milestones:
  - 12 unique landmarks/milestones with story segments and unique gameplay (include river crossings)
  - Create unique inventory items and ensure they will be found at certain milestones.
  - Do research.
  - Get external support.

Create "Learn about the trail/game page.

Places: 24 at least with inventories.

 Occurrences: 12 at least.  3 rarities.

**Bonus:  Sixth layer:** (approx 3 days)

Design and simple travel graphic.



#### Functionality Beyond An MVP:
   Link up to songs.
  **Basic travel screen graphic.**
  Date with day counter.  Could likely use an external calendar.
  Clues/pauses to stop and forage/scavenge.
  More static graphics.
  More animations.
  Unique Landmark Story & Game Play specific to character / difficulty choice.
  Option to select a start date.
    Variable adjusted for weather that's too early or too late, too wet/cold or
    dry/hot.
  Option to adjust pace.
  Choices at forks in trail, two paths.

