import logging
import time

from app.config import SYNC_INTERVAL_SECONDS

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def run_sync_job() -> None:
    logging.info("[worker] running incremental sync job")


def run_analysis_job() -> None:
    logging.info("[worker] running analysis job")


def main() -> None:
    logging.info("[worker] started (interval=%ss)", SYNC_INTERVAL_SECONDS)
    while True:
        run_sync_job()
        run_analysis_job()
        time.sleep(SYNC_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
