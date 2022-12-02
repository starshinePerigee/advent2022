import datetime
import os

import requests

from util.cookie import cookie


# thanks to https://github.com/Starwort/aoc_helper

def get_day(day: int = None) -> str:
    if day is None:
        day = datetime.datetime.today().day

    cwd = os.getcwd()
    target_path = os.path.join(os.path.dirname(cwd), "data", f"{day:02d}.txt")

    if os.path.exists(target_path):
        with open(target_path) as input_file:
            input_string = input_file.read()
        return input_string

    url = f"https://adventofcode.com/2022/day/{day}/input"

    user_string = f"https://github.com/starshinePerigee/advent2022 user {os.getlogin()}"
    request_header = {'User-Agent': user_string}

    session_cookie = {'session': cookie}

    request = requests.get(
        url,
        headers=request_header,
        cookies=session_cookie
    )

    if not request.ok:
        raise ConnectionError(f"Connection error! Response code {request.status_code}: {request.text}")

    with open(target_path, 'a+') as input_file:
        input_file.write(request.text)

    return request.text


if __name__ == '__main__':
    print(get_day())
