# -*- coding: utf-8 -*-
import os, sys, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from copy import TARGETS, cards
from shell import build

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAMES = {'cute-pop':'파스텔 낙서', 'cute-bubble':'만화 말풍선',
         'chic-bold':'대형 타이포', 'chic-mono':'모던 미니멀',
         'calm-beige':'베이지 에디토리얼', 'calm-deep':'딥톤 정숙'}
MOODS = {'cute-pop':'귀여움','cute-bubble':'귀여움','chic-bold':'세련','chic-mono':'세련',
         'calm-beige':'정적','calm-deep':'정적'}

for f in os.listdir(OUT):
    if f.endswith('.html'):
        os.remove(os.path.join(OUT, f))

made = []
for t in TARGETS:
    vers = (t['pick'],) if t.get('pick') else (1, 2)
    for v in vers:
        sty = t['styles'][v-1]
        cs = cards(t['code'], v)
        # ── 강아지 컷아웃은 흐름에 맞춰 3장에만 ──────────────
        #    1장 후킹 / 6장 학원 소개 / 마지막 상담 CTA
        hook, merit, closing = t['dogs']
        hook_only = t.get('dog_mode') == 'hook'
        for c in cs:
            if c['t'] == 'hook':                           c['dog'] = hook
            elif hook_only:                                pass
            elif c.get('slot') == 'merit':                 c['dog'] = merit
            elif c['t'] == 'cta':                          c['dog'] = closing
        fn = '%s_시안%d-%s.html' % (t['slug'], v, NAMES[sty])
        io.open(os.path.join(OUT, fn), 'w', encoding='utf-8').write(
            build(target='%s. %s' % (t['code'], t['name']), idx=v, style=sty,
                  style_name=NAMES[sty], mood=MOODS[sty], theme=t['theme'], cards=cs,
                  prefix='%s_시안%d' % (t['slug'], v),
                  title='%s · 시안%d (%s)' % (t['name'], v, NAMES[sty]),
                  foot=t.get('foot', 'go24')))
        dogs = sum(1 for c in cs if c.get('dog'))
        made.append((fn, t, v, NAMES[sty], MOODS[sty], len(cs), bool(t.get('pick'))))
        print('✓ %-44s %dKB · 강아지 %d장' % (fn, os.path.getsize(os.path.join(OUT, fn))//1024, dogs))

rows = ''
cur = None
for fn, t, v, sname, mood, n, fixed in made:
    if cur != t['code']:
        cur = t['code']
        rows += '<h2>%s. %s <em>%s</em>%s</h2><div class="grid">' % (
            t['code'], t['name'], t['mood'], '<b class="fix">확정</b>' if fixed else '')
    th = t['theme']
    sw = th['dark'] if 'deep' in fn or '딥톤' in sname else (th['beige'] if '베이지' in sname else (th['deep'] if '타이포' in sname else th['soft']))
    rows += ('<a class="it" href="./%s"><span class="sw" style="background:%s;border-color:%s"></span>'
             '<span class="tx"><b>시안%d · %s</b><small>%s · %d장</small></span>'
             '<span class="go">열기 &rsaquo;</span></a>') % (fn, sw, th['ac'], v, sname, mood, n)
    rows += '</div>' if (fixed or v == 2) else ''
index = """<!doctype html><html lang="ko"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/><title>애견국비 광고 시안</title><style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#121419;color:#E8EAEE;font-family:'Pretendard','Apple SD Gothic Neo',sans-serif;padding:34px 20px 70px}
h1{font-size:21px;font-weight:900;letter-spacing:-.03em}
p.s{margin-top:8px;color:#858B97;font-size:13px;line-height:1.75}
h2{margin:26px 0 9px;font-size:14px;font-weight:800;letter-spacing:-.02em}
h2 b.fix{font-size:11px;font-weight:800;color:#0E1016;background:#8FE3A8;
  padding:3px 9px;border-radius:999px;margin-left:6px}
h2 em{font-style:normal;font-size:11.5px;font-weight:700;color:#8FA3C8;background:#232A36;
  padding:3px 9px;border-radius:999px;margin-left:7px}
.moods{margin-top:18px;display:flex;gap:8px;flex-wrap:wrap}
.moods span{font-size:11.5px;font-weight:700;padding:6px 12px;border-radius:999px;background:#1E222A;
  border:1px solid #2A2E37;color:#B6BDCA}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:9px;max-width:1160px}
.it{display:flex;align-items:center;gap:13px;padding:13px 15px;border:1px solid #2A2E37;border-radius:12px;
  background:#1A1D23;text-decoration:none;color:inherit}
.it:hover{border-color:#5B7CFA;background:#20242C}
.sw{width:36px;height:36px;border-radius:10px;flex:none;border:3px solid}
.tx{flex:1;min-width:0}.tx b{display:block;font-size:13px;font-weight:800}
.tx small{color:#858B97;font-size:11.5px}
.go{color:#5B7CFA;font-size:12px;font-weight:800;flex:none}
.note{margin-top:26px;max-width:1160px;padding:15px 17px;border:1px solid #3A3320;background:#241F12;
  border-radius:11px;font-size:12.5px;line-height:1.85;color:#D8C9A0}
</style></head><body>
<h1>애견국비 · Meta 광고 카드뉴스 시안</h1>
<p class="s">한국반려동물전문학원 · 반려동물행동지도사 2급 국비지원 과정 · 경남 양산 · 11월 개강<br/>
타깃 8종 &times; 시안 2개 = 16세트 (각 7장). 파일 하나하나가 독립 실행됩니다 — 더블클릭해서 바로 여세요.</p>
<div class="moods"><span>무드 3갈래 · 디자인 6종</span><span>귀여움 — 파스텔 낙서 / 만화 말풍선</span>
<span>세련 — 대형 타이포 / 모던 미니멀</span><span>정적 — 베이지 에디토리얼 / 딥톤 정숙</span></div>
%s
<div class="note"><b>강아지 컷아웃</b>은 흐름에 맞춰 <b>후킹 · 학원 소개 · 마무리 상담</b> 세 장에만 넣었습니다.
자격 · 교육비 · 목록 카드는 정보 전달에 집중하도록 사진을 뺐습니다.<br/>
<b>확정</b> 표시된 타깃은 고르신 시안만 남겨 두었습니다.<br/>
<b>고용24 로고</b>는 「국민내일배움카드 국비지원 과정」 안내 용도로만 썼습니다. 정부 후원·승인으로 읽히지 않게 문구를 바꾸지 마세요.</div>
</body></html>""" % rows
io.open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(index)
print('\n총', len(made), '개 + index.html')
