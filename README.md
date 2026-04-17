## طريقة التشغيل

### المتطلبات

* Python 3.10 أو أحدث
* pip
* اتصال بالإنترنت
* مفتاح API للنموذج المستخدم

### تثبيت المشروع

```bash
git clone https://github.com/your-username/rafiq.git
cd rafiq
```

إنشاء بيئة افتراضية وتشغيلها:

```bash
python -m venv venv
```

على Linux / macOS:

```bash
source venv/bin/activate
```

على Windows:

```bash
venv\Scripts\activate
```

تثبيت المكتبات:

```bash
pip install -r requirements.txt
```

### إعداد ملف البيئة

أنشئ ملفًا باسم `.env` داخل المشروع ثم أضف:

```env
API_KEY=your_api_key
MODEL_NAME=noha
```

إذا كان المشروع يستخدم قاعدة بيانات أو ملف مصطلحات:

```env
TERMS_FILE=data/hajj_terms.json
```

### تشغيل الخادم

```bash
python app.py
```

أو إذا كان المشروع يستخدم FastAPI:

```bash
uvicorn main:app --reload
```

بعد التشغيل سيفتح الخادم على:

```text
http://127.0.0.1:8000
```

### تجربة النظام

أرسل نصًا مثل:

```text
يرجى التوجه إلى نقطة التفويج رقم 3 ثم الانتظار حتى يتم استدعاؤكم
```

وسيُرجع النظام:

```text
اذهب إلى مكان التجمع 3 ثم انتظر هنا
```

### هيكل المشروع

```text
rafiq/
│
├── app.py أو main.py
├── requirements.txt
├── .env
├── data/
│   └── hajj_terms.json
├── models/
│   └── simplifier.py
├── static/
├── templates/
└── README.md
```
