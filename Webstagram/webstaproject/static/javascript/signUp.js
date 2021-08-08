const message=document.getElementById('message');
const text=message.innerHTML;
console.log(`text: ${text}`);

//나중에 form 비어있는지 확인

if(text==='user exist'){
    alert('이미 가입되어있는 이메일 계정입니다.');
}
if(text==='password check fail'){
    alert('비밀번호가 일치하지 않습니다. 비밀번호를 다시 확인해주세요.');
}
