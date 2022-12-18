import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="grimstroke",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="grimstroke_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from grimstroke.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export grimstroke_KEY=value
export grimstroke_KEY="@int 42"
export grimstroke_KEY="@jinja {{ this.db.uri }}"
export grimstroke_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
grimstroke_ENV=production grimstroke run
```

Read more on https://dynaconf.com
"""
