/////////////// helper //////////////////

function clearLogger() {
  const logger = document.querySelector(".logger");
  logger.innerHTML = "";
}
// logging function
function log(content, color) {
  // color = color == undefined ? '#333' : color;
  let parts = undefined;
   if (content.includes("Created")) {
    parts = content.split("]", 2);
    parts[0] += "]"

    color = "Green";
  }
  else if (content.includes("INFO")) {
    parts = content.split("]", 2);
    parts[0] += "]"
    color = "blue";
  } else if (content.includes("WARNING")) {
    parts = content.split("]", 2);
    parts[0] += "]"

    color = "red";
  }
  else if (content.includes("DEBUG")) {
    parts = content.split("]", 2);
    parts[0] += "]"

    color = "violet";
  }
  
  const logger = document.querySelector(".logger");
  const el = document.createElement("div");
  const date = new Date();
  el.style.color = color;
  // el.innerHTML = `
  //   <span prefix>
  //     ${(logger.children.length + 1).toString()}
  //     ${date.toLocaleTimeString()
  //           .split(':').splice(1).join(':')
  //     }:${date.getMilliseconds().toString().padStart(3, '0')}
  //   </span>
  //   ${content}`;
  if (parts) {
    el.style.color = color;
    el.innerHTML = `
        <span style="color:gray;">
          ${parts[0]}
        </span>
        <span >
          ${parts[1]}
        </span>`
  }else {

    el.innerHTML = `${content}`;
  }
  logger.insertAdjacentElement("afterbegin", el);
}