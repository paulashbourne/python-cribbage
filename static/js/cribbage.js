require(
    ['lib/underscore', 'lib/bb'],
    function(underscore, bb) {
  var CribbageBoardView = bb.BackboneView.extend({
    
    initialize : function(options) {
      this.$gameCanvas = $("canvas#game-canvas");
      this.$boardCanvas     = $("canvas#board-canvas");
      this.$p1ScoreCanvas  = $("canvas#p1-score-canvas");
      this.$p2ScoreCanvas  = $("canvas#p2-score-canvas");
      this.$canvases = [
        this.$gameCanvas,
        this.$boardCanvas,
        this.$p1ScoreCanvas,
        this.$p2ScoreCanvas
      ];
      this.setCanvasSizes();
      $(window).resize(_.bind(this.setCanvasSizes, this));
      this.redPos  = -1;
      this.bluePos = 82;
    },
    draw : function() {
      this.CARD_IMG_WIDTH = 69;
      this.CARD_IMG_HEIGHT = 93;
      this.CARD_IMG_SPACINGX = 2;
      this.CARD_IMG_SPACINGY = 3;
      this.CARD_IMG_MARGINX      = 2;
      this.CARD_IMG_MARGINY      = 2;
      this.CARD_HEIGHT = parseInt(this.$gameCanvas.height() * 0.2);
      this.CARD_WIDTH = parseInt(this.CARD_HEIGHT * this.CARD_IMG_WIDTH / this.CARD_IMG_HEIGHT);
      this.drawBoard(this.redPos, this.bluePos);
      this.playerBox("Player", 'blue', 10);
      this.playerBox(null, 'red', 10);
      this.drawHands([0, 13, 25, 48, 23, 5], 6);
    },
    setCanvasSizes : function() {
      for (var i = 0; i < this.$canvases.length; i++) {
        $parent = this.$canvases[i].parent();
        this.$canvases[i].attr('width', $parent.width());
        this.$canvases[i].attr('height', $parent.height());
      }
      this.draw();
    },
    playerBox : function(playername, pegColour, score) {
      var x = 0;
      var y;
      var $canvas;
      if (playername !== null) {
        $canvas = this.$p1ScoreCanvas;
      } else {
        playername = "Computer";
        $canvas = this.$p2ScoreCanvas;
      }
      var height = $canvas.height();
      var width  = $canvas.width();
      var fontSize = height / 4;
      var spacing  = (height - fontSize * 2) / 3;
      // Player Name
      $canvas.drawText({
          fillStyle: 'black',
          x: width / 2,
          y: spacing + fontSize / 2,
          fontSize: fontSize,
          fontFamily: 'Arial',
          text: playername,
          maxwidth: width - 2
      });
      // Player Score
      $canvas.drawText({
          fillStyle: 'black',
          x: width / 2,
          y: height - spacing - fontSize / 2,
          fontSize: fontSize,
          fontFamily: 'Arial',
          text: "Score: " + score,
          maxwidth: width
      });
    },
    drawBoard : function(redpos, bluepos) {
      var $canvas = this.$boardCanvas;
      var bwidth  = $canvas.width();
      var bheight = $canvas.height();
      var boardPadding = 20;
      bwidth-=2*boardPadding;
      bheight-=2*boardPadding;
      var lineWidth = 0.2 * bwidth;
      var radius = bwidth / 4;
      var sectionHeight = bheight - bwidth / 2 - radius - 0.25*lineWidth;
      var vradius = (sectionHeight / 35) * 0.45;
      var hradius = 0.5*lineWidth/6;
      var pegRadius = vradius < hradius ? vradius : hradius;
      var drawHole = _.bind(function(x, y, val, currentColor) {
        var color = 'black';
        if (val == this.bluePos && currentColor === 'blue') {
          color = 'yellow'
        } else if (val == this.redPos && currentColor == 'red') {
          color = 'yellow'
        }
        $canvas.drawArc({
          x : x,
          y : y,
          radius : pegRadius,
          fillStyle : color
        });
      }, this);
      var drawStraightTrack = _.bind(function(x, y, width, height, start, end,
          reversed) {
        x+=boardPadding;
        y+=boardPadding;
        var colors = ['blue', 'green', 'red'];
        if (reversed) {
          colors.reverse();
        }
        var hspacing = (width - 6 * pegRadius) / 3;
        var vspacing = height / (end-start+1) - 2*pegRadius;
        for (var i = 0; i < 3; i++) {
          $canvas.drawRect({
            x : x + i*(width/3),
            y : y,
            height : height,
            width : width / 3,
            fillStyle : colors[i],
            fromCenter : false
          });
          for (var h = 0; h < end-start; h++) {
            drawHole(
              (0.5*hspacing)+x+i*(2*pegRadius+hspacing)+pegRadius,
              y+(h+1)*(2*pegRadius+vspacing),
              start + h,
              colors[i]
            );
          }
        }
      }, this);
      var drawArcTrack = function(x, y, width, arcRadius, startAngle,
          endAngle, start, end) {
        x+=boardPadding;
        y+=boardPadding;
        var colors = ['blue', 'green', 'red'];
        var spacing = 0.1*width;
        var angleInc = (endAngle-startAngle) / (end-start+1);
        var laneWidth = width/3.0;
        for (var i =0; i < 3; i++) {
          $canvas.drawArc({
            x : x,
            y : y,
            radius : arcRadius + (i+0.5)*laneWidth,
            strokeStyle : colors[i],
            strokeWidth : laneWidth,
            start       : startAngle+90,
            end         : endAngle+90
          });
          for (var a = 0; a < end-start; a++) {
            var hyp = arcRadius + (i+0.5)*laneWidth;
            var angle = (startAngle+(1+a)*angleInc) * Math.PI / 180;
            drawHole(
              x+hyp*Math.cos(angle),
              y+hyp*Math.sin(angle),
              start + a,
              colors[i]
            );
          }
        }
      };
      var spacing = (100 - (lineWidth * 3))/2;
      var boardSpacing = (bwidth - 3*lineWidth) / 2;
      var cury = 0.5 * bwidth;
      drawStraightTrack(
          0,
          cury,
          lineWidth,
          sectionHeight,
          0, 35,
          true);
      drawStraightTrack(
          0,
          cury + sectionHeight + 20,
          lineWidth,
          0.5 * boardSpacing + lineWidth - 20,
          -3, 0,
          true);
      drawArcTrack(
          0.5*bwidth,
          cury,
          lineWidth,
          0.5*bwidth - lineWidth,
          180, 360,
          35, 45);
      //draw finish hole
      $canvas.drawArc({
        x : boardPadding + bwidth * 0.5,
        y : boardPadding + cury - 0.3 * (0.5*bwidth - lineWidth),
        radius : pegRadius,
        strokeStyle : 'black',
        strokeWidth : 1,
        fillStyle   : 'black'
      });
      $canvas.drawText({
          fillStyle: 'black',
          strokeStyle: 'black',
          strokeWidth: 2,
          x : boardPadding + bwidth * 0.5,
          y : boardPadding + cury - 0.3 * (0.5*bwidth - lineWidth) - 20,
          fontSize: 12,
          fontFamily: 'Arial',
          text: "F I N I S H"
      });
      drawStraightTrack(
          bwidth - lineWidth,
          cury,
          lineWidth,
          sectionHeight,
          45, 80,
          false);
      cury+=sectionHeight;
      drawArcTrack(
          boardSpacing * 1.5 + 2*lineWidth,
          cury,
          lineWidth,
          0.5 * boardSpacing,
          0, 180,
          80, 85);
      drawStraightTrack(
        bwidth - 2*radius - lineWidth/2,
        0.5 * bwidth,
        lineWidth,
        bheight - 0.5*bwidth - radius - 0.25*lineWidth,
        85, 120,
        true);
    },
    drawCard : function(x, y, cardIndex, clickEvent) {
      var $canvas = this.$gameCanvas;
      var SUIT_INT_MAP = {
        0 : 2, 1 : 3, 2 : 0, 3 : 1
      }
      if (cardIndex !== -1) {
        var suitInt = SUIT_INT_MAP[Math.floor(cardIndex / 13)];
        var rankInt = cardIndex % 13;
        $canvas.drawImage({
          source: '/static/img/playing-cards.png',
          x : x,
          y : y,
          width : this.CARD_WIDTH,
          height : this.CARD_HEIGHT,
          fromCenter : false,
          sx : (this.CARD_IMG_WIDTH + this.CARD_IMG_SPACINGX) * rankInt + this.CARD_IMG_MARGINX * (rankInt + 1),
          sy : (this.CARD_IMG_HEIGHT + this.CARD_IMG_SPACINGY) * suitInt + this.CARD_IMG_MARGINY * (suitInt + 1),
          sWidth : this.CARD_IMG_WIDTH,
          sHeight : this.CARD_IMG_HEIGHT,
          click : clickEvent
        });
      } else {
        $canvas.drawImage({
          source: '/static/img/card-back.png',
          x : x,
          y : y,
          width : this.CARD_WIDTH,
          height : this.CARD_HEIGHT,
          fromCenter : false,
          click : clickEvent
        });
      }
    },
    drawHands : function(playerCardIndices, compHandLength) {
      var cardSpacing = this.CARD_WIDTH * 0.25;
      var y = this.$gameCanvas.height() - this.CARD_HEIGHT;
      for (var i = 0; i < playerCardIndices.length; i++) {
        this.drawCard(cardSpacing*(i+1), y, playerCardIndices[i]);
      }
      for (var i = 0; i < compHandLength; i++) {
        this.drawCard(cardSpacing*(i+1), 0, -1, false);
      }
    },
    drawCardDropContainer : function() {
      var width  = this.$gameCanvas.width();
      var height = this.$gameCanvas.height();
        this.$gameCanvas.drawImage({
          source: '/static/img/boardbackground.jpg',
          x : width/2,
          y : height/2,
          width : width * 0.4,
          height : height * 0.2
        });
    },
    cardDragEvent : function(evt) {
      this.drawCardDropContainer();
    },
    cardDroppedEvent : function(evt) {
      
    }
  });
  var init_page = function() {
    var cribbageBoardView = new CribbageBoardView();
  };  

  $(document).ready(init_page);
});
