#!/usr/bin/env python3.6
from pprint import pprint
import sys

from config import RTM_API_KEY, RTM_API_SECRET, RTM_API_TOKEN

from rtmapi import Rtm # type: ignore


def extract_series(api: Rtm, taskname: str):
    res = api.rtm.tasks.getList(filter=f'name:"{taskname}"')
    tlists = [tl for tl in res.tasks]
    [tlist] = tlists
    # TODO ok, task series is a defined by recurrence pattern..
    # TODO deleted?

    task = max(tlist, key = lambda t: t.modified) # just in case

    notes = [(n.created, n.value) for n in task.notes]

    for d, text in sorted(notes):
        print(f"{d} {text}")

def main():
    name = sys.argv[1]
    api = Rtm(RTM_API_KEY, RTM_API_SECRET, token=RTM_API_TOKEN)
    extract_series(api, name)

if __name__ == '__main__':
    main()
