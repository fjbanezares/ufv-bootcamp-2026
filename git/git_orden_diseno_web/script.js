(() => {
  const body = document.body;
  const themeToggle = document.getElementById('themeToggle');

  const savedTheme = localStorage.getItem('git-guide-theme');
  if (savedTheme === 'dark') body.classList.add('dark');

  themeToggle.addEventListener('click', () => {
    body.classList.toggle('dark');
    localStorage.setItem('git-guide-theme', body.classList.contains('dark') ? 'dark' : 'light');
  });

  // Buscador de conceptos por sección.
  const search = document.getElementById('sectionSearch');
  const sections = [...document.querySelectorAll('.searchable')];

  search?.addEventListener('input', () => {
    const q = search.value.trim().toLowerCase();
    sections.forEach(section => {
      const text = (section.textContent + ' ' + (section.dataset.keywords || '')).toLowerCase();
      section.classList.toggle('hidden-by-search', q && !text.includes(q));
    });
  });

  // Resaltado del índice según la sección visible.
  const tocLinks = [...document.querySelectorAll('#toc a')];
  const targetSections = tocLinks
    .map(link => document.querySelector(link.getAttribute('href')))
    .filter(Boolean);

  const observer = new IntersectionObserver(entries => {
    const visible = entries
      .filter(e => e.isIntersecting)
      .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

    if (!visible) return;
    tocLinks.forEach(link => link.classList.toggle(
      'active',
      link.getAttribute('href') === '#' + visible.target.id
    ));
  }, { rootMargin: '-20% 0px -65% 0px', threshold: [0.05, 0.2, 0.5] });

  targetSections.forEach(section => observer.observe(section));

  // Laboratorio conceptual.
  let state = {
    wd: 'clean',       // clean | modified
    staged: false,
    commit: 1
  };

  const wdState = document.getElementById('wdState');
  const stageState = document.getElementById('stageState');
  const repoState = document.getElementById('repoState');
  const wdDetail = document.getElementById('wdDetail');
  const stageDetail = document.getElementById('stageDetail');
  const repoDetail = document.getElementById('repoDetail');
  const terminal = document.getElementById('labTerminal');

  function statusText(command = 'git status', note = '') {
    const lines = [`$ ${command}`, 'On branch main'];

    if (state.wd === 'clean' && !state.staged) {
      lines.push('nothing to commit, working tree clean');
    } else {
      if (state.staged) {
        lines.push('Changes to be committed:');
        lines.push('  modified: app.js');
      }
      if (state.wd === 'modified') {
        lines.push('Changes not staged for commit:');
        lines.push('  modified: app.js');
      }
    }

    if (note) lines.push('', '# ' + note);
    return lines.join('\n');
  }

  function render(command, note) {
    wdState.textContent = state.wd === 'modified' ? 'modificado' : 'limpio';
    stageState.textContent = state.staged ? 'app.js preparado' : 'sin cambios';
    repoState.textContent = `commit C${state.commit}`;

    wdDetail.textContent = state.wd === 'modified'
      ? 'hay cambios posteriores al staging'
      : state.staged
        ? 'coincide con la versión staged'
        : 'app.js coincide con staging';

    stageDetail.textContent = state.staged
      ? `contiene la próxima versión de app.js`
      : `coincide con HEAD`;

    repoDetail.textContent = `HEAD → main → C${state.commit}`;
    terminal.innerHTML = `<code>${escapeHtml(statusText(command, note))}</code>`;
  }

  function escapeHtml(str) {
    return str.replace(/[&<>"']/g, ch => ({
      '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#039;'
    }[ch]));
  }

  document.querySelectorAll('[data-action]').forEach(btn => {
    btn.addEventListener('click', () => {
      const action = btn.dataset.action;

      if (action === 'edit') {
        state.wd = 'modified';
        render('editar app.js', 'El WD cambia; staging y repo todavía no.');
      }

      if (action === 'add') {
        if (state.wd === 'modified') {
          state.staged = true;
          state.wd = 'clean';
          render('git add app.js', 'La versión actual pasa al index.');
        } else {
          render('git add app.js', 'No había cambios nuevos que añadir.');
        }
      }

      if (action === 'commit') {
        if (state.staged) {
          state.commit += 1;
          state.staged = false;
          render('git commit -m "Actualiza app.js"', 'La rama main avanza al nuevo commit.');
        } else {
          render('git commit', 'No hay cambios staged: Git no crea un commit normal vacío.');
        }
      }

      if (action === 'unstage') {
        if (state.staged) {
          state.staged = false;
          state.wd = 'modified';
          render('git restore --staged app.js', 'Sale del index, pero el cambio sigue en el WD.');
        } else {
          render('git restore --staged app.js', 'No había nada staged.');
        }
      }

      if (action === 'restore') {
        if (state.wd === 'modified') {
          state.wd = 'clean';
          render('git restore app.js', 'Se descartan los cambios no staged del WD.');
        } else {
          render('git restore app.js', 'El WD ya coincidía con el index.');
        }
      }

      if (action === 'reset') {
        state = { wd: 'clean', staged: false, commit: 1 };
        render('git status', 'Laboratorio reiniciado.');
      }
    });
  });

  render('git status', '');
})();