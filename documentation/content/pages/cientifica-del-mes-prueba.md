Title: Científica del mes
Slug: cientifica-nn-prueba-4f7c2a
Status: hidden
Template: cientifica_hidden
Summary: Prueba privada del minijuego Científica del mes de Napkin Notes.

<style>
.nn-scientist-game {
  --nn-red: #b81424;
  --nn-text: #1f2937;
  --nn-muted: #64748b;
  --nn-border: #d7dce2;
  --nn-correct: #6aaa64;
  --nn-present: #c9b458;
  --nn-absent: #787c7e;
  --nn-soft: #f7f7f5;
  width: 100%;
  max-width: 760px;
  margin: 10px auto 40px;
  color: var(--nn-text);
  box-sizing: border-box;
}
.nn-scientist-game * { box-sizing: border-box; }

.nn-scientist-intro {
  text-align: center;
  margin: 0 auto 22px;
  max-width: 620px;
}
.nn-scientist-kicker {
  margin: 0 0 7px;
  color: var(--nn-red);
  font-size: .78rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
}
.nn-scientist-intro p { margin: 7px 0; }
.nn-scientist-rules { color: var(--nn-muted); font-size: .94rem; }

.nn-scientist-legend {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px 18px;
  margin: 18px 0 22px;
  font-size: .82rem;
  color: var(--nn-muted);
}
.nn-scientist-legend-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.nn-scientist-legend-box {
  width: 20px;
  height: 20px;
  border-radius: 3px;
}
.nn-scientist-legend-box.correct { background: var(--nn-correct); }
.nn-scientist-legend-box.present { background: var(--nn-present); }
.nn-scientist-legend-box.absent { background: var(--nn-absent); }

