# logic.py

def razure_decision_engine(energy, money_stress, clarity, weight_note=""):
    response = {}

    # -------------------------
    # 1. Stabilising Message
    # -------------------------
    if energy <= 3:
        response["stabilise"] = (
            "Low energy isn’t a failure. Today is about conserving strength, not pushing."
        )
    elif clarity <= 3:
        response["stabilise"] = (
            "When things feel unclear, action creates clarity. We’ll keep this simple."
        )
    elif money_stress >= 7:
        response["stabilise"] = (
            "Money pressure narrows thinking. We’re focusing on control, not perfection."
        )
    else:
        response["stabilise"] = (
            "You’re more steady than it feels. Let’s use today well, without overloading it."
        )

    # -------------------------
    # 2. Priority
    # -------------------------
    if money_stress >= 7:
        response["priority"] = "Stabilise finances"
    elif clarity <= 3:
        response["priority"] = "Regain mental clarity"
    elif energy <= 3:
        response["priority"] = "Restore physical energy"
    else:
        response["priority"] = "Make forward progress"

    # -------------------------
    # 3. Action (10–30 mins)
    # -------------------------
    if response["priority"] == "Stabilise finances":
        response["action"] = (
            "Spend 20 minutes listing upcoming expenses and identifying one you can pause or reduce."
        )
    elif response["priority"] == "Regain mental clarity":
        response["action"] = (
            "Write a short list of everything on your mind, then circle only ONE thing you’ll act on today."
        )
    elif response["priority"] == "Restore physical energy":
        response["action"] = (
            "Take a 10–15 minute walk or stretch session without your phone."
        )
    else:
        response["action"] = (
            "Choose one task that moves your life forward and work on it for 25 minutes, uninterrupted."
        )

    # -------------------------
    # 4. Release
    # -------------------------
    response["release"] = (
        "You don’t need to solve everything today. Today is about one contained win."
    )

    return response