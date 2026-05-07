import logging

from apscheduler.schedulers.blocking import BlockingScheduler

from app.config import (
    WEEKLY_DIGEST_CRON_DAY,
    WEEKLY_DIGEST_CRON_HOUR,
    WEEKLY_DIGEST_CRON_MINUTE,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def enqueue_incremental_sync() -> None:
    logging.info("[scheduler] enqueue incremental sync")


def enqueue_weekly_digest() -> None:
    logging.info("[scheduler] enqueue weekly digest")


def main() -> None:
    scheduler = BlockingScheduler(timezone="UTC")
    scheduler.add_job(enqueue_incremental_sync, "interval", minutes=30, id="incremental_sync")
    scheduler.add_job(
        enqueue_weekly_digest,
        "cron",
        day_of_week=WEEKLY_DIGEST_CRON_DAY,
        hour=WEEKLY_DIGEST_CRON_HOUR,
        minute=WEEKLY_DIGEST_CRON_MINUTE,
        id="weekly_digest",
    )
    logging.info("[scheduler] started")
    scheduler.start()


if __name__ == "__main__":
    main()
