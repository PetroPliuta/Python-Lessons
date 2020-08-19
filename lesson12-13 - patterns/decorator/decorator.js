class Car {
  constructor() {
    this.color = "white";
    this.price = 10000;
    this.model = "Unknown";
  }
  getPrice() {
    return this.price;
  }
  getModel() {
    return this.model;
  }
}

class Tesla extends Car {
  constructor() {
    super();
    this.price = 30000;
    this.model = "Tesla";
  }
}

class Autopilot {
  constructor(car) {
    this.car = car;
  }
  getPrice() {
    return this.car.getPrice() + 1000;
  }
}

let tesla = new Tesla();
tesla = new Autopilot(tesla);

console.log(tesla);
console.log(tesla.getPrice());
