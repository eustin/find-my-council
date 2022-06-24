const express = require("express");
const cors = require("cors");

const app = express();
app.use(express.json());
// app.use(cors({ origin: "http://localhost:3000" }));

const lgaRouter = require("./routes/lga.router");
app.use("/lga", lgaRouter);

module.exports = app;
