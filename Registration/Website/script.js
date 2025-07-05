// SHA-256 hashing via Web Crypto API
async function hashPassword(password) {
  const encoder = new TextEncoder();
  const data    = encoder.encode(password);
  const hash    = await crypto.subtle.digest('SHA-256', data);
  return Array.from(new Uint8Array(hash))
    .map(b => b.toString(16).padStart(2, '0'))
    .join('');
}

// Strength Meter Elements
const strengthBar  = document.getElementById('strengthBar');
const strengthText = document.getElementById('strengthText');

// Update Password Strength
document.getElementById('password').addEventListener('input', e => {
  const val = e.target.value;
  let score = 0;
  if (/[A-Z]/.test(val)) score++;
  if (/[a-z]/.test(val)) score++;
  if (/[0-9]/.test(val)) score++;
  if (/[\W]/.test(val))  score++;
  score += Math.min(Math.floor(val.length / 4), 2);

  const percent = Math.min((score / 6) * 100, 100);
  strengthBar.style.width = percent + '%';

  if (percent < 40) {
    strengthBar.style.background = '#ff4d4d';
    strengthText.textContent = 'Weak';
  } else if (percent < 80) {
    strengthBar.style.background = '#ffcc00';
    strengthText.textContent = 'Medium';
  } else {
    strengthBar.style.background = '#4cd137';
    strengthText.textContent = 'Strong';
  }
});

// Toggle Password Visibility
document.querySelector('.toggle-pass').addEventListener('click', () => {
  const pwd = document.getElementById('password');
  pwd.type  = pwd.type === 'password' ? 'text' : 'password';
});

// Form Submission Handler
document.getElementById('signupForm').addEventListener('submit', async e => {
  e.preventDefault();

  const userIdEl   = document.getElementById('userId');
  const passwordEl = document.getElementById('password');
  const msgEl      = document.getElementById('message');
  const btn        = e.target.querySelector('.submit-button');

  if (!userIdEl.value.trim() || !passwordEl.value.trim()) {
    msgEl.textContent = '⚠️ Fill in both fields';
    msgEl.style.color = '#ffcc00';
    return;
  }

  const userIdRaw   = userIdEl.value.trim().toLowerCase(); // Lowercased user ID
  const passwordRaw = passwordEl.value.trim();             // Password unchanged

  btn.classList.add('loading');
  msgEl.textContent = '';

  try {
    const hashed = await hashPassword(passwordRaw);
    const res    = await fetch('http://localhost:3000/signup', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        userId:   userIdRaw,
        password: hashed
      })
    });

    const text = await res.text();
    if (res.status === 201) {
      msgEl.textContent = '✅ Registered successfully!';
      msgEl.style.color = '#4cd137';
      e.target.reset();
      strengthBar.style.width = '0';
      strengthText.textContent = '';
    } else {
      msgEl.textContent = '⚠️ ' + text;
      msgEl.style.color = '#ff4444';
    }
  } catch {
    msgEl.textContent = '🚨 Server error!';
    msgEl.style.color = '#ff4444';
  } finally {
    btn.classList.remove('loading');
  }
});