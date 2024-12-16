import math
from mudlid.KinemaatikaMudel import KinemaatikaMudel
from andmed.Andmed import Andmed

andmed = Andmed().andmed

class KinemaatikaMudelKuul(KinemaatikaMudel):
    G1_DRAG_TABLE  = [
        (0.00,   0.2629),
        (0.05,   0.2558),
        (0.10,   0.2487),
        (0.15,   0.2413),
        (0.20,   0.2344),
        (0.25,   0.2278),
        (0.30,   0.2214),
        (0.35,   0.2155),
        (0.40,   0.2104),
        (0.45,   0.2061),
        (0.50,   0.2032),
        (0.55,   0.2020),
        (0.60,   0.2034),
        (0.70,   0.2165),
        (0.725,  0.2230),
        (0.75,   0.2313),
        (0.775,  0.2417),
        (0.80,   0.2546),
        (0.825,  0.2706),
        (0.85,   0.2901),
        (0.875,  0.3136),
        (0.90,   0.3415),
        (0.925,  0.3734),
        (0.95,   0.4084),
        (0.975,  0.4448),
        (1.0,    0.4805),
        (1.025,  0.5136),
        (1.05,   0.5427),
        (1.075,  0.5677),
        (1.10,   0.5883),
        (1.125,  0.6053),
        (1.15,   0.6191),
        (1.20,   0.6393),
        (1.25,   0.6518),
        (1.30,   0.6589),
        (1.35,   0.6621),
        (1.40,   0.6625),
        (1.45,   0.6607),
        (1.50,   0.6573),
        (1.55,   0.6528),
        (1.60,   0.6474),
        (1.65,   0.6413),
        (1.70,   0.6347),
        (1.75,   0.6280),
        (1.80,   0.6210),
        (1.85,   0.6141),
        (1.90,   0.6072),
        (1.95,   0.6003),
        (2.00,   0.5934),
        (2.05,   0.5867),
        (2.10,   0.5804),
        (2.15,   0.5743),
        (2.20,   0.5685),
        (2.25,   0.5630),
        (2.30,   0.5577),
        (2.35,   0.5527),
        (2.40,   0.5481),
        (2.45,   0.5438),
        (2.50,   0.5397),
        (2.60,   0.5325),
        (2.70,   0.5264),
        (2.80,   0.5211),
        (2.90,   0.5168),
        (3.00,   0.5133),
        (3.10,   0.5105),
        (3.20,   0.5084),
        (3.30,   0.5067),
        (3.40,   0.5054),
        (3.50,   0.5040),
        (3.60,   0.5030),
        (3.70,   0.5022),
        (3.80,   0.5016),
        (3.90,   0.5010),
        (4.00,   0.5006),
        (4.20,   0.4998),
        (4.40,   0.4995),
        (4.60,   0.4992),
        (4.80,   0.4990),
        (5.00,   0.4988)
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
        cd = self.__lookup_cd__(kiirus/self.mach_kiirus)

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
