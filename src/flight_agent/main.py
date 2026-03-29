#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from flight_agent.crew import FlightAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        "origin": "Delhi (DEL)",
        "destination": "London (LHR)",
        "departure_date": "2026-06-15",
        "return_date": "2026-06-25",
        "passengers": "1",
        "cabin_class": "Economy",
    }

    try:
        FlightAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()