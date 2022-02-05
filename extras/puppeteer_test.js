const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://artofvisualization.com');
  await page.screenshot({ path: 'screenshot_puppeteer.png' });
  await browser.close();
})();
