import random


def simple_synapse(input_value, weight):
    """A simplified synapse that reacts to numeric input (no learning here)."""
    return input_value * weight


def train_synapse(training_data, learning_rate=0.1, generations=100):
    """
    Trains a simple synapse using a reward-based approach.

    Args:
        training_data: A list of (input, desired_output) tuples.
        learning_rate: How much the synapse adjusts its weight.
        generations: How many training iterations.

    Returns:
        The learned weight.
    """

    weight = random.uniform(-1, 1)  # Initialize with a random weight

    for _ in range(generations):
        for input_value, desired_output in training_data:
            output = simple_synapse(input_value, weight)
            error = desired_output - output
            weight += error * learning_rate

    return weight


def run_synapse_example(training_data, test_input):
    """
    Runs an example of training and using the synapse.

    Args:
      training_data: The data to train the synapse on.
      test_input: The input to test the synapse with after training.
    """
    learned_weight = train_synapse(training_data)
    print(f"Learned weight: {learned_weight:.2f}")

    test_output = simple_synapse(test_input, learned_weight)
    print(f"Test input: {test_input}, Test output: {test_output:.2f}")


def eloquent_sample_run(sample_run_function, example_name):

    def wrapped(training_data, test_input):
        print("=" * 50)
        print(example_name)
        print("=" * 50)

        print("training data:")
        for row in training_data:
            print(f"\t{row[0]}, {row[1]}")
        print()

        sample_run_function(training_data, test_input)

        print("=" * 50)
        print()

    return wrapped


def main() -> None:
    # Example usages:
    training_data1 = [
        (1, 2),
        (2, 4),
        (3, 6),
        (4, 8)
    ]
    eloquent_sample_run(run_synapse_example, "EXAMPLE 1")(training_data1, 5)

    training_data2 = [
        (1, 10),
        (2, 20),
        (3, 30),
        (4, 40)
    ]
    eloquent_sample_run(run_synapse_example, "EXAMPLE 2")(training_data2, 10)


if __name__ == "__main__":
    main()
