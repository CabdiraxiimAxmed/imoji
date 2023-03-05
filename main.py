emoji = {
    "telescope": "🔭",
    "people": ["👯"],
    "leave": "🌱",
    "flower": ["🥀", "🎕"],
    "message": "💬",
    "football": "⚽",
    "rocket": "🚀",
    "red_circle": "🔴",
    "kaaba": "🕋",
    "guiter": "🎸",
    "message_box": "📫",
    "computer": "💻",
    "notes": ["📝", "📄"],
    "electric": "⚡",
}

searched = input("Emoji: ");
if searched== 'all':
    for key in emoji:
        print(f"{key}: {emoji[key]}")
else: print(f'{searched}: {emoji[searched]}')
