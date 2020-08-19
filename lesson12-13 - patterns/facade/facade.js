// Завод
class CarFactory {
  setEngine() {
    console.log("setEngine");
  }
  setColor() {
    console.log("setColor");
  }
  setWheels() {
    console.log("setWheels");
  }
  setBody() {
    console.log("setBody");
  }
}

class CarFactoryFacade {
  constructor(car) {
    this.car = car;
  }
  startAssembly() {
    this.car.setBody();
    this.car.setEngine();
    this.car.setWheels();
    this.car.setColor();
  }
}

const carFacade = new CarFactoryFacade(new CarFactory());
carFacade.startAssembly();

