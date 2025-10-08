class Automobile:
    def __init__(self, marca, modello, anno, num_posti):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.num_posti = num_posti

    def __str__(self):
        """Rappresentazione leggibile dell'automobile"""
        return f"{self.marca} {self.modello} ({self.anno}) {self.num_posti} posti"


