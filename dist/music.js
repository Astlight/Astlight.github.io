const ap = new APlayer({
    container: document.getElementById('aplayer'),
    fixed: true,
    autoplay: true,
    loop: 'all',
    preload: 'auto',

    audio: [
      {
        name: "Best of 2012",
        artist: '阿斯顿发光',
        url: 'http://astlight.top/Astlight/blog/blogmusic.mp3',
        cover: 'http://astlight.top/Astlight/blog/avatar.jpg',
      }
    ]
});