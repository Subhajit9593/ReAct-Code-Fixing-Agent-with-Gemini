class CustomDataset:
    def __init__(self, samples, labels=None):
        self.samples = samples
        self.labels = labels

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        if self.labels is not None:
            return self.samples[idx], self.labels[idx]
        return self.samples[idx]
