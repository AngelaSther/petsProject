// MODAIS

// LOGIN

document.addEventListener('DOMContentLoaded', () => {
  const tipo = document.body.dataset.tipo;

  if(tipo === "tutor") document.getElementById('modal-tutor').style.display='flex';
  if(tipo === "ong") document.getElementById('modal-ong').style.display='flex';
  if(tipo === "instituicao") document.getElementById('modal-instituicao').style.display='flex';
  if(tipo === "login") document.getElementById('modal-login').style.display='flex';
});

// REGISTRO PETS PÁGINA TUTOR

let display = false
document.getElementById('add-pet-btn').addEventListener('click', () => {
  if (display == false) {
    document.getElementById('add-pet-modal').style.display = 'flex'
    display = true
  } else {
    document.getElementById('add-pet-modal').style.display = 'none'
    display = false
  }
})
