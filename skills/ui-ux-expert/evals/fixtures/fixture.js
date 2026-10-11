const allowed = ['dashboard', 'mobile-form', 'editorial'];
const selected = location.hash.slice(1) || 'dashboard';
document.getElementById(allowed.includes(selected) ? selected : 'dashboard').hidden = false;
document.querySelector('#filter').addEventListener('input', event => {
  let visible = 0;
  document.querySelectorAll('tr[data-customer]').forEach(row => {
    row.hidden = !row.dataset.customer.toLowerCase().includes(event.target.value.toLowerCase());
    if (!row.hidden) visible++;
  });
  document.querySelector('#count').textContent = `${visible} records`;
});
document.querySelectorAll('[data-action]').forEach(button => button.addEventListener('click', () => {
  document.querySelector('#detail').textContent = `${button.dataset.action}: ${button.closest('tr').dataset.customer}. Simulation only; no write or clipboard action.`;
}));
document.querySelector('form').addEventListener('submit', event => {
  event.preventDefault();
  const email = event.target.elements.email;
  const invalid = !email.value || !email.validity.valid;
  document.querySelector('#email-error').hidden = !invalid;
  email.setAttribute('aria-invalid', String(invalid));
  document.querySelector('#form-status').textContent = invalid ? 'Review the email address. Your entries are retained.' : 'Preferences accepted in this simulation. Nothing was saved to a server.';
  if (invalid) email.focus();
});
// Authored bitmap diagram for the fictional article, not a third-party map.
const ctx = document.querySelector('canvas').getContext('2d');
ctx.fillStyle = '#e4efed'; ctx.fillRect(0, 0, 1000, 360);
ctx.fillStyle = '#87bdc3'; ctx.fillRect(0, 70, 1000, 100);
ctx.fillStyle = '#c8d7bb'; ctx.fillRect(0, 245, 1000, 115);
ctx.strokeStyle = '#324f47'; ctx.lineWidth = 8;
ctx.beginPath(); ctx.moveTo(30, 220); ctx.lineTo(970, 220); ctx.stroke();
for (const [i, x] of [180, 500, 820].entries()) {
  ctx.fillStyle = '#fff'; ctx.fillRect(x - 24, 45, 48, 205);
  ctx.strokeStyle = '#59686b'; ctx.lineWidth = 3; ctx.strokeRect(x - 24, 45, 48, 205);
  ctx.fillStyle = '#24262a'; ctx.font = '22px system-ui'; ctx.fillText(`Crossing ${i + 1}`, x - 60, 302);
}
