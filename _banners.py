import math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1600, 900
FB = "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i]-a[i])*t) for i in range(3))

def vgrad(draw, box, c1, c2, vertical=True):
    x0,y0,x1,y1 = box
    n = (y1-y0) if vertical else (x1-x0)
    for i in range(n):
        t = i/max(n-1,1)
        c = lerp(c1, c2, t)
        if vertical:
            draw.line([(x0, y0+i),(x1, y0+i)], fill=c)
        else:
            draw.line([(x0+i, y0),(x0+i, y1)], fill=c)

def rrect(draw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def soft_shadow(base_img, box, radius=24, blur=30, opacity=90):
    shadow = Image.new("RGBA", base_img.size, (0,0,0,0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle(box, radius=radius, fill=(0,0,0,opacity))
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur))
    base_img.alpha_composite(shadow)

def browser_frame(img, box, chrome_color, bg_color):
    draw = ImageDraw.Draw(img)
    x0,y0,x1,y1 = box
    soft_shadow(img, box, radius=20, blur=40, opacity=110)
    rrect(draw, box, 20, fill=chrome_color)
    bar_h = 46
    for i,c in enumerate([(237,106,94),(245,191,79),(97,196,80)]):
        draw.ellipse([x0+22+i*22, y0+bar_h/2-7, x0+22+i*22+14, y0+bar_h/2+7], fill=c)
    rrect(draw, [x0+90, y0+11, x1-30, y0+bar_h-11], 10, fill=(255,255,255,235) if isinstance(bg_color, tuple) and len(bg_color)==3 else (255,255,255))
    rrect(draw, [x0+2, y0+bar_h, x1-2, y1-2], 0, fill=bg_color)
    return (x0, y0+bar_h, x1, y1)

def nav_bar(img, box, color, text_color, brand, links):
    draw = ImageDraw.Draw(img)
    x0,y0,x1,y1 = box
    draw.rectangle([x0,y0,x1,y0+64], fill=color)
    draw.text((x0+28, y0+18), brand, font=font(FB,22), fill=text_color)
    lx = x1-30
    for link in reversed(links):
        w = draw.textlength(link, font=font(FR,15))
        lx -= w
        draw.text((lx, y0+24), link, font=font(FR,15), fill=text_color)
        lx -= 34
    return y0+64

def stat_card(img, xy, w, h, title, value, accent, sub, dark_text=(30,34,45)):
    draw = ImageDraw.Draw(img)
    x,y = xy
    soft_shadow(img, [x,y,x+w,y+h], radius=16, blur=18, opacity=45)
    rrect(draw, [x,y,x+w,y+h], 16, fill=(255,255,255))
    draw.text((x+20,y+18), title, font=font(FR,14), fill=(120,126,140))
    draw.text((x+20,y+40), value, font=font(FB,30), fill=accent)
    draw.text((x+20,y+h-30), sub, font=font(FR,12), fill=(150,156,168))
    draw.rounded_rectangle([x+w-10,y+14,x+w-4,y+h-14], 3, fill=accent)

def line_chart(img, box, accent, points, fill_alpha=60):
    x0,y0,x1,y1 = box
    draw = ImageDraw.Draw(img, "RGBA")
    n = len(points)
    step = (x1-x0)/(n-1)
    coords = [(x0+i*step, y1 - (y1-y0)*p) for i,p in enumerate(points)]
    poly = coords + [(x1,y1),(x0,y1)]
    draw.polygon(poly, fill=accent+(fill_alpha,))
    draw.line(coords, fill=accent, width=4, joint="curve")
    for cx,cy in [coords[-1]]:
        draw.ellipse([cx-6,cy-6,cx+6,cy+6], fill=(255,255,255))
        draw.ellipse([cx-6,cy-6,cx+6,cy+6], outline=accent, width=3)

def title_block(img, xy, eyebrow, headline, sub, color, eyebrow_color, sub_color):
    draw = ImageDraw.Draw(img)
    x,y = xy
    draw.text((x,y), eyebrow, font=font(FB,16), fill=eyebrow_color)
    draw.text((x,y+26), headline, font=font(FB,44), fill=color)
    draw.text((x,y+82), sub, font=font(FR,18), fill=sub_color)

def save(img, path):
    img.convert("RGB").save(path, "JPEG", quality=92)

# ---------------- 1. POWWR — energy / utilities, navy + teal ----------------
def powwr():
    bg1, bg2 = (10,22,38), (16,46,58)
    img = Image.new("RGBA", (W,H), bg1+(255,))
    draw = ImageDraw.Draw(img)
    vgrad(draw, [0,0,W,H], bg1, bg2)
    random.seed(1)
    for _ in range(40):
        x,y = random.randint(0,W), random.randint(0,H)
        r = random.randint(1,3)
        draw.ellipse([x,y,x+r,y+r], fill=(90,220,200,60))
    accent = (56,224,182)
    title_block(img, (90,120), "PRODUCT DESIGN LEAD  ·  B2B SAAS  ·  ENERGY & UTILITIES",
                "POWWR — Broker360", "Redesigning the quote-to-contract journey for energy brokers",
                (255,255,255), accent, (170,190,200))
    frame = browser_frame(img, [140,300,1460,860], (18,32,44), (245,247,248))
    body_top = nav_bar(img, [frame[0],frame[1],frame[2],frame[1]+64], (14,26,36), (255,255,255), "Broker360", ["Quotes","Contracts","Suppliers","Broker A."])
    bx0,by0,bx1,by1 = frame[0], body_top, frame[2], frame[3]
    draw.text((bx0+30, by0+24), "Live quote comparison", font=font(FB,20), fill=(24,30,40))
    stat_card(img, (bx0+30, by0+70), 220, 120, "Quote time", "4m 12s", accent, "down from 2h 40m avg")
    stat_card(img, (bx0+270, by0+70), 220, 120, "Contract errors", "1.2%", (255,138,80), "down from 9.4%")
    stat_card(img, (bx0+510, by0+70), 220, 120, "Broker adoption", "87%", (90,140,255), "up from 51%")
    line_chart(img, [bx0+30, by0+230, bx1-30, by0+300], accent, [0.2,0.35,0.3,0.5,0.45,0.7,0.65,0.85,0.8,0.95])
    save(img, "powwr_banner.jpg")

# ---------------- 2. Vodafone — red/black, scale telecom ----------------
def vodafone():
    bg1, bg2 = (18,18,20), (40,10,14)
    img = Image.new("RGBA", (W,H), bg1+(255,))
    draw = ImageDraw.Draw(img)
    vgrad(draw, [0,0,W,H], bg1, bg2)
    accent = (233,0,26)
    random.seed(2)
    cx,cy = 1400, 700
    for r in range(60, 900, 44):
        draw.arc([cx-r,cy-r,cx+r,cy+r], 190, 350, fill=(233,0,26,50), width=3)
    title_block(img, (90,120), "PRODUCT DESIGN LEAD  ·  B2C & B2B2C  ·  TELECOMS AT SCALE",
                "Vodafone — My Vodafone", "Making self-service the confident default over the call centre",
                (255,255,255), accent, (200,190,192))
    frame = browser_frame(img, [140,300,1460,860], (26,20,21), (250,247,247))
    body_top = nav_bar(img, [frame[0],frame[1],frame[2],frame[1]+64], (16,10,11), (255,255,255), "Vodafone", ["Plan","Billing","Devices","Support"])
    bx0,by0,bx1,by1 = frame[0], body_top, frame[2], frame[3]
    draw.text((bx0+30, by0+24), "Your account", font=font(FB,20), fill=(24,30,40))
    stat_card(img, (bx0+30, by0+70), 220, 120, "Call-centre contacts", "-31%", accent, "for redesigned tasks")
    stat_card(img, (bx0+270, by0+70), 220, 120, "Self-service completion", "+22pt", (233,0,26), "vs prior flow")
    stat_card(img, (bx0+510, by0+70), 220, 120, "App NPS", "+14", (90,140,255), "same measurement window")
    for i in range(4):
        x = bx0+30+i*(bx1-bx0-60)//4
        rrect(draw, [x, by0+230, x+ (bx1-bx0-60)//4-16, by0+300], 12, fill=(255,255,255))
        draw.text((x+16, by0+248), ["Plan","Billing","Roaming","Devices"][i], font=font(FR,14), fill=(90,20,25))
    save(img, "vodafone_banner.jpg")

# ---------------- 3. ClearScore — purple/teal, fintech consumer ----------------
def clearscore():
    bg1, bg2 = (12,10,32), (22,14,52)
    img = Image.new("RGBA", (W,H), bg1+(255,))
    draw = ImageDraw.Draw(img)
    vgrad(draw, [0,0,W,H], bg1, bg2)
    accent = (0,214,180)
    purple = (124,92,255)
    title_block(img, (90,120), "PRODUCT DESIGN LEAD  ·  B2C  ·  FINTECH · 0-TO-1 → SCALE",
                "ClearScore", "Recommendations that read as advice, not advertising",
                (255,255,255), accent, (190,185,220))
    frame = browser_frame(img, [140,300,1460,860], (24,18,46), (247,247,252))
    body_top = nav_bar(img, [frame[0],frame[1],frame[2],frame[1]+64], (16,12,34), (255,255,255), "ClearScore", ["Score","Reports","Marketplace","Profile"])
    bx0,by0,bx1,by1 = frame[0], body_top, frame[2], frame[3]
    # credit score dial
    cx, cy, r = bx0+130, by0+150, 90
    draw.arc([cx-r,cy-r,cx+r,cy+r], 150, 390, fill=(225,225,235), width=18)
    draw.arc([cx-r,cy-r,cx+r,cy+r], 150, 150+240*0.78, fill=purple, width=18)
    draw.text((cx-38,cy-18), "812", font=font(FB,34), fill=(40,30,70))
    draw.text((cx-30,cy+18), "Excellent", font=font(FR,13), fill=(120,120,140))
    draw.text((bx0+280, by0+40), "Matched for you", font=font(FB,18), fill=(30,24,60))
    for i in range(2):
        y = by0+80+i*95
        rrect(draw, [bx0+280, y, bx1-30, y+80], 14, fill=(255,255,255))
        draw.text((bx0+305, y+16), ["Balance transfer card","Personal loan · 6.4% rep APR"][i], font=font(FB,15), fill=(30,24,60))
        draw.text((bx0+305, y+42), ["87% approval likelihood for your profile","Eligibility checked without affecting your score"][i], font=font(FR,12), fill=(120,120,140))
    stat_card(img, (bx0+30, by0+260), 220, 100, "Click-through", "+41%", accent, "eligibility-first layout")
    stat_card(img, (bx0+270, by0+260), 220, 100, "Approved apps", "+18%", purple, "vs incumbent banner")
    save(img, "clearscore_banner.jpg")

# ---------------- 4. OANDA — dark navy/orange, trading ----------------
def oanda():
    bg1, bg2 = (8,14,24), (10,26,40)
    img = Image.new("RGBA", (W,H), bg1+(255,))
    draw = ImageDraw.Draw(img)
    vgrad(draw, [0,0,W,H], bg1, bg2)
    accent = (255,140,42)
    blue = (60,150,255)
    title_block(img, (90,120), "PRODUCT DESIGN LEAD  ·  B2C & B2B  ·  FX / TRADING",
                "OANDA — Trade Web", "Density that scales with expertise, not a compromise for everyone",
                (255,255,255), accent, (170,190,210))
    frame = browser_frame(img, [140,300,1460,860], (12,20,32), (16,24,36))
    body_top = nav_bar(img, [frame[0],frame[1],frame[2],frame[1]+64], (8,14,24), (230,236,245), "OANDA Trade", ["EUR/USD","Watchlist","Orders","Account"])
    bx0,by0,bx1,by1 = frame[0], body_top, frame[2], frame[3]
    rrect(draw, [bx0+30,by0+20,bx1-260,by0+300], 14, fill=(14,22,34))
    draw.text((bx0+50, by0+34), "EUR / USD", font=font(FB,18), fill=(230,236,245))
    draw.text((bx0+50, by0+58), "1.0932", font=font(FB,26), fill=accent)
    line_chart(img, [bx0+50, by0+100, bx1-280, by0+280], blue, [0.5,0.55,0.48,0.6,0.7,0.62,0.75,0.8,0.72,0.85,0.9])
    rrect(draw, [bx1-230,by0+20,bx1-30,by0+300], 14, fill=(14,22,34))
    draw.text((bx1-210, by0+34), "Order ticket", font=font(FB,15), fill=(230,236,245))
    for i,(label,val,c) in enumerate([("Buy","1.0932",(60,200,120)),("Sell","1.0930",(233,80,80))]):
        y = by0+70+i*46
        rrect(draw, [bx1-210,y,bx1-50,y+36], 8, fill=c)
        draw.text((bx1-195,y+8), f"{label}  {val}", font=font(FB,14), fill=(255,255,255))
    stat_card(img, (bx0+30, by0+320), 220, 100, "Time-to-first-trade", "-38%", accent, "new users")
    stat_card(img, (bx0+270, by0+320), 220, 100, "Pro session depth", "+12%", blue, "unchanged density")
    stat_card(img, (bx0+510, by0+320), 220, 100, "Execution tickets", "-27%", (150,200,255), "support volume")
    save(img, "oanda_banner.jpg")

powwr(); vodafone(); clearscore(); oanda()
print("done")
