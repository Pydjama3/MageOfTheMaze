from wfc import Wave, State, Rule
import colorama

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
            (x + 1, y + 1): ["dirt", "stone", "water", "grass", "path"],
            (x - 1, y + 1): ["dirt", "stone", "water", "grass", "path"],
            (x - 1, y - 1): ["dirt", "stone", "water", "grass", "path"],
            (x + 1, y - 1): ["dirt", "stone", "water", "grass", "path"],
            (x, y - 1): ["dirt", "stone", "water", "grass", "path"],
            (x, y + 1): ["dirt", "stone", "water", "grass", "path"],
            (x + 1, y): ["dirt", "stone", "water", "grass", "path"],
            (x - 1, y): ["dirt", "stone", "water", "grass", "path"]
        }))

dirt = State(
    "dirt",
    Rule(
        lambda x, y: {
            (x + 1, y + 1): ["dirt", "stone", "water", "grass", "path"],
            (x - 1, y + 1): ["dirt", "stone", "water", "grass", "path"],
            (x - 1, y - 1): ["dirt", "stone", "water", "grass", "path"],
            (x + 1, y - 1): ["dirt", "stone", "water", "grass", "path"],
            (x, y - 1): ["dirt", "stone", "water", "grass", "path"],
            (x, y + 1): ["dirt", "stone", "water", "grass", "path"],
            (x + 1, y): ["dirt", "stone", "water", "grass", "path"],
            (x - 1, y): ["dirt", "stone", "water", "grass", "path"]
        }))

stone = State(
    "stone",
    Rule(
        lambda x, y: {
            (x + 1, y + 1): ["dirt", "stone", "water", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "water", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "water", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "water", "grass"],
            (x, y - 1): [
                "dirt",
                "stone",
                "water",
                "grass",
            ],
            (x, y + 1): [
                "dirt",
                "stone",
                "water",
                "grass",
            ],
            (x + 1, y): [
                "dirt",
                "stone",
                "water",
                "grass",
            ],
            (x - 1, y): [
                "dirt",
                "stone",
                "water",
                "grass",
            ]
        }))

water = State(
    "water",
    Rule(
        lambda x, y: {
            (x + 1, y + 1): ["dirt", "stone", "water", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "water", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "water", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "water", "grass"],
            (x, y - 1): ["dirt", "stone", "water", "grass"],
            (x, y + 1): ["dirt", "stone", "water", "grass"],
            (x + 1, y): ["dirt", "stone", "water", "grass"],
            (x - 1, y): ["dirt", "stone", "water", "grass"]
        }))

path = State(
    "path",
    Rule(
        lambda x, y: {
            (x + 1, y + 1): ["dirt", "stone", "water", "grass"],
            (x - 1, y + 1): ["dirt", "stone", "water", "grass"],
            (x - 1, y - 1): ["dirt", "stone", "water", "grass"],
            (x + 1, y - 1): ["dirt", "stone", "water", "grass"],
            (x, y - 1): ["water", "grass", "path"],
            (x, y + 1): ["water", "grass", "path"],
            (x + 1, y): ["water", "grass", "path"],
            (x - 1, y): ["water", "grass", "path"]
        }))
