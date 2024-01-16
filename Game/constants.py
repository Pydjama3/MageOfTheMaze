import colorama
from wfc import State, Rule

TILES_TEXTURES = './assets/textures.png'
PLAYER_TEXTURES = './assets/raiders/Raider_3/'
ZOMBIE_TEXTURES = './assets/zombies/Wile Zombie/'

MAIN_THEME = "assets/musics/MageOfTheMazeMainTheme.mp3"

TEST_PLAYER_SIZE = 5, 5
PLAYER_SPEED_FACTOR = 1 / 400
DIST_TO_NEXT_TILE = 0.1

TILE_SIZE = 7, 7
ROOM_SIZE = 7, 7

PLAYER_IDLE_ANI = [
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 0),
    (4, 0),
    (5, 0)
]

TEXTURE_TO_COORDINATES = {
    "grass": (0, 0),
    "water_straight": (1, 0),
    "path_elbow": (2, 0),
    "water_elbow": (0, 1),
    "path_straight": (1, 1),
    "stone": (2, 1),
    "lava": (0, 2),
    "dirt": (1, 2),
    "door": (2, 2)
}

ALL_TEXTURES_REP = [
    "grass",
    "water_straight_0",
    "water_straight_90",
    "water_elbow_0",
    "water_elbow_90",
    "water_elbow_180",
    "water_elbow_270",
    "path_straight_0",
    "path_straight_90",
    "path_elbow_0",
    "path_elbow_90",
    "path_elbow_180",
    "path_elbow_270",
    "stone",
    "lava",
    "dirt",
    "door"
]

BLOCKED_TILES = [
    "water",
    "lava",
    ""
]

cmap = {
    "water": colorama.Fore.BLUE,
    "grass": colorama.Fore.GREEN,
    "dirt": colorama.Fore.WHITE,
    "stone": colorama.Fore.LIGHTBLACK_EX,
    "lava": colorama.Fore.RED,
    "path": colorama.Fore.YELLOW
}

grass = State(
    "grass",
    Rule(
        lambda x, y: {
           # (x + 1, y + 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
           #                   "water_elbow_90", "water_elbow_180", "water_elbow_270"],
           #  (x - 1, y + 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
           #                   "water_elbow_90", "water_elbow_180", "water_elbow_270"],
           #  (x - 1, y - 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
           #                   "water_elbow_90", "water_elbow_180", "water_elbow_270"],
           #  (x + 1, y - 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
           #                   "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x, y - 1): ["dirt", "stone", "grass", "water_straight_90",
                         "water_elbow_90", "water_elbow_270"],
            (x, y + 1): ["dirt", "stone", "grass", "water_straight_90",
                            "water_elbow_0", "water_elbow_180"],
            (x + 1, y): ["dirt", "stone", "grass", "water_straight_0", "water_elbow_0",
                         "water_elbow_90"],
            (x - 1, y): ["dirt", "stone", "grass", "water_straight_0", "water_elbow_180", "water_elbow_270"]
        }))

water_straight_0 = State(
    "water_straight_0",
    Rule(
        lambda x, y: {
           # (x + 1, y + 1): ["dirt", "stone", "grass"],
           # (x - 1, y + 1): ["dirt", "stone", "grass"],
           # (x - 1, y - 1): ["dirt", "stone", "grass"],
           # (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["water_straight_0", "water_elbow_0", "water_elbow_270"],
            (x, y + 1): ["water_straight_0", "water_elbow_90", "water_elbow_180"],
            (x + 1, y): ["dirt", "stone", "grass"],
            (x - 1, y): ["dirt", "stone", "grass"]
        }
    )
)

water_straight_90 = State(
    "water_straight_90",
    Rule(
        lambda x, y: {
          #  (x + 1, y + 1): ["dirt", "stone", "grass"],
          #  (x - 1, y + 1): ["dirt", "stone", "grass"],
          #  (x - 1, y - 1): ["dirt", "stone", "grass"],
          # (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["dirt", "stone", "grass"],
            (x, y + 1): ["dirt", "stone", "grass"],
            (x + 1, y): ["water_straight_90", "water_elbow_180", "water_elbow_270"],
            (x - 1, y): ["water_straight_90", "water_elbow_0", "water_elbow_90"],
        }
    )
)

water_elbow_0 = State(
    "water_elbow_0",
    Rule(
        lambda x, y: {
        #    (x + 1, y + 1): ["dirt", "stone", "grass"],
         #   (x - 1, y + 1): ["dirt", "stone", "grass"],
         #   (x - 1, y - 1): ["dirt", "stone", "grass"],
         #   (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["dirt", "stone", "grass"],
            (x, y + 1): ["water_straight_0", "water_elbow_90", "water_elbow_180"],
            (x + 1, y): ["water_straight_90", "water_elbow_180", "water_elbow_270"],
            (x - 1, y): ["dirt", "stone", "grass"],
        }
    )

)

