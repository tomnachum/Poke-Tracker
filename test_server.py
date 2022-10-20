from attr import evolve
from fastapi.testclient import TestClient
from server import app
import pytest
from queries.types_queries import get_types
import json

client = TestClient(app)


def get_pokemons_by_type(type):
    return client.get(f"/pokemons?pokemon_type={type}").json()


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


class TestAddPokemon:
    def test_add_yanma(self):
        response = client.post(
            "/pokemons", json.dumps({"name": "yanma", "height": 100, "weight": 100})
        ).json()
        assert "yanma" in get_pokemons_by_type("bug")
        assert "yanma" in get_pokemons_by_type("flying")


class TestUpdatedPokemonTypes:
    def test_venusaur(self):
        client.get("/pokemons/venusaur").json()
        assert "venusaur" in get_pokemons_by_type("poison")
        assert "venusaur" in get_pokemons_by_type("grass")


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


class TestGetOwnersByPokemon:
    def test_get_charmander_Owners(self):
        result = ["Giovanni", "Jasmine", "Whitney"]
        response = client.get("/trainers?pokemon_name=charmander").json()
        assert sorted(response) == sorted(result)


class TestEvolvePokemonByOwnerAndPokemon:
    def test_pinsir_pokemon_can_not_evolve(self):
        response = client.put(
            "/evolve/trainers/Drake/pokemons/pinsir").json()
        result = {"Message": "No evolves avilable"}
        assert response == result

    def test_archie_dosnt_have_spearow_pokemon(self):
        response = client.put(
            "/evolve/trainers/Archie/pokemons/spearow").json()
        result = {"Message": "This trainer does not have that pokemon"}
        assert response == result

    def test_oddish_should_evolve_to_gloom(self):
        response = client.put(
            "/evolve/trainers/Whitney/pokemons/oddish").json()
        result = {"Message": "The evolve succeeded", "Evolve to": "gloom"}
        assert response == result

    def test_trainer_should_not_have_the_prevuos_pokemon(self):
        response = client.put(
            "/evolve/trainers/Whitney/pokemons/oddish").json()
        result = {"Message": "This trainer does not have that pokemon"}
        assert response == result

    def test_get_all_of_trainer_pokemons_and_see_the_evlove(self):
        response = client.get("/pokemons?trainer_name=Whitney").json()
        evolve_in_list = "gloom" in response
        assert True == evolve_in_list

    def test_trainer_has_both_pokemon_and_evolve(self):
        response = client.put(
            "/evolve/trainers/Whitney/pokemons/pikachu").json()
        result = {"Message": "This trainer already has the evolve"}
        assert response == result
        
class DeletePokemonOfTrainer:
    def test_delete_pokemon_of_trainer(self):
        before_deletion_response = client.get("/pokemons?trainer_name=Whitney").json()
        before_deletion_list = "venusaur" in before_deletion_response 
               
        delete_response = client.delete("/pokemons/venusaur/trainers/Whitney")
        after_deletion_response = client.get("/pokemons?trainer_name=Whitney").json()
        
        after_deletion_list = "venusaur" in after_deletion_response
        after_deletion_list = not after_deletion_list
        assert after_deletion_list and before_deletion_list == True
        assert delete_response == {"message": "Pokemon was removed from trainer successfully"}
