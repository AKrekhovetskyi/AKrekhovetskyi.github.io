from datetime import datetime
from pathlib import Path
from typing import Any

from mdutils.mdutils import MdUtils

post_path = Path("_posts")


class PostWriter:
    def __init__(
        self,
        title: str,
        datetime: str,
        category: str,
        subcategory: str,
        tags: str | None = None,
    ) -> None:
        """Read the docs for parameter details: https://chirpy.cotes.page/posts/write-a-new-post/."""
        self.title = title
        self.datetime = datetime
        self.category = category
        self.subcategory = subcategory.title()
        self.tags = tags

        path_to_category = post_path / self.category
        path_to_category.mkdir(exist_ok=True)
        self.file_path = (
            path_to_category
            / f"{self.datetime[:10]}-{self.category}-{self.subcategory}.md"
        )
        self.md_file = MdUtils(file_name=str(self.file_path))

    def compose_metadata(self) -> str:
        line = "---"
        title = f"title: {self.title}"
        date = f"date: {self.datetime}"
        subcategory = ", " + self.subcategory if self.subcategory else ""
        categories = f"categories: [{self.category}{subcategory}]"
        tags = f"tags: [{self.tags.lower() if self.tags else ''}]"
        metadata = ""
        for metadata_item in [line, title, date, categories, tags, line]:
            metadata += f"{metadata_item}\n"
        return metadata

    def remove_top_blank_lines(self) -> None:
        """Workaround until the issue https://github.com/didix21/mdutils/issues/95 is resolved."""
        with open(self.file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Remove blank lines at the top
        while lines and lines[0].strip() == "":
            lines.pop(0)

        with open(self.file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

    def publish_statistics(
        self, diagram_path: Path, technology_frequencies: dict[str, int]
    ) -> None:
        self.md_file.write(self.compose_metadata())
        self.md_file.new_header(level=1, title=self.title.title())
        self.md_file.write(
            f"![{self.title.lower().replace(' ', '-')}](/{diagram_path})"
        )
        self.md_file.new_header(level=2, title="Technology Frequencies")
        table = ["Technology", "Frequency"]
        columns = len(table)
        for technology, frequency in technology_frequencies.items():
            table.extend([technology, frequency])
        self.md_file.new_table(columns=columns, rows=len(table) // 2, text=table)
        self.md_file.create_md_file()
        self.remove_top_blank_lines()

    def publish_vacancies(self, vacancies: list[dict[str, Any]]) -> None:
        self.md_file.write(self.compose_metadata())
        for vacancy in vacancies:
            self.md_file.new_header(
                level=3,
                title=f"[{vacancy['title']}]({vacancy['url']})",
                add_table_of_contents="n",
            )
            self.md_file.new_line(
                text=(
                    f"👁️ {vacancy['views']} views • 📩 {vacancy['applications']} applications • "
                    f"📡 Source: {vacancy['source'].title()}"
                ),
                bold_italics_code="bc",
            )
            if vacancy.get("company_name"):
                self.md_file.new_line(f"- **Company:** {vacancy['company_name']}")
            if vacancy.get("address"):
                self.md_file.new_line(f"- **Location:** {vacancy['address']}")
            self.md_file.new_line(
                f"- **Experience Required:** {vacancy['years_of_experience']}"
            )
            published = datetime.fromisoformat(vacancy["publication_date"]).strftime(
                "%d-%m-%Y %H:%M"
            )
            self.md_file.new_line(f"- **Published:** {published}")
            self.md_file.new_line()
            self.md_file.new_line()
            self.md_file.write("---")
            self.md_file.new_line()

        self.md_file.create_md_file()
        self.remove_top_blank_lines()
