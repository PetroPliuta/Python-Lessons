class Tesla {
  constructor(model, price, color, autopilot) {
    this.model = model;
    this.price = price;
    this.color = color;
    this.autopilot = autopilot;
  }
}

class TeslaFactory {
  create(type) {
    if (type == "X") {
      return new Tesla(type, 50000, "Blue", true);
    }
    if (type == "Y") {
      return new Tesla(type, 70000, "Red", false);
    }
  }
}

let factory = new TeslaFactory();
let car1 = factory.create("X");
console.log(car1);

let Y = factory.create("Y");
console.log(Y);
