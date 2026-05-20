

module.exports = function SendURL(number, carrier, url) {
    let {PythonShell} = require('python-shell');

    let options = {
        args: [number, carrier, url]
    };
        
    PythonShell.run('SMS.py', options, function (err, results) {
        if (err) throw err;
    });
}

