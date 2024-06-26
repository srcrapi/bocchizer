class Background {
  constructor() {
    this.bodyElement = document.querySelector("body");
    this.selectFileBtn = document.querySelector("button");
    this.copyright = document.querySelector(".copyright");
    this.author = document.getElementById("author");
    this.dataTable = document.getElementById("data-table");
    this.result = document.querySelector(".result");
    this.resultContainer = document.querySelector(".result-container");

    this.backgrounds = ["starry_sky.png", "niko.png"];

    this.setBackground();
  }

  setColors = (background) => {
    let primaryColor, secondaryColor, containerColor;

    if (background === "starry_sky.png") {
      primaryColor = "#1E6D9B";
      secondaryColor = "black";
      containerColor = "#5E92CC";
    } else {
      primaryColor = "#9E2649";
      secondaryColor = "white";
      containerColor = "#1e0341";
    }

    this.copyright.style.color = primaryColor;
    this.author.style.color = primaryColor;
    this.selectFileBtn.style.backgroundColor = primaryColor;
    this.dataTable.style.color = secondaryColor;
    this.result.style.color = primaryColor;
    this.resultContainer.style.backgroundColor = containerColor;
    this.resultContainer.style.borderColor = primaryColor;
  };

  setBackground = () => {
    const backgroundIndex = Math.floor(Math.random() * this.backgrounds.length);
    const background = this.backgrounds[backgroundIndex];
    const backgroundPath = `../static/img/${background}`;

    console.log(background);

    this.setColors(background);

    const boxShadowColor =
      background === "starry_sky.png" ? "#65AAE7" : "#FCF853";

    this.selectFileBtn.addEventListener("mouseover", () => {
      this.selectFileBtn.style.boxShadow = `3px 3px ${boxShadowColor}`;
    });
    this.selectFileBtn.addEventListener("mouseout", () => {
      this.selectFileBtn.style.boxShadow = "";
    });

    this.bodyElement.style.backgroundImage = `url("${backgroundPath}")`;
  };
}
