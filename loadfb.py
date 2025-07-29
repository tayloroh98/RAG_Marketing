import requests
import json

ver = "v19.0"
account = 'act_3843676962540781'
token = 'EAAO7l8ZC7BysBPIxmKyM2gMdslxf1HAJcRb9H7JO5wm7sgijUCpjLMJBgejEitMZB0eZCsjQlqUeFRGdTMJZB1GTdQvPBPgNS67QYVsMYTLFyjXYqp4B49LgNZB0QYWOO9D3pZCVm2tc2T2IcLaZBdRhq7pVZCGlcnSdM4nISkDrpxHQGlFPbqB5S2ua9iWOX7ImbFplL3jH'

insights = 'campaign_name,adset_name,ad_name,impressions,clicks,reach,spend,conversions,conversion_values'
url = f"https://graph.facebook.com/{ver}/{account}/insights"

params = {
    'fields': insights,
    'access_token': token, 
    'level': 'ad',
    'time_range[since]' : '2025-07-15',
    'time_range[until]' : '2025-07-27',
    'action_report_time' : 'conversion',
    'use_unified_attribution_setting' : 'true',
    "action_breakdowns": "action_type",
}


r = requests.get(url = url, params= params )
print(r.url)

if r.status_code != 200:
    print("something went wrong :",r.text)
    assert r.status_code == 200
else:
    content = r.text
    content_json = json.loads(content)
    print(content_json)