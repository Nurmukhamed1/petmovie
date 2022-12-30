from split_settings.tools import optional, include
import os

environment = os.environ.get("environment", "develop")
include(
    "components/base.py",
    "components/database.py",
    "components/extra.py",
    f"environments/{environment}.py",
    optional("environments/local_settings.py"),
)
