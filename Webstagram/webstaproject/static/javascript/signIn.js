const message=document.querySelector('#message');
const text=message.innerHTML;
const emailInput=document.getElementsByName('email');
const pwdInput=document.getElementsByName('pwd');

if(text==='login fail'){
    pwdInput.value="";
    emailInput.value="";
    alert('이메일(아이디) 또는 비밀번호를 다시 확인해주세요.');
}
if(text==='empty value'){
    alert('이메일과 비밀번호를 모두 입력해주세요.')
}
if(text==='join success'){
    alert('회원가입 성공!')
}