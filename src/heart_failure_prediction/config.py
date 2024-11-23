"""Configuration for the project.

This module contains the configuration for the project.
It includes the paths to the data, models, and reports directories.
"""

import logging
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from loguru import logger
from rich.console import Console
from rich.logging import RichHandler
from rich.theme import Theme

# Load environment variables from .env file if it exists
load_dotenv()

# Configure Logging
console = Console(
    theme=Theme(  # required, otherwise the color will be incorrect
        {
            "logging.level.trace": "bright_black",
            "logging.level.success": "green",
        },
    ),
)
logging.addLevelName(5, "TRACE")
logging.addLevelName(25, "SUCCESS")
logger.configure(
    handlers=[
        {
            "sink": RichHandler(
                markup=True,
                rich_tracebacks=True,
                tracebacks_show_locals=True,
                console=console,
            ),
            "format": (
                "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
                "<level>{message}</level>"
            ),
        },
    ],
)

# Set the default plotting backend to Plotly
pd.options.plotting.backend = "plotly"

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

DATA_DIRECTORY = PROJECT_ROOT / "data"
RAW_DATA_DIRECTORY = DATA_DIRECTORY / "raw"
INTERIM_DATA_DIRECTORY = DATA_DIRECTORY / "interim"
PROCESSED_DATA_DIRECTORY = DATA_DIRECTORY / "processed"
EXTERNAL_DATA_DIRECTORY = DATA_DIRECTORY / "external"

MODELS_DIRECTORY = PROJECT_ROOT / "models"

REPORTS_DIRECTORY = PROJECT_ROOT / "reports"
FIGURES_DIRECTORY = REPORTS_DIRECTORY / "figures"
