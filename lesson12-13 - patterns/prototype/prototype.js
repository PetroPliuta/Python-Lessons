class Tesla {
  constructor(model, color, price, autopilot) {
    this.model = model;
    this.price = price;
    this.color = color;
    this.autopilot = autopilot;
  }
  clone() {
    return new Tesla(this.model, this.color, this.price, this.autopilot);
  }
  show() {
    console.log(this);
  }
  set color(color) {
    this._color = color;
  }
  get color() {
    return this._color;
  }
  set price(price) {
    this._price = price;
  }
  get price() {
    return this._price;
  }
  set autopilot(autopilot) {
    this._autopilot = autopilot;
  }
  get autopilot() {
    return this._autopilot;
  }
}

const prototype = new Tesla("X", "RED", 10000, false);
const car2 = prototype.clone();
const car3 = prototype.clone();

car2.color = "blue";
car2.price = 1;
car3.autopilot = true;

prototype.show();
car2.show();
car3.show();

// 2 методв
// мінять прайс
// мінять автопілот
