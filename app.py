from flask import Flask, jsonify, request

app = Flask(__name__)

INTENT_REPLIES = {
    "pricing": "أكيد! من فضلك اذكر المنتج أو الخدمة المطلوبة عشان أعطيك السعر.",
    "hours": "ساعات العمل من الأحد إلى الخميس، 9 صباحًا إلى 6 مساءً.",
    "delivery": "نعم، نوفر خدمة التوصيل. من فضلك شاركنا موقعك والوقت المناسب.",
    "support": "أهلًا بك! كيف أقدر أساعدك اليوم؟",
}

KEYWORD_TO_INTENT = {
    "سعر": "pricing",
    "الأسعار": "pricing",
    "كم": "pricing",
    "دوام": "hours",
    "ساعات العمل": "hours",
    "توصيل": "delivery",
    "شحن": "delivery",
    "مساعدة": "support",
    "دعم": "support",
}

FALLBACK_REPLY = (
    "شكرًا لتواصلك! ممكن توضح طلبك أكثر؟ "
    "أو اذكر (السعر/ساعات العمل/التوصيل)."
)


def detect_intent(message: str) -> str | None:
    for keyword, intent in KEYWORD_TO_INTENT.items():
        if keyword in message:
            return intent
    return None


@app.post("/webhook")
def webhook():
    payload = request.get_json(silent=True) or {}
    message = (payload.get("message") or "").strip()

    if not message:
        return jsonify({"reply": "ممكن تكتب رسالتك؟"}), 400

    intent = detect_intent(message)
    if intent and intent in INTENT_REPLIES:
        reply = INTENT_REPLIES[intent]
    else:
        reply = FALLBACK_REPLY

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
