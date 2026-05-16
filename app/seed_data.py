INGREDIENTS = [
    ("鶏むね肉", "タンパク質"),
    ("鶏ひき肉", "タンパク質"),
    ("豚ひき肉", "タンパク質"),
    ("豚こま", "タンパク質"),
    ("卵", "タンパク質"),
    ("ちくわ", "タンパク質"),
    ("ツナ缶", "タンパク質"),
    ("納豆", "タンパク質"),
    ("豆腐", "タンパク質"),
    ("厚揚げ", "タンパク質"),
    ("サバ缶", "タンパク質"),
    ("イワシ缶", "タンパク質"),
    ("もやし", "野菜"),
    ("キャベツ", "野菜"),
    ("ブロッコリー", "野菜"),
    ("小松菜", "野菜"),
    ("ほうれん草", "野菜"),
    ("玉ねぎ", "野菜"),
    ("にんじん", "野菜"),
    ("米", "炭水化物"),
    ("オートミール", "炭水化物"),
    ("うどん", "炭水化物"),
    ("そば", "炭水化物"),
]

RECIPES = [
    # ===== 鶏むね肉 =====
    {
        "name": "鶏むね肉の塩こうじ蒸し",
        "description": "しっとりやわらかく仕上がる定番の蒸し鶏。サラダやそのままで。",
        "genre": "蒸し物",
        "protein": 38.0, "fat": 3.2, "carbs": 2.0, "calories": 188,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "300g"), ("玉ねぎ", "1/4個")]
    },
    {
        "name": "鶏むね肉とブロッコリーの塩炒め",
        "description": "シンプルな塩味でヘルシー。高タンパクの定番筋肉飯。",
        "genre": "炒め物",
        "protein": 42.0, "fat": 5.0, "carbs": 6.0, "calories": 237,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏むね肉", "250g"), ("ブロッコリー", "1/2株")]
    },
    {
        "name": "鶏むね肉のネギ塩丼",
        "description": "ごま油香るネギ塩ダレをかけた高タンパク丼。",
        "genre": "丼",
        "protein": 45.0, "fat": 6.5, "carbs": 58.0, "calories": 472,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "250g"), ("米", "2合"), ("玉ねぎ", "1/4個")]
    },
    {
        "name": "鶏むね肉のキャベツ炒め",
        "description": "キャベツたっぷりでかさましボリューム満点炒め。",
        "genre": "炒め物",
        "protein": 36.0, "fat": 4.8, "carbs": 8.0, "calories": 218,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏むね肉", "200g"), ("キャベツ", "1/4個")]
    },
    {
        "name": "鶏むね肉のオートミール雑炊",
        "description": "オートミールで作るヘルシー雑炊。朝食にも最適。",
        "genre": "スープ",
        "protein": 34.0, "fat": 3.5, "carbs": 28.0, "calories": 278,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏むね肉", "200g"), ("オートミール", "60g"), ("小松菜", "1束")]
    },
    {
        "name": "鶏むね肉ともやしのポン酢蒸し",
        "description": "レンジで簡単。ポン酢でさっぱり仕上げる低脂質料理。",
        "genre": "蒸し物",
        "protein": 32.0, "fat": 2.8, "carbs": 3.5, "calories": 166,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("鶏むね肉", "200g"), ("もやし", "1袋")]
    },
    {
        "name": "鶏むね肉の親子丼",
        "description": "卵でとじた定番親子丼。タンパク質をしっかり摂れる。",
        "genre": "丼",
        "protein": 48.0, "fat": 9.0, "carbs": 62.0, "calories": 522,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "200g"), ("卵", "3個"), ("玉ねぎ", "1/2個"), ("米", "2合")]
    },
    {
        "name": "鶏むね肉とほうれん草のソテー",
        "description": "鉄分豊富なほうれん草と合わせた栄養バランス抜群の一品。",
        "genre": "炒め物",
        "protein": 36.0, "fat": 4.5, "carbs": 4.0, "calories": 202,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏むね肉", "200g"), ("ほうれん草", "1束")]
    },
    {
        "name": "鶏むね肉の小松菜スープ",
        "description": "生姜を効かせた体が温まる低脂質スープ。",
        "genre": "スープ",
        "protein": 30.0, "fat": 3.0, "carbs": 4.0, "calories": 162,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏むね肉", "180g"), ("小松菜", "1束"), ("にんじん", "1/2本")]
    },
    {
        "name": "鶏むね肉の照り焼き丼",
        "description": "甘辛タレが食欲をそそる定番照り焼き丼。",
        "genre": "丼",
        "protein": 44.0, "fat": 5.5, "carbs": 65.0, "calories": 490,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "250g"), ("米", "2合")]
    },
    {
        "name": "鶏むね肉とにんじんのしりしり風",
        "description": "沖縄料理風にアレンジ。にんじんと卵でカラフルに。",
        "genre": "炒め物",
        "protein": 32.0, "fat": 6.0, "carbs": 8.0, "calories": 214,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏むね肉", "180g"), ("にんじん", "1本"), ("卵", "1個")]
    },
    {
        "name": "鶏むね肉のうどん煮込み",
        "description": "だし香るシンプルな煮込みうどん。消化も良い。",
        "genre": "麺類",
        "protein": 38.0, "fat": 4.0, "carbs": 52.0, "calories": 398,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "200g"), ("うどん", "2玉"), ("小松菜", "1束")]
    },
    {
        "name": "鶏むね肉とブロッコリーの卵炒め",
        "description": "卵でまとめた高タンパク炒め。手軽で栄養満点。",
        "genre": "炒め物",
        "protein": 44.0, "fat": 10.0, "carbs": 5.0, "calories": 286,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏むね肉", "200g"), ("ブロッコリー", "1/2株"), ("卵", "2個")]
    },
    {
        "name": "鶏むね肉のそば",
        "description": "冷たいそばに蒸し鶏をのせた夏向きヘルシー麺。",
        "genre": "麺類",
        "protein": 40.0, "fat": 4.2, "carbs": 48.0, "calories": 388,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "200g"), ("そば", "2玉")]
    },
    {
        "name": "鶏むね肉のトマト煮",
        "description": "トマト缶で煮込んだ洋風ヘルシー料理。",
        "genre": "洋食",
        "protein": 38.0, "fat": 4.8, "carbs": 10.0, "calories": 234,
        "servings": 2, "cooking_time": 25,
        "ingredients": [("鶏むね肉", "250g"), ("玉ねぎ", "1/2個"), ("にんじん", "1/2本")]
    },
    # ===== 鶏ひき肉 =====
    {
        "name": "鶏ひき肉と豆腐のそぼろ丼",
        "description": "ふわふわ豆腐入りのヘルシーそぼろ丼。",
        "genre": "丼",
        "protein": 42.0, "fat": 8.0, "carbs": 60.0, "calories": 480,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏ひき肉", "200g"), ("豆腐", "1丁"), ("米", "2合")]
    },
    {
        "name": "鶏ひき肉ともやしの炒め物",
        "description": "安くてボリューム満点のかさましひき肉炒め。",
        "genre": "炒め物",
        "protein": 30.0, "fat": 7.5, "carbs": 5.0, "calories": 208,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("鶏ひき肉", "200g"), ("もやし", "1袋")]
    },
    {
        "name": "鶏ひき肉と野菜のスープ",
        "description": "野菜たっぷりのあっさりスープ。ダイエット中に最適。",
        "genre": "スープ",
        "protein": 28.0, "fat": 5.0, "carbs": 8.0, "calories": 190,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏ひき肉", "180g"), ("キャベツ", "1/4個"), ("にんじん", "1/2本"), ("玉ねぎ", "1/2個")]
    },
    {
        "name": "鶏ひき肉のキャベツ包み蒸し",
        "description": "キャベツで包んで蒸した低カロリー料理。",
        "genre": "蒸し物",
        "protein": 26.0, "fat": 5.2, "carbs": 6.0, "calories": 176,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏ひき肉", "200g"), ("キャベツ", "1/4個")]
    },
    {
        "name": "鶏ひき肉と小松菜の炒め",
        "description": "鉄分たっぷり小松菜との組み合わせ。栄養価が高い。",
        "genre": "炒め物",
        "protein": 28.0, "fat": 6.0, "carbs": 3.0, "calories": 178,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("鶏ひき肉", "200g"), ("小松菜", "1束")]
    },
    {
        "name": "鶏ひき肉のオートミールご飯",
        "description": "オートミールを米代わりにしたそぼろご飯。低GIで満足感。",
        "genre": "丼",
        "protein": 34.0, "fat": 6.5, "carbs": 35.0, "calories": 338,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏ひき肉", "200g"), ("オートミール", "80g"), ("卵", "1個")]
    },
    {
        "name": "鶏ひき肉のレタス包み",
        "description": "甜麺醤風味のひき肉をレタスで包んで食べる。",
        "genre": "炒め物",
        "protein": 28.0, "fat": 7.0, "carbs": 5.0, "calories": 194,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏ひき肉", "200g"), ("玉ねぎ", "1/4個")]
    },
    {
        "name": "鶏ひき肉と厚揚げの煮物",
        "description": "厚揚げとひき肉のうま煮。タンパク質を二重に摂れる。",
        "genre": "煮物",
        "protein": 36.0, "fat": 12.0, "carbs": 5.0, "calories": 268,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏ひき肉", "150g"), ("厚揚げ", "1枚")]
    },
    {
        "name": "鶏ひき肉のうどん汁",
        "description": "だしの効いたひき肉うどん。お腹にやさしい。",
        "genre": "麺類",
        "protein": 34.0, "fat": 6.0, "carbs": 54.0, "calories": 410,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏ひき肉", "200g"), ("うどん", "2玉"), ("ほうれん草", "1/2束")]
    },
    # ===== 豚ひき肉 =====
    {
        "name": "豚ひき肉ともやしのガーリック炒め",
        "description": "にんにく香る食欲増進の炒め物。安くてボリューム満点。",
        "genre": "炒め物",
        "protein": 28.0, "fat": 14.0, "carbs": 5.0, "calories": 258,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豚ひき肉", "200g"), ("もやし", "1袋")]
    },
    {
        "name": "豚ひき肉と豆腐の麻婆豆腐",
        "description": "辛さ控えめ低脂質版麻婆豆腐。タンパク質たっぷり。",
        "genre": "中華",
        "protein": 32.0, "fat": 12.0, "carbs": 8.0, "calories": 268,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚ひき肉", "150g"), ("豆腐", "1丁")]
    },
    {
        "name": "豚ひき肉の担々スープ",
        "description": "ごまの風味豊かな担々スープ。ダイエット向けアレンジ。",
        "genre": "スープ",
        "protein": 28.0, "fat": 12.0, "carbs": 6.0, "calories": 244,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚ひき肉", "180g"), ("もやし", "1/2袋"), ("小松菜", "1/2束")]
    },
    {
        "name": "豚ひき肉のキャベツそぼろ炒め",
        "description": "キャベツで量増しした低カロリーそぼろ炒め。",
        "genre": "炒め物",
        "protein": 26.0, "fat": 12.0, "carbs": 7.0, "calories": 238,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豚ひき肉", "200g"), ("キャベツ", "1/4個")]
    },
    {
        "name": "豚ひき肉の肉味噌丼",
        "description": "ご飯がすすむ甘辛肉味噌丼。手軽に作れる定番メニュー。",
        "genre": "丼",
        "protein": 36.0, "fat": 14.0, "carbs": 64.0, "calories": 524,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚ひき肉", "200g"), ("玉ねぎ", "1/4個"), ("米", "2合")]
    },
    {
        "name": "豚ひき肉と玉ねぎのスープ",
        "description": "玉ねぎの甘さが引き立つシンプルスープ。",
        "genre": "スープ",
        "protein": 24.0, "fat": 12.0, "carbs": 8.0, "calories": 236,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚ひき肉", "180g"), ("玉ねぎ", "1個")]
    },
    # ===== 豚こま =====
    {
        "name": "豚こまともやしの生姜炒め",
        "description": "生姜でさっぱり仕上げた定番炒め物。ご飯によく合う。",
        "genre": "炒め物",
        "protein": 26.0, "fat": 10.0, "carbs": 5.0, "calories": 214,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豚こま", "200g"), ("もやし", "1袋")]
    },
    {
        "name": "豚こまとキャベツの塩炒め",
        "description": "シンプルな塩味で仕上げたヘルシー炒め。",
        "genre": "炒め物",
        "protein": 24.0, "fat": 9.5, "carbs": 7.0, "calories": 210,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豚こま", "180g"), ("キャベツ", "1/4個")]
    },
    {
        "name": "豚こまと野菜の味噌汁",
        "description": "豚汁風にアレンジした具だくさん味噌汁。",
        "genre": "スープ",
        "protein": 22.0, "fat": 9.0, "carbs": 8.0, "calories": 206,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("豚こま", "150g"), ("にんじん", "1/2本"), ("玉ねぎ", "1/2個")]
    },
    {
        "name": "豚こまのしょうが焼き丼",
        "description": "定番しょうが焼きを丼にアレンジ。ご飯が進む一品。",
        "genre": "丼",
        "protein": 32.0, "fat": 10.0, "carbs": 62.0, "calories": 474,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚こま", "200g"), ("玉ねぎ", "1/2個"), ("米", "2合")]
    },
    {
        "name": "豚こまとほうれん草の炒め物",
        "description": "鉄分豊富なほうれん草と合わせた栄養たっぷり炒め。",
        "genre": "炒め物",
        "protein": 24.0, "fat": 9.8, "carbs": 4.0, "calories": 202,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豚こま", "180g"), ("ほうれん草", "1束")]
    },
    {
        "name": "豚こまとブロッコリーの醤油炒め",
        "description": "醤油ベースのシンプルな炒め物。ブロッコリーで食感UP。",
        "genre": "炒め物",
        "protein": 28.0, "fat": 10.0, "carbs": 6.0, "calories": 226,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚こま", "200g"), ("ブロッコリー", "1/2株")]
    },
    {
        "name": "豚こまと厚揚げの煮物",
        "description": "厚揚げとの相性抜群。出汁が染み込んだ和風煮物。",
        "genre": "煮物",
        "protein": 30.0, "fat": 14.0, "carbs": 5.0, "calories": 266,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("豚こま", "150g"), ("厚揚げ", "1枚")]
    },
    {
        "name": "豚こまのうどん炒め",
        "description": "焼きうどん風にアレンジしたボリューム麺料理。",
        "genre": "麺類",
        "protein": 28.0, "fat": 10.0, "carbs": 58.0, "calories": 438,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚こま", "180g"), ("うどん", "2玉"), ("キャベツ", "1/4個")]
    },
    # ===== 卵 =====
    {
        "name": "スクランブルエッグと野菜炒め",
        "description": "卵ともやしでヘルシー朝食メニュー。手軽に作れる。",
        "genre": "炒め物",
        "protein": 18.0, "fat": 12.0, "carbs": 4.0, "calories": 194,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("卵", "3個"), ("もやし", "1/2袋"), ("ブロッコリー", "1/4株")]
    },
    {
        "name": "玉子とじうどん",
        "description": "卵でとじたシンプルうどん。体を温める優しい味。",
        "genre": "麺類",
        "protein": 20.0, "fat": 8.0, "carbs": 54.0, "calories": 372,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("卵", "2個"), ("うどん", "2玉"), ("ほうれん草", "1/2束")]
    },
    {
        "name": "卵とほうれん草のソテー",
        "description": "シンプルな炒め物。栄養豊富で朝食にも最適。",
        "genre": "炒め物",
        "protein": 16.0, "fat": 10.0, "carbs": 3.0, "calories": 162,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("卵", "3個"), ("ほうれん草", "1束")]
    },
    {
        "name": "オムライス風オートミール",
        "description": "オートミールをご飯代わりに使ったオムライス風。低GI。",
        "genre": "洋食",
        "protein": 22.0, "fat": 10.0, "carbs": 36.0, "calories": 322,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("卵", "3個"), ("オートミール", "80g"), ("玉ねぎ", "1/4個")]
    },
    {
        "name": "卵とにんじんの炒め物",
        "description": "にんじんと卵の黄金コンビ。β-カロテンたっぷり。",
        "genre": "炒め物",
        "protein": 14.0, "fat": 9.0, "carbs": 8.0, "calories": 170,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("卵", "3個"), ("にんじん", "1本")]
    },
    {
        "name": "茶碗蒸し風スープ",
        "description": "電子レンジで作れる簡単茶碗蒸し風スープ。",
        "genre": "スープ",
        "protein": 12.0, "fat": 6.0, "carbs": 3.0, "calories": 114,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("卵", "2個"), ("小松菜", "1/2束")]
    },
    # ===== ちくわ =====
    {
        "name": "ちくわとキャベツの炒め物",
        "description": "ちくわの旨味でシンプルな炒め。コスパ最強の一品。",
        "genre": "炒め物",
        "protein": 16.0, "fat": 3.0, "carbs": 14.0, "calories": 146,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ちくわ", "4本"), ("キャベツ", "1/4個")]
    },
    {
        "name": "ちくわともやしの炒め",
        "description": "安食材2つで作れる最安コスパ炒め物。",
        "genre": "炒め物",
        "protein": 14.0, "fat": 2.5, "carbs": 12.0, "calories": 126,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ちくわ", "4本"), ("もやし", "1袋")]
    },
    {
        "name": "ちくわとブロッコリーのマスタード炒め",
        "description": "粒マスタードで洋風にアレンジしたちくわ炒め。",
        "genre": "洋食",
        "protein": 18.0, "fat": 3.5, "carbs": 14.0, "calories": 158,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ちくわ", "4本"), ("ブロッコリー", "1/2株")]
    },
    {
        "name": "ちくわのスープ煮",
        "description": "あっさりスープで煮込んだちくわ。野菜も一緒に。",
        "genre": "スープ",
        "protein": 16.0, "fat": 3.0, "carbs": 14.0, "calories": 146,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("ちくわ", "4本"), ("玉ねぎ", "1/2個"), ("にんじん", "1/2本")]
    },
    {
        "name": "ちくわのうどん汁",
        "description": "ちくわ入りのあっさりうどん。素朴で体に優しい。",
        "genre": "麺類",
        "protein": 18.0, "fat": 3.0, "carbs": 56.0, "calories": 322,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("ちくわ", "4本"), ("うどん", "2玉"), ("ほうれん草", "1/2束")]
    },
    {
        "name": "ちくわとほうれん草の和え物",
        "description": "ごま和え風にアレンジしたちくわとほうれん草。",
        "genre": "和食",
        "protein": 14.0, "fat": 4.0, "carbs": 10.0, "calories": 132,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ちくわ", "3本"), ("ほうれん草", "1束")]
    },
    # ===== ツナ缶 =====
    {
        "name": "ツナと豆腐のサラダ",
        "description": "ヘルシーなツナ豆腐サラダ。低カロリーで満腹感。",
        "genre": "サラダ",
        "protein": 28.0, "fat": 8.0, "carbs": 5.0, "calories": 202,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ツナ缶", "2缶"), ("豆腐", "1丁")]
    },
    {
        "name": "ツナともやしのナムル",
        "description": "ごま油香るナムル風サラダ。韓国風の味付け。",
        "genre": "サラダ",
        "protein": 20.0, "fat": 7.0, "carbs": 4.0, "calories": 162,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ツナ缶", "1缶"), ("もやし", "1袋")]
    },
    {
        "name": "ツナとブロッコリーのサラダ",
        "description": "マヨネーズ控えめのあっさりサラダ。タンパク質豊富。",
        "genre": "サラダ",
        "protein": 24.0, "fat": 6.0, "carbs": 6.0, "calories": 176,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ツナ缶", "1缶"), ("ブロッコリー", "1/2株")]
    },
    {
        "name": "ツナとキャベツのさっぱり炒め",
        "description": "ポン酢で仕上げたさっぱり炒め。低カロリー。",
        "genre": "炒め物",
        "protein": 20.0, "fat": 5.0, "carbs": 7.0, "calories": 154,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ツナ缶", "1缶"), ("キャベツ", "1/4個")]
    },
    {
        "name": "ツナのオートミール粥",
        "description": "ツナとオートミールで作る高タンパク粥。朝食に。",
        "genre": "その他",
        "protein": 22.0, "fat": 5.0, "carbs": 32.0, "calories": 258,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ツナ缶", "1缶"), ("オートミール", "80g")]
    },
    {
        "name": "ツナと玉ねぎのスープ",
        "description": "玉ねぎの甘さとツナが合うシンプルスープ。",
        "genre": "スープ",
        "protein": 18.0, "fat": 5.0, "carbs": 8.0, "calories": 154,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("ツナ缶", "1缶"), ("玉ねぎ", "1個")]
    },
    {
        "name": "ツナとほうれん草の炒め",
        "description": "ツナとほうれん草の簡単炒め。栄養バランス良好。",
        "genre": "炒め物",
        "protein": 22.0, "fat": 5.5, "carbs": 4.0, "calories": 158,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ツナ缶", "1缶"), ("ほうれん草", "1束")]
    },
    # ===== 納豆 =====
    {
        "name": "納豆と卵のオートミール丼",
        "description": "栄養満点の発酵食品コンビ。ねばとろで美味。",
        "genre": "丼",
        "protein": 24.0, "fat": 8.0, "carbs": 36.0, "calories": 314,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("納豆", "2パック"), ("卵", "2個"), ("オートミール", "80g")]
    },
    {
        "name": "納豆と豆腐の冷ややっこ風",
        "description": "冷たくして食べる夏向けタンパク質メニュー。",
        "genre": "和食",
        "protein": 22.0, "fat": 9.0, "carbs": 8.0, "calories": 202,
        "servings": 2, "cooking_time": 5,
        "ingredients": [("納豆", "2パック"), ("豆腐", "1丁")]
    },
    {
        "name": "納豆ご飯",
        "description": "シンプルな納豆ご飯。発酵食品で腸活。",
        "genre": "和食",
        "protein": 20.0, "fat": 7.0, "carbs": 62.0, "calories": 394,
        "servings": 2, "cooking_time": 5,
        "ingredients": [("納豆", "2パック"), ("米", "2合")]
    },
    {
        "name": "納豆キムチそば",
        "description": "納豆とそばで高タンパク。キムチで腸活効果も。",
        "genre": "麺類",
        "protein": 22.0, "fat": 8.0, "carbs": 50.0, "calories": 362,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("納豆", "2パック"), ("そば", "2玉")]
    },
    {
        "name": "納豆とちくわの混ぜご飯",
        "description": "ちくわと納豆の意外なコンビ。コスパ最強メニュー。",
        "genre": "和食",
        "protein": 24.0, "fat": 6.0, "carbs": 62.0, "calories": 398,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("納豆", "2パック"), ("ちくわ", "2本"), ("米", "2合")]
    },
    # ===== 豆腐 =====
    {
        "name": "豆腐とブロッコリーのサラダ",
        "description": "ヘルシーで満腹感のある豆腐サラダ。低カロリー。",
        "genre": "サラダ",
        "protein": 18.0, "fat": 6.0, "carbs": 6.0, "calories": 154,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豆腐", "1丁"), ("ブロッコリー", "1/2株")]
    },
    {
        "name": "豆腐とほうれん草の白和え",
        "description": "ほうれん草の白和え。ごまの風味豊かな和食。",
        "genre": "和食",
        "protein": 16.0, "fat": 7.0, "carbs": 5.0, "calories": 150,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豆腐", "1丁"), ("ほうれん草", "1束")]
    },
    {
        "name": "豆腐と卵の炒め物",
        "description": "中華風の豆腐炒め。シンプルで美味しい。",
        "genre": "中華",
        "protein": 22.0, "fat": 10.0, "carbs": 4.0, "calories": 194,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豆腐", "1丁"), ("卵", "2個")]
    },
    {
        "name": "豆腐のみそ汁",
        "description": "定番の豆腐みそ汁。野菜をたっぷり入れて。",
        "genre": "和食",
        "protein": 14.0, "fat": 5.0, "carbs": 6.0, "calories": 126,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豆腐", "1丁"), ("小松菜", "1/2束"), ("玉ねぎ", "1/4個")]
    },
    {
        "name": "豆腐キムチチゲ風スープ",
        "description": "豆腐入りのピリ辛スープ。体が温まる一品。",
        "genre": "スープ",
        "protein": 18.0, "fat": 6.0, "carbs": 6.0, "calories": 152,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豆腐", "1丁"), ("豚こま", "100g")]
    },
    {
        "name": "豆腐ステーキ",
        "description": "焼いた豆腐にポン酢をかけたシンプルステーキ。",
        "genre": "和食",
        "protein": 14.0, "fat": 6.0, "carbs": 3.0, "calories": 122,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豆腐", "1丁")]
    },
    # ===== 厚揚げ =====
    {
        "name": "厚揚げともやしの炒め煮",
        "description": "もやしでかさましした厚揚げ煮。コスパ良し。",
        "genre": "煮物",
        "protein": 22.0, "fat": 12.0, "carbs": 6.0, "calories": 218,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("厚揚げ", "1枚"), ("もやし", "1袋")]
    },
    {
        "name": "厚揚げとキャベツの炒め物",
        "description": "キャベツの甘みと厚揚げのコクが合う炒め物。",
        "genre": "炒め物",
        "protein": 20.0, "fat": 12.0, "carbs": 8.0, "calories": 218,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("厚揚げ", "1枚"), ("キャベツ", "1/4個")]
    },
    {
        "name": "厚揚げと小松菜の煮浸し",
        "description": "だしが染み込んだ厚揚げ煮浸し。和の定番。",
        "genre": "煮物",
        "protein": 20.0, "fat": 12.0, "carbs": 5.0, "calories": 208,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("厚揚げ", "1枚"), ("小松菜", "1束")]
    },
    {
        "name": "厚揚げのみそ汁",
        "description": "ボリューム満点の厚揚げ入りみそ汁。",
        "genre": "スープ",
        "protein": 18.0, "fat": 10.0, "carbs": 5.0, "calories": 186,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("厚揚げ", "1枚"), ("ほうれん草", "1/2束")]
    },
    {
        "name": "厚揚げとにんじんの煮物",
        "description": "にんじん入りの彩り豊かな厚揚げ煮。",
        "genre": "煮物",
        "protein": 18.0, "fat": 10.0, "carbs": 8.0, "calories": 194,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("厚揚げ", "1枚"), ("にんじん", "1本")]
    },
    {
        "name": "厚揚げステーキ丼",
        "description": "焼いた厚揚げをご飯にのせたヘルシー丼。",
        "genre": "丼",
        "protein": 24.0, "fat": 12.0, "carbs": 62.0, "calories": 458,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("厚揚げ", "1枚"), ("米", "2合")]
    },
    # ===== サバ缶 =====
    {
        "name": "サバ缶ともやしのスープ",
        "description": "EPA豊富なサバ缶ともやしのヘルシースープ。",
        "genre": "スープ",
        "protein": 26.0, "fat": 10.0, "carbs": 4.0, "calories": 210,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("サバ缶", "1缶"), ("もやし", "1袋")]
    },
    {
        "name": "サバ缶とキャベツの炒め",
        "description": "サバ缶を使った手軽な炒め物。DHA・EPAが豊富。",
        "genre": "炒め物",
        "protein": 24.0, "fat": 10.0, "carbs": 6.0, "calories": 210,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("サバ缶", "1缶"), ("キャベツ", "1/4個")]
    },
    {
        "name": "サバ缶のみそ汁",
        "description": "サバ缶入りのコクあるみそ汁。旨味たっぷり。",
        "genre": "スープ",
        "protein": 24.0, "fat": 10.0, "carbs": 5.0, "calories": 206,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("サバ缶", "1缶"), ("小松菜", "1束"), ("玉ねぎ", "1/4個")]
    },
    {
        "name": "サバ缶丼",
        "description": "サバ缶をそのまま丼に。手軽に作れる高タンパク丼。",
        "genre": "丼",
        "protein": 30.0, "fat": 12.0, "carbs": 62.0, "calories": 478,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("サバ缶", "1缶"), ("米", "2合")]
    },
    {
        "name": "サバ缶とブロッコリーのサラダ",
        "description": "レモン風味のさっぱりサラダ。ブロッコリーで食べ応え。",
        "genre": "サラダ",
        "protein": 26.0, "fat": 10.0, "carbs": 6.0, "calories": 218,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("サバ缶", "1缶"), ("ブロッコリー", "1/2株")]
    },
    {
        "name": "サバ缶のトマト煮",
        "description": "サバ缶とトマトで作る洋風煮込み。栄養価が高い。",
        "genre": "洋食",
        "protein": 26.0, "fat": 10.0, "carbs": 8.0, "calories": 226,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("サバ缶", "1缶"), ("玉ねぎ", "1/2個"), ("にんじん", "1/2本")]
    },
    {
        "name": "サバ缶うどん",
        "description": "サバ缶の旨味がつゆに溶け込んだうどん。",
        "genre": "麺類",
        "protein": 28.0, "fat": 10.0, "carbs": 54.0, "calories": 418,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("サバ缶", "1缶"), ("うどん", "2玉"), ("ほうれん草", "1/2束")]
    },
    # ===== イワシ缶 =====
    {
        "name": "イワシ缶ともやしのスープ",
        "description": "イワシ缶のDHAで頭も体もパワーアップスープ。",
        "genre": "スープ",
        "protein": 22.0, "fat": 8.0, "carbs": 4.0, "calories": 178,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("イワシ缶", "1缶"), ("もやし", "1袋")]
    },
    {
        "name": "イワシ缶とキャベツの煮浸し",
        "description": "イワシのうまみがキャベツに染み込んだ煮浸し。",
        "genre": "煮物",
        "protein": 20.0, "fat": 8.0, "carbs": 6.0, "calories": 174,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("イワシ缶", "1缶"), ("キャベツ", "1/4個")]
    },
    {
        "name": "イワシ缶丼",
        "description": "手軽に作れるイワシ缶丼。コスパ最高の一品。",
        "genre": "丼",
        "protein": 26.0, "fat": 9.0, "carbs": 62.0, "calories": 434,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("イワシ缶", "1缶"), ("米", "2合")]
    },
    {
        "name": "イワシ缶のみそ汁",
        "description": "イワシ入りの具だくさんみそ汁。カルシウムも豊富。",
        "genre": "スープ",
        "protein": 20.0, "fat": 8.0, "carbs": 5.0, "calories": 170,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("イワシ缶", "1缶"), ("小松菜", "1束")]
    },
    {
        "name": "イワシ缶とブロッコリーのサラダ",
        "description": "オリーブ油風味のブロッコリーサラダ。",
        "genre": "サラダ",
        "protein": 22.0, "fat": 9.0, "carbs": 5.0, "calories": 186,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("イワシ缶", "1缶"), ("ブロッコリー", "1/2株")]
    },
    # ===== 複合レシピ =====
    {
        "name": "鶏むね肉と卵のガパオライス風",
        "description": "バジル風味の本格ガパオライス風。高タンパクな一皿。",
        "genre": "丼",
        "protein": 48.0, "fat": 10.0, "carbs": 64.0, "calories": 532,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "200g"), ("卵", "2個"), ("玉ねぎ", "1/2個"), ("米", "2合")]
    },
    {
        "name": "豆腐と鶏ひき肉の卵炒め",
        "description": "豆腐と鶏ひき肉と卵の三重タンパク炒め。",
        "genre": "炒め物",
        "protein": 42.0, "fat": 12.0, "carbs": 5.0, "calories": 296,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豆腐", "1丁"), ("鶏ひき肉", "150g"), ("卵", "2個")]
    },
    {
        "name": "サバ缶と豆腐のみそ汁",
        "description": "旨味二重のサバ豆腐みそ汁。タンパク質豊富。",
        "genre": "スープ",
        "protein": 30.0, "fat": 12.0, "carbs": 5.0, "calories": 246,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("サバ缶", "1缶"), ("豆腐", "1丁")]
    },
    {
        "name": "ツナと厚揚げのサラダ",
        "description": "タンパク質ダブルのボリュームサラダ。満腹感高い。",
        "genre": "サラダ",
        "protein": 34.0, "fat": 14.0, "carbs": 5.0, "calories": 290,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ツナ缶", "1缶"), ("厚揚げ", "1枚"), ("ブロッコリー", "1/4株")]
    },
    {
        "name": "鶏むね肉とサバ缶のスープ",
        "description": "2種のタンパク源を合わせた贅沢スープ。",
        "genre": "スープ",
        "protein": 50.0, "fat": 8.0, "carbs": 4.0, "calories": 286,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "150g"), ("サバ缶", "1缶"), ("小松菜", "1束")]
    },
    {
        "name": "豚こまと卵のチャーハン",
        "description": "パラパラ炒飯。卵と豚こまで高タンパク。",
        "genre": "中華",
        "protein": 28.0, "fat": 12.0, "carbs": 62.0, "calories": 470,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚こま", "150g"), ("卵", "2個"), ("米", "2合")]
    },
    {
        "name": "鶏ひき肉と納豆の丼",
        "description": "発酵食品と高タンパクを組み合わせた健康丼。",
        "genre": "丼",
        "protein": 46.0, "fat": 12.0, "carbs": 62.0, "calories": 536,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏ひき肉", "200g"), ("納豆", "2パック"), ("米", "2合")]
    },
    {
        "name": "豚ひき肉と豆腐の担々麺",
        "description": "低脂質な担々麺。豆腐でボリュームアップ。",
        "genre": "麺類",
        "protein": 34.0, "fat": 14.0, "carbs": 54.0, "calories": 474,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("豚ひき肉", "150g"), ("豆腐", "1/2丁"), ("うどん", "2玉")]
    },
    {
        "name": "ちくわと卵の炒め物",
        "description": "コスパ最高のちくわ卵炒め。手軽に作れる一品。",
        "genre": "炒め物",
        "protein": 20.0, "fat": 9.0, "carbs": 12.0, "calories": 210,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ちくわ", "3本"), ("卵", "2個")]
    },
    {
        "name": "サバ缶と厚揚げの煮物",
        "description": "サバのうまみが厚揚げに染み込む和風煮物。",
        "genre": "煮物",
        "protein": 38.0, "fat": 18.0, "carbs": 5.0, "calories": 330,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("サバ缶", "1缶"), ("厚揚げ", "1枚")]
    },
    {
        "name": "イワシ缶とちくわのスープ",
        "description": "魚介のうまみたっぷりのヘルシースープ。",
        "genre": "スープ",
        "protein": 28.0, "fat": 8.0, "carbs": 12.0, "calories": 234,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("イワシ缶", "1缶"), ("ちくわ", "3本")]
    },
    {
        "name": "鶏むね肉と豆腐のヘルシーバーグ",
        "description": "豆腐で増量した低カロリーチキンバーグ。",
        "genre": "洋食",
        "protein": 40.0, "fat": 7.0, "carbs": 8.0, "calories": 254,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "200g"), ("豆腐", "1/2丁"), ("玉ねぎ", "1/4個")]
    },
    {
        "name": "納豆とイワシ缶の混ぜそば",
        "description": "栄養価抜群の混ぜそば。発酵食品とDHA両取り。",
        "genre": "麺類",
        "protein": 30.0, "fat": 10.0, "carbs": 50.0, "calories": 410,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("納豆", "2パック"), ("イワシ缶", "1缶"), ("そば", "2玉")]
    },
    # ===== オートミール系 =====
    {
        "name": "オートミールと鶏むね肉のリゾット",
        "description": "オートミールをリゾット風に。クリーミーで高タンパク。",
        "genre": "洋食",
        "protein": 36.0, "fat": 4.0, "carbs": 34.0, "calories": 318,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("オートミール", "80g"), ("鶏むね肉", "200g"), ("玉ねぎ", "1/4個")]
    },
    {
        "name": "オートミールとサバ缶の雑炊",
        "description": "サバ缶の旨味たっぷりオートミール雑炊。",
        "genre": "その他",
        "protein": 28.0, "fat": 10.0, "carbs": 32.0, "calories": 330,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("オートミール", "80g"), ("サバ缶", "1缶")]
    },
    {
        "name": "オートミールと卵の雑炊",
        "description": "卵でとじたやさしい味の雑炊。消化も良い。",
        "genre": "その他",
        "protein": 18.0, "fat": 8.0, "carbs": 34.0, "calories": 282,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("オートミール", "80g"), ("卵", "2個"), ("小松菜", "1/2束")]
    },
    {
        "name": "オートミールのツナ雑炊",
        "description": "ツナとオートミールの低カロリー雑炊。",
        "genre": "その他",
        "protein": 22.0, "fat": 5.0, "carbs": 32.0, "calories": 258,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("オートミール", "80g"), ("ツナ缶", "1缶")]
    },
    # ===== そば系 =====
    {
        "name": "冷しゃぶそば",
        "description": "豚こまを茹でて冷たいそばにのせた夏の一品。",
        "genre": "麺類",
        "protein": 28.0, "fat": 9.0, "carbs": 50.0, "calories": 398,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("そば", "2玉"), ("豚こま", "150g")]
    },
    {
        "name": "鶏むね肉のおろしそば",
        "description": "蒸し鶏と大根おろしのさっぱりそば。",
        "genre": "麺類",
        "protein": 36.0, "fat": 3.5, "carbs": 50.0, "calories": 374,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("そば", "2玉"), ("鶏むね肉", "200g")]
    },
    {
        "name": "サバ缶そば",
        "description": "サバ缶のうまみをそばに。手軽な高タンパク麺。",
        "genre": "麺類",
        "protein": 28.0, "fat": 10.0, "carbs": 48.0, "calories": 394,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("そば", "2玉"), ("サバ缶", "1缶"), ("ほうれん草", "1/2束")]
    },
    # ===== もやし系 =====
    {
        "name": "もやしの醤油炒め",
        "description": "もやしだけのシンプル炒め。低カロリーの副菜。",
        "genre": "炒め物",
        "protein": 4.0, "fat": 3.0, "carbs": 4.0, "calories": 58,
        "servings": 2, "cooking_time": 5,
        "ingredients": [("もやし", "1袋")]
    },
    {
        "name": "もやしとキャベツの塩炒め",
        "description": "野菜だけのシンプルな炒め物。副菜に最適。",
        "genre": "炒め物",
        "protein": 4.0, "fat": 3.5, "carbs": 7.0, "calories": 76,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("もやし", "1袋"), ("キャベツ", "1/4個")]
    },
    {
        "name": "もやしと卵のスープ",
        "description": "もやしと卵のシンプルスープ。低カロリーで満足。",
        "genre": "スープ",
        "protein": 12.0, "fat": 6.0, "carbs": 4.0, "calories": 118,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("もやし", "1袋"), ("卵", "2個")]
    },
    # ===== ブロッコリー系 =====
    {
        "name": "ブロッコリーの卵炒め",
        "description": "ブロッコリーと卵のシンプル炒め。ビタミンC豊富。",
        "genre": "炒め物",
        "protein": 14.0, "fat": 8.0, "carbs": 7.0, "calories": 158,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ブロッコリー", "1株"), ("卵", "2個")]
    },
    {
        "name": "ブロッコリーとツナのマヨサラダ",
        "description": "マヨネーズ少なめのヘルシーサラダ。",
        "genre": "サラダ",
        "protein": 20.0, "fat": 7.0, "carbs": 6.0, "calories": 166,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ブロッコリー", "1/2株"), ("ツナ缶", "1缶")]
    },
    # ===== ミックス系・追加 =====
    {
        "name": "鶏むね肉とオートミールのデミグラ風",
        "description": "デミグラスソース風に仕上げた洋風鶏むね肉。",
        "genre": "洋食",
        "protein": 38.0, "fat": 5.0, "carbs": 36.0, "calories": 342,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "250g"), ("オートミール", "60g"), ("玉ねぎ", "1/2個")]
    },
    {
        "name": "豚こまと玉ねぎの甘酢炒め",
        "description": "甘酢でさっぱり仕上げた豚こま炒め。",
        "genre": "中華",
        "protein": 22.0, "fat": 9.0, "carbs": 12.0, "calories": 222,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚こま", "200g"), ("玉ねぎ", "1個")]
    },
    {
        "name": "鶏ひき肉のそぼろご飯",
        "description": "鶏ひき肉のそぼろをご飯にかけた定番丼。",
        "genre": "丼",
        "protein": 34.0, "fat": 7.0, "carbs": 62.0, "calories": 454,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏ひき肉", "200g"), ("米", "2合"), ("玉ねぎ", "1/4個")]
    },
    {
        "name": "豆腐とブロッコリーのチャンプルー",
        "description": "沖縄風の豆腐と野菜の炒め物。素朴な味わい。",
        "genre": "炒め物",
        "protein": 18.0, "fat": 8.0, "carbs": 6.0, "calories": 166,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豆腐", "1丁"), ("ブロッコリー", "1/2株")]
    },
    {
        "name": "鶏むね肉のバンバンジー",
        "description": "ごまだれをかけた本格バンバンジー。高タンパク前菜。",
        "genre": "中華",
        "protein": 40.0, "fat": 8.0, "carbs": 5.0, "calories": 254,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "250g"), ("キャベツ", "1/4個")]
    },
    {
        "name": "サバ缶カレー",
        "description": "サバ缶で作る時短カレー。旨味が濃厚。",
        "genre": "洋食",
        "protein": 28.0, "fat": 12.0, "carbs": 66.0, "calories": 490,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("サバ缶", "1缶"), ("玉ねぎ", "1個"), ("にんじん", "1本"), ("米", "2合")]
    },
    {
        "name": "厚揚げと卵の炒め物",
        "description": "厚揚げと卵のシンプル炒め。タンパク質豊富。",
        "genre": "炒め物",
        "protein": 26.0, "fat": 14.0, "carbs": 4.0, "calories": 250,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("厚揚げ", "1枚"), ("卵", "2個")]
    },
    {
        "name": "イワシ缶とオートミールのスープご飯",
        "description": "イワシ缶とオートミールで作る低GIスープ飯。",
        "genre": "スープ",
        "protein": 24.0, "fat": 8.0, "carbs": 32.0, "calories": 298,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("イワシ缶", "1缶"), ("オートミール", "80g")]
    },
    {
        "name": "鶏むね肉のレモン塩炒め",
        "description": "レモンでさっぱり仕上げた低脂質炒め。",
        "genre": "炒め物",
        "protein": 40.0, "fat": 4.5, "carbs": 3.0, "calories": 214,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏むね肉", "250g"), ("ブロッコリー", "1/4株")]
    },
    {
        "name": "納豆と豆腐の冷スープ",
        "description": "夏に嬉しい冷たい豆乳スープ。発酵食品ダブル。",
        "genre": "スープ",
        "protein": 22.0, "fat": 9.0, "carbs": 8.0, "calories": 202,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("納豆", "2パック"), ("豆腐", "1/2丁")]
    },
    {
        "name": "豚こまとにんじんの煮物",
        "description": "にんじんと豚こまの甘辛煮。彩りも良い。",
        "genre": "煮物",
        "protein": 20.0, "fat": 9.0, "carbs": 10.0, "calories": 206,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("豚こま", "150g"), ("にんじん", "1本")]
    },
    {
        "name": "キャベツともやしのツナ和え",
        "description": "野菜たっぷりのツナ和えサラダ。",
        "genre": "サラダ",
        "protein": 18.0, "fat": 5.0, "carbs": 8.0, "calories": 150,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("キャベツ", "1/4個"), ("もやし", "1/2袋"), ("ツナ缶", "1缶")]
    },
    {
        "name": "ほうれん草と卵のスープ",
        "description": "溶き卵を入れたほうれん草のシンプルスープ。",
        "genre": "スープ",
        "protein": 14.0, "fat": 7.0, "carbs": 4.0, "calories": 138,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ほうれん草", "1束"), ("卵", "2個")]
    },
    {
        "name": "鶏むね肉のにんじんスープ",
        "description": "にんじんたっぷりの栄養満点スープ。",
        "genre": "スープ",
        "protein": 34.0, "fat": 3.5, "carbs": 10.0, "calories": 210,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "200g"), ("にんじん", "1本"), ("玉ねぎ", "1/4個")]
    },
    {
        "name": "鶏ひき肉と厚揚げの甘辛煮",
        "description": "甘辛だれがよく合う鶏ひき肉と厚揚げの煮物。",
        "genre": "煮物",
        "protein": 36.0, "fat": 14.0, "carbs": 6.0, "calories": 290,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏ひき肉", "200g"), ("厚揚げ", "1枚")]
    },
    {
        "name": "ツナとにんじんのきんぴら",
        "description": "ツナ入りのヘルシーきんぴら。食物繊維たっぷり。",
        "genre": "和食",
        "protein": 18.0, "fat": 5.0, "carbs": 10.0, "calories": 158,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("ツナ缶", "1缶"), ("にんじん", "1本")]
    },
    {
        "name": "豚ひき肉の韓国風スープ",
        "description": "ごまとにんにくが効いた韓国風ピリ辛スープ。",
        "genre": "スープ",
        "protein": 26.0, "fat": 12.0, "carbs": 6.0, "calories": 236,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚ひき肉", "200g"), ("もやし", "1袋"), ("小松菜", "1/2束")]
    },
    {
        "name": "鶏むね肉のタイ風スープ",
        "description": "ナンプラー風味のエスニックスープ。",
        "genre": "スープ",
        "protein": 36.0, "fat": 4.0, "carbs": 6.0, "calories": 206,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "200g"), ("もやし", "1/2袋"), ("にんじん", "1/2本")]
    },
    {
        "name": "サバ缶とほうれん草のスープ",
        "description": "鉄分とDHA両方とれるスーパースープ。",
        "genre": "スープ",
        "protein": 26.0, "fat": 10.0, "carbs": 4.0, "calories": 214,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("サバ缶", "1缶"), ("ほうれん草", "1束")]
    },
    {
        "name": "豆腐ともやしのキムチ炒め",
        "description": "キムチの辛味でご飯が進む低カロリー炒め。",
        "genre": "炒め物",
        "protein": 16.0, "fat": 7.0, "carbs": 6.0, "calories": 152,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豆腐", "1丁"), ("もやし", "1/2袋")]
    },
    {
        "name": "鶏むね肉とにんじんのきんぴら",
        "description": "にんじんとチキンのきんぴら風炒め。食物繊維も豊富。",
        "genre": "炒め物",
        "protein": 38.0, "fat": 4.0, "carbs": 10.0, "calories": 230,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏むね肉", "200g"), ("にんじん", "1本")]
    },
    {
        "name": "豚ひき肉とほうれん草の炒め",
        "description": "鉄分と亜鉛が豊富な栄養炒め。",
        "genre": "炒め物",
        "protein": 24.0, "fat": 12.0, "carbs": 3.0, "calories": 220,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豚ひき肉", "180g"), ("ほうれん草", "1束")]
    },
    {
        "name": "ちくわとにんじんの炒め煮",
        "description": "ちくわとにんじんのシンプル炒め煮。",
        "genre": "煮物",
        "protein": 14.0, "fat": 2.5, "carbs": 14.0, "calories": 136,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("ちくわ", "4本"), ("にんじん", "1本")]
    },
    {
        "name": "厚揚げとほうれん草の炒め",
        "description": "厚揚げとほうれん草のシンプル炒め。ボリューム満点。",
        "genre": "炒め物",
        "protein": 20.0, "fat": 12.0, "carbs": 4.0, "calories": 208,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("厚揚げ", "1枚"), ("ほうれん草", "1束")]
    },
    {
        "name": "イワシ缶と野菜のスープパスタ風うどん",
        "description": "イワシ缶ベースのスープに野菜をたっぷり。",
        "genre": "麺類",
        "protein": 26.0, "fat": 9.0, "carbs": 54.0, "calories": 406,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("イワシ缶", "1缶"), ("うどん", "2玉"), ("玉ねぎ", "1/4個")]
    },
    {
        "name": "鶏むね肉とブロッコリーのリゾット",
        "description": "オートミールで作るヘルシーリゾット。",
        "genre": "洋食",
        "protein": 40.0, "fat": 5.0, "carbs": 32.0, "calories": 334,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "200g"), ("ブロッコリー", "1/2株"), ("オートミール", "80g")]
    },
    {
        "name": "豆腐と納豆のみそ汁",
        "description": "豆腐と納豆の豆づくしみそ汁。イソフラボン豊富。",
        "genre": "スープ",
        "protein": 20.0, "fat": 8.0, "carbs": 8.0, "calories": 184,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豆腐", "1/2丁"), ("納豆", "1パック")]
    },
    {
        "name": "豚こまと小松菜の炒め",
        "description": "シンプルな塩味の炒め物。副菜にもメインにも。",
        "genre": "炒め物",
        "protein": 22.0, "fat": 9.5, "carbs": 3.0, "calories": 190,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豚こま", "180g"), ("小松菜", "1束")]
    },
    {
        "name": "サバ缶と玉ねぎのサラダ",
        "description": "玉ねぎとサバ缶のシンプルサラダ。血液さらさら。",
        "genre": "サラダ",
        "protein": 24.0, "fat": 10.0, "carbs": 8.0, "calories": 222,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("サバ缶", "1缶"), ("玉ねぎ", "1/2個")]
    },
    {
        "name": "卵と豆腐の雑炊",
        "description": "優しい味の豆腐卵雑炊。体調不良の時にも。",
        "genre": "その他",
        "protein": 20.0, "fat": 8.0, "carbs": 34.0, "calories": 288,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("卵", "2個"), ("豆腐", "1/2丁"), ("米", "1合")]
    },
    {
        "name": "鶏ひき肉とブロッコリーの炒め",
        "description": "ブロッコリーたっぷりの高タンパク炒め。",
        "genre": "炒め物",
        "protein": 32.0, "fat": 7.0, "carbs": 6.0, "calories": 218,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏ひき肉", "200g"), ("ブロッコリー", "1/2株")]
    },
    {
        "name": "豚ひき肉とキャベツの蒸し餃子風",
        "description": "餃子の皮なしで低カロリーな蒸し餃子風。",
        "genre": "中華",
        "protein": 28.0, "fat": 12.0, "carbs": 6.0, "calories": 242,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("豚ひき肉", "200g"), ("キャベツ", "1/4個")]
    },
    {
        "name": "鶏むね肉とキャベツのコールスロー丼",
        "description": "コールスロー風キャベツをのせた食感が良い丼。",
        "genre": "丼",
        "protein": 40.0, "fat": 5.5, "carbs": 64.0, "calories": 470,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏むね肉", "250g"), ("キャベツ", "1/4個"), ("米", "2合")]
    },
    {
        "name": "ちくわと豆腐のスープ",
        "description": "ちくわと豆腐のあっさりスープ。低カロリーで満足。",
        "genre": "スープ",
        "protein": 20.0, "fat": 5.0, "carbs": 12.0, "calories": 174,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ちくわ", "3本"), ("豆腐", "1/2丁")]
    },
    {
        "name": "イワシ缶とにんじんの煮物",
        "description": "にんじんの甘みとイワシのうまみが合う煮物。",
        "genre": "煮物",
        "protein": 20.0, "fat": 8.0, "carbs": 10.0, "calories": 194,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("イワシ缶", "1缶"), ("にんじん", "1本")]
    },
    {
        "name": "鶏むね肉と小松菜の塩炒め",
        "description": "小松菜たっぷりの低カロリー炒め。",
        "genre": "炒め物",
        "protein": 38.0, "fat": 4.2, "carbs": 3.0, "calories": 205,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏むね肉", "230g"), ("小松菜", "1束")]
    },
    {
        "name": "ツナとキャベツのスープ",
        "description": "ツナとキャベツのシンプルスープ。低カロリー。",
        "genre": "スープ",
        "protein": 18.0, "fat": 5.0, "carbs": 7.0, "calories": 146,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ツナ缶", "1缶"), ("キャベツ", "1/4個")]
    },
    {
        "name": "豚こまと卵のオートミール丼",
        "description": "オートミールをご飯代わりにした低GI丼。",
        "genre": "丼",
        "protein": 28.0, "fat": 11.0, "carbs": 36.0, "calories": 358,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚こま", "180g"), ("卵", "1個"), ("オートミール", "80g")]
    },
    {
        "name": "厚揚げとブロッコリーのみそ炒め",
        "description": "みそ風味の香ばしい厚揚げ炒め。",
        "genre": "炒め物",
        "protein": 22.0, "fat": 12.0, "carbs": 7.0, "calories": 226,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("厚揚げ", "1枚"), ("ブロッコリー", "1/2株")]
    },
    {
        "name": "サバ缶とにんじんのカレー風炒め",
        "description": "カレー粉で風味付けしたサバとにんじんの炒め物。",
        "genre": "洋食",
        "protein": 24.0, "fat": 10.0, "carbs": 10.0, "calories": 226,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("サバ缶", "1缶"), ("にんじん", "1本")]
    },
    {
        "name": "鶏ひき肉と玉ねぎの和風ハンバーグ",
        "description": "ポン酢をかけたさっぱり和風ハンバーグ。",
        "genre": "洋食",
        "protein": 36.0, "fat": 10.0, "carbs": 8.0, "calories": 266,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏ひき肉", "250g"), ("玉ねぎ", "1/2個")]
    },
    {
        "name": "納豆とツナの混ぜご飯",
        "description": "発酵食品とツナの栄養素たっぷり混ぜご飯。",
        "genre": "丼",
        "protein": 32.0, "fat": 10.0, "carbs": 62.0, "calories": 470,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("納豆", "2パック"), ("ツナ缶", "1缶"), ("米", "2合")]
    },
    {
        "name": "豆腐と厚揚げのみそ汁",
        "description": "タンパク質豊富な豆製品みそ汁。朝食に最適。",
        "genre": "スープ",
        "protein": 22.0, "fat": 12.0, "carbs": 4.0, "calories": 214,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豆腐", "1/2丁"), ("厚揚げ", "1/2枚")]
    },
    {
        "name": "豚こまとブロッコリーの炒め",
        "description": "ブロッコリーで栄養価アップした豚こま炒め。",
        "genre": "炒め物",
        "protein": 26.0, "fat": 10.0, "carbs": 6.0, "calories": 222,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚こま", "200g"), ("ブロッコリー", "1/2株")]
    },
    {
        "name": "ツナとオートミールのお好み焼き風",
        "description": "小麦粉不使用のオートミールお好み焼き風。",
        "genre": "その他",
        "protein": 22.0, "fat": 6.0, "carbs": 34.0, "calories": 278,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("ツナ缶", "1缶"), ("オートミール", "80g"), ("キャベツ", "1/4個"), ("卵", "1個")]
    },
    {
        "name": "鶏むね肉のよだれ鶏",
        "description": "花椒と辣油のピリ辛タレをかけた本格よだれ鶏。",
        "genre": "中華",
        "protein": 42.0, "fat": 7.0, "carbs": 4.0, "calories": 250,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "250g")]
    },
    {
        "name": "鶏むね肉のカレー炒め",
        "description": "カレー粉で味付けした食欲増進炒め物。",
        "genre": "炒め物",
        "protein": 38.0, "fat": 5.0, "carbs": 6.0, "calories": 222,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏むね肉", "230g"), ("玉ねぎ", "1/2個")]
    },
    {
        "name": "豆腐の卵とじ丼",
        "description": "豆腐を卵でとじた低カロリー丼。",
        "genre": "丼",
        "protein": 26.0, "fat": 10.0, "carbs": 62.0, "calories": 446,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豆腐", "1丁"), ("卵", "2個"), ("米", "2合"), ("玉ねぎ", "1/4個")]
    },
    {
        "name": "サバ缶と小松菜の炒め",
        "description": "鉄分とDHAがとれるパワーフード炒め。",
        "genre": "炒め物",
        "protein": 24.0, "fat": 10.0, "carbs": 3.0, "calories": 202,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("サバ缶", "1缶"), ("小松菜", "1束")]
    },
    {
        "name": "豚ひき肉とブロッコリーの炒め",
        "description": "ブロッコリーたっぷりの食べ応えある炒め物。",
        "genre": "炒め物",
        "protein": 28.0, "fat": 13.0, "carbs": 6.0, "calories": 254,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚ひき肉", "200g"), ("ブロッコリー", "1/2株")]
    },
    {
        "name": "ちくわと小松菜の炒め煮",
        "description": "ちくわと小松菜を甘辛に炒め煮した和食。",
        "genre": "煮物",
        "protein": 14.0, "fat": 3.0, "carbs": 10.0, "calories": 122,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ちくわ", "4本"), ("小松菜", "1束")]
    },
    {
        "name": "鶏ひき肉ともやしのスープ",
        "description": "ヘルシーで腹持ちの良いクリアスープ。",
        "genre": "スープ",
        "protein": 26.0, "fat": 5.5, "carbs": 4.0, "calories": 170,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("鶏ひき肉", "180g"), ("もやし", "1袋")]
    },
    {
        "name": "厚揚げとにんじんのきんぴら",
        "description": "きんぴら風に仕上げた厚揚げのおかず。",
        "genre": "和食",
        "protein": 18.0, "fat": 10.0, "carbs": 10.0, "calories": 202,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("厚揚げ", "1枚"), ("にんじん", "1本")]
    },
    {
        "name": "イワシ缶とほうれん草の炒め",
        "description": "鉄分とDHAダブル補給の栄養炒め。",
        "genre": "炒め物",
        "protein": 22.0, "fat": 8.0, "carbs": 3.0, "calories": 174,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("イワシ缶", "1缶"), ("ほうれん草", "1束")]
    },
    {
        "name": "鶏むね肉と玉ねぎのポトフ風",
        "description": "コンソメベースの洋風スープ煮。体が温まる。",
        "genre": "洋食",
        "protein": 36.0, "fat": 4.5, "carbs": 10.0, "calories": 226,
        "servings": 2, "cooking_time": 25,
        "ingredients": [("鶏むね肉", "220g"), ("玉ねぎ", "1個"), ("にんじん", "1/2本")]
    },
    {
        "name": "豚ひき肉とオートミールの雑炊",
        "description": "満腹感の高いひき肉オートミール雑炊。",
        "genre": "その他",
        "protein": 26.0, "fat": 12.0, "carbs": 32.0, "calories": 340,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豚ひき肉", "180g"), ("オートミール", "80g")]
    },
    {
        "name": "鶏むね肉のユーリンチー",
        "description": "長ねぎたれがさっぱりの揚げない油淋鶏。",
        "genre": "中華",
        "protein": 40.0, "fat": 6.0, "carbs": 8.0, "calories": 250,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "250g"), ("玉ねぎ", "1/4個")]
    },
    {
        "name": "豚こまとキャベツのみそ炒め",
        "description": "みそ味の香ばしい豚こまとキャベツ炒め。",
        "genre": "炒め物",
        "protein": 22.0, "fat": 9.5, "carbs": 9.0, "calories": 210,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豚こま", "180g"), ("キャベツ", "1/4個")]
    },
    {
        "name": "納豆とブロッコリーのサラダ",
        "description": "納豆とブロッコリーの意外な組み合わせサラダ。",
        "genre": "サラダ",
        "protein": 20.0, "fat": 8.0, "carbs": 8.0, "calories": 182,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("納豆", "2パック"), ("ブロッコリー", "1/2株")]
    },
    {
        "name": "鶏むね肉のチーズ焼き風",
        "description": "とろけるチーズがけのヘルシーチキン焼き。",
        "genre": "洋食",
        "protein": 44.0, "fat": 8.0, "carbs": 2.0, "calories": 256,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "250g"), ("ほうれん草", "1/2束")]
    },
    {
        "name": "豆腐の麻婆茄子風",
        "description": "豆腐を茄子代わりに使った麻婆豆腐アレンジ。",
        "genre": "中華",
        "protein": 22.0, "fat": 8.0, "carbs": 6.0, "calories": 182,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豆腐", "1丁"), ("豚ひき肉", "100g")]
    },
    {
        "name": "サバ缶と豆腐のチゲ風",
        "description": "サバ缶と豆腐のピリ辛韓国風スープ。",
        "genre": "スープ",
        "protein": 32.0, "fat": 12.0, "carbs": 5.0, "calories": 258,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("サバ缶", "1缶"), ("豆腐", "1/2丁")]
    },
    {
        "name": "鶏ひき肉と卵のオムレツ",
        "description": "鶏ひき肉入りの高タンパクオムレツ。",
        "genre": "洋食",
        "protein": 32.0, "fat": 14.0, "carbs": 3.0, "calories": 266,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏ひき肉", "150g"), ("卵", "3個")]
    },
    {
        "name": "ツナとそばのサラダそば",
        "description": "ツナとそばで作るサラダ感覚の冷麺。",
        "genre": "麺類",
        "protein": 26.0, "fat": 7.0, "carbs": 50.0, "calories": 374,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("ツナ缶", "1缶"), ("そば", "2玉"), ("キャベツ", "1/4個")]
    },
    {
        "name": "厚揚げとキャベツのみそ汁",
        "description": "具だくさんのボリュームみそ汁。食べるスープ。",
        "genre": "スープ",
        "protein": 18.0, "fat": 10.0, "carbs": 8.0, "calories": 194,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("厚揚げ", "1枚"), ("キャベツ", "1/4個")]
    },
    {
        "name": "豚こまと玉ねぎのうどん",
        "description": "豚こまのうまみが染み出たあっさりうどん。",
        "genre": "麺類",
        "protein": 24.0, "fat": 9.0, "carbs": 56.0, "calories": 406,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚こま", "150g"), ("うどん", "2玉"), ("玉ねぎ", "1/2個")]
    },
    {
        "name": "鶏むね肉とオートミールのスープ",
        "description": "腹持ちの良いオートミールスープ。ダイエットに最適。",
        "genre": "スープ",
        "protein": 34.0, "fat": 3.5, "carbs": 28.0, "calories": 278,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏むね肉", "200g"), ("オートミール", "60g"), ("にんじん", "1/2本")]
    },
    # ===== 追加レシピ =====
    {
        "name": "鶏むね肉と小松菜の卵スープ",
        "description": "卵でとじた優しいスープ。タンパク質三重摂取。",
        "genre": "スープ",
        "protein": 40.0, "fat": 7.0, "carbs": 3.0, "calories": 238,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏むね肉", "200g"), ("小松菜", "1束"), ("卵", "1個")]
    },
    {
        "name": "豆腐ともやしの卵炒め",
        "description": "三つのタンパク源を一度に摂れるコスパ抜群の炒め物。",
        "genre": "炒め物",
        "protein": 22.0, "fat": 10.0, "carbs": 5.0, "calories": 198,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豆腐", "1丁"), ("もやし", "1/2袋"), ("卵", "2個")]
    },
    {
        "name": "サバ缶ともやしのキムチ炒め",
        "description": "サバとキムチの旨辛コンビ。腸活にも効果的。",
        "genre": "炒め物",
        "protein": 24.0, "fat": 10.0, "carbs": 6.0, "calories": 210,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("サバ缶", "1缶"), ("もやし", "1袋")]
    },
    {
        "name": "ツナと豆腐の炒め物",
        "description": "ツナと豆腐のタンパク質ダブル炒め。シンプルで美味。",
        "genre": "炒め物",
        "protein": 30.0, "fat": 7.0, "carbs": 4.0, "calories": 196,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ツナ缶", "1缶"), ("豆腐", "1丁")]
    },
    {
        "name": "鶏ひき肉と小松菜の和風煮",
        "description": "出汁が染み込んだほっこりする和風煮物。",
        "genre": "煮物",
        "protein": 30.0, "fat": 6.0, "carbs": 4.0, "calories": 190,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("鶏ひき肉", "200g"), ("小松菜", "1束")]
    },
    {
        "name": "豚こまとほうれん草のスープ",
        "description": "鉄分豊富なほうれん草と豚こまのあっさりスープ。",
        "genre": "スープ",
        "protein": 22.0, "fat": 9.0, "carbs": 4.0, "calories": 190,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚こま", "150g"), ("ほうれん草", "1束")]
    },
    {
        "name": "厚揚げと玉ねぎの甘辛煮",
        "description": "玉ねぎの甘みで引き立つ厚揚げの甘辛煮。ご飯に合う。",
        "genre": "煮物",
        "protein": 18.0, "fat": 11.0, "carbs": 9.0, "calories": 206,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("厚揚げ", "1枚"), ("玉ねぎ", "1/2個")]
    },
    {
        "name": "納豆と卵の炒め物",
        "description": "納豆と卵の栄養満点炒め。ご飯によく合う。",
        "genre": "炒め物",
        "protein": 20.0, "fat": 10.0, "carbs": 7.0, "calories": 198,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("納豆", "2パック"), ("卵", "2個")]
    },
    {
        "name": "イワシ缶と野菜の炒め煮",
        "description": "イワシ缶と彩り野菜の炒め煮。EPAで健康増進。",
        "genre": "煮物",
        "protein": 22.0, "fat": 8.0, "carbs": 8.0, "calories": 194,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("イワシ缶", "1缶"), ("キャベツ", "1/4個"), ("にんじん", "1/2本")]
    },
    {
        "name": "鶏むね肉と玉ねぎのさっぱり煮",
        "description": "酢を使ったさっぱり風味の鶏むね煮。",
        "genre": "煮物",
        "protein": 38.0, "fat": 4.0, "carbs": 8.0, "calories": 226,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "230g"), ("玉ねぎ", "1/2個")]
    },
    {
        "name": "ちくわとブロッコリーの卵炒め",
        "description": "ちくわとブロッコリーと卵の三種炒め。",
        "genre": "炒め物",
        "protein": 22.0, "fat": 9.0, "carbs": 14.0, "calories": 226,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ちくわ", "4本"), ("ブロッコリー", "1/2株"), ("卵", "2個")]
    },
    {
        "name": "豚ひき肉と厚揚げの丼",
        "description": "ひき肉と厚揚げを甘辛に仕上げたボリューム丼。",
        "genre": "丼",
        "protein": 40.0, "fat": 18.0, "carbs": 62.0, "calories": 570,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚ひき肉", "150g"), ("厚揚げ", "1枚"), ("米", "2合")]
    },
    {
        "name": "鶏むね肉のつけそば",
        "description": "蒸し鶏を使ったつけそば。ヘルシーで食べ応え抜群。",
        "genre": "麺類",
        "protein": 42.0, "fat": 4.0, "carbs": 50.0, "calories": 400,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "250g"), ("そば", "2玉")]
    },
    {
        "name": "豚こまとオートミールのスープ",
        "description": "オートミール入りで腹持ちのいい豚こまスープ。",
        "genre": "スープ",
        "protein": 22.0, "fat": 9.0, "carbs": 30.0, "calories": 290,
        "servings": 2, "cooking_time": 15,
        "ingredients": [("豚こま", "150g"), ("オートミール", "60g"), ("玉ねぎ", "1/4個")]
    },
    {
        "name": "ツナとちくわのうどん",
        "description": "魚介旨味ダブルのヘルシーうどん。コスパ最高。",
        "genre": "麺類",
        "protein": 26.0, "fat": 5.0, "carbs": 54.0, "calories": 370,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ツナ缶", "1缶"), ("ちくわ", "3本"), ("うどん", "2玉")]
    },
    {
        "name": "サバ缶と卵の炒め物",
        "description": "サバ缶と卵のシンプル炒め。EPAとタンパク質を同時に。",
        "genre": "炒め物",
        "protein": 28.0, "fat": 14.0, "carbs": 2.0, "calories": 246,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("サバ缶", "1缶"), ("卵", "2個")]
    },
    {
        "name": "鶏ひき肉とにんじんの炒め",
        "description": "にんじんの甘みと鶏ひき肉の旨味がマッチ。",
        "genre": "炒め物",
        "protein": 26.0, "fat": 6.5, "carbs": 9.0, "calories": 198,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("鶏ひき肉", "180g"), ("にんじん", "1本")]
    },
    {
        "name": "豆腐とにんじんの卵スープ",
        "description": "卵でとじた彩り豊かな豆腐スープ。",
        "genre": "スープ",
        "protein": 18.0, "fat": 8.0, "carbs": 9.0, "calories": 178,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("豆腐", "1/2丁"), ("にんじん", "1/2本"), ("卵", "2個")]
    },
    {
        "name": "イワシ缶と豆腐のスープ",
        "description": "イワシと豆腐でタンパク質をしっかり補給できるスープ。",
        "genre": "スープ",
        "protein": 28.0, "fat": 10.0, "carbs": 4.0, "calories": 218,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("イワシ缶", "1缶"), ("豆腐", "1/2丁")]
    },
    {
        "name": "鶏むね肉のそばサラダ",
        "description": "蒸し鶏と野菜を添えたそばサラダ。低脂質で満足感。",
        "genre": "麺類",
        "protein": 38.0, "fat": 4.0, "carbs": 50.0, "calories": 386,
        "servings": 2, "cooking_time": 20,
        "ingredients": [("鶏むね肉", "200g"), ("そば", "2玉"), ("もやし", "1/2袋")]
    },
    {
        "name": "ちくわと玉ねぎのみそ汁",
        "description": "コスパ最強のちくわ玉ねぎみそ汁。素朴な味わい。",
        "genre": "スープ",
        "protein": 14.0, "fat": 2.5, "carbs": 12.0, "calories": 126,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("ちくわ", "4本"), ("玉ねぎ", "1/2個")]
    },
    {
        "name": "厚揚げともやしのキムチ炒め",
        "description": "厚揚げともやしのピリ辛キムチ炒め。腸活にも。",
        "genre": "炒め物",
        "protein": 20.0, "fat": 12.0, "carbs": 6.0, "calories": 210,
        "servings": 2, "cooking_time": 10,
        "ingredients": [("厚揚げ", "1枚"), ("もやし", "1袋")]
    },
]
