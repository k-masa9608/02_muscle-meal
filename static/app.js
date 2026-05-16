const CATEGORIES = {
  "タンパク質": ["鶏むね肉","鶏ひき肉","豚ひき肉","豚こま","卵","ちくわ","ツナ缶","納豆","豆腐","厚揚げ","サバ缶","イワシ缶"],
  "野菜": ["もやし","キャベツ","ブロッコリー","小松菜","ほうれん草","玉ねぎ","にんじん"],
  "炭水化物": ["米","オートミール","うどん","そば"],
};

const GROUP_IDS = { "タンパク質": "protein-group", "野菜": "veggie-group", "炭水化物": "carb-group" };

let selectedIngredients = new Set();
let currentResults = [];

function init() {
  for (const [cat, items] of Object.entries(CATEGORIES)) {
    const container = document.getElementById(GROUP_IDS[cat]);
    items.forEach(name => {
      const btn = document.createElement("button");
      btn.className = "ing-btn";
      btn.textContent = name;
      btn.dataset.name = name;
      btn.addEventListener("click", () => toggleIngredient(name, btn));
      container.appendChild(btn);
    });
  }

  document.getElementById("keyword-add").addEventListener("click", addKeyword);
  document.getElementById("keyword-input").addEventListener("keydown", e => {
    if (e.key === "Enter") addKeyword();
  });
  document.getElementById("search-btn").addEventListener("click", search);
  document.getElementById("reset-btn").addEventListener("click", reset);
  document.getElementById("modal-close").addEventListener("click", closeModal);
  document.getElementById("modal-overlay").addEventListener("click", e => {
    if (e.target === document.getElementById("modal-overlay")) closeModal();
  });
}

function toggleIngredient(name, btn) {
  if (selectedIngredients.has(name)) {
    selectedIngredients.delete(name);
    btn.classList.remove("active");
  } else {
    selectedIngredients.add(name);
    btn.classList.add("active");
  }
  renderTags();
}

function addKeyword() {
  const input = document.getElementById("keyword-input");
  const val = input.value.trim();
  if (!val) return;
  selectedIngredients.add(val);
  input.value = "";
  renderTags();
}

function renderTags() {
  const container = document.getElementById("selected-tags");
  container.innerHTML = "";
  for (const name of selectedIngredients) {
    const tag = document.createElement("span");
    tag.className = "tag";
    tag.innerHTML = `${name} <span class="tag-remove" data-name="${name}">✕</span>`;
    tag.querySelector(".tag-remove").addEventListener("click", () => removeTag(name));
    container.appendChild(tag);
  }
}

function removeTag(name) {
  selectedIngredients.delete(name);
  const btn = document.querySelector(`.ing-btn[data-name="${name}"]`);
  if (btn) btn.classList.remove("active");
  renderTags();
}

async function search() {
  showLoading(true);
  hideResults();

  try {
    const res = await fetch("/api/search", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ingredients: [...selectedIngredients], limit: 30 }),
    });
    const data = await res.json();
    currentResults = data;
    renderResults(data);
  } catch (e) {
    alert("検索エラーが発生しました。");
  } finally {
    showLoading(false);
  }
}

function renderResults(recipes) {
  const section = document.getElementById("results-section");
  const list = document.getElementById("recipe-list");
  const noResults = document.getElementById("no-results");

  if (!recipes.length) {
    noResults.classList.remove("hidden");
    return;
  }

  section.classList.remove("hidden");
  document.getElementById("results-title").textContent = `検索結果 (${recipes.length}件)`;
  list.innerHTML = "";

  const maxP = Math.max(...recipes.map(r => r.protein), 1);
  const maxF = Math.max(...recipes.map(r => r.fat), 1);
  const maxC = Math.max(...recipes.map(r => r.carbs), 1);
  const barMax = Math.max(maxP, maxF, maxC);

  recipes.forEach((r, i) => {
    const card = document.createElement("div");
    card.className = "recipe-card";
    card.innerHTML = buildCard(r, i, barMax, [...selectedIngredients]);
    card.addEventListener("click", () => openModal(r));
    list.appendChild(card);
    requestAnimationFrame(() => {
      card.querySelectorAll(".bar-fill").forEach(bar => {
        bar.style.width = bar.dataset.width + "%";
      });
    });
  });
}

