(async function() {
  const showCam = document.getElementById("show-cam");
  const hideCam = document.getElementById("hide-cam");
  const captureImg = document.getElementById("capture-image");
  const library = document.getElementById("library");

  const video = document.getElementById("video");

  let consumerExisted = 0
  showCam.addEventListener("click", async () => {
    video.style.display = "initial";
  });

  hideCam.addEventListener("click", async () => {
    video.style.display = "none";
  });

  captureImg.addEventListener("click", async () => {
    
  });

  library.addEventListener("click", async () => {
    
  });

})();

// function createMediaEl(track) {
//   const el = document.createElement(track.kind);
//   el.className = "border border-solid border-gray-400 rounded";
//   el.style = "width: 100%;"
//   el.srcObject = new MediaStream([track]);
//   el.playsInline = true;
//   el.play().catch(console.error);
//   return el;
// }

// function removeMediaEl($container, key, id) {
//   Array.from($container.children)
//     .filter(el => el.getAttribute(key) === id)
//     .forEach(el => {
//       el.srcObject.getTracks().forEach(track => track.stop());
//       el.remove();
//     });
// }
