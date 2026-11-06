from src.model import SimpleModel


def test_model_forward():
    model = SimpleModel(10, 20)
    output = model.forward([1, 2, 3])
    assert output is not None