function buildCard(r, idx, barMax, selected) {
  const rank = idx < 3
    ? `<span class="rank-badge rank-${idx+1}">${idx===0?"🥇":idx===1?"🥈":"🥉"}</span>`
    : `<span class="rank-badge rank-other">${idx+1}</span>`;

  const pW = Math.round((r.protein / barMax) * 100);
  const fW = Math.round((r.fat / barMax) * 100);
  const cW = Math.round((r.carbs / barMax) * 100);

  const ingChips = r.recipe_ingredients.map(ri => {
    const name = ri.ingredient.name;
    const isMatch = selected.includes(name);
    return `<span class="ing-chip ${isMatch ? "matched" : ""}">${name}</span>`;
  }).join("");

  const time = r.cooking_time ? `⏱ ${r.cooking_time}分` : "";
  const serving = r.servings ? `🍽 ${r.servings}人分` : "";

  return `
    <div class="recipe-header">
      <div style="display:flex;align-items:flex-start;gap:4px">
        ${rank}
        <div>
          <div class="recipe-name">${r.name}</div>
          ${r.description ? `<div class="recipe-desc">${r.description}</div>` : ""}
        </div>
      </div>
      <span class="recipe-badge">${r.genre || ""}</span>
    </div>
    <div class="recipe-meta">
      ${time ? `<span>${time}</span>` : ""}
      ${serving ? `<span>${serving}</span>` : ""}
      <span>🔥 ${r.calories}kcal</span>
      ${r.score != null ? `<span class="score-pill">💪 スコア ${r.score}</span>` : ""}
    </div>
    <div class="pfc-section">
      <div class="pfc-numbers">
        <div class="pfc-item p">
          <div class="pfc-label">P タンパク質</div>
          <div class="pfc-value">${r.protein}<span class="pfc-unit">g</span></div>
        </div>
        <div class="pfc-item f">
          <div class="pfc-label">F 脂質</div>
          <div class="pfc-value">${r.fat}<span class="pfc-unit">g</span></div>
        </div>
        <div class="pfc-item c">
          <div class="pfc-label">C 糖質</div>
          <div class="pfc-value">${r.carbs}<span class="pfc-unit">g</span></div>
        </div>
      </div>
      <div class="pfc-bars">
        <div class="bar-row">
          <span class="bar-label p">P</span>
          <div class="bar-track"><div class="bar-fill p" data-width="${pW}" style="width:0%"></div></div>
          <span class="bar-val">${r.protein}g</span>
        </div>
        <div class="bar-row">
          <span class="bar-label f">F</span>
          <div class="bar-track"><div class="bar-fill f" data-width="${fW}" style="width:0%"></div></div>
          <span class="bar-val">${r.fat}g</span>
        </div>
        <div class="bar-row">
          <span class="bar-label c">C</span>
          <div class="bar-track"><div class="bar-fill c" data-width="${cW}" style="width:0%"></div></div>
          <span class="bar-val">${r.carbs}g</span>
        </div>
      </div>
    </div>
    ${ingChips ? `<div class="ing-list">${ingChips}</div>` : ""}
  `;
}

function openModal(r) {
  const content = document.getElementById("modal-content");
  const selected = [...selectedIngredients];

  const ingItems = r.recipe_ingredients.map(ri => `
    <div class="modal-ing-item">
      <span class="modal-ing-name">${ri.ingredient.name}</span>
      <span class="modal-ing-amount">${ri.amount || ""}</span>
    </div>
  `).join("");

  content.innerHTML = `
    <div class="modal-name">${r.name}</div>
    ${r.genre ? `<span class="modal-genre">${r.genre}</span>` : ""}
    ${r.description ? `<p class="modal-desc">${r.description}</p>` : ""}

    <div class="pfc-section" style="margin-top:16px">
      <div class="pfc-numbers">
        <div class="pfc-item p">
          <div class="pfc-label">P タンパク質</div>
          <div class="pfc-value">${r.protein}<span class="pfc-unit">g</span></div>
        </div>
        <div class="pfc-item f">
          <div class="pfc-label">F 脂質</div>
          <div class="pfc-value">${r.fat}<span class="pfc-unit">g</span></div>
        </div>
        <div class="pfc-item c">
          <div class="pfc-label">C 糖質</div>
          <div class="pfc-value">${r.carbs}<span class="pfc-unit">g</span></div>
        </div>
      </div>
      <div class="pfc-bars">
        <div class="bar-row">
          <span class="bar-label p">P</span>
          <div class="bar-track"><div class="bar-fill p" style="width:${Math.round(r.protein/Math.max(r.protein,r.fat,r.carbs,1)*100)}%"></div></div>
          <span class="bar-val">${r.protein}g</span>
        </div>
        <div class="bar-row">
          <span class="bar-label f">F</span>
          <div class="bar-track"><div class="bar-fill f" style="width:${Math.round(r.fat/Math.max(r.protein,r.fat,r.carbs,1)*100)}%"></div></div>
          <span class="bar-val">${r.fat}g</span>
        </div>
        <div class="bar-row">
          <span class="bar-label c">C</span>
          <div class="bar-track"><div class="bar-fill c" style="width:${Math.round(r.carbs/Math.max(r.protein,r.fat,r.carbs,1)*100)}%"></div></div>
          <span class="bar-val">${r.carbs}g</span>
        </div>
      </div>
    </div>

    <div class="modal-calories">カロリー: <strong>${r.calories}</strong> kcal / ${r.servings}人分</div>

    ${ingItems ? `<div class="modal-section-label">食材</div><div class="modal-ing-list">${ingItems}</div>` : ""}
  `;

  document.getElementById("modal-overlay").classList.remove("hidden");
  document.body.style.overflow = "hidden";
}

function closeModal() {
  document.getElementById("modal-overlay").classList.add("hidden");
  document.body.style.overflow = "";
}

function reset() {
  selectedIngredients.clear();
  document.querySelectorAll(".ing-btn.active").forEach(b => b.classList.remove("active"));
  document.getElementById("selected-tags").innerHTML = "";
  hideResults();
  document.getElementById("no-results").classList.add("hidden");
  document.getElementById("keyword-input").value = "";
}

function showLoading(show) {
  document.getElementById("loading").classList.toggle("hidden", !show);
}

function hideResults() {
  document.getElementById("results-section").classList.add("hidden");
  document.getElementById("no-results").classList.add("hidden");
}

init();
