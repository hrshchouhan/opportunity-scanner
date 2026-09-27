import os, requests

headers = {"Authorization": f"Bearer {os.environ['GH_TOKEN']}"}
queries = [
    'label:bounty state:open type:issue language:cpp',
    'label:"good first issue" state:open type:issue language:cpp no:assignee',
]
for q in queries:
    r = requests.get(
        "https://api.github.com/search/issues",
        params={"q": q, "sort": "created", "order": "desc", "per_page": 15},
        headers=headers,
    )
    print("\n==", q)
    for i in r.json().get("items", []):
        print(i["title"], "->", i["html_url"])