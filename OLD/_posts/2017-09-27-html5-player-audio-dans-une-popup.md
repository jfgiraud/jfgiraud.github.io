---
title: "html5, player audio dans une popup"
date: "2017-09-27 16:23:00"
tags: html player
---
Pour mon projet, je devais afficher un player audio HTML5 dans une popup lors d'un clic sur un span (fichier son)...

Voici ce que cela donne sur un exemple allégé :

<div class="separator" style="clear: both; text-align: center;"><a href="https://2.bp.blogspot.com/-1MaXNndeqVo/WcuxhB4-FiI/AAAAAAAAD_Q/CDp5Y64RmgkWjb6eNjeqtmpzrkSCefOJwCLcBGAs/s1600/S%25C3%25A9lection_001.jpg" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="83" data-original-width="278" height="96" src="https://2.bp.blogspot.com/-1MaXNndeqVo/WcuxhB4-FiI/AAAAAAAAD_Q/CDp5Y64RmgkWjb6eNjeqtmpzrkSCefOJwCLcBGAs/s320/S%25C3%25A9lection_001.jpg" width="320" /></a></div>
avec son code associé :


```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html >
<head>

    <link rel="stylesheet" type="text/css" href="/css/ihmadm.css"/>

    <title>Player HTML5 popup</title>

    <script type="text/javascript" src="/js/app/lib/jquery/jquery-1.10.1.js"></script>

    <script type="text/javascript">
        $(document).ready(function() {

            var playable = function(event, currentTarget) {

                var sound = $.trim(currentTarget.text());

                $("body").append('<div id="divPlayer" style="display:none"><audio id="player" controls="controls"><source id="sourceAudio" src="">Your browser does not support the audio element.</audio><span class="closePlayer">&nbsp;</span></div>');

                var onEnded = function () {
                    $("#divPlayer").hide();
                    var player = document.getElementById('player');
                    player.removeEventListener('ended', onEnded, false);
                };

                var endOnClick = function () {
                    $("#divPlayer").hide();
                    var player = document.getElementById('player');
                    player.pause();
                    $(".closePlayer").off("click", endOnClick);
                };

                var playSource = function (sourceObject) {
                    var player = document.getElementById('player');
                    var sourceAudio = document.getElementById('sourceAudio');
                    sourceAudio.src = sourceObject;
                    player.load();
                    player.play();
                }

                function play(event, source) {
                    $("#divPlayer").css({
                        'top': event.clientY,
                        'left': event.clientX,
                        'display': 'inline',
                        'position': 'absolute'
                    }).show();
                    var player = document.getElementById('player');
                    var sourceAudio = document.getElementById('sourceAudio');

                    // Patch : des fois le temps total n'était pas affiché... (contenu renvoyé par une servlet)
                    var req = new XMLHttpRequest();
                    req.open('GET', source, true);
                    req.responseType = 'blob';
                    req.onload = function() {
                        // On lit l'audio (donc tout est en buffer) et on le positionne comme source
                        if (this.status === 200) {
                            var trackBlob = this.response;
                            var track = URL.createObjectURL(trackBlob);
                            playSource(track);
                        }
                    }
                    req.onerror = function() {
                        // sinon on prie pour que le temps total soit bien affiché...
                        playSource(source);
                    }
                    req.send();
                    // fin patch

                    player.addEventListener("ended", onEnded);
                    $(".closePlayer").on("click", endOnClick);
                }


                if (!String.prototype.endsWith) {
                    String.prototype.endsWith = function(searchString, position) {
                        var subjectString = this.toString();
                        if (typeof position !== 'number' || !isFinite(position) || Math.floor(position) !== position || position > subjectString.length) {
                            position = subjectString.length;
                        }
                        position -= searchString.length;
                        var lastIndex = subjectString.lastIndexOf(searchString, position);
                        return lastIndex !== -1 && lastIndex === position;
                    };
                }

                var source = sound;
                var player = document.getElementById('player');
                play(event, source);
            };

            $('.sound').on("click", function(event) {
                return playable(event, $(this))
            });
            $('.sound').css('cursor', 'pointer');
        });
    </script>
</head>
<body>
    Player HTML5 audio ouverture popup sur clic span
    <br/>
    <br/>
    <span class="sound">incoming_call.wav</span>
    <br/>
    <span class="sound">incoming_call_short.wav</span>
    <br/>
    <span class="sound">new_im.wav</span>
    <br/>
    <span class="sound">callclosed.wav</span>
    <br/>
</body>
</html>
```

```
.closePlayer {
    color: #f00;
    cursor:pointer;
    background:url('./images/close-button.png') no-repeat center center;
    width:27px;
    height:27px;
    top:-10px;
    right:-10px;
    display:inline;
    position:absolute;
}
```

A noter :

Parfois le temps total du morceau n'était pas affiché par le player. Cela était aléatoire et ce en utilisant le même logiciel (firefox) sous linux ou sous windows (via une machine virtuelle).

Je suspecte que cela était dû au fait que le fichier son était renvoyé par une servlet...

Dans l'exemple ci-dessus, ce n'est pas le cas mais j'ai laissé le patch pour information (la source m'ayant aidé à résoudre ce problème est la suivante : 

[http://dinbror.dk/blog/how-to-preload-entire-html5-video-before-play-solved/](http://dinbror.dk/blog/how-to-preload-entire-html5-video-before-play-solved/))



