def train_model(model, dataset, epochs=10):
    predictions = []
    for epoch in range(epochs):
        predictions = []
        for item in dataset:
            if dataset.labels is not None:
                sample, label = item
            else:
                sample = item
            pred = model.forward(sample)
            predictions.append(pred)
    return predictions
