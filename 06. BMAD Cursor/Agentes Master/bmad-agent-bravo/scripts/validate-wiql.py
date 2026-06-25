import re
import sys

def validate_wiql(query):
    findings = []
    
    # Check for System.TeamProject
    if "System.TeamProject" not in query:
        findings.append({
            "severity": "High",
            "message": "Query missing [System.TeamProject]. This can lead to cross-project data leakage or performance issues.",
            "fix": "Add [System.TeamProject] = @project to the WHERE clause."
        })
    
    # Check for System.WorkItemType
    if "System.WorkItemType" not in query:
        findings.append({
            "severity": "Medium",
            "message": "Query missing [System.WorkItemType]. It's recommended to filter by type for clarity.",
            "fix": "Add [System.WorkItemType] IN ('User Story', 'Bug', ...) to filters."
        })

    # Check for ORDER BY
    if "ORDER BY" not in query.upper():
        findings.append({
            "severity": "Low",
            "message": "No ORDER BY clause found. Results might look disorganized in long lists.",
            "fix": "Add ORDER BY [System.ChangedDate] DESC."
        })

    # Basic syntax check (SELECT ... FROM)
    if not re.match(r"^\s*SELECT.*FROM.*", query, re.IGNORECASE | re.DOTALL):
        findings.append({
            "severity": "Critical",
            "message": "Invalid WIQL syntax. Query must start with SELECT and include FROM.",
            "fix": "Ensure query follows: SELECT [Fields] FROM WorkItems WHERE [Filters]"
        })

    return findings

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 validate-wiql.py \"SELECT ...\"")
        sys.exit(1)
    
    query_input = sys.argv[1]
    result = validate_wiql(query_input)
    
    if not result:
        print("✅ WIQL is valid and follows best practices.")
    else:
        for f in result:
            print(f"[{f['severity']}] {f['message']}")
            print(f"   Suggestion: {f['fix']}")
