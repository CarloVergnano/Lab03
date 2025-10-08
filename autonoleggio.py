from automobile import Automobile
from csv import DictReader
from operator import itemgetter
from noleggio import Noleggio


class Autonoleggio:
    def __init__(self, nome, responsabile, lista_auto, lista_noleggi):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self._responsabile = responsabile
        self.lista_auto = []
        self.lista_noleggi = []

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        if responsabile.isdigit():
            print('Devi inserire una stringa')
        else:
            self._responsabile = responsabile
        # TODO

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        try:
            filein = open(file_path, 'r', encoding='utf-8')
            reader = DictReader(filein, fieldnames=['codice', 'marca', 'modello', 'immatricolazione', 'posti'], delimiter=',')
            for riga in reader:
                self.lista_auto.append(riga)
            filein.close()
        except FileNotFoundError:
            print("File not found")
        # TODO

    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # Crea nuovo oggetto Automobile
        auto_nuova = Automobile(marca, modello, anno, num_posti)

        # Trova il numero più alto già presente
        if len(self.lista_auto) > 0:
            ultimo_codice = self.lista_auto[-1]['codice']
            num_max = int(ultimo_codice[1:])
        else:
            num_max = 0  # se non ci sono auto ancora

        # Crea nuovo codice progressivo
        codice_max = "A" + str(num_max + 1)

        # Aggiungi la nuova auto come dizionario
        self.lista_auto.append({
            'codice': codice_max,
            'marca': auto_nuova.marca,
            'modello': auto_nuova.modello,
            'immatricolazione': auto_nuova.anno,
            'posti': auto_nuova.num_posti
        })

        # Restituisce l'oggetto Automobile
        return auto_nuova

        # TODO

    def automobili_ordinate_per_marca(self):
        """Restituisce la lista di automobili ordinate per marca"""
        # Ordina la lista in base alla marca
        lista_ordinata = sorted(self.lista_auto, key=itemgetter("marca"))

        # Crea una lista di stringhe leggibili per la stampa
        lista_testo = []
        for auto in lista_ordinata:
            testo = f"{auto['codice']}, {auto['marca']}, {auto['modello']}, ({auto['immatricolazione']}), {auto['posti']}"
            lista_testo.append(testo)

        return lista_testo

        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio se l'auto è disponibile"""

        # Verifica che l'auto esista
        auto_trovata = False
        for auto in self.lista_auto:
            if auto['codice'] == id_automobile:
                auto_trovata = True
                break
        if not auto_trovata:
            raise Exception("Automobile non trovata nel sistema.")

        # Verifica che l'auto non sia già noleggiata
        for n in self.lista_noleggi:
            if n.ID_auto == id_automobile:
                raise Exception("L'automobile è già noleggiata.")

        # Calcola codice progressivo del nuovo noleggio
        if len(self.lista_noleggi) > 0:
            ultimo_codice = self.lista_noleggi[-1].cod_noleggio
            num_max = int(ultimo_codice[1:])
        else:
            num_max = 0
        codice_max = "N" + str(num_max + 1)

        # Crea il nuovo oggetto noleggio
        nuovo = Noleggio(codice_max, data, id_automobile, cognome_cliente)

        # Aggiungilo alla lista
        self.lista_noleggi.append(nuovo)

        # Restituisci il riferimento
        return nuovo

        # TODO

    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""

        # Se non ci sono noleggi attivi
        if len(self.lista_noleggi) == 0:
            raise Exception("Nessun noleggio presente nel sistema.")

        # Cerca il noleggio con quel codice
        for noleggio in self.lista_noleggi:
            if noleggio.cod_noleggio == id_noleggio:
                self.lista_noleggi.remove(noleggio)
                return  # Esci dal metodo dopo averlo rimosso

        # Se non lo trova, solleva un'eccezione
        raise Exception(f"Noleggio {id_noleggio} non trovato.")

        # TODO
