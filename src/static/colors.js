class Colors {
  constructor(background) {
    this.background = background;

    this.selectFileBtn = document.querySelector("button");
    this.form = document.querySelector("form");
    this.input = document.querySelector("input");

    this.loading = document.getElementById("loading");
    this.copyright = document.querySelector(".copyright");
    this.author = document.getElementById("author");
    this.dataTable = document.getElementById("data-table");
    this.result = document.querySelector(".result");
    this.resultContainer = document.querySelector(".result-container");
  }

  setColors = () => {
    const boxShadowColor =
      this.background === "starry_sky.png" ? "#65AAE7" : "#FCF853";

    this.selectFileBtn.addEventListener("mouseover", () => {
      this.selectFileBtn.style.boxShadow = `3px 3px ${boxShadowColor}`;
    });
    this.selectFileBtn.addEventListener("mouseout", () => {
      this.selectFileBtn.style.boxShadow = "";
    });

    let primaryColor, secondaryColor, containerColor, containerBorderColor;

    if (this.background === "starry_sky.png") {
      primaryColor = "#1E6D9B";
      secondaryColor = "black";
      containerColor = "#5E92CC";
      containerBorderColor = "#65AAE7";
    } else {
      primaryColor = "#9E2649";
      secondaryColor = "white";
      containerColor = "#1e0341";
      containerBorderColor = "#FCF853";
    }

    this.form.style.backgroundColor = primaryColor;
    this.form.style.color = "white";
    this.form.style.borderColor = containerBorderColor;
    this.input.style.backgroundColor = containerColor;

    this.copyright.style.color = primaryColor;
    this.author.style.color = primaryColor;
    this.selectFileBtn.style.backgroundColor = primaryColor;
    this.dataTable.style.color = secondaryColor;
    this.result.style.color = primaryColor;
    this.loading.style.color = primaryColor;
    this.resultContainer.style.backgroundColor = containerColor;
    this.resultContainer.style.borderColor = primaryColor;
  };
}
