const Crawler = require('crawler')
const jsdom = require('jsdom')

const docModel = require('../schemas/doc')

const c = new Crawler({
  maxConnections: 10,
  // This will be called for each crawled page
  callback: (error, res, done) => {
    if (error) {
      console.log(error)
      return
    }

    const dom = new jsdom.JSDOM(res.body)
    let title = dom.window.document.querySelector('font > b') ||
      dom.window.document.querySelector('b > font')
    const spans = dom.window.document.querySelectorAll('span')

    let content = ''
    for (const span of spans) {
      content += span.textContent
    }
    if (content === '') {
      done()
      return
    }

    const doc = new docModel({
      url: res.options.uri,
      title: title ? title.textContent : '',
      content: content
    })

    console.log(doc.title + ': ' + doc.content)

    doc.save(err => {
      if (err) {
        console.log(err)
      } else {
        console.log(doc.title + ': ' + doc.content)
      }
    })

    done()
  }
})

for (let i = 342200; i > 0; i--) {
  c.queue(`http://www1.szu.edu.cn/board/view.asp?id=${i}`)
}
