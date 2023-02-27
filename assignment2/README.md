# Using [`dvc`](https://dvc.org/) and [`mlflow`](https://mlflow.org/) for ML version control.

The data, preprocessing and model training/evaluation steps for this assignment are the same as in the first assignment.

## `dvc` configuration

`dvc` has been configured to track the `data` folder, which contains the original data and the train/validation/test splits. Also, we have configured `dvc` so that it uses Google Drive as it's remote storage (see `./.dvc/config`). To see this in action, in `prepare.ipynb` we create two train/validation/test splits using different random seeds, check out the two versions, and print their distributions. Note that, at the time of running this notebook, the old version of `data.dvc` had been checkout out; hence, when we run `git checkout HEAD data.dvc`, it checks out the latest version of the data.

Next, we used `mlflow` to track and register the three models. This is straightforward. Finally, we loaded the registered models, and computed their AUCPRs.
