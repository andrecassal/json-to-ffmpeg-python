from index import parse_schema

schema = {
    "version": 1,
    "inputs": {
      "source1": {
        "type": "video",
        "file": "samples/bee1920.mp4",
        "hasAudio": False,
        "hasVideo": True,
        "duration": 40
      },
      "source2": {
        "type": "video",
        "file": "samples/book1920.mp4",
        "hasAudio": False,
        "hasVideo": True,
        "duration": 13
      },
      "source3": {
        "type": "video",
        "file": "samples/cows1920.mp4",
        "hasAudio": True,
        "hasVideo": True,
        "duration": 15
      },
      "source4": {
        "type": "video",
        "file": "samples/flowers1920.mp4",
        "hasAudio": True,
        "hasVideo": True,
        "duration": 21
      },
      "audio1": {
        "type": "audio",
        "file": "samples/ever.mp3",
        "hasAudio": True,
        "hasVideo": False,
        "duration": 181
      },
      "audio2": {
        "type": "audio",
        "file": "samples/weekend.mp3",
        "hasAudio": True,
        "hasVideo": False,
        "duration": 208
      },
      "watermark": {
        "type": "image",
        "file": "samples/flower.png",
        "hasAudio": False,
        "hasVideo": True,
        "duration": 0
      }
    },
    "tracks": {
      "track_with_some_videos": {
        "type": "video",
        "clips": [
          {
            "name": "clip1",
            "source": "source1",
            "timelineTrackStart": 3,
            "duration": 2,
            "sourceStartOffset": 10,
            "clipType": "video",
            "transform": {
              "x": 0,
              "y": 0,
              "width": 1920,
              "height": 1080,
              "rotation": 0,
              "opacity": 1
            }
          },
          {
            "name": "clip2",
            "source": "source2",
            "timelineTrackStart": 5,
            "duration": 1,
            "sourceStartOffset": 5,
            "clipType": "video",
            "transform": {
              "x": 0,
              "y": 0,
              "width": 1920,
              "height": 1080,
              "rotation": 0,
              "opacity": 1
            }
          },
          {
            "name": "clip3",
            "source": "source3",
            "timelineTrackStart": 10,
            "duration": 5,
            "sourceStartOffset": 3,
            "clipType": "video",
            "transform": {
              "x": 480,
              "y": 270,
              "width": 960,
              "height": 540,
              "rotation": 45,
              "opacity": 0.5
            }
          },
          {
            "name": "clip4",
            "source": "source1",
            "timelineTrackStart": 15,
            "duration": 5,
            "sourceStartOffset": 27,
            "clipType": "video",
            "transform": {
              "x": 0,
              "y": 0,
              "width": 1920,
              "height": 1080,
              "rotation": 0,
              "opacity": 1
            }
          },
          {
            "name": "clip5",
            "source": "source2",
            "timelineTrackStart": 19,
            "duration": 5,
            "sourceStartOffset": 0,
            "clipType": "video",
            "transform": {
              "x": 50,
              "y": 50,
              "width": 400,
              "height": 300,
              "rotation": 0,
              "opacity": 1
            }
          },
          {
            "name": "clip6",
            "source": "source4",
            "timelineTrackStart": 23,
            "duration": 5,
            "sourceStartOffset": 15,
            "clipType": "video",
            "transform": {
              "x": 0,
              "y": 0,
              "width": 1920,
              "height": 1080,
              "rotation": 0,
              "opacity": 1
            }
          },
          {
            "name": "clip7",
            "source": "source3",
            "timelineTrackStart": 28,
            "duration": 5,
            "sourceStartOffset": 0,
            "clipType": "video",
            "transform": {
              "x": 0,
              "y": 0,
              "width": 1920,
              "height": 1080,
              "rotation": 0,
              "opacity": 1
            }
          },
          {
            "name": "clip8",
            "source": "source1",
            "timelineTrackStart": 33,
            "duration": 5,
            "sourceStartOffset": 0,
            "clipType": "video",
            "transform": {
              "x": 0,
              "y": 0,
              "width": 1920,
              "height": 1080,
              "rotation": 0,
              "opacity": 1
            }
          }
        ]
      },
      "track_with_watermark": {
        "type": "video",
        "clips": [
          {
            "name": "watermark_clip",
            "source": "watermark",
            "timelineTrackStart": 0,
            "duration": 30,
            "sourceStartOffset": 0,
            "clipType": "image",
            "transform": {
              "x": 1610,
              "y": 10,
              "width": 300,
              "height": 150,
              "rotation": 0,
              "opacity": 1
            }
          }
        ]
      },
      "track2": {
        "type": "audio",
        "clips": [
          {
            "name": "audio_clip1",
            "source": "audio1",
            "timelineTrackStart": 5,
            "duration": 10,
            "sourceStartOffset": 0,
            "clipType": "audio",
            "volume": 1
          },
          {
            "name": "audio_clip2",
            "source": "audio2",
            "timelineTrackStart": 20,
            "duration": 15,
            "sourceStartOffset": 0,
            "clipType": "audio",
            "volume": 1
          }
        ]
      }
    },
    "transitions": [
      {
        "type": "smoothup",
        "duration": 0.5,
        "from": None,
        "to": "clip1"
      },
      {
        "type": "smoothdown",
        "duration": 0.5,
        "from": "clip1",
        "to": None
      },
      {
        "type": "fade",
        "duration": 0.5,
        "from": None,
        "to": "clip2"
      },
      {
        "type": "circlecrop",
        "duration": 0.5,
        "from": "clip2",
        "to": None
      },
      {
        "type": "squeezev",
        "duration": 0.5,
        "from": "clip3",
        "to": None
      },
      {
        "type": "squeezeh",
        "duration": 0.5,
        "from": "watermark_clip",
        "to": None
      },
      {
        "type": "fade",
        "duration": 1,
        "from": "clip4",
        "to": "clip5"
      },
      {
        "type": "smoothdown",
        "duration": 1,
        "from": "clip5",
        "to": "clip6"
      },
      {
        "type": "smoothdown",
        "duration": 0.5,
        "from": "clip8",
        "to": None
      }
    ],
    "output": {
      "tempDir": "./tmp",
      "file": "output.mp4",
      "videoCodec": "libx264",
      "audioCodec": "aac",
      "width": 1920,
      "height": 1080,
      "audioBitrate": "320k",
      "preset": "veryfast",
      "crf": 23,
      "framerate": 30,
      "flags": [
        "-pix_fmt",
        "yuv420p"
      ],
      "startPosition": 0,
      "endPosition": 38,
      "scaleRatio": 0.2
    }
  }

command = parse_schema(schema)
print(command)


