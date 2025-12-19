
---

# HeyGen Video Generator Script

This Python script generates short AI avatar videos using the **HeyGen API**.
It loops through a list of questions and creates a video for each question using a selected avatar and voice.

## Features

* Uses HeyGen’s video generation API
* Supports multiple questions
* Customizable avatar, voice, and video dimensions
* Prints the generated `video_id` for each request

## Requirements

* Python 3.8+
* A valid **HeyGen API Key**
* `requests` library

Install dependencies:

```bash
pip install requests
```

## Setup

1. Get your API key from HeyGen.
2. Add your API key in the script:

```python
HEYGEN_API_KEY = "YOUR_API_KEY_HERE"
```

3. Make sure the `avatar_id` and `voice_id` exist in your HeyGen account.

## Usage

Run the script:

```bash
python generate_video.py
```

Each question in the `questions` list will trigger a video generation request, and the script will print the corresponding `video_id`.

## Example Questions

```python
questions = [
    "What makes you happy at work?",
    "What is your greatest achievement?"
]
```

## Notes

* Video generation is asynchronous; use the `video_id` to check status via the HeyGen status endpoint.
* API response structure may vary, so the script safely extracts the `video_id`.

## License

This project is for educational and internal use only.
Check HeyGen’s terms of service before using in production.


