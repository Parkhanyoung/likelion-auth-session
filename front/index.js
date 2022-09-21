const $ = (idSelector) => document.querySelector(`#${idSelector}`);

const $SignupUsernameInput = $('signup-username');
const $SignupPasswordInput = $('signup-password');

const $TokenUsernameInput = $('token-username');
const $TokenPasswordInput = $('token-password');

const $AccessTokenInput = $('access-token');

const $RefreshTokenInput = $('refresh-token');

const $SignupBtn = $('signup-btn');
const $CreateTokenBtn = $('create-token-btn');
const $AuthenticateBtn = $('authenticate-btn');
const $RefreshBtn = $('refresh-btn');

const SERVER_URL = 'http://localhost:8000/user/';

$SignupBtn.onclick = async (e) => {
  e.preventDefault();
  const payload = {
    username: $SignupUsernameInput.value,
    password: $SignupPasswordInput.value,
  };
  const res = await fetch(`${SERVER_URL}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });
  if (res.status === 201) {
    alert('회원가입에 성공!');
  } else {
    alert('회원가입 실패');
  }
};

$CreateTokenBtn.onclick = async (e) => {
  e.preventDefault();
  const payload = {
    username: $TokenUsernameInput.value,
    password: $TokenPasswordInput.value,
  };
  const res = await fetch(SERVER_URL + 'token/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });

  const body = await res.json();
  if (res.status === 201) {
    alert(`액세스 토큰: ${body.access}`);
  } else {
    alert('인증 실패');
  }
};
