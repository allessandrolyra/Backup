import json
import os
import sys

def generate_config(source_org, source_project, target_org, target_project, work_item_types):
    config = {
        "ChangeSetMappingFile": None,
        "Source": {
            "ObjectType": "TfsTeamProjectConfig",
            "Collection": f"https://dev.azure.com/{source_org}/",
            "Project": source_project,
            "ReflectedWorkItemIdFieldName": "Custom.ReflectedWorkItemId",
            "AllowDuplicateRequestIds": False,
            "PersonalAccessToken": "REPLACEME_SOURCE_PAT"
        },
        "Target": {
            "ObjectType": "TfsTeamProjectConfig",
            "Collection": f"https://dev.azure.com/{target_org}/",
            "Project": target_project,
            "ReflectedWorkItemIdFieldName": "Custom.ReflectedWorkItemId",
            "AllowDuplicateRequestIds": False,
            "PersonalAccessToken": "REPLACEME_TARGET_PAT"
        },
        "Processors": [
            {
                "ObjectType": "WorkItemMigrationConfig",
                "Enabled": True,
                "UpdateGrid": True,
                "UpdateSouceReflectedId": True,
                "WIQLQueryBit": f"AND [System.WorkItemType] IN ({', '.join([f\"'{t}'\" for t in work_item_types])})",
                "LinkItemMigration": True,
                "AttachmentMigration": True,
                "FixHtmlAttachmentLinks": True,
                "SkipToFinalState": False,
                "WorkItemCreateRetryLimit": 5,
                "PauseAfterEachWorkItem": False
            }
        ],
        "FieldMaps": [
            {
                "ObjectType": "MultiValueConditionalMapConfig",
                "WorkItemTypeName": "*",
                "sourceFieldsAndValues": {"System.State": "Approved"},
                "targetFieldsAndValues": {"System.State": "To Do"}
            }
        ]
    }
    return config

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python3 generate-migration-config.py <src_org> <src_proj> <tgt_org> <tgt_proj> <wit1,wit2,...>")
        sys.exit(1)

    src_org = sys.argv[1]
    src_proj = sys.argv[2]
    tgt_org = sys.argv[3]
    tgt_proj = sys.argv[4]
    wits = sys.argv[5].split(',')

    config_output = generate_config(src_org, src_proj, tgt_org, tgt_proj, wits)
    print(json.dumps(config_output, indent=2))
