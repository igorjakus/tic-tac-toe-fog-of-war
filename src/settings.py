import json


class Settings:
    def __init__(self, args=""):
        if args == "default":
            self._set_default_settings()

        with open("settings.json", "r") as file:
            loaded_settings = json.load(file)

        self.window_size = loaded_settings["window_size"]
        self.window_shape = (self.window_size, self.window_size)
        self.grid_size = loaded_settings["grid_size"]
        self.cell_size = self.window_size // self.grid_size
        # add more if needed

    def _set_default_settings(self):
        settings = dict()
        settings["window_size"] = 700
        settings["grid_size"] = 3

        with open("settings.json", "w") as file:
            json.dump(settings, file)
