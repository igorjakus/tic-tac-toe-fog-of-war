import json


def set_default_settings():
    settings = dict()
    settings["window_size"] = 700
    settings["grid_size"] = 3

    with open("settings.json", "w") as file:
        json.dump(settings, file)
