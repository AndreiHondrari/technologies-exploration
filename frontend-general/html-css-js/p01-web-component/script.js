"use strict";

function main() {
  console.log("** START **\n");

  class Some extends HTMLElement {
    constructor(...args) {
      super(...args);

      const templateSomething = document.querySelector("#template-something");
      const clone = templateSomething.content.cloneNode(true);

      const somethingTitle = clone.querySelector(".something-title");
      const somethingText = clone.querySelector(".something-text");

      console.log(this.attributes);

      if ("title" in this.attributes) {
        somethingTitle.innerText = this.attributes.title.value;
      }
      somethingText.innerText = this.innerText;

      this.innerText = null;

      this.appendChild(clone);
    }
  }

  window.customElements.define("some-thing", Some);

  console.log("\n** END **");
}

window.onload = main;
