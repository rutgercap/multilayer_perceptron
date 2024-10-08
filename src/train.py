import random
from pathlib import Path

from dataset import prep_data
from network import MLP

random.seed(42)

if __name__ == "__main__":
    print("Splitting data set...")
    X, y = prep_data(Path("train.csv"))
    X_val, y_val = prep_data(Path("test.csv"))
    model = MLP(input_size=X.shape[1], hidden_layer_sizes=[24, 24, 24], output_size=2)
    overview = model.train(
        (X, y),
        learning_rate=0.0001,
        epochs=50000,
        validation_data=(X_val, y_val),
        batch_size=256,
    )
    print("Training complete in {:.2f} seconds".format(overview.duration))
    overview.plot_loss()
    overview.plot_accuracy()
    model.save("model.json")
    print("Saved weights to model.json")
