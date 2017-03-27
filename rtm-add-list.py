#!/usr/bin/env python3
from config import api_key, secret, token

from rtm import createRTM

def process(api, super_task_name, subtasks):
    timeline = api.timelines.create().timeline  # TODO check for response
    print("Adding as subtasks of " + super_task_name)
    res = api.tasks.add(name="{} ^today #cli".format(super_task_name), timeline=timeline, parse=1)
    super_id = res.list.taskseries.task.id
    timeline = api.timelines.create().timeline  # TODO check for response

    for t in subtasks:
        if t.startswith(';'):
            print("Skipping: " + t)
        else:
            print("Adding: " + t)
            api.tasks.add(name=t, timeline=timeline, parse=1, parent_task_id=super_id)


def main():
    import sys
    super_task_name = sys.argv[1]
    # everything will be added as subtasks
    subtasks = [s.strip() for s in sys.stdin.readlines()]
    subtasks = [s for s in subtasks if len(s) > 0]
    api = createRTM(api_key, secret, token)
    process(api, super_task_name, subtasks)

if __name__ == '__main__':
    main()