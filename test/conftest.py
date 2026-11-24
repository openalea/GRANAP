"""
Test-suite wide setup: the `slow` marker, registered here so that pytest knows it whether it runs from the repository
or from test/ (the conda recipe's `cd test; pytest`, where pyproject.toml is not read).
"""


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: minutes long (anatomies generated, legacy comparisons, golden "
                                       "regressions); left out by pytest -m 'not slow', run before a release or a "
                                       "merge to main")
