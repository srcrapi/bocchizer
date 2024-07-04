class Background {
  constructor() {
    this.bodyElement = document.querySelector("body");
    this.backgrounds = ["starry_sky.png", "niko.png"];

    this.setBackground();
  }

  setBackground = () => {
    const backgroundIndex = Math.floor(Math.random() * this.backgrounds.length);
    const background = this.backgrounds[backgroundIndex];
    const backgroundPath = `../static/img/${background}`;

    const colors = new Colors(background);
    colors.setColors();

    this.bodyElement.style.backgroundImage = `url("${backgroundPath}")`;
  };
}
