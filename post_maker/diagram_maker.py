from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt

diagrams_path = Path("assets/diagrams")


class DiagramMaker:
    def __init__(self) -> None:
        diagrams_path.mkdir(exist_ok=True)

    def make_tech_frequency_diagram(
        self, statistics: dict[str, Any], limit_techs_number: int = 30
    ) -> Path:
        """
        :return Path: path to created diagram
        """
        elements_number = min(
            len(statistics["technology_frequency"]), limit_techs_number
        )
        technology_frequency = dict(
            list(statistics["technology_frequency"].items())[:elements_number]
        )

        title = (
            f"Statistics by category {statistics['category']} from {statistics['from_datetime'][:10]} "
            f"to {statistics['to_datetime'][:10]}"
        )

        # Create figure and axis
        fig, ax = plt.subplots(figsize=(7, 10))

        # Horizontal bar chart (reversing order to display highest value at top)
        ax.barh(
            list(technology_frequency.keys())[::-1],
            list(technology_frequency.values())[::-1],
        )

        # Title
        ax.set_title(title, pad=20)

        # Move x-axis label to top
        ax.set_xlabel("Frequency", labelpad=15)
        ax.xaxis.set_label_position("top")
        ax.xaxis.tick_top()

        # Y-axis label
        ax.set_ylabel("Technologies")

        # Adjust tick labels
        ax.tick_params(
            axis="x", top=True, labeltop=True, bottom=False, labelbottom=False
        )
        ax.set_xticklabels(ax.get_xticks(), rotation=90)

        # Tight layout for better spacing
        fig.tight_layout()
        file_name = f"{statistics['upsert_datetime'][:10]}-{statistics['category']}.png"
        path_to_diagram = diagrams_path / file_name
        plt.savefig(path_to_diagram)
        return path_to_diagram
