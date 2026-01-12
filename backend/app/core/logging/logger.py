import logging 
import os
from typing import Optional, Dict, Any

LOG_LEVEL = os.getenv("APP_LOG_LEVEL", "INFO").upper()

class AppLogger: 
    def __init__(self, name: str = 'app'):
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            numeric_level = getattr(logging, LOG_LEVEL, logging.INFO)
            self.logger.setLevel(numeric_level)

            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def info(self, msg: str, extra_data: Optional[Dict[str, Any]] = None):
        self.logger.info(self._format(msg, extra_data))

    def warn(self, msg: str, extra_data: Optional[Dict[str, Any]] = None):
        self.logger.warning(self._format(msg, extra_data))

    def error(self, msg: str, extra_data: Optional[Dict[str, Any]] = None):
        self.logger.error(self._format(msg, extra_data))

    def debug(self, msg: str, extra_data: Optional[Dict[str, Any]] = None):
        self.logger.debug(self._format(msg, extra_data))

    @staticmethod
    def _format(msg: str, extra_data: Optional[Dict[str, Any]] = None) -> str:
        if extra_data:
            extra_str = " | ".join(f"{k}={v}" for k, v in extra_data.items())
            msg = f"{msg} | {extra_str}"
        return msg
    
logger = AppLogger()