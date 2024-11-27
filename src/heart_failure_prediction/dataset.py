"""Dataset module.

This module contains functions to download data.
"""

import pandas as pd
from dvc.api import DVCFileSystem
from loguru import logger

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
    logger.info("Downloading raw data.")
    file_system.get("data/raw/heart.csv", "data/raw/heart.csv")
    logger.success("Raw data downloaded.")


def load_raw_data() -> pd.DataFrame:
    """Load the raw data (`heart.csv`).

    Returns
    -------
        pd.DataFrame
            The raw data.
    """
    logger.info("Loading raw data.")
    with file_system.open("data/raw/heart.csv") as file:
        return pd.read_csv(file)
