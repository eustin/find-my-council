const { spawn } = require("child_process");
const { once } = require("events");
const path = require("path");

async function getLGA(lat, lon) {
  let result;
  const scriptPath = path.join(__dirname, "..", "..", "scripts", "find_lga.py");
  const python = spawn("python3", [scriptPath, lat, lon]);

  python.stdout.on("data", (data) => {
    result = data.toString();
  });

  python.stderr.on("data", (data) => {
    console.log(`error: ${data}`);
  });

  await once(python, "close");
  return result;
}

module.exports = getLGA;
