var express = require('express');
var router = express.Router();
var mysql = require('mysql');
var mysql_configs = require('./mysql/mysql_config');

var pool = mysql.createPool({
    connectionLimit: 100,
    host: mysql_configs.host,
    user: mysql_configs.user,
    password: mysql_configs.password,
    database: mysql_configs.database,
    debug: false
});

/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('api', { title: 'Api' });
});

router.get('/sensit', function(req, res, next) {
    pool.query('select temp,hum from data ORDER BY id DESC LIMIT 1;',  function (err, rows) {
        res.send({problem: false,
            temp: rows[0].temp,
            hum: rows[0].hum,
            airQ: "Good"
        }).status(200);
    });
});

router.get('/sensit/temp/average', function(req, res, next) {
    res.send({problem: false,
        monday: "26",
        tuesday: "25",
        wednesday: "32",
        thursday: "24",
        friday: "25" ,
        saturday: "0",
        sunday: "0",
        last: "1"
    }).status(200);
});

router.get('/sensit/hum/average', function(req, res, next) {
    res.send({problem: false,
        january: "65",
        february: "75",
        march: "48",
        april: "50",
        may: "78" ,
        june: "52",
        july: "63",
        august: "80",
        september: "65",
        october: "58",
        november: "85",
        december: "64",
        last:"1"
    }).status(200);
});

router.get('/sensit/lightlamp', function(req, res, next) {
    pool.query('select light from data ORDER BY id DESC LIMIT 1;',  function (err, rows) {
        var status;
        if(rows[0].light >  20){
            status = "ON"
        }else{
            status = "OFF"
        }
        res.send({problem: false,
            status: status
        }).status(200);
    });
});

router.get('/sensit/nodes', function(req, res, next) {
    res.send({problem: false,
        battery:"45"+"%",
        trust:"100%",
        loc: "37.939973, 23.691856"
    }).status(200);
});

router.post('/sensit', function(req, res, next) {
    console.log(req);
    console.log(res);
    res.sendStatus(200);
});

router.post('/sensit/alert', function(req, res, next) {
    pool.query('insert into alert (reason,date) values(?,?)', [req.body.reason,req.body.date], function (err, rows) {

    });
    res.sendStatus(200);
});

router.post('/sensit/data', function(req, res, next) {
    var light = "";
    if(req.body.ambient_light > 20){
        light = "ON"
    }else{
        light = "OFF"
    }
    pool.query('insert into data (temp,hum,light) values(?,?,?)', [req.body.temperature,req.body.humidity,light], function (err, rows) {

    });
    res.sendStatus(200);
});

router.get('/sensit/alert', function(req, res, next) {
    pool.query('select * from alert where closed=0',  function (err, rows) {
        res.send({problem: false,
            alerts: JSON.parse(JSON.stringify(rows))
        }).status(200);
    });
});


router.delete('/sensit/alert', function(req, res, next) {
    pool.query('delete from alert',  function (err, rows) {
        res.send({problem: false
        }).status(200);
    });
});

module.exports = router;
