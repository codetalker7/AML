This assignment mainly consists of two files: `prepare_functions.py` and `train_functions.py`. We have written functions in these files to make it easier to reuse them again.

`prepare_functions.py` consists of the following four functions: 
- `load_data`, to load data from a CSV file.
- `save_data`, to save data in a CSV file.
- `preprocess`, to preprocess the into a useful form.
- `prepare_train_validation_test_split`, to split the data.
- `split_into_lemmas`, a small function used in the preprocessing step.

Look at the docstrings of each of these functions to know more about them and what they do. These functions are then used in `prepare.ipynb`.

The `train_functions.py` consists of only two functions: 
- `train_model`, which is used to train models.
- `evaluate_model`, which is used to evaluate models using the accuracy, precision and recall scores.

Please see the `train.ipynb` notebook for the working of these functions.