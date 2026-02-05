# Customer Support Bot (Simple Flask Webhook)

هذا المشروع يوفر نموذجًا بسيطًا لبوت يرد على العملاء عبر Webhook باستخدام Flask.
يمكنك ربطه مع أي منصة مراسلة عبر تمرير رسالة العميل في JSON، والبوت سيرجع الرد المناسب.

## التشغيل السريع

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## مثال طلب

```bash
curl -X POST http://localhost:5000/webhook \
  -H "Content-Type: application/json" \
  -d '{"message": "هل عندكم توصيل؟"}'
```

## مثال رد

```json
{
  "reply": "نعم، نوفر خدمة التوصيل. من فضلك شاركنا موقعك والوقت المناسب."
}
```

## تخصيص الردود

عدّل قاموس `INTENT_REPLIES` في ملف `app.py` لإضافة نوايا وردود جديدة.
