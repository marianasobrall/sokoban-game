"""Custom domain exceptions for sokoban level loading and validation."""


class SokobanError(Exception):
    """Base class for all Sokoban custom exceptions."""


class InvalidCharacterError(SokobanError):
    """Raised when an unrecognized character is detected in a level file."""


class ExtraCharacterError(SokobanError):
    """Raised when a level row contains more characters than the grid allows."""


class MissingElementError(SokobanError):
    """Raised when required level elements are missing or a row is incomplete."""


class BoxCountMismatchError(SokobanError):
    """Raised when the number of boxes does not match the number of box spots."""