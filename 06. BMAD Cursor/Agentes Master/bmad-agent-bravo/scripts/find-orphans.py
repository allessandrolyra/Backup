import requests
import json
import base64
import sys

def find_orphans(org, project, pat):
    # Prepare Auth
    auth = base64.b64encode(f":{pat}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth}",
        "Content-Type": "application/json"
    }

    # WIQL Query: Find items that SHOULD have parents but where we want to check links
    # Note: Flat WIQL can't filter out items WITH links easily, so we get the list and filter in Python.
    wiql = {
        "query": f"SELECT [System.Id], [System.Title], [System.WorkItemType] FROM WorkItems WHERE [System.TeamProject] = '{project}' AND [System.WorkItemType] IN ('Epic', 'Incidente', 'Impedimento', 'Test Case' , 'Feature', 'PBI', 'Task', 'Bug') AND [System.State] <> 'Removed'"
    }

    url = f"https://dev.azure.com/{org}/_apis/wit/wiql?api-version=7.1"
    response = requests.post(url, json=wiql, headers=headers)
    
    if response.status_code != 200:
        return {"error": f"Failed to run WIQL: {response.text}"}

    work_items = response.json().get("workItems", [])
    orphans = []

    # For each item, check links
    for item in work_items:
        item_id = item["id"]
        detail_url = f"https://dev.azure.com/{org}/{project}/_apis/wit/workitems/{item_id}?$expand=relations&api-version=7.1"
        detail_res = requests.get(detail_url, headers=headers)
        
        if detail_res.status_code == 200:
            data = detail_res.json()
            relations = data.get("relations", [])
            has_parent = any(rel["rel"] == "System.LinkTypes.Hierarchy-Reverse" for rel in relations)
            
            if not has_parent and data["fields"]["System.WorkItemType"] != "Epic":
                orphans.append({
                    "id": item_id,
                    "type": data["fields"]["System.WorkItemType"],
                    "title": data["fields"]["System.Title"],
                    "url": data["_links"]["html"]["href"]
                })

    return orphans

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 find-orphans.py <org> <project> <pat>")
        sys.exit(1)

    org = sys.argv[1]
    project = sys.argv[2]
    pat = sys.argv[3]

    result = find_orphans(org, project, pat)
    print(json.dumps(result, indent=2))
