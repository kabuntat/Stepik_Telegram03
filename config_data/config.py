from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту

@dataclass
class LogSettings:
    level: str
    format: str

@dataclass
class Config:
    bot: TgBot
    log: LogSettings

# Создаем экземпляр класса Config и наполняем его данными из переменных окружения
def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)
    return Config(
        bot=TgBot(token=env('BOT_TOKEN')),
        log=LogSettings(
            level=env('LOG_LEVEL'),
            format=env('LOG_FORMAT')
        )
    )
