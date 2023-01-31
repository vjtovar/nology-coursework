import Router from "express";
import bodyParser from "body-parser";
import {
  addStudent,
  deleteStudent,
  getStudentById,
  getStudentByName,
  getStudents,
} from "../controllers/studentController.js";

const router = Router();

router.get("/", (req, res) => getStudents(req, res));

router.get("/:id", (req, res) => getStudentById(req, res));

router.post("/", (req, res) => addStudent(req, res));

router.delete("/:id", (req, res) => deleteStudent(req, res));

router.get("/name/:name", (req, res) => getStudentByName(req, res));

export default router;
