from os import environ, getenv
from typing import Any, Self

from dotenv import load_dotenv
from pymongo import MongoClient as DefaultMongoClient
from pymongo.collection import Collection

load_dotenv()

DATABASE_NAME = "techtrendstat"
COLLECTION_STATISTICS = "statistics"
COLLECTION_VACANCIES = "vacancies"


class MongoClient(DefaultMongoClient):
    collection: Collection
    collection_name: str

    def __init__(self, **kwargs: Any) -> None:
        is_test = environ["IS_TEST"].lower() in {"1", "true", "yes", "on"}
        if is_test:
            super().__init__(
                host=environ["MONGODB_HOST"],
                port=int(environ["MONGODB_PORT"]),
                username=getenv("MONGODB_USERNAME"),
                password=getenv("MONGODB_PASSWORD"),
                **kwargs,
            )
        else:
            if (
                not environ["MONGODB_USERNAME"]
                or not environ["MONGODB_PASSWORD"]
                or not environ["MONGODB_CLUSTER_HOST"]
            ):
                raise ValueError(
                    "`username`, `password`, and `cluster_host` are required in a production environment."
                )

            kwargs = kwargs | {
                "host": f"mongodb+srv://{environ['MONGODB_USERNAME']}:{environ['MONGODB_PASSWORD']}"
                f"@{environ['MONGODB_CLUSTER_HOST']}.mongodb.net/"
            }
            super().__init__(**kwargs)

    def __enter__(self) -> Self:
        super().__enter__()
        self.collection = self.get_database(self.database_name)[self.collection_name]
        return self

    @property
    def database_name(self) -> str:
        return DATABASE_NAME

    @database_name.setter
    def database_name(self, value: str) -> None:
        self._database_name = value
