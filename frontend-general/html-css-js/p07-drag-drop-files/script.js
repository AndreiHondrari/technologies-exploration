function dragOverHandler(event) {
  event.preventDefault();
}

function dropHandler(event) {
  event.preventDefault();

  const files = [];

  if (event.dataTransfer.items) {
    console.log("_ITEMS_");

    for (let i = 0; i < event.dataTransfer.items.length; ++i) {
      const item = event.dataTransfer.items[i];

      if (item.kind === "file") {
        const file = item.getAsFile();
        files.push(file);
      }
    }
  } else {
    console.log("_FILES_");

    for (let i = 0; i < event.dataTransfer.files.length; ++i) {
      files = event.dataTransfer.files;
    }
  }

  if (files) {
    for (const file of files) {
      console.log(file.name);
      console.log(file);
    }
  }
}

function dragStartHandler(event) {
  console.log("DRAG START");
}

function dragEnterHandler(event) {
  console.log("DRAG ENTER");
}

function dragLeaveHandler(event) {
  console.log("DRAG LEAVE");
}
