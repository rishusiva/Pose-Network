from modules import *
from folder_setup import *




classes = {label:num for num, label in enumerate(actions)}

sequences, labels = [], []
for action in actions:
    for sequence in range(number_sequences):
        window = []
        for frame_num in range(sequence_length):
            res = np.load(os.path.join(DATA_PATH, action, str(sequence), "{}.npy".format(frame_num)))
            window.append(res)
        sequences.append(window)
        labels.append(classes[action])

# X and y variables 
X = np.array(sequences)
y= to_categorical(labels).astype(int)

# train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)