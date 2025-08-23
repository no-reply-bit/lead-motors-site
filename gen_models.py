import os
from string import Template

# 生成するモデル一覧（必要に応じて追加/編集OK）
models = [
  {"id":"ux300e","name":"UX300e","img":"../images/ux300e.png.png","lead":"静粛性とレスポンスを兼ね備えたコンパクトBEV。"},
  {"id":"gx","name":"GX","img":"../images/gx.png.png","lead":"力強い走破性と上質さを両立するSUV。"},
  {"id":"nx","name":"NX","img":"../images/nx.png.png","lead":"日常をアップグレードするミドルSUV。"},
  {"id":"rx","name":"RX","img":"../images/rx.png.png","lead":"フラッグシップSUVの快適性。"},
  {"id":"ux","name":"UX","img":"../images/ux.png.png","lead":"都市で映えるコンパクトクロスオーバー。"},
  {"id":"ls","name":"LS","img":"../images/ls.png.png","lead":"上質な移動空間を提供するセダン。"},
  {"id":"lx","name":"LX","img":"../images/lx.png.png","lead":"タフネスとラグジュアリーの頂点。"},
  {"id":"lbx","name":"LBX","img":"../images/lbx.png.png","lead":"取り回しの良さと上質感の新基準。"},
]

template = Template("""<!doctype html><html lang="ja"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>$name | LEAD Motors</title>
<link rel="stylesheet" href="../css/style.css">
</head><body>
<header class="site-header"><div class="container header-inner">
  <a class="brand" href="../index.html">LEAD Motors</a>
  <nav class="nav" id="nav">
    <a href="../index.html#models">モデル一覧</a>
    <a href="../index.html#news">ニュース</a>
    <a href="../index.html#support">サポート</a>
    <a href="../company.html">会社概要</a>
    <a href="../contact.html">お問い合わせ</a>
  </nav><button class="hamburger" id="hamburger"><span></span><span></span><span></span></button>
</div></header>

<main class="page">
  <nav class="breadcrumb container"><a href="../index.html">HOME</a> / <a href="../index.html#models">モデル</a> / $name</nav>

  <section class="container model-hero">
    <div class="gallery">
      <img id="mainImg" src="$img" alt="$name">
      <div class="thumbs">
        <img class="t active" src="$img" alt>
      </div>
    </div>
    <div class="model-copy">
      <h1>$name</h1>
      <p class="lead">$lead</p>
      <a class="btn" href="../contact.html">見積り・お問い合わせ</a>
      <ul class="bullets">
        <li>航続・出力などの数値はダミー</li>
        <li>装備・価格もダミー</li>
        <li>画像は手元のものに差し替え可</li>
      </ul>
    </div>
  </section>

  <section class="container two-col">
    <div>
      <h2>主な装備</h2>
      <ul class="list"><li>先進安全（ダミー）</li><li>大型ディスプレイ</li><li>コネクテッド機能</li></ul>
    </div>
    <div>
      <h2>主要諸元</h2>
      <dl class="spec">
        <div><dt>全長×全幅×全高</dt><dd>-</dd></div>
        <div><dt>車両重量</dt><dd>-</dd></div>
        <div><dt>駆動方式</dt><dd>-</dd></div>
        <div><dt>定員</dt><dd>5名</dd></div>
      </dl>
    </div>
  </section>
</main>

<footer class="site-footer"><div class="container footer-inner">
  <div class="left"><div class="brand">LEAD Motors</div><small>© 2025 LEAD作業</small></div>
  <nav class="footer-nav"><a href="../company.html">会社概要</a><a href="../contact.html">お問い合わせ</a></nav>
</div></footer>

<script>
const ham = document.getElementById('hamburger'), nav = document.getElementById('nav');
ham.addEventListener('click', () => { ham.classList.toggle('on'); nav.classList.toggle('open'); });
const main = document.getElementById('mainImg');
document.querySelectorAll('.thumbs .t').forEach(t => {
  t.addEventListener('click', () => {
    document.querySelectorAll('.thumbs .t').forEach(x => x.classList.remove('active'));
    t.classList.add('active');
    main.src = t.src;
  });
});
</script>
</body></html>""")

# スクリプトの場所を起点に 'models' を作成（どこで実行してもOK）
base_dir = os.path.dirname(os.path.abspath(__file__))
out_dir = os.path.join(base_dir, "models")
os.makedirs(out_dir, exist_ok=True)

for m in models:
  out_path = os.path.join(out_dir, f"{m['id']}.html")
  with open(out_path, "w", encoding="utf-8") as f:
    f.write(template.safe_substitute(m))

print(f"生成完了：{out_dir} に HTML を作成しました。")
