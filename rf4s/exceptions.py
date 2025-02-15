"""
A module reserved for exception classes.
"""


class FishHookedError(Exception):
    """A fish is hooked during a wrong routine."""


class FishCapturedError(Exception):
    """A fish is captured during a wrong routine."""


class LineAtEndError(Exception):
    """Fishing line is at the end during retrieval."""


class FishGotAwayError(Exception):
    """A hooked fish got away during pulling or retrieving stage."""


class GroundbaitNotChosenError(Exception):
    """Run out of groundbait on spod rod."""

class LineSnaggedError(Exception):
    """Fishing line is snagged."""