from .bot import bot, dp
from .handlers import router


dp.include_router(router)

__all__ = [
    'bot',
    'dp'
]