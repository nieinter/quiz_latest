# by _nieinter ;|
from random import randint


class App:
    def __init__(self):
        self.list_of_e_words1 = ['airport', 'arrive', 'bay', 'boat', 'cable car', 'car hire', 'catch a bus', 'collapse',
                                 'cross a continent', 'cross a river/valley', 'crossing', 'cruise',
                                 'cycle downhill/uphill', 'dirt road', 'donkey', 'drive', 'fasten a seatbelts', 'ferry',
                                 'flight', 'for pleasure', 'get a lift', 'get stuck in traffic', 'have access to',
                                 'helicopter', 'journey', 'land', 'miss the train', 'neighborhood', 'on foot', 'plane',
                                 'public transport', 'remote', 'rickshaw', 'a ride', 'the route', 'rush hour',
                                 'sea lion', 'sail', 'school bus', 'shortcut']
        self.list_of_p_words1 = ['lotnisko', 'przybyć', 'zatoka', 'łódź', 'kolejka liniowa', 'wypożyczalnia samochodów',
                                 'złapać autobus', 'zawalić się', 'przemierzyć kontynent', 'przekroczyć rzekę/dolinę',
                                 'przeprawa', 'rejs wycieczkowy', 'jechać na rowerze z górki/pod górkę',
                                 'droga gruntowa', 'osioł', 'prowadzić samochód', 'zapiąć pasy', 'prom', 'lot',
                                 'dla przyjemności', 'zostać podwiezionym', 'utknąć w korku', 'mieć dostęp do',
                                 'helikopter', 'podróż', 'wylądować', 'spóźnić się na pociąg', 'sąsiedztwo', 'pieszo',
                                 'samolot', 'transport publiczny', 'odległy', 'riksza', 'przejażdżka', 'trasa',
                                 'godzina szczytu', 'lew morski', 'płynąć statkiem', 'autobus szkolny', 'skrót']

        self.list_of_e_words2 = ['sledge', 'stroll', 'suspension bridge', 'terminal', 'tour', 'traffic jam', 'train',
                                 'travel by train', 'travel journalist', 'urban', 'valley', 'voyage', 'walk barefoot',
                                 'winding path', 'adventure', 'beach holiday', 'budget/three-star hotel', 'bus journey',
                                 'business trip', 'campsite', 'get off', 'go away', 'mountain', 'overland tour',
                                 'package holiday', 'put up a tent', 'return journey', 'round-the-world trip',
                                 'seaside resort', 'single/double/twin room', 'ski resort', 'skiing holiday',
                                 'tour guide', 'tour leader', 'travel agent', 'travel company', 'trekking',
                                 'youth hostel', 'baggage reclaim', 'cheetah']
        self.list_of_p_words2 = ['sanki', 'spacer', 'most wiszący', 'terminal', 'wycieczka', 'korek uliczny', 'pociąg',
                                 'podróżować pociągiem', 'dziennikarz piszący o podróżach', 'miejski', 'dolina',
                                 'rejs, lot', 'iść boso', 'kręta ścieżka', 'przygoda', 'wakacje nad morzem',
                                 'tani/trzygwiazdkowy hotel', 'podróż autobusem', 'podróż służbowa', 'kemping',
                                 'wysiąść', 'wyjechać', 'góra', 'długa podróż drogą lądową w odległe rejony',
                                 'wakacje zorganizowane', 'rozbić namiot', 'podróż powrotna', 'podróż dookoła świata',
                                 'kurort nadmorski', 'pokój jednoosobowy/dwuosobowy/z dwoma pojedynczymi łóżkami',
                                 'ośrodek narciarski', 'wyjazd na narty', 'przewodnik', 'pilot wycieczek',
                                 'biuro podróży/pracownik biura podróży', 'przedsiębiorstwo turystyczne', 'wędrówka',
                                 'schronisko młodzieżowe', 'miejsce odbioru bagażu', 'gepard']

        self.list_of_e_words3 = ['domestic animal', 'holidaymaker', 'lion', 'on the loose', 'pet', 'puma', 'roar',
                                 'tiger', 'zoo', 'appreciate', 'avoidable', 'backpacker', 'belittle',
                                 'book plane tickets', 'budget', 'challenge beliefs', 'connected',
                                 'cut yourself off from your family/home', 'destination', 'detract from', 'dip',
                                 'disconnected', 'execute', 'familiar', 'go backpacking', 'GPS',
                                 'have one foot firmly planted at home', 'keep up-to-date with',
                                 'immerse yourself in a foreign culture', 'informed', 'Millennial', 'overnight journey',
                                 'passenger', 'pleasant', 'problem-solve', 'profound', 'rewarding', 'save up for',
                                 'solitary', 'survive']
        self.list_of_p_words3 = ['zwierzę domowe', 'wczasowicz', 'lew', 'na wolności', 'zwierzątko domowe', 'puma',
                                 'ryczeć, ryk', 'tygrys', 'zoo', 'doceniać', 'do uniknięcia', 'turysta z plecakiem',
                                 'umniejszać', 'rezerwować bilety na samolot', 'budżetować, planować finansowo',
                                 'kwestionować przekonania', 'połączony', 'odciąć się od rodziny/domu', 'cel podróży',
                                 'szkodzić czemuś', 'maczać, zanurzać', 'odłączony',
                                 'przeprowadzić, zrobić (zgodnie z planem)', 'znajomy, znany', 'wędrować z plecakiem',
                                 'system nawigacji satelitarnej', 'być mocno związanym z domem rodzinnym',
                                 'być na bieżąco z', 'zanurzyć się w obcej kulturze', 'poinformowany',
                                 'millennials (osoba, która urodziła się między 1980 r. a 2000 г.)', 'całonocna podróż',
                                 'pasażer', 'przyjemny, mily', 'rozwiązywać problemy', 'głęboki', 'satysfakcjonujący',
                                 'oszczędzać na', 'samotny', 'przeżyć']

        self.list_of_e_words4 = ['take a gap year', 'temple', 'thinkable', 'ticket', 'travel abroad', 'traveller',
                                 'unavoidable', 'unfamiliar', 'uninformed', 'unpleasant', 'unrewarding', 'unthinkable',
                                 'withdraw money from a cash point', 'go through security', 'security check', 'sword',
                                 'traffic pollution', 'travel on the left/right', 'break down', 'head for',
                                 'hold sb up', 'keep on', 'keep up with', 'pick sb up', 'pull over', 'put sb up',
                                 'run out of', 'set off (on a journey)', 'turn into', 'walk away from',
                                 'express sympathy', 'hometown', 'incidentally', 'reassure your friend', 'uni',
                                 'pillow', 'snow boots', 'tissue', 'travel by bus', 'travel insurance']
        self.list_of_p_words4 = ['zrobić sobie rok przerwy w nauce', 'świątynia', 'wykonalny', 'bilet',
                                 'wyjeżdżać za granicę', 'podróżny', 'nieunikniony', 'obcy, nieznany',
                                 'niepoinformowany', 'nieprzyjemny', 'niedający satysfakcji', 'nie do pomyślenia',
                                 'wypłacić gotówkę z bankomatu', 'przejść kontrolę bezpieczeństwa',
                                 'kontrola bezpieczeństwa', 'miecz',
                                 'zanieczyszczenie powietrza spowodowane przez samochody',
                                 'jeździć po lewej/prawej stronie', 'zepsuć się', 'kierować się do', 'opóźniać kogoś',
                                 'kontynuować', 'dotrzymywać komuś kroku', 'odbierać kogoś', 'zjechać na bok/pobocze',
                                 'przenocować kogoś', 'wyczerpać się, nie mieć już', 'wyruszyć (w podróż)',
                                 'zmienić się w', 'zrezygnować z, porzucić', 'wyrazić współczucie', 'miasto rodzinne',
                                 'nawiasem mówiąc', 'uspokoić/pokrzepić przyjaciela', 'uniwersytet', 'poduszka',
                                 'śniegowce', 'chusteczka higieniczna', 'podróżować autobusem',
                                 'ubezpieczenie podróżne']

        self.max = 0

    def start(self):
        zestaw = input("Wybierz zestaw od 1 do 4 (wpisz liczbę od 1 do 4 i enter):\n")

        try:
            if int(zestaw) == 1:
                self.max = len(self.list_of_e_words1)
                self.loop(self.list_of_e_words1.copy(), self.list_of_p_words1.copy())
            elif int(zestaw) == 2:
                self.max = len(self.list_of_e_words2)
                self.loop(self.list_of_e_words2.copy(), self.list_of_p_words2.copy())
            elif int(zestaw) == 3:
                self.max = len(self.list_of_e_words3)
                self.loop(self.list_of_e_words3.copy(), self.list_of_p_words3.copy())
            elif int(zestaw) == 4:
                self.max = len(self.list_of_e_words4)
                self.loop(self.list_of_e_words4.copy(), self.list_of_p_words4.copy())
        except ValueError:
            print("Podano nie poprawną wartość")
            self.start()

    def los(self, list_e, list_p):
        random_index = randint(0, len(list_e) - 1)
        answer = input(f"{list_p[random_index]}:\n")
        if answer == list_e[random_index]:
            print("✅✅✅")
            del list_p[random_index]
            del list_e[random_index]
            print(f"Postęp: {self.max - len(list_p)}/{self.max} słówek")
            print("//////////////////////////////\n")
        else:
            print("❌❌❌")
            print(f"Poprawna odpowiedź➡️: {list_e[random_index]}")
            print(f"Postęp: {self.max - len(list_p)}/{self.max} słówek")
            print("//////////////////////////////\n")

    def loop(self, list_e, list_p):
        while len(list_e) != 0:
            self.los(list_e, list_p)
        self.rerun()

    def rerun(self):
        print("Zestaw zaliczony.")
        ans = input("Chcesz rozpocząć następny zestaw? (T/N):")
        if ans == "T":
            self.start()
        elif ans == "N":
            pass
        else:
            print("Podano złą wartość")
            self.rerun()


app = App()
app.start()
