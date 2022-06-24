const express = require("express");
const pyGetLGA = require("./lga.controller");

const lgaRouter = express.Router();
lgaRouter.post("/", pyGetLGA);

module.exports = lgaRouter;
