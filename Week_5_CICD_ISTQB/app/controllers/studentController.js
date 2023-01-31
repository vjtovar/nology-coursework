const studentsArr = ["Katie", "John", "Phillip"];

export const getStudents = (req, res) => {
  res.status(200).send({
    studentsArr,
  });
};

export const getStudentById = (req, res) => {
  const id = parseInt(req.params.id);
  res.status(200).send({
    student: studentsArr[id] || "Not found",
  });
};

export const addStudent = (req, res) => {
  studentsArr.push(req.body.student);
  res.status(201).send({
    message: "Student added",
  });
};

export const getStudentByName = (req, res) => {
  const name = req.params.name;
  res.status(200).send({
    student: studentsArr[studentsArr.indexOf(name)] || "Student not found",
  });
};

export const deleteStudent = (req, res) => {
  const id = parseInt(req.params.id);
  studentsArr.splice(id, 1);
  res.status(204).send("Deleted");
};
