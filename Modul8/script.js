
const evenNumber = (bil) => {
  for (i = bil; i >= 60; i--) {
    if (i % 2 == 0) {
      document.write(`${i}<br>`);
    }
  }
};
const bil = 98;
evenNumber(bil);

const say = () => {
  const nama = prompt("siapa nama anda?R");
  alert(`Selamat datang ${nama}`);
  document.write(`<b>Selamat datang ${nama}</b>`);
};
say();

const formValidation = () => {
  const form = document.querySelector("form");
  const input = document.getElementById("name");
  form.addEventListener("submit", (event) => {
    const inputValue = input.value;
    if (inputValue === "") {
      event.preventDefault();
      alert("Please fill in the 'yourname' box.");
    }
  });
};
formValidation();
