class Noleggio:
    def __init__(self, cod_noleggio, data, ID_auto, cognome_cliente):
        self.cod_noleggio = cod_noleggio
        self.data = data
        self.ID_auto = ID_auto
        self.cognome_cliente = cognome_cliente

    def __str__(self):
        return f"{self.cod_noleggio} - {self.data} - {self.ID_auto} - {self.cognome_cliente}"
