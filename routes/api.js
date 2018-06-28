var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('api', { title: 'Api' });
});

/* GET home page. */
router.post('/sensit', function(req, res, next) {
    console.log(req);
    console.log(res);
    res.sendStatus(200);
});

module.exports = router;
