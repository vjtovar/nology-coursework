import express from "express";
import router from "./routes/students.js";
import bodyParser from "body-parser";

import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const port = process.env.PORT || 3002;

app.use(express.static('public'))
app.use(bodyParser.json());

app.use("/api/students", router);
app.use("/cicd", (req, res ) => {
  res.sendFile('pages/index.html', {root: __dirname })
});
app.get("/api", (req, res) => {
  res.send("Welcome to my API!");
});
app.get("*", (req, res) =>
  res.status(404).send("There is no content at this route.")
);

app.listen(port, () => console.log(`Server is listening on port ${port}`));

export default app;