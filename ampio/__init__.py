"""Python implementation of Ampio MQTT API."""
import logging
from pathlib import Path

_LOGGER = logging.getLogger(__name__)
__version__ = (Path(__file__).parent / "VERSION").read_text(encoding="utf-8").strip()
