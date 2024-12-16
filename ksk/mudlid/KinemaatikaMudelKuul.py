import math
from mudlid.KinemaatikaMudel import KinemaatikaMudel
from andmed.Andmed import Andmed

andmed = Andmed().andmed

class KinemaatikaMudelKuul(KinemaatikaMudel):
    G1_DRAG_TABLE  = [
        (0.0, 1.0),
        (0.2, 0.85),
        (0.4, 0.75),
        (0.6, 0.65),
        (0.8, 0.55),
        (1.0, 0.50),
        (1.2, 0.45),
        (1.4, 0.42),
        (1.6, 0.40),
        (1.8, 0.38),
        (2.0, 0.35),
        (2.5, 0.32),
        (3.0, 0.30),
        (4.0, 0.28),
        (5.0, 0.27),
    ]

    def __init__(self, esialgne_kiirus: float, nurk: float, gravitatsioon: float, dt: float, 
                 suurus: float, raskus: float, tõmbekoefitsient: float, ballistilinekoefitsient: float, 
                 õhu_tihedus: float = 1.225, helikiirus: float = 343.0, mach_kiirus=343) -> None:
        super().__init__(esialgne_kiirus, nurk, gravitatsioon, dt)
        
        # Ballistilised omadused
        self.tõmbekoefitsient = tõmbekoefitsient
        self.õhu_tihedus = õhu_tihedus
        self.ristlõike_pindala = math.pi * (suurus ** 2)
        self.raskus = raskus
        self.ballistilinekoefitsient = ballistilinekoefitsient
        self.helikiirus = helikiirus
        self.mach_kiirus = mach_kiirus
        self.mode = andmed["is_g1"]*1 + (not andmed["is_g1"])*2 
        
        self.maal = False

    def __lookup_cd__(self, mach):
        """
        Leiab takistusekoefitsiendi machi kiirust
        """
        closest_entry = min(
            self.G1_DRAG_TABLE, 
            key=lambda entry: abs(entry[0] - mach)
        )
        
        return closest_entry[1]

    def __arvuta_tõmbemist__(self, kiirus_x: float, kiirus_y: float) -> tuple:
        """
        Arvutab õhutakistuse kiirusekomponente, arvestades ballistilise koefitsiendiga.
        """
        try:
            kiirus = math.sqrt(kiirus_x ** 2 + kiirus_y ** 2)
        except OverflowError:
            kiirus = math.sqrt(2**128 + 2**128)

        # Leiab takistusekoefitsiendi
        cd = self.__lookup_cd__(kiirus/self.mach_kiirus)/(self.mode) * self.ballistilinekoefitsient

        # Takistusejõud
        tõmbejõud = 0.5 * self.õhu_tihedus * cd * self.ristlõike_pindala * (kiirus ** 2)

        # Tõmbekiirendused
        try:
            tõmbe_acc_x = - ((tõmbejõud) * (kiirus_x / kiirus)) / self.raskus
            tõmbe_acc_y = - self.gravitatsioon - ((tõmbejõud) * (kiirus_y / kiirus)) / self.raskus
        except ZeroDivisionError:
            self.maal = True
            return -1e100, -1e100

        return tõmbe_acc_x, tõmbe_acc_y

    def uuenda(self, inc=100) -> None:
        """
        Uuenda objekti kõiki aspekte
        """
        for _ in range(0, inc):
            self.__arvuta_positsiooni__(inc=inc)
            self.__arvuta_kiiruse__(inc=inc)
            if not self.maal:
                self.aeg += self.dt / inc
        self.joonista_riivsai()

    def __arvuta_positsiooni__(self, inc=100) -> None:
        """
        Uuenda objekti asukohta kiiruse ja aja järgi.
        """
        if self.algus_y - self.positsioon_y > self.algus_y:
            self.maal = True
            return
        self.positsioon_x += self.kiirus_x * (self.dt / inc) / andmed["scale"]
        self.positsioon_y += self.kiirus_y * (self.dt / inc) / andmed["scale"]

    def __arvuta_kiiruse__(self, inc=100) -> None:
        """
        Uuenda objekti kiirust gravitatsiooni ja õhutakistuse alusel.
        """
        tõmbe_acc_x, tõmbe_acc_y = self.__arvuta_tõmbemist__(self.kiirus_x, self.kiirus_y)

        # Update velocity components
        self.kiirus_x += tõmbe_acc_x * (self.dt / inc)
        self.kiirus_y += tõmbe_acc_y * (self.dt / inc)

    def __str__(self) -> str:
        return (f"Esialgne kiirus: {self.esialgne_kiirus:.2f} m/s\n"
                f"Nurk: {self.nurk:.2f}°\n"
                f"Gravitatsioon: {self.gravitatsioon:.2f} m/s²\n"
                f"Ajatükk (dt): {self.dt:.4f} s\n"
                f"Suurus (raadius): {self.suurus:.3f} m\n"
                f"Raskus (mass): {self.raskus:.2f} kg\n"
                f"Tõmbekoefitsient: {self.tõmbekoefitsient:.2f}\n"
                f"Õhu tihedus: {self.õhu_tihedus:.3f} kg/m³\n"
                f"Ballistiline koefitsient: {self.ballistilinekoefitsient:.3f} kg/m²" 
                if self.ballistilinekoefitsient else "Ballistiline koefitsient: Ei ole määratud.")