water_elbow_90 = State(
    "water_elbow_90",
    Rule(
        lambda x, y: {
         #   (x + 1, y + 1): ["dirt", "stone", "grass"],
         #   (x - 1, y + 1): ["dirt", "stone", "grass"],
          #  (x - 1, y - 1): ["dirt", "stone", "grass"],
          #  (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["water_straight_0",  "water_elbow_0", "water_elbow_270"],
            (x, y + 1): ["dirt", "stone", "grass"],
            (x + 1, y): ["water_straight_90", "water_elbow_270"],
            (x - 1, y): ["dirt", "stone", "grass" ],
        }
    )

)

water_elbow_180 = State(
    "water_elbow_180",
    Rule(
        lambda x, y: {
         #   (x + 1, y + 1): ["dirt", "stone", "grass"],
         #   (x - 1, y + 1): ["dirt", "stone", "grass"],
         #   (x - 1, y - 1): ["dirt", "stone", "grass"],
         #   (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["water_straight_0", "water_elbow_0", "water_elbow_270"],
            (x, y + 1): ["dirt", "stone", "grass"],
            (x + 1, y): ["dirt", "stone", "grass"],
            (x - 1, y): ["water_straight_90", "water_elbow_0", "water_elbow_90"],
        }
    )

)

water_elbow_270 = State(
    "water_elbow_270",
    Rule(
        lambda x, y: {
         #   (x + 1, y + 1): ["dirt", "stone", "grass"],
         #   (x - 1, y + 1): ["dirt", "stone", "grass"],
          #  (x - 1, y - 1): ["dirt", "stone", "grass"],
         #   (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["dirt", "stone", "grass"],
            (x, y + 1): ["water_straight_0", "water_elbow_90", "water_elbow_180"],
            (x + 1, y): ["dirt", "stone", "grass"],
            (x - 1, y): ["water_straight_90", "water_elbow_0", "water_elbow_90"],
        }
    )

)

path_straight_0 = State(
    "path_straight_0",
    Rule(
        lambda x, y: {
          #  (x + 1, y + 1): ["dirt", "stone", "grass"],
          #  (x - 1, y + 1): ["dirt", "stone", "grass"],
          #  (x - 1, y - 1): ["dirt", "stone", "grass"],
          #  (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["path_straight_0", "grass", "path_elbow_0", "path_elbow_270"],
            (x, y + 1): ["path_straight_0", "grass", "path_elbow_90", "path_elbow_180"],
            (x + 1, y): ["dirt", "stone", "grass"],
            (x - 1, y): ["dirt", "stone", "grass"]
        }
    )
)

path_straight_90 = State(
    "path_straight_90",
    Rule(
        lambda x, y: {
            # (x + 1, y + 1): ["dirt", "stone", "grass"],
            # (x - 1, y + 1): ["dirt", "stone", "grass"],
            # (x - 1, y - 1): ["dirt", "stone", "grass"],
            # (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["dirt", "stone", "grass"],
            (x, y + 1): ["dirt", "stone", "grass"],
            (x + 1, y): ["path_straight_90", "grass", "path_elbow_180", "path_elbow_270"],
            (x - 1, y): ["path_straight_90", "grass", "path_elbow_0", "path_elbow_90"],
        }
    )
)

path_elbow_0 = State(
    "path_elbow_0",
    Rule(
        lambda x, y: {
            # (x + 1, y + 1): ["dirt", "stone", "grass"],
            # (x - 1, y + 1): ["dirt", "stone", "grass"],
            # (x - 1, y - 1): ["dirt", "stone", "grass"],
            # (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["dirt", "stone", "grass"],
            (x, y + 1): ["path_straight_0", "grass", "path_elbow_90", "path_elbow_180"],
            (x + 1, y): ["path_straight_90", "grass", "path_elbow_180", "path_elbow_270"],
            (x - 1, y): ["dirt", "stone", "grass"],
        }
    )

)

path_elbow_90 = State(
    "path_elbow_90",
    Rule(
        lambda x, y: {
          #  (x + 1, y + 1): ["dirt", "stone", "grass"],
          #  (x - 1, y + 1): ["dirt", "stone", "grass"],
          #  (x - 1, y - 1): ["dirt", "stone", "grass"],
          #  (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["path_straight_0", "grass", "path_elbow_0", "path_elbow_270"],
            (x, y + 1): ["dirt", "stone", "grass"],
            (x + 1, y): ["path_straight_90", "grass", "path_elbow_180", "path_elbow_270"],
            (x - 1, y): ["dirt", "stone", "grass"],
        }
    )

)

