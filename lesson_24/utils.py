import logging
import pytest

logger = logging.getLogger(__name__)

def validate_sorting(data: list, sort_key: str):

    values = []
    expected = []


    if not data:
        warning = "[WARNING] Empty response data, nothing to validate."
        logger.warning(warning)
        return

    try:
        values = [item[sort_key] for item in data]
    except KeyError:
        warning = f"[WARNING] Field '{sort_key}' not found in some items."
        logger.warning(warning)
        raise AssertionError(warning)

    try:
        expected = sorted(values)
    except TypeError as e:
        warning = f"[WARNING] Can't sort because of {e}"
        logger.warning(warning)
        raise AssertionError(warning)

    if values != expected:
        warning = (
            f"[WARNING] Sorting failed for field '{sort_key}'.\n"
            f"Expected: {expected}\nGot:      {values}"
        )
        logger.warning(warning)
        raise AssertionError(warning)