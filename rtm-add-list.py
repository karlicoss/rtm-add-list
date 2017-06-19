#!/usr/bin/env python3
from config import RTM_API_KEY, RTM_API_SECRET, RTM_API_TOKEN

from enhanced_rtm import EnhancedRtm

def process(api: EnhancedRtm, super_task_name, subtasks):
    print("Adding as subtasks of " + super_task_name)
    super_id = api.addTask("%s ^today #cli" % super_task_name)

    for t in subtasks:
        if t.startswith(';'):
            print("Skipping: " + t)
        else:
            print("Adding: " + t)
            api.addTask(t, parent_id=super_id)


def main():
    import sys
    super_task_name = sys.argv[1]
    # everything will be added as subtasks
    subtasks = [s.strip() for s in sys.stdin.readlines()]
    subtasks = [s for s in subtasks if len(s) > 0]

    api = EnhancedRtm(RTM_API_KEY, RTM_API_SECRET, token=RTM_API_TOKEN)
    process(api, super_task_name, subtasks)

if __name__ == '__main__':
    main()
