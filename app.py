from flask import Flask, send_file
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import io

app = Flask(__name__)

@app.route("/")
def generate_image():
    now = datetime.now().strftime("%H시")

    img = Image.open("base.png").convert("RGB")
    draw = ImageDraw.Draw(img)

    # ✅ 폰트 크게
    try:
        font = ImageFont.truetype("arial.ttf", 130)
    except:
        font = ImageFont.load_default()

    # ✅ 좌표 (이건 조금만 수정하면 됨)
    x, y = 100, 500

    # ✅ 빨간색 유지 (위치 확인용)
    draw.text((x, y), f"{now}라니……", font=font, fill=(255,0,0))

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    return send_file(buf, mimetype="image/png")

app.run(host="0.0.0.0", port=5000)

