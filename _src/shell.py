# -*- coding: utf-8 -*-
import json, base64, os
from styles import APP_CSS, CARD_CSS
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def datauri(name):
    p = os.path.join(ROOT, 'img', name)
    with open(p, 'rb') as f:
        return 'data:image/webp;base64,' + base64.b64encode(f.read()).decode()

HTML = """<!doctype html>
<html lang="ko"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>%(title)s</title><style>%(css)s</style></head><body>
<div class="bar">
  <h1>%(target)s</h1>
  <span class="tag mood">%(mood)s</span>
  <span class="tag">시안 %(idx)s · %(style_name)s</span>
  <span class="tag">1080 × 1080 · %(n)d장</span>
  <span class="sp"></span>
  <button class="btn" id="one">이 장 PNG</button>
  <button class="btn on" id="all">전체 PNG 저장</button>
</div>
<div class="wrap" id="wrap"></div><div class="toast" id="toast"></div>
<script>
/* ═══ 원고 — 이 부분 글자만 고치면 바로 반영됩니다 ═══════════
   **별표 두 개** = 강조 ｜ "왼쪽 | 오른쪽" = 세로줄로 좌우 구분
   dog = 강아지 컷아웃 (후킹 · 학원소개 · 마무리 세 장에만 들어갑니다) */
const STYLE = %(style)s;
const THEME = %(theme)s;
const ACADEMY = '한국반려동물전문학원';
const CARDS = %(cards)s;
/* ══════════════════════════════════════════════════════════ */

const IMG = %(imgs)s;
const CARD_CSS = %(card_css)s;
const W=1080,H=1080;
const CHK='<svg viewBox="0 0 24 24"><polyline points="4,12.5 9.5,18 20,6.5"/></svg>';
const STAR='<svg viewBox="0 0 24 24"><path d="M12 0c1 8 4 11 12 12-8 1-11 4-12 12-1-8-4-11-12-12 8-1 11-4 12-12z"/></svg>';
const PAW='<svg viewBox="0 0 64 64"><ellipse cx="18" cy="18" rx="8" ry="10.5"/><ellipse cx="33" cy="12" rx="8" ry="11"/><ellipse cx="48" cy="19" rx="7.5" ry="10"/><ellipse cx="55" cy="35" rx="7" ry="9"/><path d="M32 28c9 0 17 7 17 15 0 6-5 9-10 9-3 0-5-1-7-1s-4 1-7 1c-5 0-10-3-10-9 0-8 8-15 17-15z"/></svg>';
const esc=s=>String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const rich=s=>esc(s).replace(/\\*\\*(.+?)\\*\\*/g,'<span class="hl">$1</span>').replace(/\\n/g,'<br/>');
const pipe=s=>{const i=String(s).indexOf('|');return i<0?[String(s).trim(),'']:[String(s).slice(0,i).trim(),String(s).slice(i+1).trim()];};
const toast=m=>{const t=document.getElementById('toast');t.textContent=m;t.classList.add('on');
  clearTimeout(toast._t);toast._t=setTimeout(()=>t.classList.remove('on'),2000);};
const wait=ms=>new Promise(r=>setTimeout(r,ms));
const pad2=n=>String(n).padStart(2,'0');

function card(c,i){
  const T=THEME;
  const st=['--u:1px','--bg:'+T.bg,'--soft:'+T.soft,'--fg:'+T.fg,'--ac:'+T.ac,'--deep:'+T.deep,
    '--ac2:'+T.ac2,'--beige:'+T.beige,'--bfg:'+T.bfg,'--bac:'+T.bac,'--dark:'+T.dark,'--gold:'+T.gold,
    "--ff:'Pretendard','Apple SD Gothic Neo','Noto Sans KR',sans-serif",
    "--ffs:'AppleMyungjo','Nanum Myeongjo','Pretendard',serif",
    'width:'+W+'px','height:'+H+'px'].join(';');
  const it=(c.items||[]).filter(x=>String(x).trim()!=='');
  const calm = (STYLE==='calm-beige'||STYLE==='calm-deep');

  const eye=c.eye?'<div class="eye">'+rich(c.eye)+'</div>':'';
  const rule=(calm&&c.eye)?'<div class="rule"></div>':'';
  const ttl=c.ttl?'<div class="ttl">'+rich(c.ttl)+'</div>':'';
  const sub=c.sub?'<div class="sub">'+rich(c.sub)+'</div>':'';
  const txt=c.txt?'<div class="txt">'+rich(c.txt)+'</div>':'';
  const note=c.note?'<div class="note">'+rich(c.note)+'</div>':'';

  let block='';
  if(c.t==='list') block='<ul class="lst">'+it.map(x=>
    '<li><span class="ck">'+((STYLE==='cute-pop'||STYLE==='cute-bubble')?CHK:'✓')+'</span><span>'+rich(x)+'</span></li>').join('')+'</ul>';
  if(c.t==='benefit'||c.t==='cta') block='<div class="rows">'+it.map(x=>{const p=pipe(x);
    return '<div class="r"><span class="k">'+rich(p[0])+'</span><span class="v">'+rich(p[1])+'</span></div>';}).join('')+'</div>';
  if(c.t==='step') block='<div class="steps">'+it.map((x,n)=>{const p=pipe(x);
    return '<div class="s"><span class="n">'+pad2(n+1)+'</span><span><span class="sh">'+rich(p[0])+'</span>'+
      (p[1]?'<span class="sd">'+rich(p[1])+'</span>':'')+'</span></div>';}).join('')+'</div>';

  const pill=c.pill?'<div class="pill">'+rich(c.pill)+'</div>':'';
  const big=(c.btn&&STYLE!=='chic-bold')?'<div class="big">'+rich(c.btn)+'</div>':'';

  let bd;
  if(STYLE==='cute-bubble') bd=eye+'<div class="bub">'+ttl+sub+txt+block+'</div>'+pill+big+note;
  else bd=eye+rule+ttl+sub+txt+block+pill+big+note;

  const gobar='<div class="gobar"><img src="'+IMG.logo_go+'"/><span>국비지원 신청은 고용24에서</span></div>';
  let ftr='';
  if(STYLE==='chic-bold') ftr='<div class="ftr"><div class="cta">'+rich(c.btn||c.pill||'국비지원 상담 문의하기')+'</div>'+gobar+'</div>';
  else if(c.go) ftr='<div class="ftr">'+gobar+'</div>';

  let deco='';
  if(STYLE==='cute-pop') deco='<div class="blob b1"></div><div class="blob b2"></div>'+
    '<div class="dood dd1">'+STAR+'</div><div class="dood dd2">'+STAR+'</div><div class="dood dd3">'+PAW+'</div>';
  if(STYLE==='cute-bubble') deco='<div class="band bt"></div><div class="band bb"></div>';
  if(STYLE==='chic-mono') deco='<div class="idx">'+pad2(i+1)+'</div>';

  const dog=c.dog?'<img class="dog" src="'+IMG[c.dog]+'"/>':'';
  const hdr='<div class="hdr"><img class="kda" src="'+IMG.logo_kda+'"/>'+
    '<span class="nm">'+esc(ACADEMY)+'</span><span class="pg">'+pad2(i+1)+' / '+pad2(CARDS.length)+'</span></div>';

  return '<div class="card '+STYLE+' t-'+c.t+'" style="'+st+'">'+deco+
    '<div class="in">'+hdr+'<div class="bd">'+bd+'</div>'+ftr+'</div>'+dog+'</div>';
}

function render(){
  const wrap=document.getElementById('wrap');
  const sc=Math.min(1,(Math.min(window.innerWidth-56,520))/W);
  wrap.innerHTML=CARDS.map((c,i)=>'<div class="slot" data-i="'+i+'" style="width:'+(W*sc)+'px;height:'+(H*sc)+'px">'+
    '<div class="cap">'+(i+1)+'. '+c.t+(c.dog?' · 🐕':'')+'</div>'+
    '<div class="holder" style="width:'+W+'px;height:'+H+'px;transform:scale('+sc+')">'+card(c,i)+'</div></div>').join('');
}
let cur=0;
document.getElementById('wrap').addEventListener('click',e=>{const s=e.target.closest('.slot');
  if(s){cur=+s.dataset.i;toast((cur+1)+'번 선택');}});

function buildSVG(el){const NS='http://www.w3.org/2000/svg';
  const svg=document.createElementNS(NS,'svg');svg.setAttribute('width',W);svg.setAttribute('height',H);
  svg.setAttribute('viewBox','0 0 '+W+' '+H);
  const fo=document.createElementNS(NS,'foreignObject');fo.setAttribute('x',0);fo.setAttribute('y',0);
  fo.setAttribute('width',W);fo.setAttribute('height',H);
  const hold=document.createElement('div');hold.setAttribute('style','width:'+W+'px;height:'+H+'px');
  const st=document.createElement('style');st.appendChild(document.createTextNode(CARD_CSS));
  hold.appendChild(st);hold.appendChild(el.cloneNode(true));fo.appendChild(hold);svg.appendChild(fo);
  return new XMLSerializer().serializeToString(svg);}
const loadImg=src=>new Promise((res,rej)=>{const im=new Image();im.onload=()=>res(im);
  im.onerror=()=>rej(new Error('변환 실패'));im.src=src;});
function blank(cv){const t=document.createElement('canvas');t.width=32;t.height=32;
  const x=t.getContext('2d');x.drawImage(cv,0,0,32,32);const d=x.getImageData(0,0,32,32).data;
  for(let i=4;i<d.length;i+=4){if(d[i]!==d[0]||d[i+1]!==d[1]||d[i+2]!==d[2])return false;}return true;}
async function png(i){
  const el=document.querySelector('.slot[data-i="'+i+'"] .card');
  const src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(buildSVG(el));
  let cv;
  for(let a=0;a<3;a++){const im=await loadImg(src);
    cv=document.createElement('canvas');cv.width=W*2;cv.height=H*2;
    const cx=cv.getContext('2d');cx.setTransform(2,0,0,2,0,0);cx.drawImage(im,0,0,W,H);
    if(!blank(cv))break;
    if(a<2) await wait(300); else throw new Error('이 브라우저에서 변환 실패 — Chrome 으로 열어주세요');}
  return new Promise(r=>cv.toBlob(r,'image/png'));}
function dl(b,n){const u=URL.createObjectURL(b);const a=document.createElement('a');a.href=u;a.download=n;
  document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(u),2000);}
const PRE=%(prefix)s;
document.getElementById('one').onclick=async()=>{try{toast('만드는 중…');
  dl(await png(cur),PRE+'_'+pad2(cur+1)+'.png');toast('저장 완료');}catch(e){toast(e.message);}};
document.getElementById('all').onclick=async()=>{try{for(let i=0;i<CARDS.length;i++){
  toast('저장 중… '+(i+1)+'/'+CARDS.length);dl(await png(i),PRE+'_'+pad2(i+1)+'.png');
  await wait(400);}toast('전체 저장 완료');}catch(e){toast(e.message);}};
window.addEventListener('resize',render);render();
</script></body></html>
"""

def build(target, idx, style, style_name, mood, theme, cards, prefix, title):
    used = sorted({c['dog'] for c in cards if c.get('dog')})
    imgs = {'logo_kda': datauri('logo_kda.webp'), 'logo_go': datauri('logo_go.webp')}
    for u in used:
        imgs[u] = datauri(u + '.webp')
    return HTML % {
        'title': title, 'target': target, 'idx': idx, 'style_name': style_name, 'mood': mood,
        'n': len(cards), 'css': APP_CSS + CARD_CSS,
        'card_css': json.dumps(CARD_CSS, ensure_ascii=False),
        'style': json.dumps(style), 'theme': json.dumps(theme, ensure_ascii=False),
        'cards': json.dumps(cards, ensure_ascii=False, indent=2),
        'imgs': json.dumps(imgs), 'prefix': json.dumps(prefix, ensure_ascii=False),
    }
