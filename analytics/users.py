import json
from pathlib import Path
from datetime import datetime

USERS_FILE = Path("users.json")


class UserAnalytics:
    def __init__(self):
        self.users = self._load()

    def _load(self):
        if USERS_FILE.exists():
            return json.loads(USERS_FILE.read_text(encoding="utf-8"))
        return {}

    def _save(self):
        USERS_FILE.write_text(
            json.dumps(self.users, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    def register(self, tg_user):
        user_id = str(tg_user.id)

        if user_id not in self.users:
            self.users[user_id] = {
                "first_name": tg_user.first_name,
                "username": tg_user.username,
                "first_seen": datetime.utcnow().isoformat()
            }
            self._save()

    def count(self) -> int:
        return len(self.users)
