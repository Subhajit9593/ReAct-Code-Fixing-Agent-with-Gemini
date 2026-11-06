from src.dataset import CustomDataset


def test_dataset_length():
    dataset = CustomDataset(
        samples=[[1, 2], [3, 4], [5, 6]],
        labels=[0, 1, 0],
    )
    assert len(dataset) == 3


def test_dataset_indexing():
    dataset = CustomDataset(
        samples=[[1, 2], [3, 4]],
        labels=[0, 1],
    )

    assert dataset[0] == ([1, 2], 0)
    assert dataset[1] == ([3, 4], 1)
