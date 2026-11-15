from pathlib import Path

models = [
    ('DP2C','CS-DP2C',16.5,115.5,85.5,24.5,'https://www.ezviz.com/uk/product/DP2C-GLD/62467','ezviz-dp2c-1080p-smart-door-viewer-with-4-3-inch-screen'),
    ('DP2 2K','CS-DP2-R100-6E3WPFBS',14,115.5,85.5,24.5,'https://www.ezviz.com/product/dp2-2k/47961','ezviz-dp2-2k-smart-door-viewer-with-4-3-inch-touch-screen'),
    ('EP4','CS-EP4',14,103,142.4,28.4,'https://m.ezviz.com/product/ep4/70199','ezviz-ep4-4k-smart-door-viewer-touch-screen'),
]
base = 'https://elechid.github.io/smart-peephole-fit-checker/'
for zh in (False, True):
    def t(a,b):
        return a if zh else b
    title = t('電子貓眼門孔檢查器','Smart peephole fit checker')
    lang = t('zh-Hant-HK','en-HK')
    store = 'https://elechid.com'+t('','/en')
    intro = t('比較 EZVIZ DP2C、DP2 2K 和 EP4 的門厚、現有孔徑及門背空間。未量度的欄位可以留空。','Compare door thickness, existing hole diameter and indoor space for EZVIZ DP2C, DP2 2K and EP4. Leave unmeasured fields blank.')
    numeric = ''.join(f'<label>{label}<input type="number" inputmode="decimal" min="0" step="any" id="{key}"></label>' for key,label in [
        ('thickness',t('貓眼孔位置的門厚（毫米）','Door thickness at the peephole (mm)')),
        ('hole',t('拆出舊貓眼後的通孔直徑（毫米）','Clear hole diameter after removing the old viewer (mm)')),
        ('depth',t('門背開合時的最小淨深（毫米）','Shallowest indoor clearance through the door swing (mm)')),
    ])
    articles = []
    for model,sku,hole,a,b,depth,source,product in models:
        options = ''.join(f'<option value="{key}">{label}</option>' for key,label in [
            ('',t('未核對','Not checked')),
            ('yes',t('放得下，可裝拆及充電','Fits with room for fitting, removal and charging')),
            ('no',t('有遮擋或沒有操作空間','Obstructed or insufficient working room')),
        ])
        articles.append(f'''<article data-hole-min="{hole}" data-depth="{depth}">
<h2>EZVIZ {model}</h2><p class="sku">{sku}</p>
<dl>
<dt>{t('門厚','Door thickness')}</dt><dd>35–105 mm <output data-result="thickness">{t('待量度','Measure to confirm')}</output></dd>
<dt>{t('孔徑','Hole diameter')}</dt><dd>{hole}–50 mm <output data-result="hole">{t('待量度','Measure to confirm')}</output></dd>
<dt>{t('門背空間','Indoor space')}</dt><dd>{t('屏幕連底座','Screen and base')}: {a} × {b} × {depth} mm <output data-result="space">{t('待量度','Measure to confirm')}</output></dd>
</dl>
<label>{t('按此型號底座定位核對牆、門框、門鎖和充電線','Check the frame, wall, lock and charging cable against this model’s mounting position')}<select>{options}</select></label>
<p class="links"><a href="{source}">{t('EZVIZ 原廠規格','EZVIZ specifications')}</a> · <a href="{store}/products/{product}">{t('Elechid 商品頁','Elechid product page')}</a></p>
</article>''')
    file = t('zh.html','index.html')
    (Path(__file__).parent/file).write_text(f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Elechid 音立</title>
<meta name="description" content="{intro}">
<link rel="canonical" href="{base+t('zh.html','')}">
<link rel="alternate" hreflang="en-HK" href="{base}">
<link rel="alternate" hreflang="zh-Hant-HK" href="{base}zh.html">
<link rel="stylesheet" href="style.css"><script type="module" src="app.mjs"></script>
</head>
<body>
<header><nav><a href="{store}/">Elechid 音立</a><a href="{t('./','zh.html')}" lang="{t('en','zh-Hant')}">{t('English','繁體中文')}</a></nav></header>
<main><h1>{title}</h1><p>{intro}</p>
<p>{t('三款門厚均為 35–105 毫米。若實量孔徑 15 毫米，DP2 2K 和 EP4 的孔徑符合，DP2C 則需要至少 16.5 毫米。','All three accept doors 35–105 mm thick. A measured 15 mm hole passes the diameter check for DP2 2K and EP4. DP2C needs at least 16.5 mm.')}</p>
<section class="measure" aria-label="{t('門身量度','Door measurements')}">{numeric}</section>
<p class="hint">{t('EZVIZ 公布的是屏幕連底座外形尺寸。用實機或按安裝圖定位，沿開門全程量門背至最近障礙物，並核對屏幕可裝拆、線材有空間。尺寸剛好等於機身厚度時仍須確認。','EZVIZ lists the screen and base dimensions. Use the actual unit or mounting diagram to locate it, measure the nearest obstruction through the full swing, and check room to fit, remove and charge the screen. Clearance equal to the unit depth still requires confirmation.')}</p>
<div class="cards">{chr(10).join(articles)}</div>
</main><footer><a href="https://github.com/Elechid/smart-peephole-fit-checker">{t('原始碼','Source code')}</a> · <a href="https://github.com/Elechid">{t('Elechid 工具索引','Elechid tool index')}</a></footer>
</body></html>
''',encoding='utf-8')
