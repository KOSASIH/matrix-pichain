class UserBehavior:
    def __init__(self):
        self.user_actions = []  # List to store user actions

    def log_action(self, user_id, action):
        self.user_actions.append({"user_id": user_id, "action": action})

    def user_activity_count(self, user_id):
        return sum(1 for action in self.user_actions if action['user_id'] == user_id)

    def most_active_users(self, top_n=5):
        user_activity = {}
        for action in self.user_actions:
            user_id = action['user_id']
            if user_id not in user_activity:
                user_activity[user_id] = 0
            user_activity[user_id] += 1
        return sorted(user_activity.items(), key=lambda x: x[1], reverse=True)[:top_n]

    def __repr__(self):
        return f"UserBehavior(total_actions={len(self.user_actions)})"
