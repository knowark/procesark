from pytest import fixture
from procesark.application.models import Entity


@fixture
def entity() -> Entity:
    return Entity()


def test_entity_creation(entity: Entity) -> None:
    assert isinstance(entity, Entity)


def test_entity_default_attributes(entity: Entity) -> None:
    assert entity.id == ""
    assert entity.created_at == 0
    assert entity.updated_at == 0


def test_entity_attributes_from_dict() -> None:

    entity_dict = {
        "id": "ABC123",
        "created_at": 1520265903,
        "updated_at": 1520265903,
    }

    entity = Entity(**entity_dict)

    assert entity.id == entity_dict['id']
    assert entity.created_at == entity_dict['created_at']
    assert entity.updated_at == entity_dict['updated_at']
