import json

def load_rules():
    try:
        with open("rules.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def find_relevant_rule(text: str):
    text_lower = text.lower()
    
    # 1. Четы и сторонний софт
    if any(w in text_lower for w in ["чит", "софт", "аим", "рванок", "сх", "fly", "гм"]):
        return "5.2", "complaint.cheating", "p1", "Запрещено использование стороннего ПО и читов."
        
    # 2. Оскорбления и родня
    elif any(w in text_lower for w in ["оскорб", "мать", "родн", "дурак", "dibil", "урод"]):
        return "2.1", "complaint.insult", "p2", "Запрещены оскорбления игроков и родных."
        
    # 3. Реклама и спам
    elif any(w in text_lower for w in ["реклам", "ссылк", "http", "t.me", "заходи на"]):
        return "2.3", "complaint.spam", "p3", "Запрещена реклама сторонних ресурсов."
        
    # 4. Проблемы с администрацией
    elif any(w in text_lower for w in ["админ", "обман", "хам"]):
        return "3.2", "complaint.admin", "p2", "Запрещены хамство и обман администрации."
        
    # Дефолтный ответ
    return "1.1", "complaint.other", "p3", "Общие положения сервера Grand Mobile."