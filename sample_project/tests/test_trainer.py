from src.model import SimpleModel
from src.dataset import CustomDataset
from src.trainer import train_model


def test_trainer_returns_predictions():
    model = SimpleModel(2, 4)

    dataset = CustomDataset(
        samples=[[1, 2], [3, 4], [5, 6]],
        labels=[0, 1, 0],
    )

    predictions = train_model(model, dataset, epochs=1)

    assert predictions is not None
    assert len(predictions) == 3
    assert predictions == [[1, 2], [3, 4], [5, 6]]


def test_trainer_supports_unlabeled_dataset():
    model = SimpleModel(2, 4)

    dataset = CustomDataset(
        samples=[[1, 2], [3, 4]],
    )

    predictions = train_model(
        model,
        dataset,
        epochs=1,
    )

    assert predictions == [[1, 2], [3, 4]]
