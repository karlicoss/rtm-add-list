#!/usr/bin/env python3.6
from pprint import pprint
import sys

from config import RTM_API_KEY, RTM_API_SECRET, RTM_API_TOKEN

from kython.enhanced_rtm import EnhancedRtm

def extract_series(api: EnhancedRtm, taskname: str):
    task = api.getTaskByName(taskname)
    notes = [(n.created, n.value) for n in task.notes]

    for d, text in sorted(notes):
        print(f"{d} {text}")

def main():
    name = sys.argv[1]
    api = EnhancedRtm(RTM_API_KEY, RTM_API_SECRET, token=RTM_API_TOKEN)
    extract_series(api, name)

if __name__ == '__main__':
    main()
