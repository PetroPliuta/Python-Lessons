function teslaCreator(kind) {
  return kind === "sport" ? sportCarFactory : crossoverCarFactory;
}
function sportCarFactory() {
  return new ModelX();
}
function crossoverCarFactory() {
  return new CyberTruck();
}

class ModelX {
  showCar() {
    console.log("Sport car X");
  }
}
class CyberTruck {
  showCar() {
    console.log("crossover CyberTruck");
  }
}

const creator = teslaCreator("sport");
const myCar = new creator();
myCar.showCar();

