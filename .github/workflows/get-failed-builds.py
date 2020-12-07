import requests
import json
from argparse import ArgumentParser

V3_HEADER = "application/vnd.github.v3+json"
HEADERS = {
    'Accept': V3_HEADER,
}

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('owner', type=str)
    parser.add_argument('repo', type=str)
    parser.add_argument('run_id', type=str)
    args = parser.parse_args()
    owner = args.owner
    repo = args.repo
    run_id = args.run_id
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}/jobs?per_page=100&filter=latest"
    res = requests.get(url, headers=HEADERS).json()
 

    failed_builds = set()
    for job in res['jobs']:
        if job['conclusion'] == 'failure' and 'draft' not in job['steps'][2]['name']: 
            failed_builds.add(job['steps'][2]['name'].split(' ')[1])
    print(list(failed_builds))
    print(json.dumps(list(failed_builds)))
    # print(failed_builds, len(failed_builds))

