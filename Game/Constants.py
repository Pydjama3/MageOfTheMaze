from wfc import Wave, State, Rule
from random import randint
import colorama

texture_to_coordinates = {
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

all_textures_rep = [
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
            (x + 1, y + 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x - 1, y + 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x - 1, y - 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x + 1, y - 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x, y - 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x, y + 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x + 1, y): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x - 1, y): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"]
        }))

water_straight_0 = State(
    "water_straight_0",
    Rule(
        lambda x, y: {
            (x + 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["water_straight0", "grass", "water_elbow0", "water_elbow270"],
            (x, y + 1): ["water_straight0", "grass", "water_elbow90", "water_elbow180"],
            (x + 1, y): ["dirt", "stone", "grass"],
            (x - 1, y): ["dirt", "stone", "grass"]
        }
    )
)

water_straight_90 = State(
    "water_straight_90",
    Rule(
        lambda x, y: {
            (x + 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["dirt", "stone", "grass"],
            (x, y + 1): ["dirt", "stone", "grass"],
            (x + 1, y): ["water_straight90", "grass", "water_elbow180", "water_elbow270"],
            (x - 1, y): ["water_straight90", "grass", "water_elbow0", "water_elbow90"],
        }
    )
)

water_elbow_0 = State(
    "water_elbow_0",
    Rule(
        lambda x, y: {
            (x + 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["dirt", "stone", "grass"],
            (x, y + 1): ["water_straight0", "grass", "water_elbow90", "water_elbow180"],
            (x + 1, y): ["water_straight90", "grass", "water_elbow180", "water_elbow270"],
            (x - 1, y): ["dirt", "stone", "grass"],
        }
    )

)

water_elbow_90 = State(
    "water_elbow_90",
    Rule(
        lambda x, y: {
            (x + 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["water_straight0", "grass", "water_elbow0", "water_elbow270"],
            (x, y + 1): ["dirt", "stone", "grass"],
            (x + 1, y): ["water_straight90", "grass", "water_elbow180", "water_elbow270"],
            (x - 1, y): ["dirt", "stone", "grass"],
        }
    )

)

water_elbow_180 = State(
    "water_elbow_180",
    Rule(
        lambda x, y: {
            (x + 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["water_straight0", "grass", "water_elbow0", "water_elbow270"],
            (x, y + 1): ["dirt", "stone", "grass"],
            (x + 1, y): ["dirt", "stone", "grass"],
            (x - 1, y): ["water_straight90", "grass", "water_elbow0", "water_elbow90"],
        }
    )

)

water_elbow_270 = State(
    "water_elbow_270",
    Rule(
        lambda x, y: {
            (x + 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["dirt", "stone", "grass"],
            (x, y + 1): ["water_straight0", "grass", "water_elbow90", "water_elbow180"],
            (x + 1, y): ["dirt", "stone", "grass"],
            (x - 1, y): ["water_straight90", "grass", "water_elbow0", "water_elbow90"],
        }
    )

)

path_straight_0 = State(
    "path_straight_0",
    Rule(
        lambda x, y: {
            (x + 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "grass"],
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
            (x + 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "grass"],
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
            (x + 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "grass"],
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
            (x + 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "grass"],
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
            (x + 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "grass"],
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
            (x + 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["dirt", "stone", "grass"],
            (x, y + 1): ["path_straight_0", "grass", "path_elbow_90", "path_elbow_180"],
            (x + 1, y): ["dirt", "stone", "grass"],
            (x - 1, y): ["path_straight_90", "grass", "path_elbow_0", "path_elbow_90"],
        }
    )

)

dirt = State(
    "dirt",
    Rule(
        lambda x, y: {
            (x + 1, y + 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x - 1, y + 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x - 1, y - 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x + 1, y - 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x, y - 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x, y + 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x + 1, y): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x - 1, y): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"]
        }))

stone = State(
    "stone",
    Rule(
        lambda x, y: {
            (x + 1, y + 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x - 1, y + 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x - 1, y - 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x + 1, y - 1): ["dirt", "stone", "grass", "water_straight_0", "water_straight_90", "water_elbow_0", "water_elbow_90", "water_elbow_180", "water_elbow_270"],
            (x, y - 1): ["dirt", "stone", "grass"],
            (x, y + 1): ["dirt", "stone", "grass"],
            (x + 1, y): ["dirt", "stone", "grass"],
            (x - 1, y): ["dirt", "stone", "grass"]
        }))

lava = State(
    "lava",
    Rule(lambda x, y:{
        (x + 1, y + 1): ["dirt", "stone", "grass"],
        (x - 1, y + 1): ["dirt", "stone", "grass"],
        (x - 1, y - 1): ["dirt", "stone", "grass"],
        (x + 1, y - 1): ["dirt", "stone", "grass"],
        (x, y - 1): ["dirt", "stone", "grass"],
        (x, y + 1): ["dirt", "stone", "grass"],
        (x + 1, y): ["dirt", "stone", "grass"],
        (x - 1, y): ["dirt", "stone", "grass"]
    })
)

door = State(
    "door",
    Rule(lambda x, y: {
            (x + 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "grass"],
            (x, y - 1): ["path_straight_0", "grass", "path_elbow_0", "path_elbow_270"],
            (x, y + 1): ["path_straight_0", "grass", "path_elbow_90", "path_elbow_180"],
            (x + 1, y): ["path_straight_90", "grass", "path_elbow_180", "path_elbow_270"],
            (x - 1, y): ["path_straight_90", "grass", "path_elbow_0", "path_elbow_90"]
    })
)
