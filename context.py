proceses = [

    {
        "name": "P1",
        "PID": 1,
        "commands": [
            {
                "actions": "malloc",
                "size": 4,
                "target": "var1"
            },
            {
                "actions": "free",
                "target": "var1"
            },
            {
                "actions": "malloc",
                "size": 4,
                "target": "var2"
            },
            {
                "actions": "free",
                "target": "var2"
            },
            {
                "actions": "malloc",
                "size": 4,
                "target": "var3"
            },
            {
                "actions": "free",
                "target": "var3"
            }
        ]
    },
    {
        "name": "MenTest",
        "PID": 0,
        "commands": [
            {
                "actions": "read_file",
                "target": "file_test_1"
            },
            {
                "actions": "write_file",
                "target": "file_test_1"
            },
            {
                "actions": "read_file",
                "target": "file_test_4"
            },
            {
                "actions": "write_file",
                "target": "file_test_4"
            }
        ]


    },
    {
        "name": "P2",
        "PID": 2,
        "commands": [
            {
                "actions": "create_channel",
                "target": "channel1"
            },
            {
                "actions": "send",
                "target": "channel1",
                "amount": 10
            },

        ]
    },
    {
        "name": "P3",
        "PID": 3,
        "commands": [
            {
                "actions": "read_file",
                "target": "file1"
            },
            {
                "actions": "write_file",
                "target": "file1"
            },
            # {
            #     "actions": "receive",
            #     "target": "channel1",
            #     "amount": 10
            # },
            {
                "actions": "read_file",
                "target": "file2"
            },
            {
                "actions": "write_file",
                "target": "file2"
            },
            {
                "actions": "read_file",
                "target": "file3"
            },
            {
                "actions": "write_file",
                "target": "file3"
            }

        ]
    },
    {
        "name": "P4",
        "PID": 4,
        "commands": [
            {
                "actions": "create_thread",
                "target": "thread_1"
            },
            {
                "actions": "destroy_thread",
                "target": "thread_1",
            },

        ]
    }
]


def get_all_devices():
    devices = set()
    for process in proceses:
        for command in process['commands']:
            if command['actions'] == 'use_device' or command['actions'] == 'release_device':
                devices.add(command['target'])
    return devices


def get_all_files():
    files = set()
    for process in proceses:
        for command in process['commands']:
            if "actions" not in command:
                continue
            if command['actions'] == 'read_file' or command['actions'] == 'write_file':
                files.add(command['target'])
    return files


def get_all_channels():
    channels = set()
    for process in proceses:
        for command in process['commands']:
            if "actions" not in command:
                continue

            if command['actions'] == 'create_channel' or command['actions'] == 'send' or command['actions'] == 'receive':
                channels.add(command['target'])
    return channels


def get_all_threads():
    threads = set()
    for process in proceses:
        for command in process['commands']:
            if "actions" not in command:
                continue
            if command['actions'] == 'create_thread' or command['actions'] == 'destroy_thread':
                threads.add(command['target'])
    return threads
