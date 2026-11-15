import { rangeStatus, spaceStatus } from './fit.mjs';

const inputs = Object.fromEntries(['thickness', 'hole', 'depth'].map(id => [id, document.getElementById(id)]));
const cards = document.querySelectorAll('article');
const zh = document.documentElement.lang.startsWith('zh');
const labels = zh ? {yes:'符合', no:'不符合', pending:'待量度'} : {yes:'Fits', no:'Does not fit', pending:'Measure to confirm'};

function measurement(input) {
  return input.value !== '' && input.validity.valid ? input.valueAsNumber : null;
}

function render() {
  const thickness = measurement(inputs.thickness);
  const hole = measurement(inputs.hole);
  const depth = measurement(inputs.depth);
  for (const card of cards) {
    const statuses = {
      thickness: rangeStatus(thickness, 35, 105),
      hole: rangeStatus(hole, Number(card.dataset.holeMin), 50),
      space: spaceStatus(depth, Number(card.dataset.depth), card.querySelector('select').value),
    };
    for (const output of card.querySelectorAll('output')) {
      const status = statuses[output.dataset.result];
      output.className = status;
      const label = labels[status];
      if (output.textContent !== label) output.textContent = label;
    }
  }
}
document.querySelector('main').addEventListener('input', render);
render();
