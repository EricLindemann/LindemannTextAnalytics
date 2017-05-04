testAnalysisPage()
test3Level()

function test3Level(){
    var webdriver = require('selenium-webdriver'),
        By = webdriver.By,
        until = webdriver.until;

    var driver = new webdriver.Builder()
        .forBrowser('chrome')
        .build();

    driver.get('localhost:3000/analyses');

    driver.findElement(By.name('List1'));
    driver.findElement(By.name('additList1')).click();
    driver.sleep(1000);
    driver.findElement(By.name('List2'));
    driver.findElement(By.name('comprisList2')).click();
    driver.sleep(1000);
    driver.findElement(By.name('List3'));
    driver.findElement(By.name(" U.K. WHEAList3")).click();


    driver.sleep(2000).then(function() {
    driver.getTitle().then(function(title) {
        if(title === 'Analysis') {
        console.log('Test passed');
        } else {
        console.log('Test failed');
        }
    });
    });

    driver.quit();
}

function testAnalysisPage(){
    var webdriver = require('selenium-webdriver'),
    By = webdriver.By,
    until = webdriver.until;

    var driver = new webdriver.Builder()
    .forBrowser('chrome')
    .build();

    driver.get('localhost:3000');
    driver.findElement(By.name('analysisLink')).click();


    driver.sleep(2000).then(function() {
    driver.getTitle().then(function(title) {
        if(title === 'Analysis') {
        console.log('Test passed');
        } else {
        console.log('Test failed');
        }
    });
    });

    driver.quit();
}