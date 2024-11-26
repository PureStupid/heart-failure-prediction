"""Dataset module.

This module contains functions to download data.
"""

import pandas as pd
from dvc.api import DVCFileSystem

from heart_failure_prediction.config import DVC_REMOTE_CONFIG

file_system = DVCFileSystem(
    "https://github.com/PureStupid/heart-failure-prediction.git",
    rev="main",
    remote="origin",
    remote_config=DVC_REMOTE_CONFIG,
)


def download_raw_data() -> None:
    """Download the raw data.

    The raw data (`heart.csv`) is downloaded from the remote storage to the
    local storage.
    """
    file_system.get("data/raw/heart.csv", "data/raw/heart.csv")


def load_raw_data() -> pd.DataFrame:
    """Load the raw data (`heart.csv`), downloading it if it doesn't exist.

    Returns
    -------
        pd.DataFrame
            The raw data.
    """
    if not file_system.exists("data/raw/heart.csv"):
        download_raw_data()
    with file_system.open("data/raw/heart.csv") as file:
        return pd.read_csv(file)
