import logging
import configparser
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class DbConfig:
    driver: str
    user: str
    password: str
    host: str
    port: str
    db_name: str

    def conn(self) -> str:
        return f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"


@dataclass
class TgBot:
    token: str  #  токен телеграм бота
    admin_ids: str  #  идентификаторы администратора бота через запятую


@dataclass
class Settings:
    sqlalchemy_echo: bool
    sqlalchemy_expire_on_commit: bool
    default_parse_mode: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    settings: Settings


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    tg_bot = config["tg_bot"]

    return Config(
        tg_bot=TgBot(
            token=tg_bot.get("token"),
            admin_ids=list(map(int, tg_bot.get("admin_ids").split(","))),
        ),
        db=DbConfig(**config["db"]),
        settings=Settings(
            sqlalchemy_echo=config.getboolean("settings", "sqlalchemy_echo"),
            sqlalchemy_expire_on_commit=config.getboolean(
                "settings", "sqlalchemy_expire_on_commit"
            ),
            default_parse_mode=config.get("settings", "default_parse_mode"),
        ),
    )
