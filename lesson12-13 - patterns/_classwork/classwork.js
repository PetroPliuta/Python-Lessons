const URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5";

class Exchange {
  constructor() {
    if (!Exchange.instance) {
      Exchange.instance = this;
    }
    return Exchange.instance;
  }
  getData() {
    fetch(URL, {
      headers: {
        "User-Agent": "vscode",
        "Content-Type": "application/json",
      },
      mode: "no-cors", // no-cors, *cors, same-origin
      cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
      redirect: "follow", // manual, *follow, error
      referrerPolicy: "no-referrer", // no-referrer,
    })
      .then((response) => {
        console.log("Response: ", response);
        return response.json();
      })
      .then((result) => {
        console.log("Result: ", result);
        document.querySelector("#root").innerText = JSON.stringify(result);
      })
      .catch((err) => console.log(err));
  }
  add() {
    this.counter++;
  }
  counter = 0;
}

e = new Exchange();
e.getData();

e2 = new Exchange();
console.log(e);
console.log(e2);

setTimeout(() => {
  e.add();
  console.log(e);
  console.log(e2);
}, 3000);

for (i = 0; ++i; i < 10000) {
  let o = new Exchange();
}
