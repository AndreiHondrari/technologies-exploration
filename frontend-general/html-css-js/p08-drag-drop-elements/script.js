window.onload = function () {
  let dragged = null;
  let targetZone = null;
  let ignoreLeave = false;

  const panelA = document.querySelector("#panelA");
  const panelB = document.querySelector("#panelB");

  function panelDragEnterHandler(event) {
    const classes = event.target.classList;
    if (classes.contains("item")) {
      ignoreLeave = true;
    } else if (classes.contains("panel")) {
      targetZone = event.target;
      console.log("enter", targetZone.id);
    }
  }

  function panelDragLeaveHandler(event) {
    const classes = event.target.classList;

    if (classes.contains("item")) {
      ignoreLeave = false;
    } else if (
      !ignoreLeave && targetZone !== null && classes.contains("panel")
    ) {
      console.log("leave", targetZone.id);
      targetZone = null;
    }
  }

  function dropHandler(event) {
    event.preventDefault();
    console.log("drop");

    if (targetZone !== null && dragged !== null) {
      console.log("drop_do");
      dragged.parentNode.removeChild(dragged);
      targetZone.appendChild(dragged);
    }
  }

  function dragOverHandler(event) {
    event.preventDefault();
  }

  panelA.ondragenter = panelDragEnterHandler;
  panelA.ondragleave = panelDragLeaveHandler;
  panelA.ondrop = dropHandler;
  panelA.ondragover = dragOverHandler;

  panelB.ondragenter = panelDragEnterHandler;
  panelB.ondragleave = panelDragLeaveHandler;
  panelB.ondrop = dropHandler;
  panelB.ondragover = dragOverHandler;

  // set draggable items
  for (const item of document.querySelectorAll(".item")) {
    item.draggable = true;

    item.ondragstart = function (event) {
      console.log("drag_start | ", event.srcElement.innerText);
      dragged = event.srcElement;
    };

    item.ondragend = function (event) {
      console.log("drag_end | ", dragged.innerText);
      dragged = null;
    };
  }
};
