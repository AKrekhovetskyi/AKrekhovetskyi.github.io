from pymongo import DESCENDING

from .diagram_maker import DiagramMaker
from .mongo_client import COLLECTION_STATISTICS, MongoClient
from .post_writer import PostWriter


def main() -> None:
    client = MongoClient
    client.collection_name = COLLECTION_STATISTICS
    with MongoClient() as collection_stats:
        diagram_maker = DiagramMaker()
        # Fetch only the newest documents unique by the "category" field.
        pipeline = [
            {"$sort": {"upsert_datetime": DESCENDING}},
            {"$group": {"_id": "$category", "doc": {"$first": "$$ROOT"}}},
            {"$replaceRoot": {"newRoot": "$doc"}},
        ]
        for statistics in collection_stats.collection.aggregate(pipeline):
            # Create post about trending technologies.
            post_write = PostWriter(
                title=f"Trending technologies in the field of {statistics['category']}",
                datetime=statistics["upsert_datetime"],
                category=statistics["category"],
                tags=COLLECTION_STATISTICS,
            )
            diagram_path = diagram_maker.make_tech_frequency_diagram(statistics)
            post_write.write_about_statistics(
                diagram_path=diagram_path,
                technology_frequencies=statistics["technology_frequency"],
            )


if __name__ == "__main__":
    main()
