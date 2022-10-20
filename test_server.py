from fastapi.testclient import TestClient
from server import app
import pytest
from queries.queries import get_types

client = TestClient(app)


class TestGetPokemonsByType:
    def test_get_normal_type(self):
        # get all pokemons of type normal and check eevee is in there.
        response = client.get("/pokemons?pokemon_type=normal").json()
        assert "eevee" in response

    def test_types_are_unique(self):
        # when getting a pokemon, all it's types are being added to the DB.
        # normal type is already in the DB, so when we try to get eevee,
        # the normal type will be added again to the DB. we need to check that the app is not crashing,
        # and that the types in the DB are unique.
        response = client.get("/pokemons/eevee").json()
        all_types = get_types().keys()
        assert len(set(all_types)) == len(all_types)


class TestUpdatedPokemonTypes:
    def get_pokemons_by_type(self, type):
        return client.get(f"/pokemons?pokemon_type={type}").json()

    def test_venusaur(self):
        client.get("/pokemons/venusaur").json()
        assert "venusaur" in self.get_pokemons_by_type("poison")
        assert "venusaur" in self.get_pokemons_by_type("grass")


class TestGetPokemonsByOwner:
    def test_get_drasnas_pokemons(self):
        result = [
            "wartortle",
            "caterpie",
            "beedrill",
            "arbok",
            "clefairy",
            "wigglytuff",
            "persian",
            "growlithe",
            "machamp",
            "golem",
            "dodrio",
            "hypno",
            "cubone",
            "eevee",
            "kabutops",
        ]
        response = client.get("/pokemons?trainer_name=Drasna").json()
        assert sorted(response) == sorted(result)
