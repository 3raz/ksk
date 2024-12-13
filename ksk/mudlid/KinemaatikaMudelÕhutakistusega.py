import math
from mudlid.KinemaatikaMudel import KinemaatikaMudel

class KinemaatikaMudelÕhutakistusega(KinemaatikaMudel):
    def __init__(self, esialgne_kiirus: float, nurk: float, gravitatsioon: float, dt: float, 
                 suurus: float, raskus: float, tõmbetegur: float=0.295, õhu_tihedus: float=1.225) -> None:
        super().__init__(esialgne_kiirus, nurk, gravitatsioon, dt)
        
        # Õhutakistuse paraameterid
        self.tõmbetegur = tõmbetegur
        self.õhu_tihedus = õhu_tihedus
        self.ristlõike_pindala = math.pi * (suurus ** 2)
        self.raskus = raskus

        self.maal = False

    def __arvuta_tõmbemist__(self, kiirus_x: float, kiirus_y: float) -> tuple:
        """
        Arvutab õhutakistuse kiirusekomponente.
        """
        kiirus = math.sqrt(kiirus_x ** 2 + kiirus_y ** 2)
        tõmbejõud = 0.5 * self.õhu_tihedus * self.tõmbetegur * self.ristlõike_pindala * (kiirus ** 2)

        # Tõmbekiirendused
        tõmbe_acc_x = - (tõmbejõud / self.raskus) * (kiirus_x / kiirus)
        tõmbe_acc_y = - (tõmbejõud / self.raskus) * (kiirus_y / kiirus)

        return tõmbe_acc_x, tõmbe_acc_y

    def __arvuta_positsiooni__(self) -> None:
        """
        Uuenda objekti asukohta kiiruse ja aja järgi.
        """
        if self.algus_y - self.positsioon_y > self.algus_y:
            self.maal = True
            return
        self.positsioon_x += self.kiirus_x * self.dt
        self.positsioon_y += self.kiirus_y * self.dt

    def __arvuta_kiiruse__(self) -> None:
        """
        Uuenda objekti kiirust gravitatsiooni ja õhutakistuse alusel.
        """
        tõmbe_acc_x, tõmbe_acc_y = self.__arvuta_tõmbemist__(self.kiirus_x, self.kiirus_y)

        # Update velocity components
        self.kiirus_x += tõmbe_acc_x * self.dt
        self.kiirus_y += (-self.gravitatsioon + tõmbe_acc_y) * self.dt

    def __str__(self):
        return (f"Velocity X: {self.kiirus_x}, Velocity Y: {self.kiirus_y}, "f"Position: ({self.positsioon_x}, {self.positsioon_y})")