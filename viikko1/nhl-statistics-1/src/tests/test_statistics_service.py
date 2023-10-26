import unittest
from statistics_service import StatisticsService
from player import Player
from player_reader import PlayerReader

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    #..

    def test_search(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 4)
        self.assertEqual(player.assists, 12)

    def test_team(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        self.assertTrue(any(p.name == "Semenko" for p in edm_players))
        self.assertTrue(any(p.name == "Kurri" for p in edm_players))

    def test_top(self):
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 3)
        self.assertTrue(any(p.name == "Gretzky" for p in top_players))

    def test_search_invalid_player(self):
        player = self.stats.search("IamAGhostBooo")
        self.assertIsNone(player)

    def test_top_by_goals(self):
        players = self.stats.top(2,"GOALS")
        self.assertEqual(players[0].name, "Lemieux")
        self.assertEqual(players[1].name, "Yzerman")

    def test_top_by_assists(self):
        players = self.stats.top(2,"ASSISTS")
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Yzerman")

    def test_top_by_points(self):
        players = self.stats.top(2,"POINTS")
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        




class TestPlayerReader(unittest.TestCase):
    def setUp(self):
        self.reader = PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt")
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_url_is_valid(self):
        self.assertEqual(self.reader._url, "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt")

    def test_get_players(self): # Tämä tehtävä on varmaankin väärin, kommentoin alemmas yksityiskohdat:

        # Tehtävienannoissa sanotaan, että testi ei saisi käyttää verkkoa, mutta ensimmäiset rivit ovat:
        # def get_players(self):
        # players_file = request.urlopen(self._url)
        # Täten Jätän kaksi vaihtoehtoa testille, sen mikä toimii verkolliselle, ja ei verkolliselle.

        # Verkollinen

        players = self.reader.get_players()

        self.assertEqual(len(players), 1058)
        self.assertEqual(players[0].name, "Brendan Smith")
        self.assertEqual(players[0].team, "NJD")
        self.assertEqual(players[0].goals, 0)
        self.assertEqual(players[0].assists, 5)

        # Ei verkollinen

        players = self.stats._players

        self.assertEqual(len(players), 5)
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[0].team, "EDM")
        self.assertEqual(players[0].goals, 4)
        self.assertEqual(players[0].assists, 12)

class TestPlayer(unittest.TestCase):
    def test_str_representation(self):
        player = Player("Semenko", "EDM", 4, 12)
        self.assertEqual(str(player), "Semenko EDM 4 + 12 = 16")