path_elbow_180 = State(
    "path_elbow_180",
    Rule(
        lambda x, y: {
          #  (x + 1, y + 1): ["dirt", "stone", "grass"],
           # (x - 1, y + 1): ["dirt", "stone", "grass"],
            #(x - 1, y - 1): ["dirt", "stone", "grass"],
            #(x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["path_straight_0", "grass", "path_elbow_0", "path_elbow_270"],
            (x, y + 1): ["dirt", "stone", "grass"],
            (x + 1, y): ["dirt", "stone", "grass"],
            (x - 1, y): ["path_straight_90", "grass", "path_elbow_0", "path_elbow_90"],
        }
    )

)

path_elbow_270 = State(
    "path_elbow_270",
    Rule(
        lambda x, y: {
            # (x + 1, y + 1): ["dirt", "stone", "grass"],
            # (x - 1, y + 1): ["dirt", "stone", "grass"],
            # (x - 1, y - 1): ["dirt", "stone", "grass"],
            # (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["dirt", "stone", "grass"],
            (x, y + 1): ["path_straight_0", "grass", "path_elbow_90", "path_elbow_180"],
            (x + 1, y): ["dirt", "stone", "grass"],
            (x - 1, y): ["path_straight_90", "grass", "pddath_elbow_0", "path_elbow_90"],
        }
    )

)

dirt = State(
    "dirt",
    Rule(
        lambda x, y: {
         #   (x + 1, y + 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
                             # "water_elbow_90", "water_elbow_180", "water_elbow_270"],
         #   (x - 1, y + 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
                             # "water_elbow_90", "water_elbow_180", "water_elbow_270"],
         #   (x - 1, y - 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
                             # "water_elbow_90", "water_elbow_180", "water_elbow_270"],
        #    (x + 1, y - 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
                             # "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            # (x, y - 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
            #              "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            # (x, y + 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
            #              "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            # (x + 1, y): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
            #              "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            # (x - 1, y): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
            #              "water_elbow_90", "water_elbow_180", "water_elbow_270"]
            (x, y - 1): ["dirt", "stone", "grass", "water_straight_90",
                         "water_elbow_90", "water_elbow_270"],
            (x, y + 1): ["dirt", "stone", "grass", "water_straight_90",
                            "water_elbow_0", "water_elbow_180"],
            (x + 1, y): ["dirt", "stone", "grass", "water_straight_0", "water_elbow_0",
                         "water_elbow_90"],
            (x - 1, y): ["dirt", "stone", "grass", "water_straight_0", "water_elbow_180", "water_elbow_270"]
        }))

stone = State(
    "stone",
    Rule(
        lambda x, y: {
            # (x + 1, y + 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
            #                  "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            # (x - 1, y + 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
            #                  "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            # (x - 1, y - 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
            #                  "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            # (x + 1, y - 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0",
            #                  "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x, y - 1): ["dirt", "stone", "grass"],
            (x, y + 1): ["dirt", "stone", "grass"],
            (x + 1, y): ["dirt", "stone", "grass"],
            (x - 1, y): ["dirt", "stone", "grass"]
        }))

lava = State(
    "lava",
    Rule(lambda x, y: {
     #   (x + 1, y + 1): ["dirt", "stone", "grass"],
      #  (x - 1, y + 1): ["dirt", "stone", "grass"],
       # (x - 1, y - 1): ["dirt", "stone", "grass"],
        #(x + 1, y - 1): ["dirt", "stone", "grass"],
        (x, y - 1): ["dirt", "stone", "grass"],
        (x, y + 1): ["dirt", "stone", "grass"],
        (x + 1, y): ["dirt", "stone", "grass"],
        (x - 1, y): ["dirt", "stone", "grass"]
    })
)

door = State(
    "door",
    Rule(lambda x, y: {
        # (x + 1, y + 1): ["dirt", "stone", "grass"],
        # (x - 1, y + 1): ["dirt", "stone", "grass"],
        # (x - 1, y - 1): ["dirt", "stone", "grass"],
        # (x + 1, y - 1): ["dirt", "stone", "grass"],
        (x, y - 1): ["path_straight_0", "grass", "path_elbow_0", "path_elbow_270"],
        (x, y + 1): ["path_straight_0", "grass", "path_elbow_90", "path_elbow_180"],
        (x + 1, y): ["path_straight_90", "grass", "path_elbow_180", "path_elbow_270"],
        (x - 1, y): ["path_straight_90", "grass", "path_elbow_0", "path_elbow_90"]
    })
)
