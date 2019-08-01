const express = require("express");

const router = express.Router();

/* GET home Speakers Page. */
router.get("/", function(req, res) {
  res.send("Hello Home Speakers");
});

router.get("/:name", function(req, res) {
  res.send(`Hello ${req.params.name}`);
});

module.exports = router;