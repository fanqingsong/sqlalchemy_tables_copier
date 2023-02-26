import logging

from app.db.session import SessionLocal
from app.db.session import engine

from app.db.session import SessionLocal_dest
from app.db.session import engine_dest

from sqlalchemy_tables_copier import TablesCopier

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Before copy data")

    tc = TablesCopier(engine, SessionLocal(), engine_dest, SessionLocal_dest())
    tc.run()

    logger.info("After copy data")


if __name__ == "__main__":
    main()
