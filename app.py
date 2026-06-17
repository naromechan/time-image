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

    # ✅ 시스템 Arial 폰트 직접 지정
    font = ImageFont.truetype("font.ttf", 110)

    x, y = 300, 750

    draw.text((x, y), f"{now}라니……", font=font, fill=(255,0,0))

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    return send_file(buf, mimetype="image/png")

app.run(host="0.0.0.0", port=5000)
