const ap = new APlayer({
    container: document.getElementById('aplayer'),
    fixed: true,
    autoplay: true,
    loop: 'all',
    preload: 'auto',
    volume: 0.2,
    audio: [
      {
        name: "Best of 2012",
        artist: '阿斯顿发光',
        url: 'http://pht1wbp11.bkt.clouddn.com/blogmusic.mp3',
        // url: 'http://astlight.top/Astlight/blog/blogmusic.mp3',
        cover: 'http://astlight.top/Astlight/blog/avatar.jpg',
      }
    ]
});