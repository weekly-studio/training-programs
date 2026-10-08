# -*- coding: utf-8 -*-
"""무드 3갈래 × 2종 = 디자인 6종
   귀여움: cute-pop(파스텔 낙서) / cute-bubble(만화 말풍선)
   세련  : chic-bold(대형 타이포) / chic-mono(모던 미니멀)
   정적  : calm-beige(베이지 에디토리얼) / calm-deep(딥톤 정숙)"""

APP_CSS = r"""
*{margin:0;padding:0;box-sizing:border-box}
body{background:#121419;font-family:'Pretendard','Apple SD Gothic Neo','Noto Sans KR',sans-serif;color:#E8EAEE}
.bar{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:10px;flex-wrap:wrap;
  padding:12px 18px;background:#1A1D23;border-bottom:1px solid #2A2E37}
.bar h1{font-size:15px;font-weight:800;letter-spacing:-.02em}
.bar .tag{font-size:11px;font-weight:700;padding:4px 10px;border-radius:999px;background:#2A2E37;color:#AAB0BC}
.bar .mood{background:#2E3A4E;color:#A8C4F0}
.bar .sp{flex:1}
.btn{background:#2A2E37;color:#E8EAEE;border:1px solid #383D47;padding:8px 14px;border-radius:9px;
  cursor:pointer;font:600 12px/1 inherit;font-family:inherit}
.btn:hover{background:#343A45}.btn.on{background:#5B7CFA;border-color:#5B7CFA;color:#0E1016}
.wrap{display:flex;flex-direction:column;align-items:center;gap:22px;padding:26px 16px 60px}
.slot{position:relative}
.slot .cap{position:absolute;left:2px;top:-18px;font-size:11px;color:#858B97;font-weight:700}
.holder{transform-origin:top left;box-shadow:0 14px 40px rgba(0,0,0,.45)}
.toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%) translateY(18px);background:#2A2E37;
  border:1px solid #383D47;padding:10px 18px;border-radius:10px;font-size:12.5px;opacity:0;
  pointer-events:none;transition:.2s;z-index:50}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
"""

