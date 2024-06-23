class Background {
  constructor() {
    this.mainElement = document.querySelector("main");
    this.selectFileBtn = document.querySelector("button");

    this.backgrounds = [
      "starry_sky.png",
      "niko.png"
    ];
    
    this.setBackground();
  }

  setBackground = () => {
    const backgroundIndex = Math.floor(Math.random() * this.backgrounds.length);
    const backgroundPath = `../static/img/${this.backgrounds[backgroundIndex]}`
    
    console.log(backgroundPath);

    this.mainElement.style.backgroundImage = `url("${backgroundPath}")`;
  }
}


const background = new Background();
