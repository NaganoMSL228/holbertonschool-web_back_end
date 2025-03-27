class Building {
  constructor(sqft) {
    this.sqft = sqft;

    if (
      this.constructor !== Building
        && this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage
    ) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    if (typeof value !== 'number') {
      throw new TypeError('sqft must be a number');
    }
    this._sqft = value;
  }

  evacuationWarningMessage() {
    if (this.constructor === Building) {
      throw new Error('Cannot call abstract method directly');
    }
    // Force subclasses to override by referencing this
    return `evacuationWarningMessage not implemented in ${this.constructor.name}`;
  }
}

export default Building;
