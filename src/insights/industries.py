from typing import List, Dict
import csv


def get_unique_industries(path: str) -> List[str]:
    with open(path, 'r') as file:
        data = [*csv.DictReader(file)]
    return set([ind['industry'] for ind in data if ind['industry'] != ''])


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [filt for filt in jobs if filt['industry'] == industry]
