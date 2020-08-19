class Car {
  constructor() {
    this.color = "white";
    this.audiosystem = false;
    this.autopilot = false;
    this.model = "Unknown";
  }
}

class CarBuilder {
  constructor() {
    this.car = new Car();
  }
  addColor(color) {
    this.car.color = color;
    return this;
  }
  addAudioSystem(audio) {
    this.car.audiosystem = audio;
    return this;
  }
  addAutopilot(autopilot) {
    this.car.autopilot = autopilot;
    return this;
  }
  addModel(model) {
    this.car.model = model;
    return this;
  }
  build() {
    return this.car;
  }
  show() {
    // console.log(this.car);
    console.log(
      `Model: ${this.car.model}. \ncolor: ${this.car.color}. \naudio: ${this.car.audiosystem}. \nautopilot: ${this.car.autopilot}`
    );
  }
}

let car = new CarBuilder();
car.addColor("red").add;
car.show();

car
  .addAudioSystem("Samsung")
  .addColor("Red")
  .addModel("Tesla")
  .addAutopilot("stage 4");

car.show();
