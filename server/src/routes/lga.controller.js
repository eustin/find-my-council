const getLGA = require("../models/lga.model");

async function pyGetLGA(req, res) {
  const body = req.body;
  if (!body.lat || !body.lon) {
    return res.status(400).json({
      error: "Missing latitude or longitude",
    });
  }

  const lat = parseFloat(body.lat);
  const lon = parseFloat(body.lon);

  if (isNaN(lat) || isNaN(lon)) {
    return res.status(400).json({
      error: "Latitude and longitude must be numbers",
    });
  }

  try {
    const result = await getLGA();
    return res.status(200).json({ lga: result });
  } catch (err) {
    return res.status(500).json({ error: "Error getting LGA" });
  }
}

module.exports = pyGetLGA;
