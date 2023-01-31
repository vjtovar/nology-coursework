import chai from 'chai';
import chaiHttp from 'chai-http';
import app from '../index.js';

const should = chai.should();

chai.use(chaiHttp);

describe('Get All Students Service', () => {
    it('should return all the students', (done) => {
        chai.request(app)
            .get('/api/students')
            .end((err, res) => {
                res.status.should.equal(200);
                res.body.studentsArr.length.should.equal(3);
                done();
            })
    })

    it('should return Katie as the first entry', (done) => {
        chai.request(app)
            .get('/api/students')
            .end((err, res) => {
                res.status.should.equal(200);
                res.body.studentsArr[0].should.equal("Katie");
                done();
            })
    })

    it('should return John as the second entry', (done) => {
        chai.request(app)
            .get('/api/students')
            .end((err, res) => {
                res.status.should.equal(200);
                res.body.studentsArr[1].should.equal("John");
                done();
            })
    })

    it('should return Philip as the third entry', (done) => {
        chai.request(app)
            .get('/api/students')
            .end((err, res) => {
                res.status.should.equal(200);
                res.body.studentsArr[2].should.equal("Phillip");
                done();
            })
    })
}) 

describe('Get Student Service', () => {
    it('should return Katie as the first entry', (done) => {
        chai.request(app)
            .get('/api/students/0')
            .end((err, res) => {
                res.status.should.equal(200);
                res.body.student.should.equal("Katie");
                done();
            })
    })

    it('should return John as the second entry', (done) => {
        chai.request(app)
            .get('/api/students/1')
            .end((err, res) => {
                res.status.should.equal(200);
                res.body.student.should.equal("John");
                done();
            })
    })

    it('should return Philip as the third entry', (done) => {
        chai.request(app)
            .get('/api/students/2')
            .end((err, res) => {
                res.status.should.equal(200);
                res.body.student.should.equal("Phillip");
                done();
            })
    })
}) 

describe('Post Student Service', () => {
    it('should creare a new student called Ash ', (done) => {
        const student = { student: "Ash" };
        chai.request(app)
            .post('/api/students/')
            .send(student)
            .end((err, res) => {
                chai.request(app)
                .get('/api/students')
                .end((err, res) => {
                    res.status.should.equal(200);
                    res.body.studentsArr.length.should.equal(4);
                    res.body.studentsArr[3].should.equal("Ash");
                    done();
                })
            })
    })

})

describe('Get Student by Name', () => {
    it('should return the student requested by name Katie', (done) => {
        const student = { student: "Katie" };
        chai.request(app)
        .get('/api/students/name/Katie')
        .end((err, res) => {
            res.status.should.equal(200);
            res.body.student.should.equal("Katie");
            done();
        })
    })    
})

describe('Delete Student by Id', () => {
    it('should delete the student requested by id', (done) => {
        chai.request(app)
        .delete('/api/students/1')
        .end((err, res) => {
            res.status.should.equal(204);
            done();
        })
    })    
})