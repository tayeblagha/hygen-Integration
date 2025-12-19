import os
import time
import requests
import json

HEYGEN_API_KEY = "" # enter your api token here

if not HEYGEN_API_KEY:
    raise RuntimeError("Set HEYGEN_API_KEY environment variable before running.")

GEN_URL = "https://api.heygen.com/v2/video/generate"
STATUS_URL = "https://api.heygen.com/v1/video_status.get"  # ?video_id=...


questions=["what makes you happy at work ?", "what is your greatest achievements ?"]

for question in questions:
    payload = {
        "video_inputs": [
            {
                "character": {
                    "type": "avatar",
                    "avatar_id": "Harrison_public_20240313"   # make sure this avatar_id exists in your account
                },
                "voice": {
                    "type": "text",
                    "voice_id": "f38a635bee7a4d1f9b0a654a31d050d2",  # verify this voice_id via the voices endpoint
                    "input_text": (
                        question
                    )
                }
            }
        ],
        "dimension": {"width": 1280, "height": 720},
        "caption": False
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": HEYGEN_API_KEY
    }

    # 1) create video job
    resp = requests.post(GEN_URL, headers=headers, json=payload)
    if not resp.ok:
        print("Create video failed:", resp.status_code, resp.text)
        raise SystemExit(1)

    data = resp.json()
    # API responses vary; look for video_id in the usual places
    video_id = data.get("data", {}).get("video_id") or data.get("video_id") or data.get("id")
    if not video_id:
        print("Couldn't find video_id in response:", json.dumps(data, indent=2))
        raise SystemExit(1)

    print("video_id:", video_id)

















### this is optional part is to get the video from their public cloud 
# # 2) poll status endpoint
# for _ in range(120):  # up to ~60 checks (~5-10 minutes depending on sleep)
#     status_resp = requests.get(f"{STATUS_URL}?video_id={video_id}", headers=headers)
#     if not status_resp.ok:
#         print("Status check failed:", status_resp.status_code, status_resp.text)
#         break

#     s = status_resp.json()
#     # adapt these keys depending on the exact status response you get
#     status = s.get("data", {}).get("status") or s.get("status") or s.get("video_status")
#     print("status:", status)

#     if status in ("completed", "succeeded"):
#         # video_url, thumbnail_url, captions etc. are usually included
#         video_url = s.get("data", {}).get("video_url") or s.get("video_url")
#         print("Video ready:", video_url)
#         break
#     if status in ("failed", "error"):
#         print("Video generation failed:", json.dumps(s, indent=2))
#         break

#     time.sleep(5)  # polite backoff; adjust as needed

# else:
#     print("Timed out waiting for video to finish; check status later or via webhook.")