.nn-scientist-board {
  display: flex;
  flex-direction: column;
  gap: 8px;
  width: 100%;
  margin: 0 auto 22px;
}
.nn-scientist-row {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px;
  min-width: 0;
}
.nn-scientist-word {
  display: grid;
  gap: 5px;
}
.nn-scientist-word--3 {
  grid-template-columns: repeat(3, minmax(34px, 48px));
}
.nn-scientist-word--7 {
  grid-template-columns: repeat(7, minmax(34px, 48px));
}
.nn-scientist-space {
  width: 13px;
  flex: 0 0 13px;
  color: #a5adb8;
  font-weight: 700;
  text-align: center;
  user-select: none;
}
.nn-scientist-cell {
  aspect-ratio: 1 / 1;
  min-width: 0;
  border: 2px solid var(--nn-border);
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  color: var(--nn-text);
  font-size: clamp(1rem, 3.2vw, 1.35rem);
  line-height: 1;
  font-weight: 800;
  text-transform: uppercase;
  transition: transform .15s ease, background .2s ease, border-color .2s ease, color .2s ease;
}
.nn-scientist-cell.filled { border-color: #9aa3ad; }
.nn-scientist-cell.correct,
.nn-scientist-cell.present,
.nn-scientist-cell.absent {
  color: #fff;
  border-color: transparent;
}
.nn-scientist-cell.correct { background: var(--nn-correct); }
.nn-scientist-cell.present { background: var(--nn-present); }
.nn-scientist-cell.absent { background: var(--nn-absent); }
.nn-scientist-cell.reveal { animation: nnScientistFlip .36s ease; }

@keyframes nnScientistFlip {
  0% { transform: rotateX(0deg); }
  50% { transform: rotateX(90deg); }
  100% { transform: rotateX(0deg); }
}

.nn-scientist-form {
  max-width: 580px;
  margin: 0 auto;
}
.nn-scientist-label {
  display: block;
  margin-bottom: 7px;
  font-weight: 700;
}
.nn-scientist-input-row {
  display: flex;
  gap: 8px;
}
.nn-scientist-input {
  width: 100%;
  min-width: 0;
  height: 44px;
  padding: 0 12px;
  border: 2px solid var(--nn-border);
  border-radius: 6px;
  background: #fff;
  font: inherit;
  font-size: 1rem;
  text-transform: uppercase;
}
.nn-scientist-input:focus {
  outline: none;
  border-color: var(--nn-red);
  box-shadow: 0 0 0 3px rgba(184, 20, 36, .08);
}
.nn-scientist-submit {
  min-width: 104px;
  height: 44px;
  padding: 0 17px;
  border: 2px solid var(--nn-red);
  border-radius: 6px;
  background: var(--nn-red);
  color: #fff;
  font: inherit;
  font-weight: 700;
  cursor: pointer;
}
.nn-scientist-submit:disabled,
.nn-scientist-input:disabled {
  cursor: not-allowed;
  opacity: .62;
}
.nn-scientist-message {
  min-height: 1.4em;
  margin: 9px 0 0;
  color: var(--nn-red);
  text-align: center;
  font-size: .9rem;
  font-weight: 600;
}
.nn-scientist-counter {
  margin: 10px 0 0;
  text-align: center;
  color: var(--nn-muted);
  font-size: .86rem;
}

.nn-scientist-result {
  max-width: 620px;
  margin: 26px auto 0;
  padding: 22px;
  border: 1px solid #e2e5e9;
  border-radius: 12px;
  background: var(--nn-soft);
}
.nn-scientist-result[hidden] { display: none; }
.nn-scientist-result-heading {
  margin: 0 0 16px;
  text-align: center;
}
.nn-scientist-result-heading strong { color: var(--nn-red); }
.nn-scientist-profile {
  display: grid;
  grid-template-columns: 118px 1fr;
  gap: 18px;
  align-items: start;
}
.nn-scientist-photo {
  width: 118px;
  height: 118px;
  object-fit: cover;
  border-radius: 10px;
  display: block;
}
.nn-scientist-profile h3 { margin: 0 0 7px; }
.nn-scientist-profile p {
  margin: 0 0 12px;
  line-height: 1.55;
}
.nn-scientist-more {
  display: inline-block;
  color: var(--nn-red);
  font-weight: 700;
  text-decoration: none;
}
.nn-scientist-more:hover { text-decoration: underline; }
.nn-scientist-test-tools {
  margin-top: 18px;
  text-align: center;
}
.nn-scientist-reset {
  border: 0;
  background: transparent;
  color: var(--nn-muted);
  font: inherit;
  font-size: .8rem;
  text-decoration: underline;
  cursor: pointer;
}

@media (max-width: 620px) {
  .nn-scientist-row { gap: 7px; }
  .nn-scientist-word { gap: 3px; }
  .nn-scientist-word--3 { grid-template-columns: repeat(3, minmax(26px, 38px)); }
  .nn-scientist-word--7 { grid-template-columns: repeat(7, minmax(26px, 38px)); }
  .nn-scientist-space {
    width: 7px;
    flex-basis: 7px;
    font-size: .75rem;
  }
  .nn-scientist-cell {
    font-size: clamp(.86rem, 4vw, 1.08rem);
    border-width: 1.5px;
  }
  .nn-scientist-input-row { flex-direction: column; }
  .nn-scientist-submit { width: 100%; }
  .nn-scientist-profile {
    grid-template-columns: 1fr;
    text-align: center;
  }
  .nn-scientist-photo { margin: 0 auto; }
}

@media (max-width: 390px) {
  .nn-scientist-row { gap: 4px; }
  .nn-scientist-word { gap: 2px; }
  .nn-scientist-word--3 { grid-template-columns: repeat(3, minmax(23px, 32px)); }
  .nn-scientist-word--7 { grid-template-columns: repeat(7, minmax(23px, 32px)); }
  .nn-scientist-space {
    width: 4px;
    flex-basis: 4px;
  }
}
</style>

<div class="nn-scientist-game" id="nnScientistGame">
  <div class="nn-scientist-intro">
    <p class="nn-scientist-kicker">Prototipo · Científica del mes</p>
    <p><strong>Adivina el nombre de la científica.</strong></p>
    <p class="nn-scientist-rules">Tienes 5 intentos. El nombre tiene dos palabras: <strong>3 letras + 7 letras</strong>. Las tildes no cuentan.</p>
  </div>

  <div class="nn-scientist-legend" aria-label="Leyenda de colores">
    <span class="nn-scientist-legend-item"><span class="nn-scientist-legend-box correct"></span> letra y posición correctas</span>
    <span class="nn-scientist-legend-item"><span class="nn-scientist-legend-box present"></span> letra en otra posición</span>
    <span class="nn-scientist-legend-item"><span class="nn-scientist-legend-box absent"></span> letra ausente</span>
  </div>

  <div class="nn-scientist-board" id="nnScientistBoard" aria-label="Tablero de cinco intentos"></div>

  <form class="nn-scientist-form" id="nnScientistForm" novalidate>
    <label class="nn-scientist-label" for="nnScientistGuess">Escribe tu intento</label>
    <div class="nn-scientist-input-row">
      <input
        class="nn-scientist-input"
        id="nnScientistGuess"
        name="guess"
        type="text"
        autocomplete="off"
        autocapitalize="characters"
        spellcheck="false"
        maxlength="20"
        placeholder="___ _______"
        aria-describedby="nnScientistMessage"
      >
      <button class="nn-scientist-submit" id="nnScientistSubmit" type="submit">Probar</button>
    </div>
    <p class="nn-scientist-message" id="nnScientistMessage" aria-live="polite"></p>
    <p class="nn-scientist-counter" id="nnScientistCounter">Intento 1 de 5</p>
  </form>

  <section class="nn-scientist-result" id="nnScientistResult" hidden aria-live="polite">
    <p class="nn-scientist-result-heading" id="nnScientistResultHeading"></p>
    <div class="nn-scientist-profile">
      <img class="nn-scientist-photo" src="{static}/images/paz.jpg" alt="Paz Albares Vicente">
      <div>
        <h3>Paz Albares Vicente</h3>
        <p>Paz es doctora en Física, especializada en Física Matemática, exploradora de ecuaciones no lineales y de los patrones que de ellas emergen donde menos se esperan. Modeliza fenómenos complejos e intenta descubrir y entender qué estructuras se esconden detrás, combinando la física con herramientas y el lenguaje de las matemáticas.</p>
        <a class="nn-scientist-more" href="https://napkinnotes.es/autor/paz-albares-vicente">Conoce más sobre Paz →</a>
      </div>
    </div>
  </section>

  <div class="nn-scientist-test-tools">
    <button class="nn-scientist-reset" id="nnScientistReset" type="button">Reiniciar prueba</button>
  </div>
</div>

<script>
(function () {
  "use strict";

  const ANSWER_DISPLAY = "PAZ ALBARES";
  const ANSWER_WORDS = [3, 7];
  const MAX_ATTEMPTS = 5;
  const STORAGE_KEY = "nn_scientist_paz_albares_test_v1";

  const board = document.getElementById("nnScientistBoard");
  const form = document.getElementById("nnScientistForm");
  const input = document.getElementById("nnScientistGuess");
  const submit = document.getElementById("nnScientistSubmit");
  const message = document.getElementById("nnScientistMessage");
  const counter = document.getElementById("nnScientistCounter");
  const result = document.getElementById("nnScientistResult");
  const resultHeading = document.getElementById("nnScientistResultHeading");
  const reset = document.getElementById("nnScientistReset");

  function normalizeName(value) {
    return String(value)
      .trim()
      .replace(/\s+/g, " ")
      .toUpperCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "");
  }

  const ANSWER = normalizeName(ANSWER_DISPLAY);
  const ANSWER_LETTERS = ANSWER.replace(/ /g, "");

  function createBoard() {
    board.innerHTML = "";

    for (let rowIndex = 0; rowIndex < MAX_ATTEMPTS; rowIndex++) {
      const row = document.createElement("div");
      row.className = "nn-scientist-row";
      row.dataset.row = String(rowIndex);

      ANSWER_WORDS.forEach((wordLength, wordIndex) => {
        const group = document.createElement("div");
        group.className = "nn-scientist-word nn-scientist-word--" + wordLength;

        for (let i = 0; i < wordLength; i++) {
          const cell = document.createElement("div");
          cell.className = "nn-scientist-cell";
          group.appendChild(cell);
        }

        row.appendChild(group);

        if (wordIndex < ANSWER_WORDS.length - 1) {
          const spacer = document.createElement("div");
          spacer.className = "nn-scientist-space";
          spacer.textContent = "·";
          spacer.title = "Espacio";
          row.appendChild(spacer);
        }
      });

      board.appendChild(row);
    }
  }

  function readState() {
    try {
      const saved = JSON.parse(localStorage.getItem(STORAGE_KEY));
      if (saved && Array.isArray(saved.guesses) && ["playing", "won", "lost"].includes(saved.status)) {
        return { guesses: saved.guesses.slice(0, MAX_ATTEMPTS), status: saved.status };
      }
    } catch (error) {}
    return { guesses: [], status: "playing" };
  }

  function saveState(state) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (error) {}
  }

  function validateGuess(rawValue) {
    const guess = normalizeName(rawValue);

    if (!guess) return { ok: false, error: "Escribe un nombre antes de probar." };
    if (!/^[A-ZÑ ]+$/.test(guess)) return { ok: false, error: "Usa solo letras y espacios." };

    const words = guess.split(" ");

    if (
      words.length !== ANSWER_WORDS.length ||
      words.some((word, index) => word.length !== ANSWER_WORDS[index])
    ) {
      return { ok: false, error: "El nombre debe tener la forma 3 letras + 7 letras." };
    }

    return { ok: true, normalized: guess, letters: words.join("") };
  }

  function scoreGuess(guessLetters) {
    const states = new Array(ANSWER_LETTERS.length).fill("absent");
    const remaining = Object.create(null);

    for (let i = 0; i < ANSWER_LETTERS.length; i++) {
      if (guessLetters[i] === ANSWER_LETTERS[i]) {
        states[i] = "correct";
      } else {
        const letter = ANSWER_LETTERS[i];
        remaining[letter] = (remaining[letter] || 0) + 1;
      }
    }

    for (let i = 0; i < guessLetters.length; i++) {
      if (states[i] === "correct") continue;
      const letter = guessLetters[i];
      if (remaining[letter] > 0) {
        states[i] = "present";
        remaining[letter] -= 1;
      }
    }

    return states;
  }

  function paintRow(rowIndex, guess, animate) {
    const row = board.querySelector('[data-row="' + rowIndex + '"]');
    if (!row) return;

    const letters = guess.replace(/ /g, "");
    const scores = scoreGuess(letters);
    const cells = row.querySelectorAll(".nn-scientist-cell");

    cells.forEach((cell, index) => {
      cell.textContent = letters[index] || "";
      cell.classList.add("filled", scores[index]);
      if (animate) {
        window.setTimeout(function () {
          cell.classList.add("reveal");
        }, index * 35);
      }
    });
  }

  function showResult(status, attempts) {
    result.hidden = false;
    if (status === "won") {
      resultHeading.innerHTML =
        "¡La encontraste! Era <strong>Paz Albares</strong>. La has acertado en " +
        attempts + (attempts === 1 ? " intento." : " intentos.");
    } else {
      resultHeading.innerHTML =
        "Esta vez no pudo ser. La científica era <strong>Paz Albares</strong>.";
    }
  }

  function updateControls(state) {
    const finished = state.status !== "playing";
    input.disabled = finished;
    submit.disabled = finished;

    if (finished) {
      counter.textContent = state.status === "won" ? "Partida completada" : "5 de 5 intentos";
    } else {
      counter.textContent = "Intento " + (state.guesses.length + 1) + " de " + MAX_ATTEMPTS;
    }
  }

  function renderState(state) {
    createBoard();

    state.guesses.forEach(function (guess, index) {
      paintRow(index, guess, false);
    });

    if (state.status === "won" || state.status === "lost") {
      showResult(state.status, state.guesses.length);
    } else {
      result.hidden = true;
      resultHeading.textContent = "";
    }

    updateControls(state);
  }

  let state = readState();
  renderState(state);

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    if (state.status !== "playing") return;

    message.textContent = "";
    const validation = validateGuess(input.value);

    if (!validation.ok) {
      message.textContent = validation.error;
      return;
    }

    const rowIndex = state.guesses.length;
    state.guesses.push(validation.normalized);
    paintRow(rowIndex, validation.normalized, true);

    const won = validation.normalized === ANSWER;

    if (won) {
      state.status = "won";
    } else if (state.guesses.length >= MAX_ATTEMPTS) {
      state.status = "lost";
    }

    saveState(state);
    updateControls(state);

    if (state.status !== "playing") {
      window.setTimeout(function () {
        showResult(state.status, state.guesses.length);
        result.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }, 430);
      return;
    }

    input.value = "";
    input.focus();
  });

  reset.addEventListener("click", function () {
    try {
      localStorage.removeItem(STORAGE_KEY);
    } catch (error) {}

    state = { guesses: [], status: "playing" };
    message.textContent = "";
    input.value = "";
    result.hidden = true;
    renderState(state);
    input.focus();
  });
})();
</script>
