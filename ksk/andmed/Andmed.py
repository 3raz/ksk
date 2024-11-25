import json
import threading
import time
import ctypes


class Andmed:
    """
    See klass rakendab ainus eksemplari disainimustrit, et jagada andmeid mitme objekti vahel.
    """
    _eksemplar = None

    def __new__(cls, fn="ksk\\andmed\\Andmed.json"):
        """
        Ainus eksemplari disainimustri abifunktsioon.
        """
        if cls._eksemplar is None:
            cls._eksemplar = super(Andmed, cls).__new__(cls)
            cls._eksemplar.andmed = {}
            cls._eksemplar.fn = fn
            cls._eksemplar.laadi_failist()
            cls._eksemplar.alusta_perioodiline_salvestus()
        return cls._eksemplar

    def laadi_failist(self):
        with open(self.fn, 'r', encoding="UTF-8") as f:
            self.andmed = json.load(f)

        # Kui resolution on liiga suur ekraani jaoks (Andmed.json on laadinud teistest arvutist) siis parandab resolutionit.
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
        if self.andmed["resolution"][0] > w or self.andmed["resolution"][1] > h:
            self.andmed["resolution"] = [w-50,h-50] 

    def salvesta_faili(self):
        with open(self.fn, 'w', encoding="UTF-8") as f:
            json.dump(self.andmed, f, indent=4)

    def alusta_perioodiline_salvestus(self):
        def salvesta_perioodiliselt():
            while True:
                time.sleep(self.andmed["salvestamise_intervall"])
                self.salvesta_faili()

        thread = threading.Thread(target=salvesta_perioodiliselt, daemon=True)
        thread.start()

    def __del__(self):
        self.salvesta_faili()