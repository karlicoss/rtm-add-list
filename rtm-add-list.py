#!/usr/bin/env python3
from config import RTM_API_KEY, RTM_API_SECRET, RTM_API_TOKEN

from rtmapi import Rtm # type: ignore

def process(api: Rtm, super_task_name, subtasks):
    timeline = api.rtm.timelines.create().timeline.value  # TODO check for response
    print("Adding as subtasks of " + super_task_name)
    res = api.rtm.tasks.add(name="{} ^today #cli".format(super_task_name), timeline=timeline, parse="1")
    super_id = res.list.taskseries.task.id
    timeline = api.rtm.timelines.create().timeline.value  # TODO check for response

    for t in subtasks:
        if t.startswith(';'):
            print("Skipping: " + t)
        else:
            print("Adding: " + t)
            api.rtm.tasks.add(name=t, timeline=timeline, parse=str(1), parent_task_id=str(super_id))


def main():
    import sys
    super_task_name = sys.argv[1]
    # everything will be added as subtasks
    subtasks = [s.strip() for s in sys.stdin.readlines()]
    subtasks = [s for s in subtasks if len(s) > 0]

    api = Rtm(RTM_API_KEY, RTM_API_SECRET, token=RTM_API_TOKEN)
    process(api, super_task_name, subtasks)

if __name__ == '__main__':
    main()
