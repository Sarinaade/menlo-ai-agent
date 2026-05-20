import json
from pathlib import Path
import requests
from config import settings

MOCK_PATH = Path("data/canvas_mock.json")

def _load_mock_canvas() -> dict:
    return json.loads(MOCK_PATH.read_text())

def get_canvas_assignments() -> list[dict]:
    """Read-only tool: returns assignments from mock Canvas or real Canvas API."""
    if settings.use_mock_canvas or not settings.canvas_api_token:
        return _load_mock_canvas()["assignments"]

    url = f"{settings.canvas_base_url}/api/v1/courses/{settings.canvas_course_id}/assignments"
    headers = {"Authorization": f"Bearer {settings.canvas_api_token}"}
    r = requests.get(url, headers=headers, timeout=20)
    r.raise_for_status()
    return r.json()

def get_canvas_announcements() -> list[dict]:
    """Read-only tool: returns announcements from mock Canvas or real Canvas API."""
    if settings.use_mock_canvas or not settings.canvas_api_token:
        return _load_mock_canvas()["announcements"]

    # Canvas announcements are discussion topics with only_announcements=true.
    url = f"{settings.canvas_base_url}/api/v1/courses/{settings.canvas_course_id}/discussion_topics"
    headers = {"Authorization": f"Bearer {settings.canvas_api_token}"}
    params = {"only_announcements": "true"}
    r = requests.get(url, headers=headers, params=params, timeout=20)
    r.raise_for_status()
    return r.json()

def canvas_context() -> str:
    assignments = get_canvas_assignments()
    announcements = get_canvas_announcements()

    lines = ["CANVAS ASSIGNMENTS:"]
    for a in assignments:
        lines.append(f"- {a.get('course','Course')}: {a.get('title') or a.get('name')} due {a.get('due_at')} points={a.get('points') or a.get('points_possible')}")

    lines.append("\nCANVAS ANNOUNCEMENTS:")
    for ann in announcements:
        title = ann.get("title", "Announcement")
        msg = ann.get("message", ann.get("html_url", ""))
        course = ann.get("course", "Course")
        lines.append(f"- {course}: {title} — {msg}")

    return "\n".join(lines)