CARD_CSS = r"""
.card,.card *{margin:0;padding:0;box-sizing:border-box}
.card{position:relative;overflow:hidden;font-family:var(--ff);-webkit-font-smoothing:antialiased;
  background:var(--bg);color:var(--fg)}
.card img{display:block}
.card .hl{color:var(--ac)}
.card .in{position:relative;z-index:3;height:100%;display:flex;flex-direction:column}
.card .hdr{display:flex;align-items:center;gap:calc(var(--u)*12)}
.card .hdr .kda{width:calc(var(--u)*50);height:calc(var(--u)*50);object-fit:contain;flex:none}
.card .hdr .nm{font-size:calc(var(--u)*22);font-weight:800;letter-spacing:-.02em}
.card .hdr .pg{margin-left:auto;font-size:calc(var(--u)*20);font-weight:800;letter-spacing:.1em;opacity:.55}
.card .bd{flex:1;display:flex;flex-direction:column;justify-content:center}
.card .dog{position:absolute;z-index:2;pointer-events:none}
.card .gobar{display:flex;align-items:center;gap:calc(var(--u)*11);
  font-size:calc(var(--u)*20);font-weight:800}
.card .gobar img{height:calc(var(--u)*26);object-fit:contain}
.card .note{font-size:calc(var(--u)*18);line-height:1.6;font-weight:600;opacity:.72;word-break:keep-all}
.card .sub,.card .txt{font-size:calc(var(--u)*28);line-height:1.76;font-weight:600;word-break:keep-all}
.card .ttl{font-weight:900;letter-spacing:-.04em;word-break:keep-all}
.card .ttl .hl{background:#fff;border-radius:calc(var(--u)*12);
  padding:calc(var(--u)*4) calc(var(--u)*13);
  -webkit-box-decoration-break:clone;box-decoration-break:clone;
  box-shadow:0 calc(var(--u)*2) calc(var(--u)*9) rgba(0,0,0,.07)}
.card .lst{list-style:none}
.card .lst li{word-break:keep-all}
.card .rows .v,.card .steps .sd{word-break:keep-all}

/* ═══════ 귀여움 ① cute-pop — 파스텔 낙서 ═══════════════════ */
.cute-pop{background:var(--bg)}
.cute-pop .blob{position:absolute;border-radius:50% 46% 54% 48%/48% 52% 46% 54%;z-index:1}
.cute-pop .b1{width:calc(var(--u)*430);height:calc(var(--u)*380);left:calc(var(--u)*-110);top:calc(var(--u)*-90);
  background:var(--soft)}
.cute-pop .b2{width:calc(var(--u)*330);height:calc(var(--u)*300);right:calc(var(--u)*-90);bottom:calc(var(--u)*-70);
  background:var(--soft);opacity:.8}
.cute-pop .dood{position:absolute;z-index:2}
.cute-pop .dood svg{width:100%;height:100%;fill:var(--ac)}
.cute-pop .dd1{width:calc(var(--u)*44);height:calc(var(--u)*44);right:calc(var(--u)*120);top:calc(var(--u)*130);opacity:.85}
.cute-pop .dd2{width:calc(var(--u)*28);height:calc(var(--u)*28);right:calc(var(--u)*196);top:calc(var(--u)*196);opacity:.6}
.cute-pop .dd3{width:calc(var(--u)*54);height:calc(var(--u)*54);left:calc(var(--u)*62);bottom:calc(var(--u)*150);
  opacity:.28;fill:var(--deep)}
.cute-pop .in{padding:calc(var(--u)*54) calc(var(--u)*58) calc(var(--u)*50)}
.cute-pop .hdr .nm{color:var(--deep)}
.cute-pop .hdr .pg{color:var(--deep)}
.cute-pop .bd{padding-top:calc(var(--u)*10)}
.cute-pop .eye{align-self:flex-start;background:var(--ac);color:#fff;font-size:calc(var(--u)*22);
  font-weight:900;padding:calc(var(--u)*10) calc(var(--u)*22);border-radius:999px}
.cute-pop .ttl{margin-top:calc(var(--u)*24);font-size:calc(var(--u)*68);line-height:1.36;color:var(--fg)}
.cute-pop .ttl .hl{color:var(--deep)}
.cute-pop .sub,.cute-pop .txt{margin-top:calc(var(--u)*22);color:var(--fg);opacity:.72}
.cute-pop .lst{margin-top:calc(var(--u)*24);display:flex;flex-direction:column;gap:calc(var(--u)*12)}
.cute-pop .lst li{display:flex;gap:calc(var(--u)*14);align-items:flex-start;background:#fff;
  border-radius:calc(var(--u)*20);padding:calc(var(--u)*18) calc(var(--u)*20);
  font-size:calc(var(--u)*26);font-weight:700;line-height:1.5;
  box-shadow:0 calc(var(--u)*4) calc(var(--u)*12) rgba(60,40,30,.06)}
.cute-pop .lst .ck{flex:none;width:calc(var(--u)*30);height:calc(var(--u)*30);border-radius:999px;
  background:var(--ac);display:flex;align-items:center;justify-content:center;margin-top:calc(var(--u)*2)}
.cute-pop .lst .ck svg{width:calc(var(--u)*16);height:calc(var(--u)*16);fill:none;stroke:#fff;stroke-width:3.6;
  stroke-linecap:round;stroke-linejoin:round}
.cute-pop .rows{margin-top:calc(var(--u)*22);display:flex;flex-direction:column;gap:calc(var(--u)*12)}
.cute-pop .rows .r{background:#fff;border-radius:calc(var(--u)*20);padding:calc(var(--u)*18) calc(var(--u)*20);
  display:flex;align-items:center;gap:calc(var(--u)*14);
  box-shadow:0 calc(var(--u)*4) calc(var(--u)*12) rgba(60,40,30,.06)}
.cute-pop .rows .k{flex:none;background:var(--soft);color:var(--deep);font-size:calc(var(--u)*19);
  font-weight:900;padding:calc(var(--u)*7) calc(var(--u)*14);border-radius:999px}
.cute-pop .rows .v{flex:1;font-size:calc(var(--u)*25);font-weight:800;line-height:1.5}
.cute-pop .steps{margin-top:calc(var(--u)*20);display:flex;flex-direction:column;gap:calc(var(--u)*16)}
.cute-pop .steps .s{display:flex;gap:calc(var(--u)*15);align-items:flex-start}
.cute-pop .steps .n{flex:none;width:calc(var(--u)*40);height:calc(var(--u)*40);border-radius:999px;
  background:var(--ac);color:#fff;font-weight:900;font-size:calc(var(--u)*21);
  display:flex;align-items:center;justify-content:center}
.cute-pop .steps .sh{display:block;font-size:calc(var(--u)*26);font-weight:900}
.cute-pop .steps .sd{display:block;margin-top:calc(var(--u)*4);font-size:calc(var(--u)*22);opacity:.68;
  font-weight:600;line-height:1.55}
.cute-pop .pill{align-self:flex-start;margin-top:calc(var(--u)*28);background:var(--deep);color:#fff;
  font-size:calc(var(--u)*26);font-weight:900;padding:calc(var(--u)*18) calc(var(--u)*34);border-radius:999px}
.cute-pop .big{margin-top:calc(var(--u)*22);text-align:center;background:var(--ac);color:#fff;
  font-size:calc(var(--u)*30);font-weight:900;padding:calc(var(--u)*24);border-radius:calc(var(--u)*22)}
.cute-pop .note{margin-top:calc(var(--u)*16);color:var(--fg)}
.cute-pop .ftr{display:flex;justify-content:center;margin-top:calc(var(--u)*18)}
.cute-pop .gobar{background:#fff;border-radius:999px;padding:calc(var(--u)*9) calc(var(--u)*18);color:var(--deep)}
.cute-pop .dog{right:0;bottom:0;width:calc(var(--u)*380)}
.cute-pop.t-hook .dog{width:calc(var(--u)*410)}
.cute-pop.t-list .dog{width:calc(var(--u)*215);right:calc(var(--u)*8);bottom:0}
.cute-pop.t-cta .dog{width:calc(var(--u)*195);right:calc(var(--u)*10);bottom:calc(var(--u)*74)}

/* ═══════ 귀여움 ② cute-bubble — 만화 말풍선 ═══════════════ */
.cute-bubble{background:var(--soft)}
.cute-bubble .band{position:absolute;left:0;right:0;z-index:1;background:var(--ac)}
.cute-bubble .bt{top:0;height:calc(var(--u)*18)}
.cute-bubble .bb{bottom:0;height:calc(var(--u)*18)}
.cute-bubble .in{padding:calc(var(--u)*56) calc(var(--u)*54) calc(var(--u)*54)}
.cute-bubble .hdr .nm,.cute-bubble .hdr .pg{color:var(--deep)}
.cute-bubble .bub{position:relative;background:#fff;border:calc(var(--u)*5) solid var(--fg);
  border-radius:calc(var(--u)*28);padding:calc(var(--u)*26) calc(var(--u)*30);
  box-shadow:calc(var(--u)*8) calc(var(--u)*8) 0 var(--deep)}
.cute-bubble .bub:after{content:'';position:absolute;left:calc(var(--u)*54);bottom:calc(var(--u)*-26);
  width:0;height:0;border-left:calc(var(--u)*24) solid transparent;border-right:calc(var(--u)*10) solid transparent;
  border-top:calc(var(--u)*26) solid var(--fg)}
.cute-bubble .eye{align-self:flex-start;background:var(--fg);color:#fff;font-size:calc(var(--u)*21);
  font-weight:900;padding:calc(var(--u)*9) calc(var(--u)*20);border-radius:calc(var(--u)*10);
  transform:rotate(-2deg)}
.cute-bubble .ttl{margin-top:calc(var(--u)*20);font-size:calc(var(--u)*64);line-height:1.34;color:var(--fg)}
.cute-bubble .ttl .hl{color:var(--deep);background:var(--soft);box-shadow:none}
.cute-bubble .sub,.cute-bubble .txt{margin-top:calc(var(--u)*18);color:var(--fg);opacity:.78}
.cute-bubble .lst{display:flex;flex-direction:column;gap:calc(var(--u)*11);margin-top:calc(var(--u)*6)}
.cute-bubble .lst li{display:flex;gap:calc(var(--u)*13);align-items:flex-start;font-size:calc(var(--u)*25);
  font-weight:800;line-height:1.5}
.cute-bubble .lst .ck{flex:none;width:calc(var(--u)*28);height:calc(var(--u)*28);border-radius:calc(var(--u)*9);
  background:var(--ac);display:flex;align-items:center;justify-content:center;margin-top:calc(var(--u)*2)}
.cute-bubble .lst .ck svg{width:calc(var(--u)*15);height:calc(var(--u)*15);fill:none;stroke:#fff;stroke-width:3.8;
  stroke-linecap:round;stroke-linejoin:round}
.cute-bubble .rows{display:flex;flex-direction:column;gap:calc(var(--u)*10)}
.cute-bubble .rows .r{display:flex;gap:calc(var(--u)*13);align-items:flex-start;
  padding:calc(var(--u)*11) 0;border-bottom:calc(var(--u)*3) dashed rgba(0,0,0,.12)}
.cute-bubble .rows .r:last-child{border-bottom:0}
.cute-bubble .rows .k{flex:none;width:calc(var(--u)*105);font-size:calc(var(--u)*21);font-weight:900;color:var(--deep)}
.cute-bubble .rows .v{flex:1;font-size:calc(var(--u)*25);font-weight:800;line-height:1.5}
.cute-bubble .steps{display:flex;flex-direction:column;gap:calc(var(--u)*14)}
.cute-bubble .steps .s{display:flex;gap:calc(var(--u)*14);align-items:flex-start}
.cute-bubble .steps .n{flex:none;width:calc(var(--u)*38);height:calc(var(--u)*38);border-radius:calc(var(--u)*12);
  background:var(--fg);color:#fff;font-weight:900;font-size:calc(var(--u)*20);
  display:flex;align-items:center;justify-content:center}
.cute-bubble .steps .sh{display:block;font-size:calc(var(--u)*25);font-weight:900}
.cute-bubble .steps .sd{display:block;margin-top:calc(var(--u)*3);font-size:calc(var(--u)*21);opacity:.7;font-weight:600}
.cute-bubble .pill{align-self:flex-start;margin-top:calc(var(--u)*26);background:var(--ac);color:#fff;
  border:calc(var(--u)*4) solid var(--fg);box-shadow:calc(var(--u)*6) calc(var(--u)*6) 0 var(--fg);
  font-size:calc(var(--u)*25);font-weight:900;padding:calc(var(--u)*15) calc(var(--u)*30);border-radius:999px}
.cute-bubble .big{margin-top:calc(var(--u)*18);text-align:center;background:var(--ac);color:#fff;
  border:calc(var(--u)*5) solid var(--fg);box-shadow:calc(var(--u)*8) calc(var(--u)*8) 0 var(--fg);
  font-size:calc(var(--u)*29);font-weight:900;padding:calc(var(--u)*22);border-radius:calc(var(--u)*20)}
.cute-bubble .note{margin-top:calc(var(--u)*16);color:var(--fg)}
.cute-bubble .ftr{display:flex;justify-content:center;margin-top:calc(var(--u)*16)}
.cute-bubble .gobar{background:#fff;border:calc(var(--u)*3) solid var(--fg);border-radius:999px;
  padding:calc(var(--u)*8) calc(var(--u)*18);color:var(--fg)}
.cute-bubble .dog{right:calc(var(--u)*6);bottom:calc(var(--u)*22);width:calc(var(--u)*330)}
.cute-bubble.t-hook .dog{width:calc(var(--u)*360)}
.cute-bubble.t-list .dog{width:calc(var(--u)*200)}
.cute-bubble.t-cta .dog{width:calc(var(--u)*180);bottom:calc(var(--u)*88)}

/* ═══════ 세련 ① chic-bold — 대형 타이포 ═══════════════════ */
.chic-bold{background:var(--deep);color:#fff}
.chic-bold .in{padding:0}
.chic-bold .hdr{padding:calc(var(--u)*30) calc(var(--u)*50) calc(var(--u)*22);
  border-bottom:calc(var(--u)*2) solid rgba(255,255,255,.26)}
.chic-bold .hdr .kda{width:calc(var(--u)*44);height:calc(var(--u)*44)}
.chic-bold .hdr .nm{color:rgba(255,255,255,.95);font-size:calc(var(--u)*21)}
.chic-bold .hdr .pg{color:rgba(255,255,255,.72)}
.chic-bold .bd{padding:calc(var(--u)*46) calc(var(--u)*50) calc(var(--u)*20)}
.chic-bold .eye{align-self:flex-start;background:rgba(255,255,255,.16);color:#fff;
  border:calc(var(--u)*2) solid rgba(255,255,255,.4);font-size:calc(var(--u)*21);font-weight:800;
  padding:calc(var(--u)*9) calc(var(--u)*20);border-radius:calc(var(--u)*8);letter-spacing:.02em}
.chic-bold .ttl{margin-top:calc(var(--u)*26);font-size:calc(var(--u)*88);line-height:1.22;
  letter-spacing:-.05em;color:#fff}
.chic-bold .ttl .hl{color:var(--deep)}
.chic-bold .sub,.chic-bold .txt{margin-top:calc(var(--u)*24);color:rgba(255,255,255,.84)}
.chic-bold .lst{margin-top:calc(var(--u)*26)}
.chic-bold .lst li{display:flex;gap:calc(var(--u)*16);align-items:flex-start;
  padding:calc(var(--u)*18) 0;border-top:calc(var(--u)*2) solid rgba(255,255,255,.22);
  font-size:calc(var(--u)*26);font-weight:700;line-height:1.5;color:rgba(255,255,255,.95)}
.chic-bold .lst li:last-child{border-bottom:calc(var(--u)*2) solid rgba(255,255,255,.22)}
.chic-bold .lst .ck{flex:none;color:var(--ac2);font-size:calc(var(--u)*24);font-weight:900;
  min-width:calc(var(--u)*26)}
.chic-bold .rows{margin-top:calc(var(--u)*22);display:flex;flex-direction:column;gap:calc(var(--u)*11)}
.chic-bold .rows .r{background:#fff;color:var(--fg);border-radius:calc(var(--u)*16);
  padding:calc(var(--u)*18) calc(var(--u)*20);display:flex;align-items:center;gap:calc(var(--u)*14)}
.chic-bold .rows .k{flex:none;background:var(--deep);color:#fff;font-size:calc(var(--u)*18);font-weight:900;
  padding:calc(var(--u)*6) calc(var(--u)*13);border-radius:calc(var(--u)*7)}
.chic-bold .rows .v{flex:1;font-size:calc(var(--u)*25);font-weight:800;line-height:1.5}
.chic-bold .rows .v .hl{color:var(--deep)}
.chic-bold .steps{margin-top:calc(var(--u)*20);display:flex;flex-direction:column;gap:calc(var(--u)*16)}
.chic-bold .steps .s{display:flex;gap:calc(var(--u)*15);align-items:flex-start}
.chic-bold .steps .n{flex:none;width:calc(var(--u)*40);height:calc(var(--u)*40);border-radius:calc(var(--u)*11);
  background:var(--ac2);color:var(--deep);font-weight:900;font-size:calc(var(--u)*21);
  display:flex;align-items:center;justify-content:center}
.chic-bold .steps .sh{display:block;font-size:calc(var(--u)*26);font-weight:900;color:#fff}
.chic-bold .steps .sd{display:block;margin-top:calc(var(--u)*4);font-size:calc(var(--u)*22);
  color:rgba(255,255,255,.78);font-weight:600;line-height:1.55}
.chic-bold .pill{display:none}
.chic-bold .note{margin-top:calc(var(--u)*18);color:rgba(255,255,255,.7)}
.chic-bold .ftr{background:#fff;padding:calc(var(--u)*24) calc(var(--u)*50);display:flex;
  align-items:center;gap:calc(var(--u)*16)}
.chic-bold .ftr .cta{flex:1;background:var(--deep);color:#fff;text-align:center;border-radius:999px;
  font-size:calc(var(--u)*27);font-weight:900;padding:calc(var(--u)*19)}
.chic-bold .gobar{color:var(--fg);flex:none}
.chic-bold .ftr.ig{flex-direction:column;align-items:center;gap:calc(var(--u)*13);
  padding:calc(var(--u)*24) calc(var(--u)*50) calc(var(--u)*22)}
.chic-bold .ftr.ig .cta{flex:none;width:auto;padding:calc(var(--u)*18) calc(var(--u)*74)}
.chic-bold .ftr.ig .gobar{font-size:calc(var(--u)*19);opacity:.7}
.card .gobar.insta{align-items:center;gap:calc(var(--u)*9);font-weight:800;letter-spacing:.01em}
.card .gobar.insta svg{width:calc(var(--u)*26);height:calc(var(--u)*26);fill:none;stroke:currentColor;stroke-width:1.9}
.chic-bold .dog{right:calc(var(--u)*6);bottom:calc(var(--u)*112);width:calc(var(--u)*350);z-index:1}
.chic-bold.t-hook .dog{width:calc(var(--u)*390);bottom:calc(var(--u)*110)}
.chic-bold.t-list .dog,.chic-bold.t-cta .dog{width:calc(var(--u)*200);right:calc(var(--u)*10);bottom:calc(var(--u)*112)}

/* ═══════ 세련 ② chic-mono — 모던 미니멀 ═══════════════════ */
.chic-mono{background:var(--bg)}
.chic-mono .in{padding:calc(var(--u)*58) calc(var(--u)*62) calc(var(--u)*54)}
.chic-mono .hdr{padding-bottom:calc(var(--u)*20);border-bottom:calc(var(--u)*1) solid rgba(0,0,0,.16)}
.chic-mono .hdr .kda{width:calc(var(--u)*42);height:calc(var(--u)*42)}
.chic-mono .hdr .nm{font-size:calc(var(--u)*20);letter-spacing:0;opacity:.85}
.chic-mono .idx{position:absolute;right:calc(var(--u)*62);top:calc(var(--u)*150);
  font-size:calc(var(--u)*120);font-weight:900;color:var(--fg);opacity:.07;letter-spacing:-.06em;z-index:1}
.chic-mono .bd{padding-top:calc(var(--u)*34)}
.chic-mono .eye{align-self:flex-start;font-size:calc(var(--u)*21);font-weight:900;letter-spacing:.08em;
  line-height:1.5;color:var(--ac)}
.chic-mono .ttl{margin-top:calc(var(--u)*22);font-size:calc(var(--u)*62);line-height:1.34;color:var(--fg)}
.chic-mono .ttl .hl{color:var(--ac)}
.chic-mono .sub{margin-top:calc(var(--u)*20);font-size:calc(var(--u)*27);font-weight:800;opacity:.92}
.chic-mono .txt{margin-top:calc(var(--u)*20);opacity:.68}
.chic-mono .lst{margin-top:calc(var(--u)*26)}
.chic-mono .lst li{display:flex;gap:calc(var(--u)*18);align-items:flex-start;padding:calc(var(--u)*17) 0;
  border-top:calc(var(--u)*1) solid rgba(0,0,0,.14);font-size:calc(var(--u)*25);font-weight:700;line-height:1.5}
.chic-mono .lst li:last-child{border-bottom:calc(var(--u)*1) solid rgba(0,0,0,.14)}
.chic-mono .lst .ck{flex:none;color:var(--ac);font-size:calc(var(--u)*20);font-weight:900;
  min-width:calc(var(--u)*24);padding-top:calc(var(--u)*3)}
.chic-mono .rows{margin-top:calc(var(--u)*22)}
.chic-mono .rows .r{display:flex;gap:calc(var(--u)*18);align-items:flex-start;padding:calc(var(--u)*17) 0;
  border-top:calc(var(--u)*1) solid rgba(0,0,0,.14)}
.chic-mono .rows .r:last-child{border-bottom:calc(var(--u)*1) solid rgba(0,0,0,.14)}
.chic-mono .rows .k{flex:none;width:calc(var(--u)*116);font-size:calc(var(--u)*20);font-weight:900;
  color:var(--ac);letter-spacing:.02em;padding-top:calc(var(--u)*3)}
.chic-mono .rows .v{flex:1;font-size:calc(var(--u)*25);font-weight:800;line-height:1.5}
.chic-mono .steps{margin-top:calc(var(--u)*22)}
.chic-mono .steps .s{display:flex;gap:calc(var(--u)*18);align-items:flex-start;padding:calc(var(--u)*15) 0;
  border-top:calc(var(--u)*1) solid rgba(0,0,0,.14)}
.chic-mono .steps .s:last-child{border-bottom:calc(var(--u)*1) solid rgba(0,0,0,.14)}
.chic-mono .steps .n{flex:none;width:calc(var(--u)*36);font-size:calc(var(--u)*22);font-weight:900;color:var(--ac)}
.chic-mono .steps .sh{display:block;font-size:calc(var(--u)*25);font-weight:900}
.chic-mono .steps .sd{display:block;margin-top:calc(var(--u)*4);font-size:calc(var(--u)*22);opacity:.65;
  font-weight:600;line-height:1.55}
.chic-mono .pill{align-self:flex-start;margin-top:calc(var(--u)*28);border:calc(var(--u)*2) solid var(--fg);
  color:var(--fg);font-size:calc(var(--u)*25);font-weight:900;
  padding:calc(var(--u)*16) calc(var(--u)*32);border-radius:999px}
.chic-mono .big{margin-top:calc(var(--u)*24);text-align:center;background:var(--fg);color:var(--bg);
  font-size:calc(var(--u)*29);font-weight:900;padding:calc(var(--u)*23);border-radius:calc(var(--u)*6)}
.chic-mono .note{margin-top:calc(var(--u)*18)}
.chic-mono .ftr{margin-top:calc(var(--u)*20);padding-top:calc(var(--u)*18);
  border-top:calc(var(--u)*1) solid rgba(0,0,0,.14);display:flex;justify-content:flex-start}
.chic-mono .gobar{color:var(--fg);opacity:.8}
.chic-mono .dog{right:0;bottom:0;width:calc(var(--u)*330);z-index:1}
.chic-mono.t-hook .dog{width:calc(var(--u)*370)}
.chic-mono.t-list .dog{width:calc(var(--u)*195);right:calc(var(--u)*10)}
.chic-mono.t-cta .dog{width:calc(var(--u)*175);right:calc(var(--u)*10);bottom:calc(var(--u)*82)}

/* ═══════ 정적 ① calm-beige — 베이지 에디토리얼 ═══════════ */
.calm-beige{background:var(--beige);color:var(--bfg)}
.calm-beige .in{padding:calc(var(--u)*60) calc(var(--u)*72) calc(var(--u)*56);text-align:center}
.calm-beige .hdr{justify-content:center}
.calm-beige .hdr .kda{width:calc(var(--u)*46);height:calc(var(--u)*46)}
.calm-beige .hdr .nm{font-size:calc(var(--u)*20);font-weight:700;letter-spacing:.04em;opacity:.8}
.calm-beige .hdr .pg{position:absolute;right:calc(var(--u)*72);top:calc(var(--u)*66);margin:0;opacity:.45}
.calm-beige .bd{align-items:center;padding-top:calc(var(--u)*16)}
.calm-beige .eye{font-size:calc(var(--u)*20);font-weight:700;letter-spacing:.34em;opacity:.6}
.calm-beige .rule{width:calc(var(--u)*56);height:calc(var(--u)*1);background:currentColor;opacity:.4;
  margin:calc(var(--u)*22) 0 calc(var(--u)*4)}
.calm-beige .ttl{margin-top:calc(var(--u)*20);font-size:calc(var(--u)*58);line-height:1.46;font-weight:700;
  letter-spacing:-.02em;font-family:var(--ffs)}
.calm-beige .ttl .hl{color:var(--bac);font-weight:800;border-radius:calc(var(--u)*10)}
.calm-beige .sub,.calm-beige .txt{margin-top:calc(var(--u)*22);font-size:calc(var(--u)*26);
  line-height:1.9;font-weight:500;opacity:.78}
.calm-beige .lst{margin-top:calc(var(--u)*26);width:100%}
.calm-beige .lst li{display:flex;gap:calc(var(--u)*14);align-items:flex-start;justify-content:center;
  padding:calc(var(--u)*16) 0;border-top:calc(var(--u)*1) solid currentColor;
  font-size:calc(var(--u)*24);font-weight:600;line-height:1.6;text-align:left}
.calm-beige .lst li:last-child{border-bottom:calc(var(--u)*1) solid currentColor}
.calm-beige .lst .ck{flex:none;color:var(--bac);font-size:calc(var(--u)*19);font-weight:900;
  min-width:calc(var(--u)*22);padding-top:calc(var(--u)*4)}
.calm-beige .rows{margin-top:calc(var(--u)*24);width:100%}
.calm-beige .rows .r{display:flex;gap:calc(var(--u)*16);align-items:flex-start;text-align:left;
  padding:calc(var(--u)*16) 0;border-top:calc(var(--u)*1) solid currentColor}
.calm-beige .rows .r:last-child{border-bottom:calc(var(--u)*1) solid currentColor}
.calm-beige .rows .k{flex:none;width:calc(var(--u)*118);font-size:calc(var(--u)*20);font-weight:800;
  letter-spacing:.06em;opacity:.65;padding-top:calc(var(--u)*3)}
.calm-beige .rows .v{flex:1;font-size:calc(var(--u)*25);font-weight:700;line-height:1.55}
.calm-beige .steps{margin-top:calc(var(--u)*22);width:100%}
.calm-beige .steps .s{display:flex;gap:calc(var(--u)*16);align-items:flex-start;text-align:left;
  padding:calc(var(--u)*15) 0;border-top:calc(var(--u)*1) solid currentColor}
.calm-beige .steps .s:last-child{border-bottom:calc(var(--u)*1) solid currentColor}
.calm-beige .steps .n{flex:none;width:calc(var(--u)*34);font-size:calc(var(--u)*21);font-weight:800;color:var(--bac)}
.calm-beige .steps .sh{display:block;font-size:calc(var(--u)*25);font-weight:800}
.calm-beige .steps .sd{display:block;margin-top:calc(var(--u)*4);font-size:calc(var(--u)*22);opacity:.7;
  font-weight:500;line-height:1.6}
.calm-beige .pill{margin-top:calc(var(--u)*30);border:calc(var(--u)*1) solid currentColor;
  font-size:calc(var(--u)*24);font-weight:700;letter-spacing:.06em;
  padding:calc(var(--u)*16) calc(var(--u)*34);border-radius:0}
.calm-beige .big{margin-top:calc(var(--u)*24);width:100%;text-align:center;background:var(--bfg);
  color:var(--beige);font-size:calc(var(--u)*28);font-weight:800;padding:calc(var(--u)*22);letter-spacing:.02em}
.calm-beige .note{margin-top:calc(var(--u)*18);font-weight:500}
.calm-beige .ftr{display:flex;justify-content:center;margin-top:calc(var(--u)*18)}
.calm-beige .gobar{opacity:.75;font-weight:700;letter-spacing:.02em}
.calm-beige .dog{left:50%;transform:translateX(-50%);bottom:0;width:calc(var(--u)*340);z-index:1}
.calm-beige.t-hook .dog{width:calc(var(--u)*370);bottom:0}
.calm-beige.t-hook .bd{padding-bottom:calc(var(--u)*330)}
.calm-beige.t-text .bd{padding-bottom:calc(var(--u)*300)}
.calm-beige.t-list .dog{width:calc(var(--u)*180);left:auto;right:calc(var(--u)*10);transform:none;bottom:0}
.calm-beige.t-cta .dog{width:calc(var(--u)*165);left:auto;right:calc(var(--u)*12);transform:none;
  bottom:calc(var(--u)*70)}

/* ═══════ 정적 ② calm-deep — 딥톤 정숙 ════════════════════ */
.calm-deep{background:var(--dark);color:#F2EFE8}
.calm-deep .in{padding:calc(var(--u)*56) calc(var(--u)*60) calc(var(--u)*52)}
.calm-deep .hdr .kda{width:calc(var(--u)*46);height:calc(var(--u)*46)}
.calm-deep .hdr .nm{color:rgba(242,239,232,.9);font-size:calc(var(--u)*21);font-weight:700;letter-spacing:.02em}
.calm-deep .hdr .pg{color:rgba(242,239,232,.5)}
.calm-deep .bd{padding-top:calc(var(--u)*20)}
.calm-deep .eye{align-self:flex-start;font-size:calc(var(--u)*20);font-weight:800;letter-spacing:.26em;
  color:var(--gold)}
.calm-deep .rule{width:calc(var(--u)*70);height:calc(var(--u)*1);background:var(--gold);opacity:.6;
  margin-top:calc(var(--u)*18)}
.calm-deep .ttl{margin-top:calc(var(--u)*26);font-size:calc(var(--u)*64);line-height:1.38;font-weight:800;
  letter-spacing:-.03em;color:#FBF8F2}
.calm-deep .ttl .hl{color:var(--dark)}
.calm-deep .sub,.calm-deep .txt{margin-top:calc(var(--u)*22);color:rgba(242,239,232,.72);
  font-size:calc(var(--u)*27);line-height:1.86}
.calm-deep .lst{margin-top:calc(var(--u)*26)}
.calm-deep .lst li{display:flex;gap:calc(var(--u)*16);align-items:flex-start;padding:calc(var(--u)*17) 0;
  border-top:calc(var(--u)*1) solid rgba(242,239,232,.2);font-size:calc(var(--u)*25);
  font-weight:600;line-height:1.56;color:rgba(242,239,232,.94)}
.calm-deep .lst li:last-child{border-bottom:calc(var(--u)*1) solid rgba(242,239,232,.2)}
.calm-deep .lst .ck{flex:none;color:var(--gold);font-size:calc(var(--u)*19);font-weight:900;
  min-width:calc(var(--u)*22);padding-top:calc(var(--u)*4)}
.calm-deep .rows{margin-top:calc(var(--u)*24)}
.calm-deep .rows .r{display:flex;gap:calc(var(--u)*18);align-items:flex-start;padding:calc(var(--u)*16) 0;
  border-top:calc(var(--u)*1) solid rgba(242,239,232,.2)}
.calm-deep .rows .r:last-child{border-bottom:calc(var(--u)*1) solid rgba(242,239,232,.2)}
.calm-deep .rows .k{flex:none;width:calc(var(--u)*114);font-size:calc(var(--u)*20);font-weight:800;
  color:var(--gold);letter-spacing:.04em;padding-top:calc(var(--u)*3)}
.calm-deep .rows .v{flex:1;font-size:calc(var(--u)*25);font-weight:700;line-height:1.55}
.calm-deep .steps{margin-top:calc(var(--u)*22)}
.calm-deep .steps .s{display:flex;gap:calc(var(--u)*18);align-items:flex-start;padding:calc(var(--u)*15) 0;
  border-top:calc(var(--u)*1) solid rgba(242,239,232,.2)}
.calm-deep .steps .s:last-child{border-bottom:calc(var(--u)*1) solid rgba(242,239,232,.2)}
.calm-deep .steps .n{flex:none;width:calc(var(--u)*34);font-size:calc(var(--u)*21);font-weight:900;color:var(--gold)}
.calm-deep .steps .sh{display:block;font-size:calc(var(--u)*25);font-weight:800}
.calm-deep .steps .sd{display:block;margin-top:calc(var(--u)*4);font-size:calc(var(--u)*22);
  color:rgba(242,239,232,.66);font-weight:600;line-height:1.58}
.calm-deep .pill{align-self:flex-start;margin-top:calc(var(--u)*30);border:calc(var(--u)*1) solid var(--gold);
  color:var(--gold);font-size:calc(var(--u)*24);font-weight:800;letter-spacing:.04em;
  padding:calc(var(--u)*15) calc(var(--u)*32);border-radius:999px}
.calm-deep .big{margin-top:calc(var(--u)*24);text-align:center;background:var(--gold);color:var(--dark);
  font-size:calc(var(--u)*28);font-weight:900;padding:calc(var(--u)*22);border-radius:calc(var(--u)*8)}
.calm-deep .note{margin-top:calc(var(--u)*18);color:rgba(242,239,232,.6)}
.calm-deep .ftr{margin-top:calc(var(--u)*20);display:flex;justify-content:flex-start}
.calm-deep .gobar{background:rgba(255,255,255,.95);color:#2A2A2A;border-radius:999px;
  padding:calc(var(--u)*8) calc(var(--u)*18)}
.calm-deep .dog{right:0;bottom:0;width:calc(var(--u)*320);z-index:1}
.calm-deep.t-hook .dog{width:calc(var(--u)*350);bottom:0}
.calm-deep.t-list .dog{width:calc(var(--u)*180);right:calc(var(--u)*10)}
.calm-deep.t-cta .dog{width:calc(var(--u)*165);right:calc(var(--u)*12);bottom:calc(var(--u)*82)}

/* 어두운 배경 시안 — 본문·목록 강조도 흰 박스로 또렷하게 */
.chic-bold .lst li .hl,.chic-bold .sub .hl,.chic-bold .txt .hl,
.chic-bold .steps .sh .hl,.chic-bold .steps .sd .hl,
.calm-deep .lst li .hl,.calm-deep .sub .hl,.calm-deep .txt .hl,
.calm-deep .rows .v .hl,.calm-deep .steps .sh .hl,.calm-deep .steps .sd .hl{
  background:#fff;border-radius:calc(var(--u)*8);padding:calc(var(--u)*1) calc(var(--u)*10);
  -webkit-box-decoration-break:clone;box-decoration-break:clone}
.chic-bold .lst li .hl,.chic-bold .sub .hl,.chic-bold .txt .hl,
.chic-bold .steps .sh .hl,.chic-bold .steps .sd .hl{color:var(--deep)}
.calm-deep .lst li .hl,.calm-deep .sub .hl,.calm-deep .txt .hl,
.calm-deep .rows .v .hl,.calm-deep .steps .sh .hl,.calm-deep .steps .sd .hl{color:var(--dark)}
"""
